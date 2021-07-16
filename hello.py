import requests 
from bs4 import BeautifulSoup 
""" 
1. 
https://www.data.go.kr/tcs/dss/selectApiDataDetailView.do?publicDataPk=15073861 에서 활용 신청  
2. 
로컬에서 진행 시 패키지 설치 
$ pip install beautifulsoup4 requests lxml 
""" 

 
KEY = 'iTpdD5hhMW71PQus57ztCitlpMM8T4ntl3mEe%2FTzhseoUcgTpG5kR29kq7%2FcxYy4ky3ufUl%2B5wvT5JURzmFmTg%3D%3D' 
url = f'http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey={KEY}&numOfRows=10&pageNo=3&sidoName=서울&ver=1.0' 
# print(url) 
response = requests.get(url).text 
data = BeautifulSoup(response, 'xml') 
# print(data) 
item = data('item')[7] 
time = item.dataTime.text 
station = item.stationName.text 
dust = int(item.pm10Value.text) 

 
print(f'{time} 기준 {station}의 미세먼지 농도는 {dust} 입니다.') 
