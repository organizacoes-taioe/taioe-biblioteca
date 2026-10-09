# Prompt: terminar a tradução do Beowulf em verso livre

Tarefa: continuar a tradução do _Beowulf_ do inglês antigo em **verso livre**, dos cantos III a XLIII
(`original/03.txt` a `43.txt`, versos 115–3184) e do fragmento de Finnsburh (`original/finnsburh.txt`).
Os cantos I e II já estão prontos, e são o modelo de tudo o que segue.

## Onde estão as coisas

Repositório: `C:\Users\geren\OneDrive\Documentos\Onedrive do Gere\Software MEU\biblioteca`, branch
`claude/beowulf-translation-69wsfr`. Confira com `git status` que está nele. Os arquivos de
`edicoes/beowulf/teste-verso-livre/` podem ainda não ter commit: não os apague nem os sobrescreva.

Leia antes de começar, nesta ordem:

1. `edicoes/beowulf/teste-verso-livre/notas.md`: o método, as escolhas, as passagens revistas e as
   metas de ritmo dos cantos I–II. **É a referência principal.**
2. `edicoes/beowulf/teste-verso-livre/01.txt` e `02.txt`: o modelo pronto (formato, registro, ritmo).
3. `edicoes/CONVENCOES-TRADUCAO.md`: regras gerais da Biblioteca.
4. `edicoes/beowulf/CONVENCOES.md`: nomes, termos, fórmulas, tratamento, tipografia das falas,
   lacunas, títulos das seções (§ 8) e decisões de harmonização (§ 9). **Ignore o § 2** (a medida
   aliterativa com cesura): aqui o verso é livre, sem tabulação.
5. `edicoes/beowulf/referencias/LEIAME.md`: como usar as referências.
6. Versificador, em `C:\Users\geren\OneDrive\Documentos\Onedrive do Gere\Solar\Editora\Versificador\`:
   `traducao\MANUAL-DE-TRADUCAO.md`, `estudo\ESTUDO-DO-RITMO.md` (§§ 3.5 e 5) e
   `estudo\metros\verso-livre.md` (sobretudo as «Lições para quem traduz»).

Fontes:

- Original: `edicoes/beowulf/original/NN.txt` (Harrison e Sharp, 4.ª ed.; a tabulação é a cesura) e
  `original/LEIAME.md` (aspas, lacunas, parênteses).
- Referências em `edicoes/beowulf/referencias/`:
  - `hall-1892.txt`: numera os versos **por seção**, como os nossos arquivos; é a primeira a abrir.
  - `gummere-1910.txt`: verso a verso, sem numeração.
  - `morris-wyatt-1895.txt`: numeração moderna a cada 10 versos.
  - `harrison-sharp-1894-edicao-completa.txt`: notas a partir da linha 4460, glossário a partir da
    6659. O glossário dá o sentido de cada palavra **no verso em que ela ocorre**; ele decide os casos
    disputados.
  - `clark-hall-1916-dicionario.txt`, `bosworth-toller-1898-dicionario.txt.gz` (leia com
    `zcat ... | grep`), `kirtlan-1913-prosa.txt` e `chambers-1921-introducao.txt` (Finn, Ingeld,
    suecos e geatas).
- `edicoes/beowulf/traducao/`: a tradução anterior, aliterativa. Consulte-a só para manter os mesmos
  nomes e termos. **Não a copie e não a altere.**

## O que fazer

1. **Tradução.** Do inglês antigo, em verso livre, verso a verso: o mesmo número de linhas do
   original, sem tabulação de cesura, sem imitar o ritmo do original. Grave em
   `edicoes/beowulf/teste-verso-livre/NN.txt` (e `finnsburh.txt`), com o cabeçalho dos arquivos de
   `traducao/`:
   ```
   # canto: III
   # titulo: As visitas de Grendel

   ```
   Depois do cabeçalho vem uma linha em branco e um verso por linha, sem linhas em branco no meio.
   Os títulos estão no § 8 do guia.
   - Guarde todas as aposições no lugar delas.
   - Traduza a imagem dos kennings e as fórmulas sempre do mesmo modo (guia, §§ 3 e 9).
   - Tratamento: tu e vós. Deus tem os nomes do guia, e o pronome que se refere a ele vai em minúscula.
   - Falas: as aspas abrem no verso em que a fala começa e fecham no verso em que acaba. Fala que
     atravessa duas seções fecha as aspas no fim de um arquivo e reabre no começo do seguinte.
   - Lacunas `. . .` e `(?)` ficam no mesmo lugar do verso.
   - **Nunca mesóclise.**

2. **Ritmo.** Passe cada canto pelo Versificador e reescreva até ficar bom. O objetivo é um verso livre
   agradável: nenhuma «leitura natural» forçada, cadências variadas, nada de prosa achatada. As metas e
   o modo de agir estão em `notas.md`, § 4. Comandos (rodar de dentro da pasta do Versificador):
   ```
   node ferramentas/verso-livre.mjs <canto-com-trocas>.txt
   node ferramentas/molde.mjs <canto>.txt <molde>.txt
   ```
   - **Arquivos temporários.** Grave os temporários só numa pasta sua:
     `C:\Users\geren\AppData\Local\Temp\claude\beowulf-verso-livre-<trecho>\`.
   - **Molde livre.** O molde é uma linha `*` por verso, mais linhas `# troca:` com a pronúncia dos
     nomes:
     ```
     # troca: Healfdene => Hélfdene
     # troca: Heorogar => Héorogar
     # troca: Hrothgar => Hrótgar
     # troca: Heorot => Héorot
     # troca: Scedeland => Scédeland
     # troca: Ongentheow => Ôngentiou
     # troca: Scefing => Scéfing
     # troca: Scylfing => Scílfing
     # troca: Scyldings => Scíldings
     # troca: Grendel => Grêndel
     # troca: Beowulf => Bêovulf
     # troca: Elan => Élan
     ```
     Acrescente as trocas dos nomes novos (Hygelac, Wealhtheow, Unferth, Ecgtheow, Æschere, Wiglaf…).
   - **Trocas no `verso-livre.mjs`.** Ele não lê trocas: aplique-as numa cópia temporária do canto
     (com `sed`) e meça a cópia.
   - **Meta.**
     - No `molde.mjs`: nenhum ✗, nenhum ≠, nenhum «leitura natural tem».
     - No `verso-livre.mjs`: nenhum verso marcado (`ralo`, `vazio`, `choques`) e de 2,4 a 2,8 sílabas
       por acento.
     - Versos com 4 átonas seguidas: no máximo uns 20%.
     - Nada de três vogais seguidas (_dia a alegria_).
     - Não repetir o mesmo esqueleto (sobretudo o 2-5-8-11) em versos vizinhos.
   - **Visão compacta.** Para ver um verso por linha, com o esqueleto e os intervalos, use este script
     `.mjs` na sua pasta temporária:
     ```js
     import { readFileSync } from 'node:fs';
     import { medirVerso } from 'file:///C:/Users/geren/OneDrive/Documentos/Onedrive%20do%20Gere/Solar/Editora/Versificador/ferramentas/verso-livre.mjs';
     const [arq, ini] = process.argv.slice(2);
     const ls = readFileSync(arq, 'utf8').replace(/\r/g,'').split('\n').filter(l => l && !l.startsWith('#'));
     let n = Number(ini || 1);
     for (const l of ls) { const m = medirVerso(l); console.log(`${String(n++).padStart(4)} ${String(m.medida).padStart(2)} ${m.acentos.join('-').padEnd(18)} [${m.intervalos.join(' ')}] ${m.marcas.join(',')} ${l}`); }
     ```
     Uso: `node compacto.mjs <canto-com-trocas>.txt <número do primeiro verso>`.

