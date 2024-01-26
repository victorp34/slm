import random

with open("/Users/victor/Downloads/slm/liste_francais.txt", 'r', encoding='utf-8') as file:
    text = file.read()

listeMots = text.lower().split()

transitions = {}
transitionsTotal = {}
proba = {}

for mot in listeMots:
    mot += '!'
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


for lettre1, transitionsLettres in transitions.items():
    proba[lettre1] = {}
    for lettre2, frequence in transitionsLettres.items():
        proba[lettre1][lettre2] = frequence / transitionsTotal[lettre1]

