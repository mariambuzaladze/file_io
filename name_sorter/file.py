with open("names.txt", "r") as file:
    names = [name.strip() for name in file.readlines()]

sorted_names = sorted(names)

with open("sorted_names.txt", "w") as file:
    file.write(f"Total of {len(sorted_names)} names\n")
    file.write("-" * 17 + "\n")
    for name in sorted_names:
        file.write(name + "\n")
