import urllib.request
from bs4 import BeautifulSoup
import requests
class Reptile:
    def __init__(self) -> None:
        self.price_class_table={
            'www.amazon.com' : 'a-text-price',
            'www.alternate.de' : 'price',
            'www.newegg.com':'price-current'
        }
    def get_price(self):
        url='https://www.amazon.com/Thermaltake-TOUGHRAM-Motherboard-Syncable-R009D408GX2-3600C18B/dp/B07XVZHHXS/ref=sr_1_2?dchild=1&keywords=Thermaltake%2BTOUGHRAM%2BRGB&qid=1613613259&sr=8-2&th=1'
        web_header={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0',
        'Accept': '*/*',
        'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        'Cookie': '你的cookie值',
        'TE': 'Trailers'}
        r = requests.get(url,headers=web_header)
        print(r.status_code)
        # response = urllib.request.urlopen("https://www.amazon.com/Thermaltake-TOUGHRAM-Motherboard-Syncable-R009D408GX2-3600C18B/dp/B07XVZHHXS/ref=sr_1_2?dchild=1&keywords=Thermaltake%2BTOUGHRAM%2BRGB&qid=1613613259&sr=8-2&th=1")
        # print(response)
        # soup = BeautifulSoup(response.text, "html.parser")
        # print(soup.find("span"))  #輸出排版後的HTML內容
        
if __name__ == "__main__":
    reptile=Reptile()
    reptile.get_price()