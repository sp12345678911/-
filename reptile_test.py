from requests_html import AsyncHTMLSession
asession = AsyncHTMLSession()
web_header={
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0',
'Accept': '*/*',
'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
'Accept-Encoding': 'gzip, deflate, br',
'Connection': 'keep-alive',
'Cookie': 'session-id=138-8109177-6343214; Domain=.amazon.com; Expires=Sat, 06-May-2023 06:01:04 GMT; Path=/; Secure, session-id-time=2082787201l; Domain=.amazon.com; Expires=Sat, 06-May-2023 06:01:04 GMT; Path=/; Secure, i18n-prefs=USD; Domain=.amazon.com; Expires=Sat, 06-May-2023 06:01:04 GMT; Path=/, sp-cdn="L5Z9:TW"; Version=1; Domain=.amazon.com; Max-Age=31536000; Expires=Sat, 06-May-2023 06:01:04 GMT; Path=/; Secure; HttpOnly, skin=noskin; path=/; domain=.amazon.com',
'TE': 'Trailers'}
async def get_pythonorg():
    r = await asession.get('https://python.org/')
    return r

async def get_reddit():
    r = await asession.get('https://reddit.com/')
    return r

async def get_amazon():
    r = await asession.get('https://www.amazon.com/Thermaltake-TOUGHRAM-Motherboard-Syncable-R016D408GX2-3600C18A/dp/B08XWK554J/ref=sr_1_3?crid=1WCLJPD9DV8ER&dchild=1&keywords=toughram+xg+rgb&qid=1615956921&sprefix=toughram+XG%2Caps%2C347&sr=8-3',headers=web_header)
    return r

results = asession.run(get_amazon)
for result in results:
    pricce=result.html.find('.a-price',first=True).text
    print(pricce)