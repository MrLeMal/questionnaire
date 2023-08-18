from questionnaire import Questionnaire


def main():
  menu = """
    PROJET QUESTIONNAIRE:
  
      Commandes disponibles:
      1- charger
      2- creer
      3- lancer
      4- quitter
  """
  questionnaire = Questionnaire()
  
  print(menu)
  
  while True:
    commande_str = input("\nQuel est votre choix ? ")
  
    try:
      commande = int(commande_str)
  
      if commande == 1:
        fichier = input("\nQuel fichier voulez-vous charger ? ")
        questionnaire.charger(fichier+'.json')
      elif commande == 2:
        questionnaire.creer()
      elif commande == 3:
        questionnaire.lancer()
      elif commande == 4:
        print("Sortie du programme.")
        break
      else: 
        print("\nErreur: le nombre entré ne correspond pas à un des choix.")
  
    except ValueError:
      print("Erreur: le choix doit être un nombre correspondant à un des choix.")

# PROGRAMME PRINCIPALE

if __name__ == "__main__":
  main()
