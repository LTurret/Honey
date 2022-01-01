data = {
    "mass": {},
    "amplitude": {}
}

def check(data, key:str):
    if key in data['mass']:
        print(data['mass'][key])
    else:
        print("no data found")

check(data, "meow")