# Introdução à vida devota (Filoteia), de São Francisco de Sales — convenções da tradução

Leia antes `edicoes/CONVENCOES-TRADUCAO.md`, com as regras gerais. Este guia acrescenta o que é próprio desta obra e prevalece onde for mais específico. O modelo é `edicoes/santa-teresinha/CONVENCOES.md`.

Na dúvida, a regra é: **fidelidade ao que Francisco de Sales escreveu, em português do Brasil correto, natural e literário**, com a doçura e a clareza dele.

## 1. Texto-fonte

- Os arquivos são `original/00-oracao-e-prefacio.txt` a `05-quinta-parte.txt`. É o texto de 1619 na edição Boulenger (1909), com a ortografia modernizada (ver `original/LEIAME.md`).
- As linhas `# ` do topo são do arquivo, não do livro. Traduza só o `# titulo:`.
- Marcas:
  - `## Chapitre N — Título` → `## Capítulo N — Título traduzido`, com os números romanos como estão.
  - `[I.1]` (parte e capítulo) fica igual, no começo do primeiro parágrafo do capítulo.
- Os sumários das partes («_Contenant ..._») e os subtítulos das meditações (_Préparation_, _Considérations_, _Affections et résolutions_, _Conclusion_, _Faites un bouquet..._) são parágrafos próprios, em itálico. Traduza-os em itálico, no mesmo lugar.
- A numeração «1.», «2.» dos pontos das meditações e dos conselhos é do autor e fica.
- Na conferência, onde o francês parecer errado, veja a edição de Annecy, t. III (link no LEIAME) e registre nas notas.

## 2. Registro e tratamento

- **Tom:** prosa do começo do século XVII, afetuosa, cheia de comparações (abelhas, plantas, pássaros, pedras preciosas, histórias de Plínio e dos Padres), com períodos longos encadeados por *car*, *mais*, *ains*. Guarde o encadeamento e as imagens; não corte nem «arrume» as frases.
- **Vocabulário antigo:** traduza pelo sentido, em português culto atual, sem fingir arcaísmo.

  | francês antigo | sentido / tradução |
  |---|---|
  | *ains* | mas, antes |
  | *icelui*, *icelle* | ele, ela, este, aquele |
  | *meshui* | agora, doravante |
  | *voirement* | verdadeiramente |
  | *ès* | nos, nas, em |
  | *emmi* | no meio de |
  | *partant* | por isso |
  | *jaçoit que* | ainda que |

  Um ou outro torneio de época, quando é natural em português culto, pode ficar.
- **Tratamento:**
  - **Filoteia** é tratada por *vous* → **vós** (*vós*, *vos*, *vosso*, verbo na 2.ª pessoa do plural). Exemplo: «Vous aspirez à la dévotion, très chère Philothée» → «Aspirais à devoção, caríssima Filoteia».
  - **O leitor do Prefácio** é tratado por *tu* → **tu** («Mon cher Lecteur, je te prie» → «Meu caro leitor, peço-te»).
  - **Deus, Jesus e Maria,** nas orações e nos colóquios das meditações, são tratados por *vous* → **vós**.
  - **A própria alma:** quando o autor ou Filoteia fala à própria alma por *tu* («Ô mon âme, sache que...»), fica **tu**; quando por *vous*, fica **vós**.
  - Siga sempre o original, passagem por passagem.
- **Maiúsculas de reverência** onde o texto as põe (*Dieu*, *Seigneur*, *Sauveur*, *Majesté divine*). Pronomes referidos a Deus em minúscula, como no francês.
- **Nunca mesóclise.** Antes de entregar, rode:

  ```
  grep -n -E -o "[A-Za-zÀ-ÿ]+-(lo|la|los|las|o|a|os|as|me|te|se|lhe|lhes|nos|vos|no|na)-(ei|as|á|ás|emos|eis|ão|ia|ias|íamos|íeis|iam)\b" traducao/*.txt
  ```

  Não pode sair nada. Exemplos de solução: *vous direz* → «direis»; *je vous dirai* → «eu vos direi»; *il se fera* → «há de fazer-se».

## 3. Escritura, Padres e citações

- **Escritura:** traduza do francês do autor, que cita de memória ou da Vulgata, às vezes parafraseando. Não copie uma Bíblia portuguesa.
  - As referências, quando ele as dá, vão no formato dele, com os nomes em português.
  - Quando ele não dá referência, não acrescente.
  - Latim que fique em latim no original fica em latim, em itálico.
