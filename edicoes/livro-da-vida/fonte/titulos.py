import json,re
P=json.load(open('dl/bmc1_pags.json'))
txt=[]
for p,ls in P[527:533]:
    for a,b,c,d,t,par in ls:
        t=t.strip()
        if re.fullmatch(r'(INDICE|DE CAPITULOS|P[áa]gin[ae]s\.?|\d+)', t): continue
        txt.append(t)
s='\n'.join(txt)
s=s[s.index('CAPITULO PRIMERO'):]
s=re.sub(r'-\s*\n','',s).replace('\n',' ')
ps=re.split(r'CAP[IÍ]TULO\s+(?:PRIMERO|[IVXLC]+(?:\s?[IL])?)\s*[.,]?\s*[—–-]+\s*', s)[1:]
out=[]
for t in ps:
    t=re.sub(r'[\s.,…]*\b[\dvxlcui*?]{1,4}\s*$','',t.strip())
    t=re.sub(r'[\s.,]+$','',t)
    t=t.replace("'",'').replace('<é!','él').replace('cosas muy subidas;,','cosas muy subidas,').replace('causa^','causa').replace('tina persona','una persona').replace('la hecho','le ha hecho')
    t=re.sub(r'\s+v$','',t.strip()); t=re.sub(r'[\s.]*\d+\s*DE CAPITULOS$','',t); t=re.sub(r'\s*1\*7 P[áa]ginas$','',t)
    out.append(t.strip().rstrip('.')+'.')
print(len(out))
json.dump(out,open('dl/titulos.json','w'),ensure_ascii=False,indent=0)
