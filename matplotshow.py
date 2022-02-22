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
    mass_array=[]
    amplitude_array=[]
    tasks=[]
    datas = [
        "List1",
        "List2"
    ]
    for List in datas:
        data = softopen(List, "r")
        for line in data:
            mass = float(line.split('\t')[0])
            amplitude = float(line.split('\t')[-1][:-1])
            
            # arrays for plot
            mass_array.append(mass)
            amplitude_array.append(amplitude)
            tasks.append((mass, amplitude))
        data.close() # file involk terminates here

        plt.plot(mass_array, amplitude_array, color='b')
        plt.xlabel('mass') # 設定x軸標題
        plt.xticks(mass_array, rotation='vertical') # 設定x軸label以及垂直顯示
        plt.title('honey') # 設定圖表標題
        #plt.show()
        plt.savefig(f"./output/{List}.png")

if __name__ == "__main__":
    main()
