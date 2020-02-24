## task: create a new col which store True if city name contains "San" and area>50
import pandas as pd
#import matplotlib as plt
      
city_names=pd.Series(['San Francisco','San Jose','Sacramento'])
population=pd.Series([852469,1015785,485199])
area=pd.Series([46.87, 176.53, 97.92])
cities=pd.DataFrame({ 'City name':city_names, 'Population':population, 'Area square miles':area })
print(cities)
print()
print(cities['Area square miles'] > 50)
print()
print(cities['City name'])
print()
print((cities['Area square miles'] > 50) & cities['City name'])
# here we use '&' not 'and' caz..
#       "Boolean Series are combined using the bitwise, rather than the traditional boolean, operators"
#       "when performing logical and, use & instead of and."
cities['Is wide and has saint name'] = (cities['Area square miles'] > 50) & cities['City name'].apply(lambda name: name.startswith('San'))
print()
print(cities)

#print(list(cities['Name']))