# PN 39 — Um Doutor Santo e Célebre — notas do tradutor

**Metro do original.** Octossílabo francês sem cesura fixa (8 sílabas até a última tônica, e mudo final = +1); o v. 4 («N'a-t-il pas un cœur de feu ?...») tem 7 sílabas nos dois testemunhos, e a tradução o mantém curto.

**Metro da tradução.** Octossílabo com a 4.ª obrigatória (`8: 4`); o v. 4 em redondilha maior (`7: 3`, sem acento na 6.ª), no mesmo lugar do verso curto de Teresa.

**Rimas.** Septilha ABABCBC, como no original: grave nos ímpares (*empresa / defesa*, *porfia / Maria*) e aguda nos pares (*não / coração / multidão*, que respondem a *Dieu / feu / aveu*).

**Forma especial.** O poema é um acróstico do nome de Francis La Néele (FRANCIS). A tradução guarda as mesmas iniciais, verso a verso: **F**rancis, **R**endo-me, **A**ssim, **N**ão, **C**ontra, **I**sto, **S**ó. No arquivo-fonte as iniciais vêm separadas por espaço («F rancis», «R ien»...) para marcar o acróstico; no `original.txt` e na tradução ficam juntas.

**Escolhas e perdas.** A rima com *Igreja*/*defesa* e o acróstico estreitaram o v. 1: *devise* virou *empresa*, que em português é também o termo de heráldica para emblema com divisa (Houaiss) e, no sentido comum, «aquilo que alguém se propõe»; os dois sentidos servem. O lema (v. 2) ficou na primeira pessoa, como em Teresa, mas reformulado para começar por R: *Rendo-me a Deus; ao homem, não* (cedem *tout* e *mon*; a antítese homem / Deus fica). No v. 3, *pour défendre l'Église* → *da Igreja na defesa* (hipérbato). No v. 4, o *cœur de feu* virou o coração que *flameja*. No v. 5, *combattant la science impie* → *contra o saber sem Deus porfia*: *saber* por *science* e *sem Deus* por *impie* (sinônimos, para a rima em -ia com *Maria*), e o particípio virou verbo (*porfia*, «luta com insistência»). No v. 6, *il en a fait bien haut l'aveu* → *isto confessa à multidão*: *confessa* é o *aveu*, *à multidão* faz as vezes de *bien haut* (confissão pública). No v. 7, *sa gloire est celle de Marie* → *só tem por glória a de Maria*: o «só» explicita o que a frase francesa diz pela equação (a glória dele é a de Maria, não outra); a forma literal *Sua glória é a de Maria* dava choque 3-4 no molde. Nenhuma imagem central foi trocada.

**Cabeçalho.** Título do arquivo dos Arquivos («Un Docteur Saint et Célèbre»; no site antigo ele vem depois da data). Destinatário e data das notas do arquivo. A assinatura brincalhona *L'enfant du Docteur séraphique : / Sainte Thérèse* foi para `# assinatura` como *A filha do Doutor seráfico: / Santa Teresa*; *enfant* (sem gênero em francês) ficou *filha*, porque quem assina é Teresa e *a criança do Doutor* soaria estranho; o *Doutor seráfico* fica literal, sem resolver a alusão (Francis, «Docteur» de profissão, com o nome do Seráfico de Assis). Francis fica em francês: não é santo, e o nome é o próprio acróstico.

**Testemunhos.** O site antigo traz o mesmo texto (com «Francis» sem o espaço e «coeur» por «cœur»); nenhum dos dois indica ária.

**Conferência.** `molde.mjs traducao.txt traducao-molde.txt`: 7 ✓, 0 ~, 0 ✗, 0 ≠; nenhuma leitura forçada. Linha final:

```
7 versos: 7 exatos, 0 aceitáveis, 0 falhos, 0 fora da medida; forçamento médio 0; custo total 1.5
```

Grep de mesóclise: nada. Esqueletos: 2-4-8, 1-4-6-8, 2-4-8, 1-3-7, 4-6-8, 1-4-8, 1-2-4-8 (sem três iguais seguidos).

**Revisão após a crítica.**
- V. 4: «Não flameja o coração?...» → «Não lhe abrasa o coração?...»: o *lhe* devolve o dono do coração (*n'a-t-il pas*), e *abrasar* (arder, estar em brasa) guarda o *feu*; acróstico N mantido. `molde.mjs`: 7 ✓, 0 ~, 0 ✗, 0 ≠.
