import matplotlib.pyplot as plt
import pandas as pd

# comparison and sort with mass
def tupleShift(datasets):
    for mass, amplitude in datasets:
        print(mass, amplitude)

# open file, terminate externally
def softopen(filename:str, openmode:str):
    filename += ".txt" # file extension
    return open(filename, mode=openmode, encoding="utf-8")

def main():
    # create tasks that awaited be sort
    tasks = [
        "./raw/List",
    ]
    for List in tasks:
        data = softopen(List, "r")
        mass_array=[]
        amplitude_array=[]
        for line in data:
            mass = float(line.split('\t')[0])
            amplitude = float(line.split('\t')[-1][:-1])
            
            # arrays for plot
            mass_array.append(mass)
            amplitude_array.append(amplitude)
        data.close() # file involk terminates here

        plt.rcParams["figure.figsize"] = (19.2, 10.8)
        plt.bar(
            [1, 2, 3],
            [1, 2, 3],
            width=0.5,
            bottom=None,
            align='center',
            )
        plt.xticks(rotation='vertical')
        plt.show()

if __name__ == "__main__":
    main()
