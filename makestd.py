import json
import os

def display(dataset):
    for mass, amplitude in zip(dataset['mass'], dataset['amplitude']):
        print(f"{mass}: {amplitude}")

def makefile(dataset):
    with open("dataset.json", mode='w') as file:
        json.dump(dataset, file, indent=4)

def import_data(dataname:str = "List.txt"):
    for file in os.listdir():
        if file == dataname:
            return open(file, 'r', encoding="UTF-8")

def main():
    dataset = {"mass": [], "amplitude": []}
    data = import_data("Real.txt")
    try:
        for line in data:
            dataset['amplitude'].append(float(line.split('\t')[-1][:-1]))
            dataset['mass'].append(line.split('\t')[0])
        data.close()
        makefile(dataset)
    except Exception as e:
        print(e)
        pass 

if __name__ == "__main__":
    # main()

    for dirPath, dirNames, fileNames in os.walk("./data"):
        path = f"{dirPath}/List.txt"
        path = path.replace("\\", "/")
        try:
            with open(path, 'r') as file:
                print(f'List on path: "{dirPath[7:]}" joins!')
        except:
            pass