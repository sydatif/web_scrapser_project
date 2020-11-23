from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
import re
from csv import writer
import sys


my_url = "https://www.yelp.com/biz/marked-restaurant-toronto"
#my_url = "https://www.yelp.ca/biz/lov-king-west-toronto-2"

uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()
page_soup = soup(page_html, "html.parser")


containers = page_soup.findAll ("div", { "class": "lemon--div__373c0__1mboc review__373c0__13kpL sidebarActionsHoverTarget__373c0__2kfhE arrange__373c0__2C9bH gutter-2__373c0__1DiLQ grid__373c0__1Pz7f layout-stack-small__373c0__27wVp border-color--default__373c0__3-ifU"})
nuser = (len(containers))
print ("Number of user ", str(nuser))
print()

filename = "post.csv"
f = open (filename, "w")
headers = "Name ,Address,No. of Friends,Date, No. of Reviews,Post\n"
f.write(headers)

for n in range(nuser):
    container = containers[n]

    search = container.select("span",{"class":"lemon--span__373c0__3997G"})
    name = search[0].text
    print("Name : ",name)

    address = search[1].text
    print("Address :",address)

    friend = search[3].text
    friend_regx = re.findall(r"[0-9]+", friend)
    tnum_of_friend = friend_regx[0]
    print("Friends :",tnum_of_friend)

    review = search[7].text
    review_regx = re.findall(r"[0-9]+", review)
    tnum_of_review = review_regx[0]
    print("No.of Reviews :", tnum_of_review) 
    
            
    search = container.findAll("span", {"class":"lemon--span__373c0__3997G text__373c0__2Kxyz text-color--mid__373c0__jCeOG text-align--left__373c0__2XGa-"})
    date = search[0].text
    print("date :", date)

    
    search = container.findAll("span", {"class":"lemon--span__373c0__3997G raw__373c0__3rcx7"})
    post = search[0].text
    print("Review :", post)
    print()

    
    f.write(name + "," + address.replace(","," ") + "," + tnum_of_friend + "," + date + "," + tnum_of_review + "," + post.replace(",",".") + "\n" )
        
f.close()