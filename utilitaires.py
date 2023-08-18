import json



def créer_fichier_json(nom_fichier, donnees):
  with open(f"{nom_fichier}.json", 'w', encoding ='utf8') as file:
    json.dump(donnees, file, ensure_ascii=False)

def lire_fichier_json(nom_fichier):
  with open(nom_fichier) as file:
   data = json.load(file)

  return data
