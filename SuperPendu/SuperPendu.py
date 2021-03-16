from PenduSolo_WIP import PenduSolo
from PenduMulti_WIP import PenduMulti


def gamemode():
    solo = input("Veux tu jouer en Solo Y/N : ")
    if solo == "Y":
        PenduSolo()
    elif solo == "N":
        PenduMulti()
    else:
        gamemode()

gamemode()


