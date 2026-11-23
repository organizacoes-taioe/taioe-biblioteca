import json, urllib.request, urllib.parse, os, sys, time
D = os.path.join(os.environ.get('URAGUAI_CACHE') or os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'ferramentas', 'cache', 'o-uraguai'), 'ws1769')
UA = {'User-Agent': 'biblioteca-script/1.0'}
def get(params):
    url = 'https://pt.wikisource.org/w/api.php?' + urllib.parse.urlencode(params)
    return json.load(urllib.request.urlopen(urllib.request.Request(url, headers=UA)))
titles = ['Página:O Uraguay.djvu/%d' % i for i in range(1, 115)]
for k in range(0, len(titles), 40):
    d = get({'action': 'query', 'titles': '|'.join(titles[k:k+40]), 'prop': 'revisions', 'rvprop': 'content', 'rvslots': 'main', 'format': 'json'})
    for p in d['query']['pages'].values():
        n = int(p['title'].rsplit('/', 1)[1])
        if 'revisions' not in p: print('falta', n); continue
        open(os.path.join(D, '%03d.txt' % n), 'w').write(p['revisions'][0]['slots']['main']['*'])
    time.sleep(1)
