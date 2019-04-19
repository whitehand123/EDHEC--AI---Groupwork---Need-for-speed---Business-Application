#%%
import pandas as pd
path = 'C:/Users/Luo Daojun/OneDrive - EDHEC/EDHEC M2/Data analytics and Artificial Intelligence/Python/trail.csv'
data = pd.read_csv(path)
data

#%%
row0 = '<hr class="featurette-divider">\n<div class="container">\n<div class="row featurette">\n<div class="col-md-12">'
row1 = '<div class="col-md-6">'
row2 =  '   <p class="lead" id=brand1><span class=leadbold>Car Brand:</span>\'{}\'</p >'
row3 =  '   <p class="lead" id=color1><span class=leadbold>Color</span> Black</p >'
row4 =  '   <p class="lead" id=type1><span class=leadbold>Type: </span> SUV</p >'
row5 =  '   <p class="lead" id=price1><span class=leadbold>Price: </span>\'{}\'</p >'
row6 =  '   <p class="lead"><a href=\'{}\'>Link to page</a></p>'
row7 =  ' </div>'
row8 =  ' <div class="col-md-6">'
row9 =  '   <img class="featurette-image img-responsive center-block" id=image1 src=\'{}\' alt="car image">'
row10 = ' </div>'
row11 = '</div>\n</div>\n</div>'


#%%
car_name = data.iloc[:,1]
car_price = data.iloc[:,3]
car_image = data.iloc[:,0]
car_link = data.iloc[:,2]

#%%
f = open('html_full.txt','w')

for i,j,x,y in zip(car_name,car_price,car_image,car_link):
    row21 = row2.format(i)
    row51 = row5.format(j)
    row61 = row6.format(y)
    print(row61)
    row91 = row9.format(x)
    rows = [row0,row1,row21,row3,row4,row51,row61,row7,row8,row91,row10,row11]
    print('\n'.join(rows),file=f)

f.close()


#%%
