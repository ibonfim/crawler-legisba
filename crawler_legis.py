from bs4 import BeautifulSoup
from urllib.request import urlopen
import json



html= urlopen('https://www.legislabahia.ba.gov.br/')
bs= BeautifulSoup(html.read(),'html.parser')
#print(bs)
seletor='.view-categorias-de-documento > div:nth-child(1) > table:nth-child(1) > tbody:nth-child(1) > tr > td > a'
td_elements= bs.find_all('td', {'class':'views-field views-field-name views-align-left'})
links=[]

#coleta os links da primeira página do site de legis
for td in td_elements:
    a_tags=td.find_all('a',href=True)
    for a in a_tags:
        link= 'https://www.legislabahia.ba.gov.br' + a['href']
        links.append(link)

#print (links)

#acessa cada legislação
def acessa_links(urls):
    if type(urls)==list:
        for link in urls:
            html= urlopen(link)
            bs= BeautifulSoup(html.read(),'html.parser')
            
            print(bs)
            return bs
    else:
        html= urlopen(urls)
        bs= BeautifulSoup(html.read(),'html.parser')
        return bs



 
acessa_links(links)

print (acessa_links)

# html_str = str(bs)
# data={
#     'html':html_str 
    
# }
#json_data = json.dumps(data, indent=4)
# file_name = 'pagina.json'
# # Gravar o JSON em um arquivo
# with open(file_name, 'w', encoding='utf-8') as file:
#     json.dump(data, file, ensure_ascii=False, indent=4)