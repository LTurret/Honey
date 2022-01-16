import json, os
import numpy as np

def makefile(dataset):
    with open("dataset.json", mode='w') as file:
        json.dump(dataset, file, indent=4)

def import_data(path:str):
    return open(path, 'r', encoding="UTF-8")

def read_data(data, structure:list):
    try:
        counter = 0
        for line in data:
            counter += 1
            # data format definition
            mass = float(line.split('\t')[0])
            amplitude = float(line.split('\t')[-1][:-1])

            # times counter
            if mass not in structure['times']:
                structure['times'][mass] = 1
            else:
                structure['times'][mass] += 1

            # make average
            if mass not in structure['set']:
                structure['set'][mass] = amplitude
            elif mass in structure['times']:
                structure['set'][mass] = 0
        data.close()
        print(counter)
        return structure
    except Exception as e:
        print(e)
        return

def main():
    structure = {
        "set": {},  # fullform of data
        "times": {} # mass counter
    }

    folder = "./data"
    tasks = []
    for dirPath, _, _ in os.walk(folder):
        path = f"{dirPath}/List.txt"
        path = path.replace("\\", "/")
        tasks.append(path)
    try:
        for task in range(1, len(tasks)):
            data = import_data(tasks[task])
            structure = read_data(data, structure)
            # print(len(structure))
    except Exception as e:
        print(e)
        pass
    # makefile(structure)

if __name__ == "__main__":
    main()