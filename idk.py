import json

import pandas as pd

class operation():
    def full_package(data, name:str):
        with open(data, mode="r") as List:
            with open(f"./output/{name}", mode="w") as package:
                package.write(formatting(List))

def softopen(filename:str, openmode:str):
    filename += ".txt"
    return open(filename, mode=openmode, encoding="utf-8")

# 設計class，一個用來整理成Series，一個用來整理成List
def formatting(file):
    mass_list = []
    amplitude_list = []
    for line in file:
        mass = float(line.split('\t')[0])
        amplitude = float(line.split('\t')[-1][:-1])

        mass_list.append(mass)
        amplitude_list.append(amplitude)
    tasks = pd.Series(data=amplitude_list, index=mass_list)
    return tasks

def main():
    operation.full_package(data="./raw/List1.txt", name="List1")

if __name__ == "__main__":
    main()
