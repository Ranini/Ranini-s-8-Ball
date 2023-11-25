from random import choice
from time import sleep
from clear import clear
from colorama import Fore
import fade
import os

def bybye():
            x = 4
            for n in range(3):
                x = (x - 1)
                print(x)
                sleep(1.0)
            quitter = True
            exit(0)
            
def set_terminal_title(title):
    # Vérifie si le système d'exploitation est Windows
    if os.name == 'nt':
        os.system(f"title {title}")
    else:
        # Utilise une séquence d'échappement ANSI pour changer le titre (valide pour certains terminaux)
        print(f"\033]0;{title}\007")

# Utilisation
nouveau_titre = "Ranini\u0027s ball"
set_terminal_title(nouveau_titre)

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
quitter = False
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

faded_logo = fade.water(logo)

print(faded_logo)
while not quitter:
    question = input(Fore.RESET + "Quelle est votre question? (tapez 'quitter' pour quitter)")
    if question.lower() == "quitter":
        sur = input(Fore.RED + "Êtes-vous sûr? (tapez 'oui' si vous êtes sûr)")
        if sur.lower() == "oui":
            bybye()
                        
    else:
                answer_string = fade.random(choice(response))
                print(answer_string)
                next_question = input("voulez-vous passer au suivant? (tapez suivant) ")
                if next_question.lower() == "suivant":
                    clear()
                    print(faded_logo)
                else:
                    bybye()