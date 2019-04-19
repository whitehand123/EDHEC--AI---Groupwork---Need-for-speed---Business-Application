import csv
import json
from crawl_and_sort import crawlAndSort

#specify keywords, remember to capitalize the first letter of the color and type parameters
keywords = {'brand':'','color':'Black','type':'SUV'}

#build headers to dodge the possible barriers
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'}

#create the file and extract the data to csv format
Go = crawlAndSort()
k = keywords
h = headers
Go.autotraderGo(k,h)
Go.carsnipGo(k,h)

#transfer the file to json
csvfile = open('trail.csv', 'r')
jsonfile = open('trail.json', 'w')

fieldnames = ('img','name','url','price','desc','loc','grabber','specs')
reader = csv.DictReader( csvfile, fieldnames)
for row in reader:
    json.dump(row, jsonfile)
    jsonfile.write('\n')