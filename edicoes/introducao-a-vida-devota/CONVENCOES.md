# Introdução à vida devota (Filoteia), de São Francisco de Sales — convenções da tradução

Leia antes `edicoes/CONVENCOES-TRADUCAO.md`, com as regras gerais. Este guia acrescenta o que é próprio desta obra e prevalece onde for mais específico. O modelo é `edicoes/santa-teresinha/CONVENCOES.md`.

Na dúvida, a regra é: **fidelidade ao que Francisco de Sales escreveu, em português do Brasil correto, natural e literário**, com a doçura e a clareza dele.

## 1. Texto-fonte

- Os arquivos são `original/00-oracao-e-prefacio.txt` a `05-quinta-parte.txt`. É o texto de 1619 na edição Boulenger (1909), com a ortografia modernizada, emendado em 233 pontos pela colação com a edição de Annecy (lacunas de linha, palavras, números de ponto, pontuação; ver `original/LEIAME.md`). A tradução acompanha o texto emendado.
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
| affections; résolutions (da meditação) | afetos; resoluções (as inclinações do coração são «afeições»: ver § 7) |
| considérations | considerações |
| préparation | preparação |
| examen de conscience | exame de consciência |
| conducteur, guide (diretor espiritual) | guia (nunca «condutor») |
| confession; communion | confissão; comunhão |
| la sainte messe | a santa missa (minúscula, como no original) |
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

## 7. Termos fixados na harmonização

Fixados ao harmonizar as oito partes (outubro de 2026). Prevalecem sobre o que vai acima e sobre as notas dos tradutores (`traducao/notas-*.md`), que ficam como registro do trabalho. O relatório está em `traducao/HARMONIZACAO.md`.

### Texto

- **Original emendado.** A tradução segue o texto francês emendado por Annecy (233 pontos; lista no `original/LEIAME.md`): as sete lacunas de linha (I.20, II.4, II.19, II.20, II.21, III.3, III.38), as palavras que mudam o sentido, as palavras omitidas e os números de ponto (V.2 «6.», V.4 «10.», V.5 «6.»).
- **Lições de Boulenger que ficam** (variantes das edições anteriores, preferidas por ele e mantidas no original): I.4 «envers sa mère», «ne le considérez pas»; III.3 «désirais», «peines». A tradução as segue.
- **Nomes que Annecy corrige contra 1619.** O original fica com a lição de 1619; a tradução segue a correção, sem nota no corpo, e a apresentação da edição («Sobre esta tradução») registra o fato. Regra única:
  - Prefácio: «Campaspe» (1619: *Compaspé*);
  - I.4: «Catarina de Cardona» (1619: *Cordoue*);
  - I.15: «as palavras de Isaías» (1619: *Job*; a citação é de Is 33,14);
  - III.40: «Salvina», a destinatária da carta 79 de são Jerônimo (1619 e Annecy: *Salvia*).
- **Aspas que Boulenger abre e não fecha** (I.4, I.14, I.15, I.17, III.14, III.18, III.21, III.27, IV.1, IV.12, V.2, V.4): a tradução fecha onde a fala termina. O original fica como está.
- **Dísticos** (III.1 e V.18): em verso, pelo Versificador, conferidos com `molde.mjs` (sem ✗ nem ≠). O segundo verso começa com maiúscula, como no original.

### Vocabulário

| francês | português | observação |
|---|---|---|
| conducteur; guide | guia | «condutor» não se usa; *celui qui conduit votre âme* → «aquele que guia a vossa alma» |
| directeur | diretor | |
| père spirituel | pai espiritual | |
| affections (atos da meditação) | afetos | «Afetos e resoluções»; «passareis aos afetos» |
| affection(s) (inclinação, apego) | afeição, afeições | «afeição ao pecado», «pôr a afeição», «as boas afeições das mães» |
| douceur (virtude) | doçura | também IV.1, IV.11, V.11; *les douceurs* (consolações) → «doçuras» ou «suavidades» |
| débonnaireté; débonnaire | mansidão; manso | também quando dito de Deus («liberal em mansidão», «meu Salvador manso», «ó Pai manso») |
| Apprenez de moi que je suis doux et humble de cœur | «manso e humilde de coração» | forma consagrada de Mt 11,29 |
| empressement; s'empresser; empressé | afã; afanar-se; afanoso | nunca «sofreguidão», «ânsia», «açodado»; a pressa concreta fica «pressa», «apressar-se» (I.13, IV.1) |
| souci; sollicitude; inquiétude | preocupação; solicitude; inquietação | |
| avancement; s'avancer | progresso; progredir, avançar | nunca «adiantamento» |
| renommée | fama | *réputation* → «reputação» |
| ire; colère; courroux | ira; cólera; irritação | |
| conversation (trato social, reuniões, visitas) | conversação, conversações | inclusive «a mútua conversação» (III.38–39) e «a conversação dos mundanos» (III.40) |
| conversation particulière; devis; entretien | conversa | «conversas familiares», «toda conversa particular, toda conversa secreta» |
| bonne conversation (eutrapelia) | boa conversação | |
| amourettes | namoricos | |
| honnêteté; honnête | honestidade; honesto | exceção: III.24, *conversations qui ont pour leur fin l'honnêteté* → «cortesia» |
| recherche (amorosa) | corte | |
| mugueter; muguetterie | galantear; galanteio | *muguetteries* do cabelo (III.25) → «faceirices» |
| protestation; protester | protestação; protestar | *je proteste* (dito de quem fala mal, III.29) → «asseguro» |
| avis | avisos | o parecer de uma pessoa → «parecer» |
| loisir | vagar | |
| vacation | vocação | |
| dîner; souper; collation | almoço; ceia; colação | nunca «jantar» |
| potirons; champignons (III.33) | cogumelos; fungos | nunca «tortulhos»; em IV.13 *champignons* → «cogumelos» |
| mouchons; avettes | crias; abelhinhas | |
| élancements | impulsos | |
| saint Antoine (o abade) | santo Antão | |
| messe | missa | minúscula |

### Nomes

Raab; padre Gracián; madre Teresa (sempre em minúscula, como «padre Arias», «padre João Cassiano»); Godofredo de Péronne; o senhor Gautier de Nemours; Du Pont (como o autor escreve); Capilia; Granada; Mitridates; Elzeário, conde de Ariano; lago de Rieti; a mãe de são Sinforiano (Annecy e o original emendado: *de saint Symphorien*).

### Tratamento e fórmulas

- Vocativos: *très chère Philothée* → «caríssima Filoteia»; *chère Philothée* → «cara Filoteia» (nunca «querida Filoteia»); *ma Philothée* → «minha Filoteia»; *ma chère Philothée* → «minha cara Filoteia».
- Fórmulas das meditações: «Ponde-vos na presença de Deus» (*devant Dieu* → «diante de Deus»); «Suplicai-lhe que vos inspire» (*Suppliez-le*), «Pedi-lhe que vos inspire» (*Priez-le*); *Priez Dieu qu'il* → «Pedi a Deus que»; *Priez.* → «Orai»; o refrão «Agradecei, oferecei, orai».
- Pronomes combinados: nunca «no-lo», «no-la», «vo-lo», «vo-la», «lho», «lha», «lhos». Reescrever: «Deus as deu a nós», «se o vosso pai espiritual não vos mandar expressamente».
- *Celui* referido a Deus ou a Cristo: «Aquele», «Daquele» (sem apóstrofo).
