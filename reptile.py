from requests_html import AsyncHTMLSession
import asyncio
asession = AsyncHTMLSession()
class Reptile:
    def __init__(self,url:str) -> None:
        self.url=url
        self.price_class_table={
            'www.amazon.com' : '.a-price',
            'www.alternate.de' : 'price',
            'www.newegg.com':'price-current'
        }
        self.web_header={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0',
            'Accept': '*/*',
            'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'Cookie': 'session-id=138-8109177-6343214; Domain=.amazon.com; Expires=Sat, 06-May-2023 06:01:04 GMT; Path=/; Secure, session-id-time=2082787201l; Domain=.amazon.com; Expires=Sat, 06-May-2023 06:01:04 GMT; Path=/; Secure, i18n-prefs=USD; Domain=.amazon.com; Expires=Sat, 06-May-2023 06:01:04 GMT; Path=/, sp-cdn="L5Z9:TW"; Version=1; Domain=.amazon.com; Max-Age=31536000; Expires=Sat, 06-May-2023 06:01:04 GMT; Path=/; Secure; HttpOnly, skin=noskin; path=/; domain=.amazon.com',
            'TE': 'Trailers'}
    async def get_amazon(self):
        r = await asession.get(self.url,headers=self.web_header)
        return r
    
    def get_price(self,url:str) -> str:
        results = asession.run(self.get_amazon())
        for result in results:
            pricce=result.html.find(self.price_class_table.get(url.split("/")[2]),first=True).text
            print(pricce)

if __name__ == '__main__':
    reptile=Reptile('https://www.amazon.com/Thermaltake-TOUGHRAM-Motherboard-Syncable-R016D408GX2-3600C18A/dp/B08XWK554J/ref=sr_1_3?crid=1WCLJPD9DV8ER&dchild=1&keywords=toughram+xg+rgb&qid=1615956921&sprefix=toughram+XG%2Caps%2C347&sr=8-3')
    reptile.get_price('https://www.amazon.com/Thermaltake-TOUGHRAM-Motherboard-Syncable-R016D408GX2-3600C18A/dp/B08XWK554J/ref=sr_1_3?crid=1WCLJPD9DV8ER&dchild=1&keywords=toughram+xg+rgb&qid=1615956921&sprefix=toughram+XG%2Caps%2C347&sr=8-3')





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