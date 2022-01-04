import json
import os

def makefile(dataset):
    with open("dataset.json", mode='w') as file:
        json.dump(dataset, file, indent=4)

def import_data(path:str):
    return open(path, 'r', encoding="UTF-8")

def sortion(payload):
    items = payload.items()
    sorted_items = sorted(items)
    new_dict = {}
    for key, value in sorted_items:
        new_dict[key] = value
    return new_dict

def read_data(data, structure:list):
    try:
        for line in data:
            mass = line.split('\t')[0]

            # counter
            if mass not in structure['times']:
                structure['times'][mass] = 1
            else:
                structure['times'][mass] += 1

            # make average
            if mass not in structure['mass']:
                structure['mass'].append(float(mass))
                structure['amplitude'].append(float(line.split('\t')[-1][:-1]))
            elif mass in structure['times']:
                structure['amplitude'][mass] = (
                    structure['amplitude'][mass]+ mass
                    ) / structure['times'][mass]
        data.close()
        return structure
    except Exception as e:
        print(e)
        return

def main():
    structure = {
        "mass": [],
        "amplitude": [],
        "times": {}
    }

    folder = "./data"
    for dirPath, _, _ in os.walk(folder):
        path = f"{dirPath}/List.txt"
        path = path.replace("\\", "/")
        if (dirPath == folder):
            pass
        else:
            try:
                # print(f'List on path: "{dirPath[7:]}" joins!')
                # print(path)
                data = import_data(path)
                structure = read_data(data, structure)
            except Exception as e:
                print(e)
                pass
    structure['times'] = sortion(structure['times'])
    makefile(structure)

if __name__ == "__main__":
    main()