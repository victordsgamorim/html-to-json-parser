from datetime import datetime

import html_to_json
import urllib3
from bs4 import BeautifulSoup

import json

start = datetime.now()

http = urllib3.PoolManager()

with open("links.txt") as f:
    for line in f:
        url = line.strip()
        productName = url.split("/")[-4]

        response = http.request('GET', url)
        soup = BeautifulSoup(response.data, "html.parser")

        myDiv = soup.find("div", {"class": "ANFproduct product-essential"})

        for script in myDiv(["script", "style"]):
            script.decompose()

        with open(f"html/{productName}.html", "w") as file:
            file.write(str(myDiv))

        with open(f"html/{productName}.html", "r") as html_file:
            html = html_file.read().replace("\n", "").strip()
            output_json = html_to_json.convert(html)
            with open(f"json/{productName}.json", "w") as file:
                json.dump(output_json, file)

end = datetime.now()

print(f'Start {start}')
print(f'End {end}')
print(f'Levou {end - start}')
