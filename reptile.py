from requests_html import AsyncHTMLSession
import asyncio

asession = AsyncHTMLSession()
class Reptile:
    def __init__(self,url:str) -> None:
        self.url=url
        self.url_dict={
            'www.amazon.com' : {
                'class_name':'.a-price',
                'use_function':self.get_amazon
                },
            'www.alternate.de' :{
                'class_name':'price',
                'use_function':self.get_alternate
                },
            'www.newegg.com':{
                'class_name':'price-current',
                'use_function':self.get_newegg
                },
            }
        self.web_header={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0',
            'Accept': '*/*',
            'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'Cookie': 'session-id=138-8109177-6343214; Domain=.amazon.com; Expires=Sat, 06-May-2023 06:01:04 GMT; Path=/; Secure, session-id-time=2082787201l; Domain=.amazon.com; Expires=Sat, 06-May-2023 06:01:04 GMT; Path=/; Secure, i18n-prefs=USD; Domain=.amazon.com; Expires=Sat, 06-May-2023 06:01:04 GMT; Path=/, sp-cdn="L5Z9:TW"; Version=1; Domain=.amazon.com; Max-Age=31536000; Expires=Sat, 06-May-2023 06:01:04 GMT; Path=/; Secure; HttpOnly, skin=noskin; path=/; domain=.amazon.com',
            'TE': 'Trailers',
            }
    
    async def get_amazon(self):
        r = await asession.get(self.url,headers=self.web_header)
        return r
    
    async def get_alternate(self):
        r = await asession.get(self.url)
        print(r)
        return r
    
    async def get_newegg(self):
        r = await asession.get(self.url)
        print(r.text)
        return r
    
    def get_price(self) -> str:
        # 網站選擇
        item = self.url_dict.get(self.url.split("/")[2])
        usefunction=item.get("use_function")
        results = asession.run(usefunction)

        for result in results:
            print(result.html.find(item.get('class_name'),first=True))
            # pricce=result.html.find(item.get('class_name'),first=True).text
            # print(pricce)

if __name__ == '__main__':
    reptile=Reptile('https://www.alternate.de/Thermaltake/DIMM-16-GB-DDR4-3200-Kit-Arbeitsspeicher/html/product/1588667')
    reptile.get_price()





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