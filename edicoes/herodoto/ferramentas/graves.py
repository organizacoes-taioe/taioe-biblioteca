"""Grave no lugar do agudo final quando a palavra não fecha a frase (regra da ortografia do grego impresso),
que a transcrição do Perseus de Godley ignora em centenas de lugares («σχεδόν πάντων» → «σχεδὸν πάντων»).
Também tira o segundo agudo de palavra com dois acentos que não vem antes de enclítica («Ἕλληνές λέγουσι»).
Não mexe antes de pontuação, antes de enclítica (lista abaixo, comparada sem acentos: os casos ambíguos, como
οἱ artigo × οἱ pronome, ficam como no Perseus e a colação com o fac-símile decide), nem em τίς/τί."""
import re, unicodedata as u
ACU, GRA, CIRC = '́', '̀', '͂'
ENCL = set('τε τοι γε περ νυν μιν νιν σφι σφιν σφεας σφεα σφεων σφισι σφε οι μοι μου με σοι σου σε τις τι τινος τινι '
           'τινα τινες τινων τισι τισιν τινας του τευ τεο τεω τω τεων ποτε πω που πη πως ποθεν ποθι θην κε κεν ρα '
           'εστι εστιν εισι εισιν ειμι εσμεν εστε φημι φησι φησιν φαμεν φατε φασι φασιν'.split())
VOG = set('αεηιουωΑΕΗΙΟΥΩ')
PAL = re.compile(r'[\ẁ-ͯ]+', re.U)
def nu(w):
    d = u.normalize('NFD', w.lower())
    return ''.join(c for c in d if not u.combining(c)).replace('ς', 'σ').replace('σ', 'σ')
def _sem(w):
    return nu(w).replace('σ', 'ς') if nu(w).endswith('σ') else nu(w)
ENCL_SEGURAS = ENCL - {'οι'}
def _acentos(d):
    return [i for i, c in enumerate(d) if c in (ACU, GRA, CIRC)]
def _vogais_depois(d, i):
    return sum(1 for c in d[i + 1:] if not u.combining(c) and c.lower() in VOG and not (c.lower() in 'ιυ' and False))
def _silabas(d):
    """posições (índices em d) dos núcleos vocálicos, contando ditongos como um núcleo"""
    nuc, ant = [], None
    base = [(i, c) for i, c in enumerate(d) if not u.combining(c)]
    for k, (i, c) in enumerate(base):
        cl = c.lower()
        if cl not in VOG: ant = None; continue
        if ant is not None and cl in 'ιυ' and ant in 'αεοηω' + 'υ' and not any(d[j] == '\u0308' for j in range(i + 1, min(i + 3, len(d)))):
            # ditongo (sem trema): fica no núcleo anterior
            if not any(d[j] in (ACU, GRA, CIRC, '\u0313', '\u0314') for j in range(base[k - 1][0] + 1, i)):
                ant = None; continue
        nuc.append(i); ant = cl
    return nuc
def _sem_acento(w):
    return not _acentos(u.normalize('NFD', w))
def corrigir(t):
    """Devolve (texto, n_graves, n_duplos). Regras, só entre palavras separadas por espaço:
    R1 agudo final → grave antes de palavra que não é enclítica; com dois acentos, sai o segundo;
    R2 dois acentos com o último grave: antes de enclítica (aqui também οἱ), o último vira agudo; senão sai;
    R3 grave final → agudo antes de enclítica segura sem acento (γὰρ σε → γάρ σε);
    R4 proparoxítona ou properispômena antes de enclítica segura sem acento ganha o agudo final (πείθεσθαί μοι)."""
    out, ng, nd = [], 0, 0
    ms = list(PAL.finditer(t))
    pos = 0
    for k, m in enumerate(ms):
        w = m.group(); out.append(t[pos:m.start()]); pos = m.end()
        nxt = ms[k + 1] if k + 1 < len(ms) else None
        entre = t[m.end():nxt.start()] if nxt else '.'
        if not nxt or entre.strip() != '':
            out.append(w); continue
        prox = _sem(nxt.group()).replace('ς', 'σ')
        encl = prox in ENCL
        segura = prox in ENCL_SEGURAS and _sem_acento(nxt.group())
        d = u.normalize('NFD', w)
        ac = _acentos(d)
        if not ac or nu(w) in ('τισ', 'τι'):
            out.append(w); continue
        i = ac[-1]
        final = not any(c.lower() in VOG for c in d[i + 1:] if not u.combining(c))
        novo = d
        if len(ac) >= 2 and final and d[i] == GRA:                     # R2
            novo = d[:i] + (ACU if encl else '') + d[i + 1:]
        elif d[i] == ACU and final and not encl:                        # R1
            novo = d[:i] + ('' if len(ac) >= 2 else GRA) + d[i + 1:]
        elif d[i] == GRA and final and segura and len(ac) == 1:         # R3
            novo = d[:i] + ACU + d[i + 1:]
        elif len(ac) == 1 and segura and not final:                     # R4
            nuc = _silabas(d)
            if len(nuc) >= 2:
                pos_ac = max(j for j in nuc if j < i) if any(j < i for j in nuc) else None
                # sílaba do acento: o núcleo cujo índice é o maior <= i
                s_ac = max(k2 for k2, j in enumerate(nuc) if j <= i)
                antep = s_ac == len(nuc) - 3 and d[i] == ACU
                prop = s_ac == len(nuc) - 2 and d[i] == CIRC
                if antep or prop:
                    j = max(k3 for k3, c in enumerate(d) if not u.combining(c) and c.lower() in VOG)
                    # o acento vai na última vogal (a 2ª do ditongo), depois dos sinais que já estão nela
                    fim = j + 1
                    while fim < len(d) and u.combining(d[fim]): fim += 1
                    novo = d[:fim] + ACU + d[fim:]
        if novo != d:
            if len(_acentos(novo)) < len(ac): nd += 1
            else: ng += 1
        out.append(u.normalize('NFC', novo))
    out.append(t[pos:])
    return ''.join(out), ng, nd
if __name__ == '__main__':
    for s in ['πέμπτῃ δὲ ἢ ἕκτῃ ἡμέρῃ ἀπʼ ἧς ἀπίκοντο, ἐξεμπολημένων σφι σχεδόν πάντων, ἐλθεῖν ἐπὶ τὴν θάλασσαν γυναῖκας ἄλλας τε πολλάς καὶ δὴ καὶ τοῦ βασιλέος θυγατέρα· τὸ δέ οἱ οὔνομα εἶναι, κατὰ τὠυτὸ τὸ καὶ Ἕλληνές λέγουσι, Ἰοῦν τὴν Ἰνάχου·',
              'Ἑλλήνων τινάς (οὐ γὰρ', 'οὐ γὰρ σε δοκέω πείθεσθαι μοι λέγοντι', 'φοινίκων τοὺς ἔρσενας Ἕλληνὲς καλέουσι', 'ἐντειλάμενὸς οἱ ἀπὸ', 'θεῖναὶ μιν ἐς', 'παῖδα μοι', 'ἔδοσαν σφι', 'νῦν τοί δυῶν ὁδῶν παρεουσέων Γύγη δίδωμί αἵρεσιν', 'ἤ σε τὸν ἐμὲ γυμνήν θεησάμενον', 'καταπλώσαντας γὰρ μακρῇ νηί ἐς Αἶαν']:
        print(corrigir(s))
