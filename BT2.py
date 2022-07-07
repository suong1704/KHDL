from numpy import append
mang = []
mang1=[('Tom', '19', '80'),('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), 
]
def Nhap(n):
    for i in range(n):
        print("Nhap ",i+1)
        a=input()
        if(a != 'done'):
            tp = tuple(str(x) for x in a.split(","))
            mang.append(tp)
        else:
             break
# Nhap(2)
result = sorted(mang, key=lambda x:(x[0], x[1], x[2]))
result1 = sorted(mang1, key=lambda x:(x[0], x[1], x[2]))
print(result1)