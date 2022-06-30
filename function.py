import csv
import json



def getDataFromCSV(csvfilename):
    csv_list_of_dict=[]
    with open(file=csvfilename) as f:
        reader=csv.DictReader(f, delimiter=';')
        for content in reader :
            csv_list_of_dict.append(content)
            """
            NUM_FEUILLET =content['FEUILLET']
            CODE_SITE =content['Code site']
            COMMUNE =content['Commune']
            ADMIN_ROUTEUR_VSAT =content['@IP  Admin routeur VSAT']
            INTERCO_MODEM_VLAN =content['INTERCO MODEM VLAN']
            INTERCO_MODEM_IP_MODEM =content['INTERCO MODEM - @IP  Modem']
            INTERCO_MODEM_NETMASK_MODEM =content['INTERCO MODEM - Netmask Modem']
            PS_VRF_EXPLOITATION_NO_VLAN =content['PS - VRF EXPLOITATION- No VLAN']
            PS_VRF_EXPLOITATION_IP_MODEM =content['PS - VRF EXPLOITATION - @IP  Modem']
            PS_VRF_EXPLOITATION_NETMASK_MODEM =content['PS - VRF EXPLOITATION - Netmask Modem']
            PS_VRF_CONDUITE_NO_VLAN =content['PS - VRF CONDUITE_xxx - No VLAN']
            PS_VRF_CONDUITE_VLAN_IP_MODEM =content['PS - VRF CONDUITE_xxx - VLAN #4 - @IP  Modem']
            PS_VRF_CONDUITE_VLAN_NETMASK_MODEM =content['PS - VRF CONDUITE_xxx - VLAN #4 - Netmask Modem']
            PS_VRF_CONDUITE_NOM_VRF =content['PS - VRF CONDUITE_xxx  - NOM VRF']

            afficher = ["Num_feuillet : "+ NUM_FEUILLET,
                        "Code site : " + CODE_SITE,
                        "Commune : " + COMMUNE,
                        "IP Admin routeur VSAT : " + ADMIN_ROUTEUR_VSAT,
                        "Interco Modem VLAN : "+ INTERCO_MODEM_VLAN,
                        "IP  Interco modem : "+ INTERCO_MODEM_IP_MODEM,
                        "Netmask interco modem : "+ INTERCO_MODEM_NETMASK_MODEM,
                        "PS - VRF Exploitation - NO VLAN : "+ PS_VRF_EXPLOITATION_NO_VLAN,
                        "PS - VRF Exploitation - IP Modem : "+ PS_VRF_EXPLOITATION_IP_MODEM,
                        "PS - VRF Exploitation - Netmask Modem : "+ PS_VRF_EXPLOITATION_NETMASK_MODEM,
                        "PS - VRF Conduite - NO VLAN : "+ PS_VRF_CONDUITE_NO_VLAN,
                        "PS - VRF Conduite - VLAN IP Modem : "+ PS_VRF_CONDUITE_VLAN_IP_MODEM,
                        "PS - VRF Conduite - VLAN Netmask Modem : "+ PS_VRF_CONDUITE_VLAN_NETMASK_MODEM,
                        "PS - VRF Conduite - Nom VRF : "+PS_VRF_CONDUITE_NOM_VRF]

            list_csv=[]
            TotalInfo_csv={}
            list_csv=TotalInfo_csv

            TotalInfo_csv['Feuillet'] = str(NUM_FEUILLET)
            TotalInfo_csv['Code_Site'] = str(CODE_SITE)
            TotalInfo_csv['Commune'] = str(COMMUNE)
            TotalInfo_csv['Admin_Routeur_VSAT'] = str(ADMIN_ROUTEUR_VSAT)                                # Création d'indexs
            TotalInfo_csv['Interco_Modem_VLAN'] = str(INTERCO_MODEM_VLAN)                                # au dictionnaire TotalInfo
            TotalInfo_csv['Interco_Modem_IP'] = str(INTERCO_MODEM_IP_MODEM)
            TotalInfo_csv['Interco_Modem_Netmask_Modem'] = str(INTERCO_MODEM_NETMASK_MODEM)
            TotalInfo_csv['PS_VRF_Exploitation_NO_VLAN'] = str(PS_VRF_EXPLOITATION_NO_VLAN)
            TotalInfo_csv['PS_VRF_Exploitation_IP_Modem'] = str(PS_VRF_EXPLOITATION_IP_MODEM)
            TotalInfo_csv['PS_VRF_Exploitation_Netmask_Modem'] = str(PS_VRF_EXPLOITATION_NETMASK_MODEM)
            TotalInfo_csv['PS_VRF_Conduite_NO_VLAN'] = str(PS_VRF_CONDUITE_NO_VLAN)
            TotalInfo_csv['PS_VRF_Conduite_Vlan_IP_Modem'] = str(PS_VRF_CONDUITE_VLAN_IP_MODEM)
            TotalInfo_csv['PS_VRF_Conduite_VLAN_Netmask_Modem'] = str(PS_VRF_CONDUITE_VLAN_NETMASK_MODEM)
            TotalInfo_csv['PS_VRF_Conduite_Nom_VRF'] = str(PS_VRF_CONDUITE_NOM_VRF)
            """
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
                
    



"""
            if feuillet_csv == feuillet_json  :
                #print("Les données sont conformes","csv =>",feuillet_csv,"json =>",feuillet_json,)  
                print()      
            else: 
                #print("erreur :","csv =>",feuillet_csv,"json =>",feuillet_json)
                error_feuillet = ["Erreur Feuillet:", feuillet_csv, "donnée attendue :", feuillet_json]
                list_of_errors.append(error_feuillet)
                    
            if descr_json in descr_csv  :
                #print("Les données sont conformes","csv =>",descr_csv,"json =>",descr_json)
                print() 

            else: 
                #print("erreur :","csv =>",descr_csv,"json =>",descr_json)
                error_descr = ["Erreur Site:", descr_csv, "donnée attendue :", descr_json]
                list_of_errors.append(error_descr)
                print(*list_of_errors, sep='\n\n\n')
"""

     