3. **Revisão de sentido.** Confira cada verso com Hall, Gummere e Morris e Wyatt, e com as notas e o
   glossário de Harrison e Sharp, e com os dicionários quando for preciso. Garanta que o sentido está
   certo, claro e sem confusão:
   - sujeito explícito quando o pronome deixaria dúvida;
   - comparações completas;
   - nada de aposição truncada.

   Nas passagens disputadas, siga o texto e o glossário da edição e registre a outra leitura. A
   tradução é nossa: não copie nem parafraseie as referências.

4. **Crítica.** A cada lote, chame um crítico barato (Sonnet, esforço médio), como no passo 8 do
   manual. Ele lê o original, a tradução, o guia e as referências e aponta até 15 problemas reais:
   - sentido;
   - ambiguidade;
   - gramática, crase, colocação, mesóclise;
   - desvio do guia;
   - anglicismo.

   Ele não comenta o ritmo e não edita nada. Recuse as sugestões que o glossário da edição contradiz.
   Confira cada sugestão aceita com o `verso-livre.mjs`.

5. **Notas.** A cada lote, grave `edicoes/beowulf/teste-verso-livre/notas-<NN-NN>.md` no formato de
   `notas.md`:
   - as escolhas;
   - as passagens revistas, com verso, original, leitura adotada e apoio;
   - as reescritas de ritmo (antes, depois, por quê);
   - a tabela final do `verso-livre.mjs` e o resultado do `molde.mjs`;
   - a crítica (o que foi aceito e o que foi recusado, e por quê);
   - nomes e termos novos.

   Não altere os guias: proponha as mudanças nas notas.

## Lotes e conferência

- **Tamanho.** Trabalhe em lotes de 3 a 5 cantos, na ordem.
- **Antes de fechar cada lote:**
  - **Contagem de versos.** O número de versos de cada arquivo traduzido tem de ser igual ao do
    original:
    ```
    grep -vc '^#\|^$' original/NN.txt teste-verso-livre/NN.txt
    ```
  - **Tabulação.** Nenhuma: `grep -c $'\t'` tem de dar 0.
  - **Mesóclise.** O grep de mesóclise não pode achar nada:
    ```
    grep -n -E -o "[A-Za-zÀ-ÿ]+-(lo|la|los|las|o|a|os|as|me|te|se|lhe|lhes|nos|vos|no|na)-(ei|as|á|ás|emos|eis|ão|ia|ias|íamos|íeis|iam)\b" teste-verso-livre/*.txt
    ```
  - **Aspas.** Confira as aspas das falas.
  - **Leitura.** Releia o lote inteiro de uma vez, em voz alta.
- **Commit.** Ao fim de cada lote, faça commit local no branch, com mensagem em português. Não faça
  push nem publique nada sem pedir ao usuário.
- **Outras sessões.** Outras sessões podem estar mexendo em outros worktrees: não toque em nada fora de
  `edicoes/beowulf/teste-verso-livre/`.
- **Relato.** No fim de cada lote, informe ao usuário os números do ritmo, as passagens difíceis e o
  que a crítica mudou.
