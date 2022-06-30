import csv
import json



def getDataFromCSV(csvfilename):
    csv_list_of_dict=[]
    with open(file=csvfilename) as f:
        reader=csv.DictReader(f, delimiter=';')
        for content in reader :
            csv_list_of_dict.append(content)
     
    return csv_list_of_dict
    
            # print("Taille du dictionaire du CSV : {}".format(len(list_csv)))

            # affichage_espacé = "\n".join(afficher)

            #  print(affichage_espacé, end= "\n\n"



def getDataFromJson(jsonfilename):
    with open(jsonfilename)as j:
        
        json_list_of_dict = json.load(j)
        
        #print(json_list_of_dict)
        #print for debug only
        #for element in json_list_of_dict :
        #   print(element)
    print("Taille du dictionaire du JSON : {}".format(len(json_list_of_dict)))
    return json_list_of_dict



        

def findGilatConfigFromApi(jsondict,site):
#find if site is in field "description" in dict jsondict

    if jsondict :
        for elt in jsondict :
            descr= elt["description"]
            print(descr+ "===>"+site)
            pos_site=descr.find(site)
            print(pos_site)
            if (pos_site != -1):
                return True
    return False


def compareDatasBetweenFiles(jsondict,csv_data,site_exist):
    
    if site_exist == True: 
        list_of_pair = []
        list_of_errors = []
        Checkdone = False
        
        for elt_json in jsondict :
            feuillet_json = elt_json["Feuillet"]
            descr_json = elt_json["description"]
            #print("json_feuillet",feuillet_json)
            #print("json_descr",descr_json)

            for elt_csv in csv_data :
                
                feuillet_csv =elt_csv["FEUILLET"]
                descr_csv = elt_csv["Code site"]
                #print("csv_feuillet",feuillet_csv)
                #print("csv_decsr",descr_csv)

                if feuillet_csv == feuillet_json :
                    Checkdone = True
                    pair_feuillet = ["Feuillet CSV =>",feuillet_csv,"Feuillet JSON =>",feuillet_json,"CheckDone =>",Checkdone]
                    list_of_pair.append(pair_feuillet)

                elif feuillet_csv != feuillet_json:
                    Checkdone = False
                    wrong_pair_feuillet = ["Feuillet CSV =>",feuillet_csv,"Feuillet JSON =>",feuillet_json,"CheckDone =>",Checkdone]
                    list_of_errors.append(wrong_pair_feuillet)



                if descr_json in descr_csv  :
                    Checkdone=True
                    pair_descr = ["Site CSV =>",descr_csv,"Site JSON =>",descr_json,"CheckDone =>",Checkdone]
                    list_of_pair.append(pair_descr)

                elif descr_json not in descr_csv:
                    Checkdone = False
                    wrong_pair_descr = ["Site CSV =>",descr_csv,"Site JSON =>",descr_json,"CheckDone =>",Checkdone]
                    list_of_errors.append(wrong_pair_descr)

                
                

        print("Liste des paires :",*list_of_pair, sep = "\n\n")
        print("\n","Liste des erreurs :",*list_of_errors, sep = "\n\n")
              
    else: print("Il y a une erreur dans le fichier csv")    
                
    




     
