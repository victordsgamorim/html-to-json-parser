import urllib3
from bs4 import BeautifulSoup
from datetime import datetime

start = datetime.now()

http = urllib3.PoolManager()
limit = 36
links = []

for page in range(1, 29):
    url = f'https://www.farmaciasportuguesas.pt/catalogo/produtos.html?limit={limit}&p={page}'

    response = http.request('GET', url)
    soup = BeautifulSoup(response.data, "html.parser")

    ul = soup.find("ul", {"class": "row"})
    lis = ul.find_all("li", {'class': 'col-lg-4 col-md-6 col-sm-12 col-xs-12 item'})
    for li in lis:
        links.append(li.find('a').get('href'))

links = "\n".join(links)

with open("../links.txt", "w") as file:
    file.write(links)

end = datetime.now()

print(f'Start {start}')
print(f'End {end}')
print(f'Levou {end - start}')
