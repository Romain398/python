import function
import test

#print("=================CSV DATA ===================")
list_from_csv=function.getDataFromCSV("data.csv")
#for element in list_from_csv:
   # print(element)
   # print(len(list_from_csv))
#print("=================CSV DATA END ===============")


#print("=================JSON DATA ===================")
list_from_json=function.getDataFromJson("test.json")
for element in list_from_json:
   print(element)
#print("=================JSON  DATA END ===============")

#print("=================CHECK IF SITE EXIST ===================")
for csv_elt in list_from_csv :
   found=function.findGilatConfigFromApi(list_from_json,csv_elt['Code site'])
   print("!!!!!!!!   "+csv_elt['Code site']+"   =>"+str(found)) 
#print("=================CHECK IF SITE EXIST END ===================")

print("=================COMPARE DATAS ===================")
compare = function.compareDatasBetweenFiles(list_from_json,list_from_csv,found)
print("=================COMPARE DATAS END ===================")