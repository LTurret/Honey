# open file, terminate externally
def softopen(filename:str, openmode:str):
    filename += ".txt" # file extension handler
    return open(filename, mode=openmode, encoding="utf-8")

def fetch(datafile):
    tasks = []
    for line in datafile:

        # define data format
        mass = float(line.split('\t')[0])
        amplitude = float(line.split('\t')[-1][:-1])

        # create dict-like list for sorts
        tasks.append((mass, amplitude))
    datafile.close() # file involk terminates here
    return tasks

def main():
    datasets = []
    data = softopen("List", "r")
    datasets.extend(fetch(data))
    data = softopen("List2", "r")
    datasets.extend(fetch(data))
    print(datasets)
    # datasets.sort()

if __name__ == "__main__":
    main()