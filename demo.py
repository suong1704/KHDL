from itertools import count
from pickle import TRUE


n = "10"
#print(n*3)
#print(type(n*3))
fruits_name_1 = "Cam"
fruits_num_1 = 2
fruits_name_2 = "Chanh"
fruits_num_2 = 10
fruits=[[fruits_name_1,fruits_num_1],[fruits_name_2,fruits_num_2]]
print(fruits)
fruits.append(["Xa",5])
print(fruits)
fruits += [["Tao", 7]]
print(fruits)
alphabet = ["a", "b", "c"]
alphabet_copy = alphabet
alphabet_copy[0] = "A"
print(alphabet_copy) # ["A", "b", "c"]
print(alphabet) # giá trị trong alphabet: ["A", "b", "c"]
#copy có nhân bản
alphabet_copy1 = alphabet[:]
alphabet_copy1[2] = "D"
print(alphabet_copy1) # ["A", "b", "c"]
print(alphabet) # giá trị trong alphabet: ["A", "b", "c"]

list = ["a", "b"]
for index, value in enumerate(list): # lấy index của list
    print(index, value)

town = {"Aichi": "Nagoya", "Kanagawa": "Yokohama", "Hokkaido": "Sapporo"}
for city, citys in town.items():
    print(city,citys)
fruits = {"strawberry": "red", "peach": "pink", "banana": "yellow"}
for fruit, color in fruits.items(): # fruit là key và color là giá trị
    print(fruit+" is "+color)

animal = "elephant"
# Hãy tạo biến animal_big với chuỗi viết hoa của animal
animal_big = animal.upper();
print(animal)
print(animal_big)
print(animal.count("e"))

print("Tôi sinh ra ở {} và sống ở {}".format("Hòa Khánh", "Hải Châu"))
# Tôi sinh ra ở Hòa Khánh và sống ở Hải Châu
print("Tôi sinh ra ở {0} và sống ở {1}, và đi làm ở {0}".format("Hòa Khánh", "Hải Châu"))
# Tôi sinh ra ở Hòa Khánh và sống ở Hải Châu, và đi làm ở Hòa Khánh

n = [53, 26, 37, 69, 24, 2]
# Hãy sắp xếp n theo thứ tự tăng dần
n.sort(reverse=False)
print(n)
# Hãy sắp xếp n theo thứ tự giảm dần
n.sort(reverse=True)
print(n)

def GiaiThua(n):
    T=1
    for i in range(1,n+1) :
        T *=i
    print(T)
GiaiThua(40)

class MyProduct: #Định nghĩa lớp
    def __init__(self, name, price): # phương thức khởi tạo
        self.name = name # gán tên vào member
        self.price = price
        self.stock = 0
        self.sales = 0
# tạo đối tượng product1
product1 = MyProduct("cake", 500)
print(product1.name) # cake
print(product1.price) # 500

class MyProduct: #Định nghĩa lớp
    def __init__(self, name, price): # phương thức khởi tạo
        self.name = name # gán tên vào member
        self.price = price
    def gia(self,soluong):
        return self.price * soluong
class GiamgiaProduct(MyProduct):
    def __init__(self,name, price,sales):
        super().__init__(name,price)
        self.sales = sales
    def gia(self,soluong):
        return self.price * soluong * (1.0-self.sales)
# tạo đối tượng product1
product1 = GiamgiaProduct("cake", 500, 0.1)
print(product1.gia(10)) # 4500.0