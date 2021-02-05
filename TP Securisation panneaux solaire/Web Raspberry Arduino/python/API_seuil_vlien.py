import urllib.request
import json
from datetime import datetime
import time
from time import strftime


f1 = open("../db/historique.txt", "w")
f1.write("")
f1.close()
f = open("../db/seuilDepasse.txt", "w")
f.write("")
f.close()
now = time.localtime(time.time())
dateActuelle = time.strftime("%Y-%m-%d %H:%M:%S", now)
dateActuelleStr = str(dateActuelle)
url = "http://www.infoclimat.fr/public-api/gfs/json?_ll=48.9,2.08333&_auth=CBIHEAN9ASNVeFBnB3EHLgBoUGUJfwQjAHwHZF86An8EblEqD3MDY1QlB2UFPQA3WWlVNgEhAyQLagZoXzVUPghsB2sDYwF8VSVQLwc2BywALFA0CTAEIgBhB2FfOgJ%2FBGZRMQ9sA39UPAdhBSoAK1lrVTMBPwM6C2AGY187VDEIbAdmA38BfFU8UDIHNgcxADpQMQlnBG4AawdhX2MCNQRnUTcPcgNhVDoHYAU2ADBZa1UyATgDJAt3BhhfQVQqCCsHIQM1ASVVJ1BnB2kHZw%3D%3D&_c=7092dce3f05b4548107504e9fdcd199a"
operUrl = urllib.request.urlopen(url)
if(operUrl.getcode()==200):
    data = operUrl.read()
    donnees = json.loads(data)
    donnees.pop('request_state')
    donnees.pop('request_key')
    donnees.pop('message')
    donnees.pop('model_run')
    donnees.pop('source')
    print(donnees)
    for i,v in donnees.items():
        vMoy = v['vent_moyen']['10m']
        vRaf = v['vent_rafales']['10m']
        vDir = v['vent_direction']['10m']
        if vDir > 360 :
            vDir = vDir - 360
            if vDir > 360 :
                vDir = vDir - 360
                if vDir > 360 :
                   vDir = vDir - 360
        vMoy = vMoy * 1000 / 3600
        vRaf = vRaf * 1000 / 3600
        if vRaf > 16 :
            vMoy = str(vMoy)
            vRaf = str(vRaf)
            vDir = str(vDir)
            date = i
            print("/!\ seuil d'alerte dépassé : " + vRaf + " à " + date)
            print("Date et heure : " + date + " --> vent moyen : " + vMoy + "m/s --> vent rafales : " + vRaf + "m/s --> vent direction : " + vDir + "°")
            f = open("../db/seuilDepasse.txt", "a")
            f.write(date + "\n")
            f.close()
            vMoy = float(vMoy)
            vRaf = float(vRaf)
            vMoy = vMoy * 3600 / 1000
            vRaf = vRaf * 3600 / 1000
            vMoy = round(vMoy, 2)
            vRaf = round(vRaf, 2)
            vMoy = str(vMoy)
            vRaf = str(vRaf)
            f1 = open("../db/historique.txt", "a")
            f1.write(date + "," + vMoy + "," + vRaf + "," + vDir + "\n")
            f1.close()


        else :
            vMoy = str(vMoy)
            vRaf = str(vRaf)
            vDir = str(vDir)
            date = i
            print("Le seuil d'alerte n'est pas dépassé : " + vRaf + " à " + date)
            print("Date et heure : " + date + " --> vent moyen : " + vMoy + "m/s --> vent rafales : " + vRaf + "m/s --> vent direction : " + vDir + "°")
            vMoy = float(vMoy)
            vRaf = float(vRaf)
            vMoy = vMoy * 3600 / 1000
            vRaf = vRaf * 3600 / 1000
            vMoy = round(vMoy, 2)
            vRaf = round(vRaf, 2)
            vMoy = str(vMoy)
            vRaf = str(vRaf)
            f1 = open("../db/historique.txt", "a")
            f1.write(date + "," + vMoy + "," + vRaf + "," + vDir + "\n")
            f1.close()
    else:
       print("Error receiving data", operUrl.getcode())
       exit()