name = input("enter your name : ")
temp = ""
for i in range(len(name)):
    if name in [i] not in temp:
        print(f"{name[i]}: {name.count(name[i])}")
        temp += name[i]