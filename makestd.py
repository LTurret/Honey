import json
import os

def makefile(dataset):
    with open("dataset.json", mode='w') as file:
        json.dump(dataset, file, indent=4)

def import_data(dataname:str = "List.txt"):
    for file in os.listdir():
        if file == dataname:
            return open(file, 'r', encoding="UTF-8")

def main():
    structure = {
        "mass": {},
        "amplitude": {}
    }

    data = import_data("Real.txt")
    try:
        for line in data:
            mass = line.split('\t')[0]
            if mass not in structure:
                structure['mass'].append(mass)
                structure['amplitude'].append(
                    mass = 
                    {
                        "value": float(line.split('\t')[-1][:-1])
                    }
                )
            elif mass in structure:
                structure['amplitude'][mass] = mass
        data.close()

        makefile(structure)
    except Exception as e:
        print(e)
        return 0

if __name__ == "__main__":
    main()

    # for dirPath, dirNames, fileNames in os.walk("./data"):
    #     path = f"{dirPath}/List.txt"
    #     path = path.replace("\\", "/")
    #     try:
    #         with open(path, 'r') as file:
    #             print(f'List on path: "{dirPath[7:]}" joins!')
    #     except:
    #         pass