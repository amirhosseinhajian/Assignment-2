import math

seccond = int(input("Enter the seccond: ")) / 3600
hour = math.floor(seccond)
ashar = (seccond - math.floor(seccond)) * 60
minute = math.floor(ashar)
ashar2 = (ashar - math.floor(ashar)) * 60
seccond = math.ceil(ashar2)
if hour < 10 and hour < 10:
    print(f"0{hour}:0{minute}:{seccond}")
elif hour < 10:
    print(f"0{hour}:{minute}:{seccond}")
elif minute < 10:
    print(f"{hour}:0{minute}:{seccond}")
else:
    print(f"{hour}:{minute}:{seccond}")
