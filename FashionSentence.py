import requests
from bs4 import BeautifulSoup

def read ( word ):
        
    url = f'https://nwbw.naer.edu.tw/index.php/{word}'

    html = requests.get( url , verify=False )
    bs = BeautifulSoup(html.text,'lxml')
    data = bs.find_all('p')
    try:
        rslt= data[0].text
        return ( rslt )
    except:
        return( '查無此字' )
