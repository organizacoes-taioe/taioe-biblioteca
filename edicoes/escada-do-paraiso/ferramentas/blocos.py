import sys, json, os, re
b = json.load(open(os.path.expanduser('~/.cache/claude-pedidos-0511/escada-do-paraiso/blocos.json'), encoding='utf-8'))
for i in range(int(sys.argv[1]), int(sys.argv[2])):
    t = re.sub(r'\{PG[^}]*\}\s*', '', b[i]['texto'])
    print(i, next((p[1] for p in b[i]['pal'] if p[1]), ''), len(t.split()), t[:int(sys.argv[3]) if len(sys.argv) > 3 else 90])
