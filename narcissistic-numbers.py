rangee = int(input("Set your range: "))

for i in range(rangee):
    total = 0
    listt = list(str(i))
    power = len(listt)
    for a in listt:
        total += int(a)**power
    if total == i:
        print(total)
    
