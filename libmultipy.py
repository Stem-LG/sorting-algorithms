class sorting:

    def shell(a):
        n = len(a)
        gap = n//2
        for i in range(gap):
            while gap > 0:
                for i in range(gap,n):
                    temp = a[i]
                    while  i >= gap and a[i-gap] >temp:
                        a[i] = a[i-gap]
                        i -= gap
                    a[i] = temp
                gap //= 2

    def insertion(a):
        for i in range(1,len(a)):
            c=a[i]
            while i>0 and a[i-1]>c:
                a[i]=a[i-1]
                i-=1
            a[i]=c

    def bullet(a):
        for y in range(6):
            changed = False
            for x in range(6):
                if a[x] > a[x+1]:
                    a[x],a[x+1] = a[x+1],a[x]
                    changed = True
            if not(changed):
                break

    def selection(a):
        for i in range(6):
            s = i
            for j in range(i+1 , 7):
                if a[s] > a[j]:
                    a[s],a[j] = a[j],a[s]