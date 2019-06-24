#!/usr/bin/python3

import sys
import requests
from bs4 import BeautifulSoup
from googlesearch import search

q=' '.join(sys.argv[1:])
print("Query: " + q)

s=search(q, stop=5)

for url in s:
    print("Result URL: " + url)

    # Get first result
    page=requests.get(url)

    # find all code blocks
    soup = BeautifulSoup(str(page.content), features="lxml")
    code = soup.findAll('code')

    for block in code:
        # replace br
        for br in block.find_all("br"):
            br.replace_with("\n")

        # Print out one by one
        print(block.decode_contents())
        input("\n\nPress Enter for next code block...\n")

    if len(code) > 0:
        break
    else:
        print("No solution found, checking next URL")

    

