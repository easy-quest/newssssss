from requests_html import HTMLSession
session = HTMLSession()
#url = 'https://news.google.com/topstories?hl=ru&gl=RU&ceid=RU:ru'
url = 'https://news.google.com/topics/CAAqHAgKIhZDQklTQ2pvSWJHOWpZV3hmZGpJb0FBUAE/sections/CAQiUENCSVNOam9JYkc5allXeGZkakpDRUd4dlkyRnNYM1l5WDNObFkzUnBiMjV5Q3hJSkwyMHZNR1p3Y3pBMWVnc0tDUzl0THpCbWNITXdOU2dBKjEIACotCAoiJ0NCSVNGem9JYkc5allXeGZkako2Q3dvSkwyMHZNR1p3Y3pBMUtBQVABUAE?hl=ru&gl=RU&ceid=RU%3Aru'

r = session.get(url)
r.html.render(sleep=1, scrolldown=5)

articles = r.html.find('article')
# print(articles)
newslist = []

for item in articles:
    try:
        newsitem = item.find('h3', first=True)
        newsarticle = {
        'title' : newsitem.text,
        'link' :  newsitem.absolute_links
        }
        newslist.append(newsarticle)
        #print(title, link)
    except:
        pass

#print(len(newslist))
print(newslist)
