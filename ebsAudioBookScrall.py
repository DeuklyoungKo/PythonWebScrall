from urllib.request import urlopen
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver import Chrome
from requests import get  # to make GET request

def download(url, file_name):
    with open(file_name, "wb") as file:   # open in binary mode
        response = get(url)               # get request
        file.write(response.content)      # write to file

def getBsObject(url) :
  driver.get(url)
  bsObject = BeautifulSoup(driver.page_source, "html.parser")
  return bsObject

driver = webdriver.Chrome(executable_path='E:/Lecture/python/chromedriver.exe')

for pageNum in range(15,105):

  baseUrl = 'https://home.ebs.co.kr/drama/replay/2/view?courseId=BP0PHPK0000000046&stepId=01BP0PHPK0000000046&prodId=10312&lectId=10243989&lectNm=&bsktPchsYn=&prodDetlId=&oderProdClsCd=&prodFig=&vod=&oderProdDetlClsCd=&pageNo='+str(pageNum)
  bsObject = getBsObject(baseUrl)
  pageDatas = bsObject.find('div', {'id':'replayList'}).select('tr td a')

  for pageData in pageDatas:

    baseUrlArray = baseUrl.split('&')
    baseUrlArray[3] = 'lectId='+pageData.get('href')[1:]

    newUrl = "&".join(baseUrlArray)

    url = baseUrl+pageData.get('href')
    print('==================')
    print(newUrl)
    bsObjectItem = getBsObject(newUrl)
    DownfileNameUrl = bsObjectItem.find('audio', {'id':'aod_player'}).get('src')
    print(DownfileNameUrl.split('.')[-1])

    # extra

    fileName = bsObjectItem.find('h5').text.strip()
    fileName = fileName.replace("<","(").replace(">",")").replace("/"," ")
    print(fileName)
    if DownfileNameUrl :
      download(DownfileNameUrl,fileName+'.'+DownfileNameUrl.split('.')[-1])

driver.close();