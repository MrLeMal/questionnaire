from question import Question
from utilitaires import créer_fichier_json, lire_fichier_json


class Questionnaire():
  def __init__(self, questions=[], theme=""):
    self.theme = theme
    self.questions = questions

  def lancer(self):
    print("\nDébut du questionnaire sur le thème : '{}'".format(self.theme))
    for question in self.questions:
      question.poser()

    print("\nFin du questionnaire.")

  
  def charger(self, f_json):
    self.theme = f_json[:-5]
    self.questions = []

    liste_questions = lire_fichier_json(f_json)

    for question in liste_questions:
      self.questions.append(Question.fromData(question))

  @classmethod
  def creer(cls):
    print("Création du questionnaire : ")
    questions = []

    titre_questionnaire = input("\nQuel est le titre du questionnaire ? ")
    
    while True:
      ajouter_question = input("\nVoulez-vous ajouter une question ? ").lower()

      if ajouter_question != 'non' and ajouter_question != 'oui':
        print("\nCommande incorrecte, veuillez répondre par oui ou non. ")
        continue

      if ajouter_question == 'non':
        break

      # Création de la question puis ajout de la question à la liste
      question = Question.creer()
      questions.append(question)

    # TODO : Créer une méthode pour l'écriture du JSON (dans un fichier utilitaires.py ?)
    créer_fichier_json(titre_questionnaire, questions)
