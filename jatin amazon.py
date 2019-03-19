from bs4 import BeautifulSoup as soup
from  urllib.request import Request
from urllib.request import urlopen as uReq

def product(x):
    req= Request(x,None,{'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'})
    url=req
    uClient=uReq(url)
    html=uClient.read()
    uClient.close()
    html_page=soup(html,'lxml')
    tags=html_page.findAll("span",{"class": "a-size-large","id":"productTitle"})
    tag=tags[0].text
    
    tags1=html_page.findAll("span",{"class": "a-size-medium a-color-price"})
    tag1=tags1[0].text

    tags2=html_page.findAll("a",{"class": "a-popover-trigger a-declarative"})
    tag2=tags2[0].text

    print("Product_name: ".ljust(30," ")+((tag).replace('\n',' ')).strip(" "))

    print("Price: ".ljust(30," ")+(tag1))

    if(str(tag2[1]).isdigit()):
        print("Reviews: ".ljust(30," ")+((tag2).replace('\n',' ')).strip(" "))

    else:
        print("Reviews: ".ljust(30," ")+"Not rated yet")
    
print("Please enter a link:")
m=str(input())
product(m)

