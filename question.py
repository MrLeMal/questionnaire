
class Question():
  def __init__(self, titre, liste_choix, bonne_reponse):
    self.titre = titre
    self.liste_choix = liste_choix
    self.bonne_reponse = bonne_reponse

  @classmethod
  def fromData(cls, data):
    q = Question(data['titre'], data['liste_choix'], data['bonne_reponse'])
    return q

  @classmethod
  def creer(cls):
      cls.titre = input("\nTitre de la question : ")
      
      liste_choix_str = input("\nListez les choix séparés par un '/': ")
      cls.liste_choix = liste_choix_str.split('/')

      while True:
        cls.bonne_reponse = input("\nDonnez le numéro de la bonne réponse : ")

        try:
          bonne_reponse_int = int(cls.bonne_reponse)

          if not 1 <= bonne_reponse_int <= len(cls.liste_choix):
            print("Entrez un nombre compris entre 1 et {}".format(len(cls.liste_choix)))

          break
        except ValueError:
          print("Erreur : Entrez une valeur numérique.")

      return{
        "titre": cls.titre,
        "liste_choix": cls.liste_choix,
        "bonne_reponse": cls.bonne_reponse
      }
    
  def poser(self):
    print(self.titre)
    for i in range(len(self.liste_choix)):
      print(f"{i+1}- {self.liste_choix[i]}")

    reponse = Question.demander_reponse_utilisateur(1, len(self.liste_choix))

    self.reponse_correct(reponse)
  
  def reponse_correct(self, reponse):
    if  reponse != self.bonne_reponse:
      print('Mauvaise réponse')
    else:
      print('Bonne réponse')

  @classmethod
  def reponse_valide(cls,reponse, min, max):
    try:
      reponse_int = int(reponse)
    except ValueError:
      print('Vous devez entrer une valeur numérique.')
      return False
  
    if reponse_int < min or reponse_int > max:
      print('Erreur: la valeur ne correpond à un des choix.')
      return False
  
    return True

  @classmethod
  def demander_reponse_utilisateur(cls, min, max):
    reponse = input(f"Entrez votre réponse (entre {min} et {max}): ")
  
    if not Question.reponse_valide(reponse, min, max):
      Question.demander_reponse_utilisateur(min, max)
  
    return reponse
