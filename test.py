import random

with open("/Users/victor/Downloads/slm/liste_francais.txt", 'r', encoding='utf-8') as file:
    text = file.read()

listeMots = text.lower().split()

# sert à calculer les probas utiles à générer un caractère par rapport aux 2 caractères précédents
transitions = {}
transitionsTotal = {}
proba = {}

# sert à calculer les probas utiles à générer le 2ème caractère
transitions2 = {}
transitionsTotal2 = {}
proba2 = {}

# sert à générer le premier caractère
premiereLettreCount = {}
totalMots = len(listeMots)


# dans ce script le premier caractère est généré en fonction des probas des premières lettre de chaque mot,
# le 2ème caractère est généré en fonction des probas qu'un caractère suive le caractère généré,
# une fois qu'on a 2 caractères on peut se baser sur les 2 caractères précédents pour générer chaque nouveau caractère


for mot in listeMots:
    # on ajoute un ! à la fin de chaque mot qui signifiera que dans transition de x vers ! alors x est la dernière lettre du mot
    mot += "!"

    # on compte pour chaque caractère le nombre de fois ou c'est le premier caractère d'un mot
    premiereLettre = mot[0]
    if premiereLettre in premiereLettreCount:
        premiereLettreCount[premiereLettre] += 1
    else:
        premiereLettreCount[premiereLettre] = 1
    
    # on compte le total de fois ou chaque caractère est suivis par un autre caractère spécifique
    for i in range(len(mot) - 1):
        lettre1 = mot[i]
        lettre2 = mot[i + 1]
        if lettre1 not in transitions2:
            transitions2[lettre1] = {}
            
        if lettre2 not in transitions2[lettre1]:
            transitions2[lettre1][lettre2] = 0
        transitions2[lettre1][lettre2] += 1

        if lettre1 not in transitionsTotal2:
            transitionsTotal2[lettre1] = 0
        transitionsTotal2[lettre1] += 1

    # on compte le total de fois ou chaque caractère est suivis par deux autres caractères spécifiques
    for i in range(len(mot) - 2):
        lettres1_2 = mot[i:i + 2]
        lettre3 = mot[i + 2]

        if lettres1_2 not in transitions:
            transitions[lettres1_2] = {}
            transitionsTotal[lettres1_2] = 0

        if lettre3 not in transitions[lettres1_2]:
            transitions[lettres1_2][lettre3] = 0

        transitions[lettres1_2][lettre3] += 1
        transitionsTotal[lettres1_2] += 1


# on calcule la proba que chaque caractère soit le premier caractère d'un mot
probaPremiereLettre = {lettre: frequence / totalMots for lettre, frequence in premiereLettreCount.items()}

# on calcule la proba pour chaque caractère d'être suivi par un autre caractère spécifique
for lettre1, transitionsLettres in transitions2.items():
    proba2[lettre1] = {}
    for lettre2, frequence in transitionsLettres.items():
        proba2[lettre1][lettre2] = frequence / transitionsTotal2[lettre1]

# on calcule la probabilité pour chaque caractère d'être suivi par deux autres caractères spécifiques
for lettres1_2, transitionsLettres in transitions.items():
    proba[lettres1_2] = {}
    for lettre3, frequence in transitionsLettres.items():
        proba[lettres1_2][lettre3] = frequence / transitionsTotal[lettres1_2]


# génère une première lettre au hasard parmi les probas calculées
premiereLettre = random.choices(list(probaPremiereLettre.keys()), weights=list(probaPremiereLettre.values()), k=1)
motGénéré = premiereLettre[0]

# génère une deuxième lettre au hasard en prenant compte de la première lettre
probaTransition = proba2[motGénéré[-1]]
lettres, probabilites = zip(*probaTransition.items())
while True:
    lettreGénérée = random.choices(lettres, weights=probabilites, k=1)
    if lettreGénérée[0] != '!':
        motGénéré += lettreGénérée[0]
        break


# Utiliser les deux dernières lettres du mot généré pour trouver les probabilités de la lettre suivante
while True:
    lettresActuelles = motGénéré[-2:]
    probaTransition = proba.get(lettresActuelles, {})
    if not probaTransition:
        break

    lettres, probabilites = zip(*probaTransition.items())
    lettreGénérée = random.choices(lettres, weights=probabilites, k=1)[0]

    if lettreGénérée == '!':
        break

    motGénéré += lettreGénérée


print(motGénéré)
