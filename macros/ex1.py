from time import sleep

from requests_html_macro import Macro
from requests_html import HTMLSession

# Create a standard requests-html session
session = HTMLSession()
response = session.get('http://python.org')

# Create a macro with the response
macro = Macro(response=response)

# Create a macro that uses the parse library to search through the html
@macro.search_pattern('Python is a {} language', first=True)
def foo(data):
    print(data[0])

# Creates a macro that uses a css selector
@macro.css_selector('#about', first=True)
def foo1(data):
    print(data.text)


@macro.xpath('//a', first=True)
def foo2(data):
    print(data)

while True:
    macro.parse()
    sleep(30)
    macro.response = session.get('http://python.org')

