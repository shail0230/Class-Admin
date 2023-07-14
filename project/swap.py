from bs4 import BeautifulSoup
import requests


try:
    r = requests.get('https://ngodarpan.gov.in/index.php/home/statewise_ngo/23074/27/1' )
    r.raise_for_status()

    soup=BeautifulSoup(r.text, 'html.parser')


except Exception as e:
    print(e)



data = soup.find_all('td', class_='titleColumn')


print(data)
