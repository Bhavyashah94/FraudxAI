import urllib.request
import urllib.parse
import xml.etree.ElementTree as ET
import sys

sys.stdout.reconfigure(encoding='utf-8')

# Search arXiv API for credit card fraud and explainable / SHAP
query = 'all:"credit card fraud" AND (all:"explainable" OR all:"SHAP" OR all:"interpretable")'
url = f'http://export.arxiv.org/api/query?search_query={urllib.parse.quote(query)}&start=0&max_results=10&sortBy=submittedDate&sortOrder=descending'

import ssl
ctx = ssl._create_unverified_context()
req = urllib.request.Request(url, headers={'User-Agent': 'FraudxAI-Research/1.0'})
try:
    with urllib.request.urlopen(req, context=ctx) as resp:
        xml_data = resp.read()
    
    root = ET.fromstring(xml_data)
    ns = {'atom': 'http://www.w3.org/2005/Atom'}
    
    entries = root.findall('atom:entry', ns)
    print(f"Total entries found: {len(entries)}\n")
    
    for i, entry in enumerate(entries, 1):
        title = entry.find('atom:title', ns).text.strip().replace('\n', ' ')
        published = entry.find('atom:published', ns).text.strip()[:10]
        summary = entry.find('atom:summary', ns).text.strip().replace('\n', ' ')
        id_url = entry.find('atom:id', ns).text.strip()
        arxiv_id = id_url.split('/abs/')[-1]
        authors = [a.find('atom:name', ns).text.strip() for a in entry.findall('atom:author', ns)]
        
        print(f"[{i}] {title}")
        print(f"    arXiv ID: {arxiv_id} | Date: {published} | Authors: {', '.join(authors[:3])}")
        print(f"    Summary: {summary[:250]}...\n")

except Exception as e:
    print("Error querying arXiv:", e)
