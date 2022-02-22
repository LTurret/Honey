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
        "List1",
        "List2"
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
        plt.plot(mass_array, amplitude_array, color="b")

        # 設定x軸標題
        plt.xlabel('mass') 

        # 設定x軸label以及垂直顯示
        plt.xticks(mass_array, rotation="vertical", fontsize=10)
        
        # 設定圖表標題
        plt.title('honey') 

        # 顯示圖表，需要GUI
        #plt.show()

        plt.savefig(f"./output/{List}.jpg")

        # 清除圖表
        plt.clf()

if __name__ == "__main__":
    main()
