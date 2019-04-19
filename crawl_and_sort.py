# -*- coding: utf-8 -*
from bs4 import BeautifulSoup as bs
import requests
import csv

#specify keywords, remember to capitalize the first letter of the color and type parameters
keywords = {'brand':'VOLKSWAGEN','color':'blue','type':'Hatchback'}

#build headers to dodge the possible barriers
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'}


#write the extract function, n as an instance, x as a string, Y as a dict, t controls the method we call in
def extract(n,x,Y=None,t=None):
	if t == 1:
		return n.find_next(x,Y).get_text().encode('utf-8').strip()
	if t == 2:
		return n.find_previous(x,Y).get('src')
	if t == 4:
		return n.find(x,Y).get('src').encode('utf-8').strip()
	if t == 3:
		return n.find(x,Y).get('href').encode('utf-8').strip()
	return n.find(x,Y).get_text().encode('utf-8').strip()
	
def check_keywords(keywords):
	res = []
	for key, val in keywords.items():
		if val!='':
			res.append(key)
	return res

class crawlAndSort:
	def __init__(self):
		pass

	
	def autotraderGo(self,keywords,headers):
		#build the URL
		URL = 'https://www.autotrader.co.uk/car-search?sort=recommended&radius=1500&postcode=e16an&onesearchad=Used'
		res = check_keywords(keywords)
		if 'brand' in res:
			URL = URL + '&make=' + keywords['brand']
		if 'color' in res:
			URL = URL + '&colour=' + keywords['color']
		if 'type' in res:
			URL = URL +'&keywords=' + keywords['type']
		#get request and parse response
		r = requests.get(URL,headers = headers)
		res = r.content
		soup = bs(res,'html.parser')
		contents = soup.find_all('div',{'class':'information-container'})
		
		#extract the data and write into the file
		file = open('trail.csv','wb')
		writer = csv.writer(file,delimiter=',')
		for i in contents:
			#extract the data and store in RAM
			img = extract(i,'img',t = 2)
			name = extract(i,'a',{'class':'js-click-handler'})
			grabber = extract(i,'p',{'class':'listing-attention-grabber '})
			specs = extract(i,'ul',{'class':'listing-key-specs'})
			desc = extract(i,'p',{'class':'listing-description'})
			loc = extract(i,'span',{'class':'seller-town'})
			price = extract(i,'div',{'class':'vehicle-price'},t = 1)
			url = extract(i,'a',{'class':'js-click-handler'},t=3)

			#eliminate unneccessary strings
			name = name.replace('\xe2\x80\xa6','...')
			desc = desc.replace('\xe2\x80\xa6','...')
			price = price.replace('\xc2\xa3','GBP ')
			
			url = 'http://www.autotrader.co.uk' + url
			#write it into th csv
			writer.writerow([img,name,url,price,desc,loc,grabber,specs])
		file.close()
	
	def carsnipGo(self,keywords,headers):
		#build the URL
		URL = 'https://carsnip.com/search'
		res = check_keywords(keywords)
		if 'type' in res:
			URL = URL+'/bodyStyle/'+keywords['type']
		if 'color' in res:
			URL = URL+'/colour/'+keywords['color']
		if 'brand' in res:
			URL = URL+'/manufacturer/'+keywords['brand']

		#get request and parse
		r = requests.get(URL,headers = headers)
		res = r.content
		soup = bs(res,'html.parser')
		
		contents = soup.find('div',{'class':'sc-dyGzUR'}).children
		
		file = open('trail.csv','ab')
		writer = csv.writer(file,delimiter=',')
		for i in contents:
			try:
				#extract the data and store in RAM
				price = extract(i,'a',{'class':'cs-price'})
				name = extract(i,'a',{'class':'Title-kEkEAm'})
				desc = extract(i,'ul',{'class':'Wrapper-ThVjl eMvmwp'})
				loc = extract(i,'div', {'class':"Wrapper-ThVjl gDbCCj"})
				url = extract(i,'a',{'class':'AdvertImage__Link-jtjfGx'},t = 3)
				img = extract(i,'img',{'class':'AdvertImage__Image-bnbAfu'},t = 4)
		
				#eliminate unneccessary strings
				name = name.replace('\xe2\x80\xa6','...')
				desc = desc.replace('\xe2\x80\xa6','...')
				price = price.replace('\xc2\xa3','GBP ')
				
				url = 'http://carsnip.com' + url
				#fill in the blank cols
				grabber = None
				specs = None
			except AttributeError:
				continue
			writer.writerow([img,name,url,price,desc,loc,grabber,specs])
		file.close()


if __name__ == '__main__':
	Go = crawlAndSort()
	k = keywords
	h = headers
	Go.autotraderGo(k,h)
	Go.carsnipGo(k,h)