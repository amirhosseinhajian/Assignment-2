time = input("Enter the time: ")
list = time.split(":")
seccond = int(list[0]) * 3600 + int(list[1]) * 60 + int(list[2])
print(seccond)