- **Santos e autores citados:** a forma portuguesa usual.

  | francês | português |
  |---|---|
  | saint Grégoire Nazianzène | são Gregório Nazianzeno |
  | saint Jean Chrysostome | são João Crisóstomo |
  | Jean Cassien | João Cassiano |
  | saint Bernard | são Bernardo |
  | saint Bonaventure | são Boaventura |
  | sainte Catherine de Sienne | santa Catarina de Sena |
  | sainte Élisabeth (de Hongrie) | santa Isabel (da Hungria) |
  | sainte Monique | santa Mônica |
  | saint Louis | são Luís |
  | saint Charles (Borromée) | são Carlos (Borromeu) |
  | sainte Paule | santa Paula |
  | sainte Angèle de Foligno | santa Ângela de Foligno |
  | saint François (d'Assise) | são Francisco (de Assis) |

  Nomes da Antiguidade: Plínio, Aristóteles, Arélio, Glícera, Páusias, Dioscórides. «Saint», com nome, vai em minúscula: *são Paulo*, *santa Teresa*.

- **Versos citados:** são dois dísticos, em III.1 («En son beau vêtement de drap d'or recamé, / Et d'ouvrages divers à l'aiguille semé») e V.18 («A cause des biens que j'attends, / Les travaux me sont passe-temps»). Traduza-os **em verso, pelo método do Versificador**: leia `C:\Users\geren\OneDrive\Documentos\Onedrive do Gere\Solar\Editora\Versificador\traducao\MANUAL-DE-TRADUCAO.md` e o `estudo\ESTUDO-DO-RITMO.md` (§ 5). Mantenha:
  - a medida: alexandrinos → dodecassílabos; octossílabos franceses → a medida portuguesa correspondente, conforme o manual;
  - as rimas emparelhadas e o número de versos.

  Confira com `ferramentas\molde.mjs` até não sobrar ✗ nem ≠, e registre nas notas.

## 4. Vocabulário

| francês | português |
|---|---|
| Philothée | Filoteia |
| la dévotion; dévot, dévote | a devoção; devoto, devota |
| la vie dévote | a vida devota |
| Introduction | Introdução |
| oraison (mentale) | oração (mental) |
| oraison vocale | oração vocal |
| méditation | meditação |
| aspirations; oraisons jaculatoires | aspirações; orações jaculatórias |
| retraite spirituelle (o recolhimento no meio do dia) | retiro espiritual |
| bouquet spirituel | ramalhete espiritual |
| affections; résolutions | afetos; resoluções |
| considérations | considerações |
| préparation | preparação |
| examen de conscience | exame de consciência |
| conducteur, guide (diretor espiritual) | guia, condutor |
| confession; communion | confissão; comunhão |
| la sainte Messe | a santa Missa |
| péché mortel, véniel | pecado mortal, venial |
| affection au péché | afeição ao pecado |
| purgation | purificação |
| tentation; délectation; consentement | tentação; deleite; consentimento |
| inquiétude; tristesse | inquietação; tristeza |
| sécheresses et stérilités spirituelles | securas e esterilidades espirituais |
| la divine Majesté | a divina Majestade |
| Notre-Seigneur | Nosso Senhor |
| la sainte Vierge, Notre-Dame | a santa Virgem, Nossa Senhora |
| l'ange gardien | o anjo da guarda |
| le monde; mondain | o mundo; mundano |
| honnête, honnêteté | honesto, honestidade (no sentido de decoro, pudor: escolha pelo contexto) |
| bals, danses, jeux | bailes, danças, jogos |
| Vive Jésus | Viva Jesus |

Os títulos de obras citadas vão em português quando há forma consagrada (*Confissões*, *Imitação de Cristo*). Os demais ficam como estão, em itálico.

## 5. Tipografia

- **Aspas:** as angulares do original, «...»; dentro delas, “...”.
- **Itálico:** `_assim_`, onde o texto o tem.
- **Pontuação** e reticências como no original. Os pontos de exclamação das orações ficam; o espaço antes de «!», «?», «;» e «:» do francês desaparece em português.
- **Abreviaturas:** *S.* → *são*/*santo*/*santa*, por extenso.

## 6. Formato de saída

- Cada arquivo traduzido vai para `traducao/<mesmo nome>.txt`, com o cabeçalho `# titulo: <título traduzido>`. Por exemplo, «Primeira parte da Introdução» e «Terceira parte da Introdução, capítulos I a XIII».
- Depois vem o texto: **um parágrafo traduzido para cada parágrafo do original, na mesma ordem**, com os títulos `## ` e as marcas `[I.1]` no mesmo lugar.
- Versos com `| `, um por linha.
- As notas do tradutor vão em `traducao/notas-<arquivo>.md` (ver as regras gerais, § 4): termos novos, passagens difíceis, versos, conferências com Annecy.
