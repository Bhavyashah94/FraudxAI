import urllib.request, xml.etree.ElementTree as ET, ssl, sys
sys.stdout.reconfigure(encoding='utf-8')
ctx = ssl._create_unverified_context()
ids = ['2607.14686', '2602.06955', '2601.05578']
id_str = ','.join(ids)
url = f'http://export.arxiv.org/api/query?id_list={id_str}'
req = urllib.request.Request(url, headers={'User-Agent': 'FraudxAI/1.0'})
with urllib.request.urlopen(req, context=ctx) as r:
    root = ET.fromstring(r.read())
ns = {'atom': 'http://www.w3.org/2005/Atom'}
for e in root.findall('atom:entry', ns):
    print('TITLE:', e.find('atom:title', ns).text.strip().replace('\n', ' '))
    print('ID:', e.find('atom:id', ns).text.strip().split('/abs/')[-1])
    print('DATE:', e.find('atom:published', ns).text.strip()[:10])
    print('SUMMARY:\n', e.find('atom:summary', ns).text.strip())
    print('='*60)
