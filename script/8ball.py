from random import choice #importation du module random pour un choix automatiquec de la réponse
from time import sleep #importation de sleep pour le décompte
from clear import clear #srx c'est pour clear un terminal
from colorama import Fore #pour changer la couleur du terminal
import fade #parce que je sais pas faire de dégradé avec colorama et cela son stylé et facile
import os #pour changer le titre du terminal

def byebye(): #fonction pour quitter le jeu de mqnirèe stylé
    sur = input(Fore.RED + "Êtes-vous sûr? (tapez 'oui' si vous êtes sûr) ")
    if sur.lower() == "oui":
        x = 4
        for n in range(3):
            x -= 1
            print(x)
            sleep(1.0)
        print("0" + Fore.RESET)
        exit()
            
def set_terminal_title(title): #fonction permettant de chqnger le nom du programme (fait avec chatgpt stackoverflow n'a pas tout dit)
    # Vérifie si le système d'exploitation est Windows
    if os.name == 'nt':
        os.system(f"title {title}")
    else:
        # Utilise une séquence d'échappement ANSI pour changer le titre (valide pour certains terminaux)
        print(f"\033]0;{title}\007")

# Utilisation
nouveau_titre = "Ranini\u0027s ball"
set_terminal_title(nouveau_titre)

#liste des réponses disponibles

response = [
        "C'est certain",
        "Sans aucun doute",
        "Oui, définitivement",
        "Oui, absolument",
        "Vous pouvez compter dessus",
        "Pas sûr, essayez à nouveau",
        "Demandez plus tard",
        "Mieux vaut ne pas vous le dire maintenant",
        "Impossible de prédire maintenant",
        "Ne comptez pas là-dessus",
        "Ma réponse est non",
        "Mes sources disent non",
        "Outlook n'est pas si bon",
        "Très douteux"
    ]
quitter = False #permet de rester dans la boucle et de la sortir (pouvoir poser plusieurs questions)
logo = (r"""


                                                                 ,---,            ,---.-,                                ,--,      ,--,    
                                                              ,`--.' |           '   ,'  '.                           ,---.'|   ,---.'|    
,-.----.                                                      |   :  :          /   /      \    ,---,.    ,---,       |   | :   |   | :    
\    /  \                            ,--,                 ,--,|   |  '         .   ;  ,/.  :  ,'  .'  \  '  .' \      :   : |   :   : |    
;   :    \                   ,---, ,--.'|         ,---, ,--.'|'   :  |         '   |  | :  ;,---.' .' | /  ;    '.    |   ' :   |   ' :    
|   | .\ :               ,-+-. /  ||  |,      ,-+-. /  ||  |, ;   |.'.--.--.   '   |  ./   :|   |  |: |:  :       \   ;   ; '   ;   ; '    
.   : |: |   ,--.--.    ,--.'|'   |`--'_     ,--.'|'   |`--'_ '---' /  /    '  |   :       ,:   :  :  /:  |   /\   \  '   | |__ '   | |__  
|   |  \ :  /       \  |   |  ,"' |,' ,'|   |   |  ,"' |,' ,'|     |  :  /`./   \   \     / :   |    ; |  :  ' ;.   : |   | :.'||   | :.'| 
|   : .  / .--.  .-. | |   | /  | |'  | |   |   | /  | |'  | |     |  :  ;_      ;   ,   '\ |   :     \|  |  ;/  \   \'   :    ;'   :    ; 
;   | |  \  \__\/: . . |   | |  | ||  | :   |   | |  | ||  | :      \  \    `.  /   /      \|   |   . |'  :  | \  \ ,'|   |  ./ |   |  ./  
|   | ;\  \ ," .--.; | |   | |  |/ '  : |__ |   | |  |/ '  : |__     `----.   \.   ;  ,/.  :'   :  '; ||  |  '  '--'  ;   : ;   ;   : ;    
:   ' | \.'/  /  ,.  | |   | |--'  |  | '.'||   | |--'  |  | '.'|   /  /`--'  /'   |  | :  ;|   |  | ; |  :  :        |   ,/    |   ,/     
:   : :-' ;  :   .'   \|   |/      ;  :    ;|   |/      ;  :    ;  '--'.     / '   |  ./   :|   :   /  |  | ,'        '---'     '---'      
|   |.'   |  ,     .-./'---'       |  ,   / '---'       |  ,   /     `--'---'  |   :      / |   | ,'   `--''                               
`---'      `--`---'                 ---`-'               ---`-'                 \   \   .'  `----'                                         
                                                                                 `---`-'                                                   

""")

faded_logo = fade.water(logo) #permet de faire un dégradé de couleur de couleur bleu

print(faded_logo)
while not quitter:
    question = input(Fore.RESET + "Quelle est votre question? (tapez 'quitter' pour quitter) ") #boucle principal
    if question.lower() == "quitter":
            byebye()                        
    else:
                answer_string = fade.random(choice(response))
                print(answer_string)
                next_question = input("voulez-vous passer au suivant? (tapez suivant) ou tappez autre chose pour quitter: ")
                if next_question.lower() == "suivant":
                    clear()
                    print(faded_logo)
                else:
                    byebye()
