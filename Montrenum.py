import time
for i in range (24):
    if i==24:
        i=00
    for j in range(60):
        for k in range(60):
            print(i,'h:',j,'min:',k,'s')
            time.sleep(1)