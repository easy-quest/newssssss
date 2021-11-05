#!/usr/bin/env python
# -*- coding: utf-8 -*-


from requests_html import HTMLSession
session = HTMLSession

url = 'https://kubnews.ru/all/'

r = session.get(url)
r.html.render(sleep=1, scrolldown=5)

articles = r.html.find('article')
print(articles)
