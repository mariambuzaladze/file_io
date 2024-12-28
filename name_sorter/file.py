with open("names.txt","r") as file:
    names = [name.strip() for name in file.readlines()]


with open("sorted_names.txt","w") as file:
    for name in sorted(names):
        file.write(name+"\n")