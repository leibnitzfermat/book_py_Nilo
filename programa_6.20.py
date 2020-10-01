l = [7, 1, 3, 12, 8]
#l = [1, 2, 3, 4, 5]
#l = [3, 3, 1, 5, 4]
fim = 5                    #1
while fim > 1:              #2
    trocou = False           #3
    x = 0                     #4
    while x < (fim - 1):       #5
        if l[x] > l[x + 1]:     #6
            trocou = True        #7
            temp = l[x]           #8
            l[x] = l[x + 1]
            l[x + 1] = temp
        x += 1
    if not trocou:                  #9
        break
    fim -= 1                         #10
for e in l:
    print(e)
