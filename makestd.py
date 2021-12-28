import json
import os

def make_std():
    std = {"mz": [], "ap": []}
    with open("std.json", mode='w') as file:
        json.dump(std, file, indent=4)

def import_data():
    dump = ""
    for file in os.listdir():
        if file == "List.txt":
            with open(file, mode='r') as data:
                for line in data:
                    dump += line
    return dump

def main():
    data = import_data()
    data = data.split("\t")
    mz, ap = data[0], data[1][:-1]
    print(mz, float(ap))
    make_std()

if __name__ == "__main__":
    for root, dirs, files in os.walk("./data"):
        for file in files:
            if (file == "List.txt"):
                print("founds")