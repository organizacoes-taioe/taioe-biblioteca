import re, sys
p = sys.argv[1]
t = open(p, encoding='utf-8').read().replace('\u2019', "'")
out = []
for b in t.split('\n\n'):
    if b.startswith(('| ', '## ', '# ')):
        out.append(b.replace("'", '′')); continue
    b = re.sub(r"(?<=[A-Za-z₁₂₃₄])'", '′', b)
    b = re.sub(r"(?<![\w_′.])(X′?)(?=-Achse)", r'_\1_', b)
    b = re.sub(r"(?<![\w_′])([xyztKcvabrλμσF]′?|x[₁₂₃₄]′?)(?![\w_′-])(?!\. [Bh]\.)", r'_\1_', b)
    b = re.sub(r"\((\d+) ?_?([ab])_?\)", r"(\1\2)", b)
    b = re.sub(r"\(_?(\d+)_? ?_([ab])_\)", r"(\1\2)", b)
    out.append(b)
open(p, 'w', encoding='utf-8').write('\n\n'.join(out))
