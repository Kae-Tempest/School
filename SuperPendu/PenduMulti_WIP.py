def PenduMulti():

    from pyfiglet import Figlet
    from termcolor import colored
    from getpass import getpass

    class Player:
        def __init__(self, name, life):
            self.name = name
            self.Life = life

    player1 = Player(input("Quel est le nom du joueur qui donne le mot a trouvé: "), 100)
    player2 = Player(input("Quel est le nom du joueur qui joue: "), 10)

    print(player1.name, "veuillez donnez le mot a trouvé")
    soluce = input("mot : ")
    colored_soluce = colored(soluce, 'red', attrs=['bold', 'underline'])
    colored_name1 = colored(player1.name, 'red', attrs=['bold', 'underline'])
    propositions = ""
    affichage = ""
    letter_found = ""

    for l in soluce:
        affichage = affichage + "_ "

    custom_fig = Figlet(font='Slant')
    print(custom_fig.renderText('Bienvenue dans le jeu du pendu'))
    print(custom_fig.renderText('3'))
    print(custom_fig.renderText('2'))
    print(custom_fig.renderText('1'))
    print(custom_fig.renderText('Start'))

    while player2.Life > 0:
        print("\nMot à deviner : ", affichage)
        proposition = input("proposer une lettre : ")

        if proposition in soluce:
            letter_found = letter_found + proposition
            print("Bien joué !")

        else:
            player2.life -= 1
            print("Loupé ! cherche encore !")

            if player2.life == 10:
                print("\n")
                print("\n")
                print("\n")
                print("\n")
                print("\n")
                print("\n")
                print("\n")
                print("Il te reste encore", player2.life, "vie !")

            if player2.life == 9:
                print("\n")
                print("\n")
                print("\n")
                print("\n")
                print("\n")
                print("_____________\n")
                print("Il te reste encore", player2.life, "vie !")

            if player2.life == 8:
                print("\n")
                print(" |\n")
                print(" |\n")
                print(" |\n")
                print(" |\n")
                print(" |\n")
                print("_|____________\n")
                print("Il te reste encore", player2.life, "vie !")

            if player2.life == 7:
                print("_____________\n")
                print(" |\n")
                print(" |\n")
                print(" |\n")
                print(" |\n")
                print(" |\n")
                print("_|____________\n")
                print("Il te reste encore", player2.life, "vie !")

            if player2.life == 6:
                print("_____________\n")
                print(" | /\n")
                print(" |/\n")
                print(" |\n")
                print(" |\n")
                print(" |\n")
                print("_|____________\n")
                print("Il te reste encore", player2.life, "vie !")

            if player2.life == 5:
                print("_____________\n")
                print(" | /       |\n")
                print(" |/\n")
                print(" |\n")
                print(" |\n")
                print(" |\n")
                print("_|____________\n")
                print("Il te reste encore", player2.life, "vie !")

            if player2.life == 4:
                print("_____________\n")
                print(" | /       |\n")
                print(" |/        O\n")
                print(" |\n")
                print(" |\n")
                print(" |\n")
                print("_|____________\n")
                print("Il te reste encore", player2.life, "vie !")

            if player2.life == 3:
                print("_____________\n")
                print(" | /       |\n")
                print(" |/        O\n")
                print(" |         |\n")
                print(" |\n")
                print(" |\n")
                print("_|____________\n")
                print("Il te reste encore", player2.life, "vie !")

            if player2.life == 2:
                print("_____________\n")
                print(" | /       |\n")
                print(" |/        O\n")
                print(" |        -|-\n")
                print(" |\n")
                print(" |\n")
                print("_|____________\n")
                print("Il te reste encore", player2.life, "vie !")

            if player2.life == 1:
                print("_____________\n")
                print(" | /       |\n")
                print(" |/        O\n")
                print(" |        -|-\n")
                print(" |         /\\\n")
                print(" |\n")
                print("_|____________\n")
                print("Il te reste encore", player2.life, "vie !")

            if player2.life == 0:
                print("_____________\n")
                print(" | /       |\n")
                print(" |/        O\n")
                print(" |        -|-\n")
                print(" |        /\\\n")
                print(" |\n")
                print("_|____________\n")
                print(colored_name1, "est mort !\n")
                print("le mot a trouvé etait", soluce, "tu feras mieux la prochaine fois !")

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