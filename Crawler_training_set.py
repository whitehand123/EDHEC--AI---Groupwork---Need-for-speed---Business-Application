from google_images_download import google_images_download

#build the instance
response = google_images_download.googleimagesdownload()

#select the keywords for search
target = {'brand':['VOLKSWAGEN CAR','AUDI CAR','SKODA CAR'],'color':['silver car','black car','white car'],'type':['hatchback car','sports car','SUV']}

#download the images using loop
for i in target:
	for j in target[i]:
		argument = {'keywords':j,'limit':20,'print_urls':True,'format':'jpg'}#specify further parameters
		paths = response.download(argument)