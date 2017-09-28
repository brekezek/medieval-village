#Simulation d'un village médiéval depuis sa fondation

from random import randint,choice


class Peasant:
    def __init__(self, age, sex, name):
        self.age=age
        self.sex=sex
        self.name=name

def creer_paysan(paysans,age='?',sex='?',name='?'):
    names_male=['Ulysse','Emile','Jean','Alphonse','Alexis', 'Brieuc', 'Jean-Jacques','Marc','Paul','Gargamel','Charles','Frédéric','Titouan','Cyprien','Victor','Elie','Antoine','Iba','Xavier','JB','Elhadji','Momodou','Moussa','Omar','Idy','Cheickh']
    names_female=['Nolwenn','Magali','Françoise','Marion','Alice','Anne','Momo','Juju','Fatou','Maglousse','Carmen','Christine','Marie','Clarisse','Lina-May','Ludivine','Louise','Mathilde','Léa','Juliette','Emilienne','Jeannine','Seynabou','Mbou',]
    if age=='?':
        age=randint(12,50)
    if sex=='?':
        sex=choice(['M','F'])
    if name=='?':
        if sex=='M':
             name=choice(names_male)
        elif sex=='F':
             name=choice(names_female)
    new_character=Peasant(age,sex,name)
    paysans.append(new_character)
    return paysans

def tuer_paysan(cause="e vieillesse"):
    mort=paysans.pop(randint(0,len(paysans)-1))
    print('Le paysan {} est mort.e d{} à l\'âge de {!s} ans.'.format(mort.name,cause,mort.age))

def defaite():
    print('Désastre! Votre village est dépeuplé! Vous avez perdu.')

def attaque():
    ennemis=choice(range(stocks["r"]+1))
    if ennemis>0:
        if ennemis<=stocks["c"]:
            print('\nDes pillards ont été découragés par vos défenses et ont passé leur chemin.\n')
        else: #fight!
            morts=min(randint(0,ennemis),len(paysans))#on ne peut pas tuer plus de paysans qu'il y en a
            for i in range(morts):
                tuer_paysan("\'une blessure de guerre par les pillards")
            pillage=morts
            stocks["r"]-=min(pillage,stocks["r"])
            if pillage>0:
                print ("Les pillards sont partis avec {!s} unités de richesse!".format(pillage))

print('Bienvenue dans #Dorf Meister# le meilleur jeu de simulation de village médiéval du moment (probablement).')
nom_village=input('Comment devrait s\'appeler le village?\n')
annee=1200
stocks={"a":0,"b":0,"p":0,"r":10,"c":0}
recap_abr_taches={"a":"Agriculture","c":"Construction de bâtiments et défenses","b":"Coupe de bois","p":"Taille de pierre","r":"Artisanat"}
recap_abr_stocks={"a":"Nourriture","c":"Niveau de défense","b":"Bois coupé","p":"Pierre taillée","r":"Richesse"}
print('Le village de {} est fondé par une bande de paysans surmotivés en l\'an {!s}.'.format(nom_village,annee))
##choix=print('Veux-tu leur donner des noms ou des noms au pif c\'est bien?')

paysans=[]
for i in range(7):
    paysans=creer_paysan(paysans)

affichage_paysans=input('Veux-tu jeter un coup d\'oeil à ta bande de joyeux drilles? \nAppuie sur o pour oui, n\'importe quoi sinon.\n')
if affichage_paysans=="o":
    for i in range(0,len(paysans)):
        print('{!s}- Âge : {!s} ans,   Nom : {!s},   Sexe : {!s}'.format(i+1,paysans[i].age,paysans[i].name,paysans[i].sex))

