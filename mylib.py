
def Dem():
    f = open('test.txt')
    data = f.read()
    data = data.lower()
    list = data.split(" ")
    count={}
    for i in list:
        i = i.strip(".,?/!<>()")
        if i in count:
            count[i]+=1
        else:
            count[i]=1
    for j in sorted(count, key=count.get, reverse=False):
        if (j != ''):
            print(j, count[j])
    