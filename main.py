import os

# Sciencetific notation converter
def snc(input:str):
    return float(input.split('\t')[-1][:-1])

os.system("cls")

with open("./raw/List1.txt", mode="r") as raw:
    for i in raw:
        piece = i.split()
        piece[1] = snc(piece[1])
        print(piece)