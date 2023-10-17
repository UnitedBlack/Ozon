import requests
import pandas as pd
from lxml import etree
import os
from lxml import html

TRUSIKI = "http://stripmag.ru/cat.php?id=316&show=30"
PIZHAMKI = "http://stripmag.ru/cat.php?id=269&show=30"
VIBRATORI = "http://stripmag.ru/cat.php?id=3&show=5000"

# login_url = "https://stripmag.ru/user.php?stop=1"  # Замените на URL страницы входа
# username = "alekseiybro"  # Замените на ваше имя пользователя
# password = "palatlerspe"  # Замените на ваш пароль

# # Отправляем запрос на вход в систему
# session_requests = requests.session()
# login_payload = {
#     "username": username, 
#     "password": password, 
# }
# headers = {
#        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3',
#    }
# result = session_requests.post(
#     login_url, 
#     data = login_payload, 
#     headers = headers
# )

# # Проверяем, успешно ли прошел вход
# if result.status_code == 200:
#     print("Вход в систему выполнен успешно")
# else:
#     print("Ошибка входа в систему")

# url = VIBRATORI  # URL страницы, которую вы хотите обработать
# result = session_requests.get(
#     url, 
#     headers = dict(referer = url)
# )

# # Парсим страницу с помощью lxml
# tree = html.fromstring(result.content)
# some_data = tree.xpath('//tr/td[@align="LEFT"]/a//@href')  # Ваш XPath
# print(len(some_data))
# url = 'https://stripmag.ru/prod.php?id=251223'
# result = session_requests.get(
#     url, 
#     headers = dict(referer = url)
# )
# tree = html.fromstring(result.content)
# some_data = tree.xpath('//tr[2]/td[@class="small"][2]/text()')
# print(some_data)



def get_product_specs(url):
    html = requests.get(url).text
    print(1)
    root = etree.HTML(html)
    print(2)
    product_page = ["https://stripmag.ru" + item for item in root.xpath('//tr/td[@align="LEFT"]/a//@href')]
    print(3)
    product_page_html = [requests.get(item).text for item in product_page]
    print(4)
    root_product_page = [etree.HTML(item) for item in product_page_html]
    print(5)
    
    product_price = [item.xpath('//b[@class="red"][1]/text()')[0] for item in root_product_page]
    print(6)
    product_name = [item.xpath('//h1[1]/text()[1]')[0] for item in root_product_page]
    print(7)
    product_aID_and_barcode = [item.xpath('//tr[2]/td[@class="small"][2]/text()')[0] for item in root_product_page]
    return product_price, product_name, product_aID_and_barcode
    
    
price, name, aID_barcode = get_product_specs(VIBRATORI)
print(len(price))
print(len(name))
# print(aID_barcode)

# df = pd.read_excel('output.xlsx', engine='openpyxl')

# # Вывод первых 5 строк DataFrame
# print(df.head())

# # Изменение данных в DataFrame
# df['hueta'] = df['hueta2'] * 2

# # Запись DataFrame обратно в Excel
# df.to_excel('output.xlsx', index=False)

# trusiki_html = requests.get(TRUSIKI).text
# pizhamki_html = requests.get(PIZHAMKI).text
# vibratori_html = requests.get(VIBRATORI).text

# root_trusiki = etree.HTML(trusiki_html)
# root_pizhamki = etree.HTML(pizhamki_html)
# root_vibratori = etree.HTML(vibratori_html)

# trusi_product_page = ["https://stripmag.ru" + trusiki for trusiki in root_trusiki.xpath('//tr/td[@align="LEFT"]/a//@href')]
# pizhamki_product_page = ["https://stripmag.ru" + pizhamki for pizhamki in root_pizhamki.xpath('//tr/td[@align="LEFT"]/a//@href')]
# vibratori_product_page = ["https://stripmag.ru" + vibratori for vibratori in root_vibratori.xpath('//tr/td[@align="LEFT"]/a//@href')]

# trusiki_product_page_html = [requests.get(item).text for item in trusi_product_page] 
# pizhamki_product_page_html = [requests.get(item).text for item in pizhamki_product_page] 
# vibratori_product_page_html = [requests.get(item).text for item in vibratori_product_page] 

# root_trusiki_pp = [etree.HTML(item) for item in trusiki_product_page_html]
# root_pizhamki_pp = etree.HTML(pizhamki_product_page_html)
# root_vibratori_pp = etree.HTML(vibratori_product_page_html)

# trusiki_price = [item.xpath('//b[@class="red"][1]/text()')[0] for item in root_trusiki_pp]
# pizhamki_price = root_pizhamki_pp.xpath('//b[@class="red"][1]/text()')[0]
# vibratori_price = root_vibratori_pp.xpath('//b[@class="red"][1]/text()')[0]

# trusiki_name = [item.xpath('//h1[1]/text()[1]')[0] for item in root_trusiki_pp]


# //h1[1]/text()[1] - название

# //td[@valign][2]/b/@class
# //b[@class="red"][1]/text()

"""
Артикул
Цена
НДС %
Вес
Ширина, высота, длина упаковки
Ссылка на пикчу
Бренд
Длина см
Тип

"""
# cd - change directory 
# cd .. - вернуться назад
# cd tab x2 показывает папки доступые ладно это только для линуксоидов
# тебе нужно смотреть на то где у тебя консолль находится приучайся к этой хуйне
# попрыгай щас по папкам поперемещайс ls показывает файлы и папки вот слева видишь ключи d это директория
