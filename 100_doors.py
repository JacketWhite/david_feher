door =[0 for i in range(100)]
step = 1
while step <= 100:
    i = step-1
    while i < 100:
        if door [i] == 0:
            door [i] = 1
        else:
            door [i] = 0
        i=i+step
    step = step + 1

for i in range(0, 100):
    if door[i] == 1:
        print(i+1)
