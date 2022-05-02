from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Reptile:
    def __init__(self) -> None:
        self.price_class_table={
            'www.amazon.com' : 'a-text-price',
            'www.alternate.de' : 'price',
            'www.newegg.com':'price-current'
        }
        self.chromedriver_path = "chromedriver.exe"

    def get_price(self,url:str) -> str:
        driver = webdriver.Chrome(self.chromedriver_path)
        driver.get(url)
        price=driver.find_element_by_class_name(self.price_class_table.get(url.split("/")[2])).text
        return price









    # with open('output.csv','w', newline='') as csvfile:
    #     writer = csv.writer(csvfile)
    #     for url in urls:
    #         driver.get(url)
    #         # search = driver.find_element_by_class_name("shopee-searchbar-input__input")
    #         # search.send_keys("彼特必")
    #         # search.send_keys(Keys.RETURN)
    #         time.sleep(5)
    #         productTitle=driver.find_element_by_id("productTitle")
    #         titles = driver.find_element_by_class_name("a-text-price")
    #         # for title in titles:
    #         print(titles.text)
    #         # 寫入csv
    #         writer.writerow([productTitle.text, titles.text])
    #         time.sleep(1)
    #         # 開啟輸出的 CSV 檔案