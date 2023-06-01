import requests
from bs4 import BeautifulSoup

def read ( word ):
        
    url = f'https://nwbw.naer.edu.tw/index.php/{word}'

    html = requests.get( url , verify=False )
    bs = BeautifulSoup(html.text,'lxml')
    data = bs.find_all('p')
    try:
        rslt= data[0].text
        
        if '沒有內容' in rslt :
            return ('找不到相關資料，請重試。')
        elif '需要編修' in rslt:
            return ('該資料正在建立中。')
        else:
            return( rslt)
    except:
        return( '查無此字' )
