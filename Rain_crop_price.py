import matplotlib.pyplot as plt 
import pandas as pd

###################Read the files##############################
retail_price = pd.read_csv("Item-Price.txt", delimiter="\t")
rainfall =pd.read_csv("Rainfall_data.txt", delimiter="\t")
###################Check for missing values####################
print(retail_price.isnull().sum())
print(rainfall.isnull().sum())

if(rainfall.isnull().sum().sum()>0):
    rainfall.fillna(0)
if(retail_price.isnull().sum().sum()>0):
    retail_price.fillna(0)  
center_list=[]

for i in range(1, retail_price.shape[0]):
    fig = plt.figure(figsize=(56,6))
    
    place = retail_price.iloc[i,2]
    if(place not in center_list):
        
        f ="place"+str(i)
        f =fig.add_subplot(231)
        f.set_title(place+" Price Analysis-1")
        center_list.append(place)
        item_place = retail_price.loc[(retail_price["State"]==place)]

        price_item = item_place["Price per Kg"]
        f.plot(item_place["Year"].loc[(item_place["Commodity"]=="Tur/Arhar Dal")], price_item.loc[(item_place["Commodity"]=="Tur/Arhar Dal")],color='green', label="Tur/Arhar Dal")
        f.plot(item_place["Year"].loc[(item_place["Commodity"]=="Milk")], price_item.loc[(item_place["Commodity"]=="Milk")],color='red', label="Milk")
        f.plot(item_place["Year"].loc[(item_place["Commodity"]=="Salt Pack (Iodised)")], price_item.loc[(item_place["Commodity"]=="Salt Pack (Iodised)")],color='yellow', label="Salt Pack")
        f.plot(item_place["Year"].loc[(item_place["Commodity"]=="Tea Loose")], price_item.loc[(item_place["Commodity"]=="Tea Loose")],color='blue', label="Tea Loose")
        f.plot(item_place["Year"].loc[(item_place["Commodity"]=="Rice")], price_item.loc[(item_place["Commodity"]=="Rice")],color='gray', label="Rice")
        plt.xticks(rotation=90)
        plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
        f =fig.add_subplot(232)
        f.set_title(place+" Price Analysis-2")
        f.plot(item_place["Year"].loc[(item_place["Commodity"]=="Onion")], price_item.loc[(item_place["Commodity"]=="Onion")],color='brown', label="Onion")
        f.plot(item_place["Year"].loc[(item_place["Commodity"]=="Sugar")], price_item.loc[(item_place["Commodity"]=="Sugar")],color='orange', label="Sugar")
        f.plot(item_place["Year"].loc[(item_place["Commodity"]=="Sunflower Oil (Packed)")], price_item.loc[(item_place["Commodity"]=="Sunflower Oil (Packed)")],color='black', label="Sunflower Oil")
        f.plot(item_place["Year"].loc[(item_place["Commodity"]=="Tomato")], price_item.loc[(item_place["Commodity"]=="Tomato")],color='purple', label="Tomatos")
        plt.xticks(rotation=90)
        plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
        plt.savefig(place+" Price Analysis.pdf")
    else:
        continue
area_list=[]
plt.figure(figsize=(65,6))
for j in range(0, rainfall.shape[0]):
    place = rainfall.iloc[j,1]
    
    if(place not in area_list):
        area_list.append(place)
        item_place = rainfall.loc[(rainfall["Area"]==place)]
        
        plt.plot(list(rainfall.columns)[2:rainfall.shape[1]],item_place.iloc[2,range(2,item_place.shape[1])], label=place)
        plt.xticks(rotation=90)
        plt.xlabel("Years")
        plt.ylabel("Rainfall in mm")
        plt.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.savefig("Regions Rainfall.pdf")
