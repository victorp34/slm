with open("/Users/victor/Downloads/slm/liste_francais.txt", 'r', encoding='utf-8') as file:
    text = file.read()

listeMots = text.lower().split()

transitions = {}
transitionsTotal = {}
proba = {}
premiereLettreFrequences = {}
totalMots = len(listeMots)


for mot in listeMots:
    # on ajoute un ! à la fin de chaque mot qui signifiera que dans transition de x vers ! alors x est la dernière lettre du mot
    mot += '!'
    
    # on compte pour chaque caractère le nombre de fois ou il a été le premier caractère d'un mot
    premiereLettre = mot[0]
    if premiereLettre in premiereLettreFrequences:
        premiereLettreFrequences[premiereLettre] += 1
    else:
        premiereLettreFrequences[premiereLettre] = 1

    # on compte le total de fois ou chaque caractère est suivis par tel ou tel autre caractère
    for i in range(len(mot) - 1):
        lettre1 = mot[i]
        lettre2 = mot[i + 1]
        if lettre1 not in transitions:
            transitions[lettre1] = {}
            
        if lettre2 not in transitions[lettre1]:
            transitions[lettre1][lettre2] = 0
        transitions[lettre1][lettre2] += 1

        if lettre1 not in transitionsTotal:
            transitionsTotal[lettre1] = 0
        transitionsTotal[lettre1] += 1

# on calcule la proba que chaque caractère soit le premier caractère d'un mot
probaPremiereLettre = {lettre: frequence / totalMots for lettre, frequence in premiereLettreFrequences.items()}

# on calcule la proba que chaque caractère soit suivis par un autre dans un dictionanire de dictionanire 
for lettre1, transitionsLettres in transitions.items():
    proba[lettre1] = {}
    for lettre2, frequence in transitionsLettres.items():
        proba[lettre1][lettre2] = frequence / transitionsTotal[lettre1]

