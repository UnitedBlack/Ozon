from playwright.sync_api import sync_playwright
import time

class OZON():

    def __init__(self):
        self.TRUSIKI = "http://stripmag.ru/cat.php?id=316&show=30"
        self.PIZHAMKI = "http://stripmag.ru/cat.php?id=269&show=30"
        self.VIBRATORI = "http://stripmag.ru/cat.php?id=3&show=30"

    def product_info(self, page):
        for item in self.all_products:
            page.goto(item, wait_until="domcontentloaded")
            name = page.query_selector('//h1[1]').text_content()
            price = page.query_selector('b[class="price"]').text_content()
            #aID = page.query_selector('//tr[2]/td[@class="small"][2]').text_content()
            texts = page.locator('//tr[2]/td[@class="small"][2]').all_inner_texts()
            aID = texts[0] if texts else None
            # barcode = page.query_selector('//tr[2]/td[@class="small"][2]/text()[2]').text_content()
            print(aID)

            time.sleep(10)
            # print(name)
            # print(price)
            


    def all_product_links(self, page):
        page.goto(self.VIBRATORI, wait_until="domcontentloaded")
        self.all_products = ["https://stripmag.ru" + item for item in [item.get_attribute('href') for item in page.query_selector_all("//tr/td[@align='LEFT']/a")]]
        time.sleep(2)
        # print(len(all_products))
        # print(all_products)
        self.product_info(page)

    def login(self, page):
        print("Logging in")
        page.goto("https://stripmag.ru/user.php?", wait_until="domcontentloaded")
        page.wait_for_selector('//tr[1]/td[2]/input[1]', timeout=3000)
        page.query_selector('//tr[1]/td[2]/input[1]').fill('alekseiybro')
        page.query_selector('//tr[2]/td[2]/input[1]').fill('palatlerspe')
        page.query_selector('//tr[3]/td[2]/input[1]').click()
        time.sleep(2)
        self.all_product_links(page)

    def initialize(self):
        with sync_playwright() as playwright:
            browser = playwright.firefox.launch(headless=False) 
            context = browser.new_context() 
            page = context.new_page()
            self.login(page)

    # initialize()

ozon = OZON()
ozon.initialize()

# cum потом убери
# короче если у тебя будет гига ебка с данными и/или надо будет запускать код из другого файла
# то ебашь классы, если все тупо и просто то тупо функциями все делай и все а какая может быть ебка с данными
# когда тебе нужно передавать переменную между функциями в не зависимости от того какая она по очереди идет лан то есть
# мне щас как нормальный русский человек сверху вниз писать или как еблан да, снизу вверх вот логин у тебя первая функция инит вторая
# и тип вконце каждой функции вызывать ту что выше да ну да бля ебаная залупа
# ладно давай я короче чернорабочий пидарас раб плиточник а ты прораб рефакторер тим лид енжинир ахахахха да ну говна напиши я отрефакторю если будет нужда
# лан все давай надеюсь разберусь ну если че пиши все я пошел