#boucle générale
while paysans!=[]:

    #attribution des tâches à accomplir
    print('Vous disposez de {!s} paysans. Quelles actions souhaitez-vous réaliser cette annee?'.format(len(paysans)))

    actions_dispos=len(paysans)
    actions={"a":0,"c":0,"b":0,"p":0,"r":0}
    while actions_dispos>0:
        print('\n {!s} unités de travail restantes. Comment souhaitez-vous les répartir?'.format(actions_dispos))
        choix_action=input('Appuyez sur : \n "a" pour affecter des paysans à l\'agriculture \n "c" pour affecter des paysans à la construction de bâtiments et défenses \n "r" pour ffecter des paysans à l\'artisanat \n "b" pour la coupe de bois \n "p" pour la taille de pierre\n')
        while choix_action not in {"a","c","b","p","r"}:
            print('Tu dois appuyer sur une des touches proposées')
            choix_action=input('Appuyez sur : \n "a" pour affecter des paysans à l\'agriculture \n "c" pour affecter des paysans à la construction de bâtiments et défenses \n "r" pour ffecter des paysans à l\'artisanat \n "b" pour la coupe de bois \n "p" pour la taille de pierre\n')

        max_paysans_autorises=actions_dispos
        if (choix_action=="r")|(choix_action=="c"):
            print('Ces actions consomment des ressources. Il te reste {!s} unités de pierre pour la construction et {!s} unités de bois pour l\'artisanat'.format(stocks["p"],stocks["b"]))
            if choix_action=="r":
                max_paysans_autorises=min(max_paysans_autorises,stocks["b"])
            else:
                max_paysans_autorises=min(max_paysans_autorises,stocks["p"])

        nb_affectes=int(input('Combien de paysans en plus souhaites-tu envoyer à cette tâche cette année? \n note: il te reste {!s} paysans sans tache assignée cette année.\n'.format(actions_dispos)))
        while nb_affectes not in range(0,max_paysans_autorises+1):
            nb_affectes=int(input('Tu dois rentrer un nombre valide, entre 0 (si finalement tu veux pas) et {!s} (si tu veux envoyer tous tes paysans restants à cette action).\n'.format(max_paysans_autorises)))
        print('{!s} paysans supplémentaires affectés à "{!s}"'.format(nb_affectes,recap_abr_taches[choix_action]))
        actions[choix_action]+=nb_affectes
        actions_dispos-=nb_affectes

    affichage_choix_actions=input('\nTu as affecté tous tes paysans à des tâches diverses. Souhaites-tu un récapitulatif de ces assignations? Appuye sur "o" si oui, n\'importe quoi sinon.\n')
    if affichage_choix_actions=="o":
        print('\n')
        for i in actions:
            print('{}: {} paysans'.format(recap_abr_taches[i],actions[i]))

    #accomplissement des tâches durant l'année
    for i in actions:
        stocks[i]+=actions[i]
    stocks["p"]-=actions["c"]
    stocks["b"]-=actions["r"]

    #consommation de nourriture
    while stocks["a"]<len(paysans)/3:
        tuer_paysan("famine")
    if paysans==[]:
        break #on peut s'arrêter là, tous les paysans sont morts de faim
    stocks["a"]-=len(paysans)/3
    print('Tes paysans ont consommé {} unités de nourriture au cours de l\'annee.'.format(len(paysans)/3))

    #attaques ennemies
    attaque()
    if paysans==[]:
        break

    #arrivee de migrants
    attrait_migrants=(stocks["a"]+stocks["c"]+1)/2
    migrants=choice(range(round(attrait_migrants)))
    for i in range(migrants+1):
        paysans=creer_paysan(paysans)
    if migrants>0:
        print('Attirés par vos défenses et votre nourriture, {!s} paysans ont décidé de s\'installer dans votre village.'.format(migrants))

    #naissances
    fertiles=0
    for paysan in paysans:
        if paysan.sex=='F' and paysan.age in range (16,50):
            fertiles+=1
    naissances=randint(0,fertiles)
    for i in range(naissances):
        paysans=creer_paysan(paysans,0)
    print('{!s} bébés paysans sont nés cette année dans le village.'.format(naissances))

    #récapitulatif
    affichage_recapitulatif=input('\nTes paysans ont effectué des tâches diverses. Souhaites-tu un récapitulatif de l\'état actuel de ton village? Appuye sur "o" si oui, n\'importe quoi sinon.\n')
    if affichage_recapitulatif=="o":
        print('Etat des stocks:')
        for i in actions:
            print('{}: {} unités'.format(recap_abr_stocks[i],stocks[i]))
        print('Nombre de paysans: {}\n dont migrants de l\'année : {!s}\n et naissances de l\'année: {!s}'.format(len(paysans),migrants,naissances))

    annee+=1
    print(('\n'*10) + 'Nous sommes désormais en l\'an {!s}.'.format(annee))
    for paysan in paysans:
        paysan.age+=1

defaite()
