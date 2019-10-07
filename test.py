import bs4 as bs 
import urllib.request

# List of AirBnB Urls 
urls = [
    "https://www.airbnb.com/rooms/20305254?source_impression_id=p3_1570481869_mTI3HOH5hhlpek0V",
    "https://www.airbnb.com/rooms/25034481?source_impression_id=p3_1570481877_dRr2UFoWpEPiu1ju",
    "https://www.airbnb.com/rooms/7619516?source_impression_id=p3_1570481915_0ICbmJzEbSr7JDcq",
    "https://www.airbnb.com/rooms/7619521?source_impression_id=p3_1570481926_CIfQQ1P%2BqA%2BhRqZy"
]

#################################
# Loop Through the list of URLs #
#################################
for i in urls:
    # Open each link with BeautifulSoup
    url = urllib.request.urlopen(i)
    soup = bs.BeautifulSoup(url, 'lxml')
    body = soup.body.find_all('span', class_='_doc79r')

    # Loop to find class='_doc79r' #
    for s in body:
        print(s.text)
        updatedPrice = [s.text]
        