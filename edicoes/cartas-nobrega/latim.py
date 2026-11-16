"""Detecta as passagens em latim (citações bíblicas e litúrgicas que Nóbrega mistura ao português) nos parágrafos
já juntados, para pô-las em itálico e fora da modernização de grafia. Léxico levantado à mão nas passagens do volume."""
import re

SURE0 = set('''ego pater mi positus igne charitatis sicut alioquin te audivi prophetantem compelle multas intrare naves et venire ad hanc quam
plantat dominus vineam suam tu autem ora pro omnibus presertim filiis quos enutristi qui quaerunt quærunt quœrunt jesum christum solum
crucifixum omnes quae quæ sua sunt mitte filios tuos domino nutritos fratres meos ut omnem terram exeat sonus eorum quia patres nuntiaverunt
eis igitur operarios jam satis alba est messis vale semper domini benedic nos fratres obsequium prestare deo petentes panem non frangat
quod dolendum sed christi dedisti ex quemquam solum volumus videre opera didicerunt mixti inter gentes quos mihi veniat amat
patrem meum ipse amat me nomine titulo curavimus babilonem curata apposuit apprehendere sancti spiritus irruit spiritus miserere mei deus
quis daret ignem aquam tuae israel defecerunt praë prae lacrymis oculi mei conturbata viscera mea effusum terra jecur meum quaerere ovem
perierat salvum facere beati misericordes pauperibus egenis pertinebat eum fur erat respicite nationes hominum scitote nullus sperabit
hunc mittere accendatur ne redeat immundus cum aliis septem et pax in omni eam quia lumen revelationem gentium gloriam plebis tuæ
sunt mundi vobis mihi quis qui quid ave maria gratia plena benedicta omnibus laudate dominum gloria patri filio deo
nobiscum amen gratia pax domini nostri jesu christi sit semper nobiscuim'''.split())
AMB = {'sua', 'terra', 'gloria', 'deus', 'deo', 'israel', 'nos', 'mi', 'mei', 'sit', 'amen', 'est', 'qui', 'non', 'et', 'pater', 'sunt', 'domino', 'dominus', 'domini', 'christi', 'jesu', 'quia', 'ora', 'pro', 'sed', 'quod', 'eis', 'ego', 'in', 'de', 'me', 'si', 'a', 'e', 'ad', 'ex', 'o', 'dom', 'cum', 'per', 'ne', 'ut'}
SURE = SURE0 - AMB
TOK = re.compile(r"[A-Za-zÀ-ÿœæŒÆ]+|[,;:.!?]|\s+|[^\sA-Za-zÀ-ÿœæŒÆ]")


def corridas(texto):
    """Lista de trechos (substrings de `texto`) em latim, com ≥ 2 palavras seguras."""
    toks = TOK.findall(texto)
    pos, p = [], 0
    for t in toks:
        pos.append(p)
        p += len(t)
    out = []
    i, n = 0, len(toks)
    while i < n:
        t = toks[i]
        w = t.lower()
        if w in SURE:
            j, ult, seguras = i, i, 0
            k = i
            while k < n:
                tk, wk = toks[k], toks[k].lower()
                if wk in SURE:
                    seguras += 1
                    ult = k
                elif wk in AMB or tk in ',;:.' or tk.isspace():
                    pass
                else:
                    break
                k += 1
            if seguras >= 2:
                out.append(texto[pos[i]:pos[ult] + len(toks[ult])])
            i = k if seguras >= 2 else i + 1
        else:
            i += 1
    return out
