from bs4 import BeautifulSoup as bs
import requests
import pandas
import csv
import time
with open("D:\\Scraping Jumia\jumia_products.csv","w",newline='',encoding='utf-8-sig') as file:
    mywriter = csv.writer(file)
    mywriter.writerow(["name","new_price","old_price","percent_discount","rate",
                       "verified_ratings","Seller_Score","followers","Order_Fulfillment_Rate",
                      "Quality_Score","Customer_Rating","link","page_number"])
    for i in range(1,2):
        page_number = i
        print(f"------------page number {i}-----------")
        url = f"https://www.jumia.com.eg/laptop-accessories/?page={i}#catalog-listing"
        r = requests.get(url)
        soup1 = bs(r.content,"html.parser")
        ancher = soup1.html.find("div",{"class":"-paxs row _no-g _4cl-3cm-shs"})
        for link in ancher.findAll('a',{"class":"core"}):
            a = link.get("href")
            if a != None:
                link = "https://www.jumia.com.eg"+a
                product_page = requests.get(link)
                soup = bs(product_page.content,"html.parser")
                try:
                    name = soup.html.find("h1",{"class":"-fs20 -pts -pbxs"}).text
                except:
                    name = None
                try:
                    new_price = soup.html.find("span",{"class":"-b -ltr -tal -fs24"}).text
                except:
                    new_price = None
                try:   
                    old_price = soup.html.find("span",{"class":"-tal -gy5 -lthr -fs16"}).text
                except:
                    old_price = None
                try:
                    percent_discount = soup.html.find("span",{"class":"bdg _dsct _dyn -mls"}).text
                except:
                    percent_discount = None
                try:
                    rate = soup.html.find("div",{"class":"-fs29 -yl5 -pvxs"}).text
                    rate = rate.split('/5')[0]
                except:
                    rate = None
                try:
                    verified_ratings = soup.html.find("p",{"class":"-fs16 -pts"}).text
                    verified_ratings = verified_ratings.split(' ')[0]
                except:
                    verified_ratings = None       
                try:
                    Seller_Score = soup.html.find("bdo",{"class":"-m -prxs"}).text
                except:
                    Seller_Score = None
                try:
                    followers = soup.html.find("div",{"class":"-df -d-co -j-bet -prs"}).text
                    followers = followers.split('Score')[1].split(' ')[0]
                except:
                    followers = None
                try:
                    Seller_Performance = soup.html.find("div",{"class":"-pas -bt -fs12"}).text
                    Order_Fulfillment_Rate = Seller_Performance.split('Rate:')[1].split('Quality Score:')[0]
                except:
                    Order_Fulfillment_Rate = None
                try:
                    Seller_Performance = soup.html.find("div",{"class":"-pas -bt -fs12"}).text
                    Quality_Score = Seller_Performance.split('Score:')[1].split('Customer')[0]
                except:
                    Quality_Score = None
                try:
                    Seller_Performance = soup.html.find("div",{"class":"-pas -bt -fs12"}).text
                    Customer_Rating = Seller_Performance.split('Rating:')[1]
                except:
                    Customer_Rating = None
                time.sleep(4)
                mywriter.writerow([name,new_price,old_price,percent_discount,rate,
                       verified_ratings,Seller_Score,followers,Order_Fulfillment_Rate,
                      Quality_Score,Customer_Rating,link,page_number])