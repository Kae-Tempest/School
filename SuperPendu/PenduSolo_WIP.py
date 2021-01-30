def PenduSolo():

    from pyfiglet import Figlet
    from termcolor import colored
    import random

    words = open('mots.txt', 'r')
    words = words.readlines()
    soluce = random.choice(words)[:-1].lower()
    colored_soluce = colored(soluce, 'red', attrs=['bold', 'underline'])
    life = 10
    affichage = ""
    letter_found = ""
    propositions = ""

    for l in soluce:
        affichage = affichage + "_ "

    custom_fig = Figlet(font='Slant')
    print(custom_fig.renderText('Bienvenue dans le jeu du pendu'))

    while life > 0:
        print("\nMot à deviner : ", affichage)
        proposition = input("proposer une lettre : ")

        if proposition in soluce:
            letter_found = letter_found + proposition
            print("Bien joué !")

        else:
            life -= 1
            print("Loupé ! cherche encore !")

            if life == 10:
                print("\n")
                print("\n")
                print("\n")
                print("\n")
                print("\n")
                print("\n")
                print("\n")
                print("Il te reste encore", life, "vie !")

            if life == 9:
                print("\n")
                print("\n")
                print("\n")
                print("\n")
                print("\n")
                print("_____________\n")
                print("Il te reste encore", life, "vie !")

            if life == 8:
                print("\n")
                print(" |\n")
                print(" |\n")
                print(" |\n")
                print(" |\n")
                print(" |\n")
                print("_|____________\n")
                print("Il te reste encore", life, "vie !")

            if life == 7:
                print("_____________\n")
                print(" |\n")
                print(" |\n")
                print(" |\n")
                print(" |\n")
                print(" |\n")
                print("_|____________\n")
                print("Il te reste encore", life, "vie !")

            if life == 6:
                print("_____________\n")
                print(" | /\n")
                print(" |/\n")
                print(" |\n")
                print(" |\n")
                print(" |\n")
                print("_|____________\n")
                print("Il te reste encore", life, "vie !")

            if life == 5:
                print("_____________\n")
                print(" | /       |\n")
                print(" |/\n")
                print(" |\n")
                print(" |\n")
                print(" |\n")
                print("_|____________\n")
                print("Il te reste encore", life, "vie !")

            if life == 4:
                print("_____________\n")
                print(" | /       |\n")
                print(" |/        O\n")
                print(" |\n")
                print(" |\n")
                print(" |\n")
                print("_|____________\n")
                print("Il te reste encore", life, "vie !")

            if life == 3:
                print("_____________\n")
                print(" | /       |\n")
                print(" |/        O\n")
                print(" |         |\n")
                print(" |\n")
                print(" |\n")
                print("_|____________\n")
                print("Il te reste encore", life, "vie !")

            if life == 2:
                print("_____________\n")
                print(" | /       |\n")
                print(" |/        O\n")
                print(" |        -|-\n")
                print(" |\n")
                print(" |\n")
                print("_|____________\n")
                print("Il te reste encore", life, "vie !")

            if life == 1:
                print("_____________\n")
                print(" | /       |\n")
                print(" |/        O\n")
                print(" |        -|-\n")
                print(" |         /\\\n")
                print(" |\n")
                print("_|____________\n")
                print("Il te reste encore", life, "vie !")

            if life == 0:
                print("_____________\n")
                print(" | /       |\n")
                print(" |/        O\n")
                print(" |        -|-\n")
                print(" |        /\\\n")
                print(" |\n")
                print("_|____________\n")
                print("Trop tard je suis mort !\n")
                print("le mot a trouvé etait", colored_soluce , "tu feras mieux la prochaine fois !")

        propositions = propositions + proposition
        print("tu as deja proposé", propositions)

        affichage = ""
        for x in soluce:
            if x in letter_found:
                affichage += x + " "
            else:
                affichage += "_ "

        if "_" not in affichage:
            print("Le mot à trouver etait :", colored_soluce)
            print(custom_fig.renderText("\n >>> YOU WIN ! <<< "))
            break
    print(custom_fig.renderText('     >>> END ! <<<'))