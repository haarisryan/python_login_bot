from bs4 import BeautifulSoup
import requests
from win10toast import ToastNotifier
 
n=ToastNotifier()
def getdata(url):
    r=requests.get(url)
    return r.text
htmldata=getdata("https://www.accuweather.com/en/in/chennai/206671/weather-forecast/206671")
soup=BeautifulSoup(htmldata,'html.parser')
current_temp=soup.find_all("span", id="TemperatureValue")
temp=(str(current_temp))
result = "current_temp " + temp[128:-9] + "  in chennai" 
n.show_toast("live Weather update",  
             result, duration = 10) 