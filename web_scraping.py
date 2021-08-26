 
import requests
from bs4 import BeautifulSoup
import pandas as pd

#url = "https://www.amazon.in/Fire-Boltt-Display-Waterpoof-Monitoring-Rotating/product-reviews/B093GWY1WQ/ref=cm_cr_arp_d_paging_btm_next_2?ie=UTF8&reviewerType=all_reviews&pageNumber=2"

reviewlist=[]
def get_soup(url):
    response=requests.get(url)
    soup= BeautifulSoup(response.text,'html.parser')
    return soup

def get_reviews(soup): 
    reviews = soup.find_all('div',{'data-hook':'review'})
    try:
        for item in reviews:
            review = {
            'product':soup.title.text.replace('Amazon.in:Customer reviews:','').strip(),
            'title ':item.find('a',{'data-hook':'review-title'}).text.strip(),
            'rating':float(item.find('i',{'data-hook':'review-star-rating'}).text.replace('out of 5 stars','').strip()),
            'body': item.find('span',{'data-hook':'review-body'}).text.strip(),
            }
            reviewlist.append(review)
    except:
        pass
for x in range(1,100):
    soup = get_soup(f'https://www.amazon.in/Fire-Boltt-Display-Waterpoof-Monitoring-Rotating/product-reviews/B093GWY1WQ/ref=cm_cr_arp_d_paging_btm_next_2?ie=UTF8&reviewerType=all_reviews&pageNumber={x}')
    print(f'Getting page:{x}')
    get_reviews(soup) 
    print(len(reviewlist))
    if not soup.find('li',{'class':'a-disabled a-last'}):
        pass
    else:
        break

df = pd.DataFrame(reviewlist)
df.to_csv('smart_watch_reviews.csv')
print('Collected !!')