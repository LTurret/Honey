import json

class fileoperations():
    # open file, terminate externally
    def softopen(filename:str, openmode:str):
        filename += ".txt" # file extension handler
        return open(filename, mode=openmode, encoding="utf-8")

    def save(file:dict, filename:str):
        with open(filename, mode="w") as file:
            json.dump(file, filename)
        return 1

    def save_exit(file:dict, filename:str):
        with open(filename, mode="w") as file:
            file = json.load(file)
            json.dump(file, filename)
        file.close()
        return 1

def formatting(file):
    tasks = []
    for line in file:

        # define data format
        mass = float(line.split('\t')[0])
        amplitude = float(line.split('\t')[-1][:-1])

        # create dict-like list for sorts
        tasks.append((mass, amplitude))
    file.close()
    return tasks

def main():
    # first manifest
    datasets = []
    data = fileoperations.softopen(filename="./raw/List1", openmode="r")
    datasets.extend(formatting(data))

    # second manifest
    datasets = []
    data = fileoperations.softopen(filename="./raw/List2", openmode="r")
    datasets.extend(formatting(data))

if __name__ == "__main__":
    main()