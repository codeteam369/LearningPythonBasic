#bài tập xây dựng
class Animal:
    def __init__ (self, animalTypeA, nameA, widthA, heightA, weightA):
        self.animalType = animalTypeA
        self.name = nameA
        self.width = widthA
        self.height = heightA
        self.weight = weightA

#tạo tra âm thanh
    def makeVoice(self):
        print("Unknow voice")

#in thông tin
    def printMe(self):
        print(f"animalType : {self.animalType}, name : {self.name}, width : {self.width}, height : {self.height}, weight : {self.weight}")

a1 = Animal("human","teo", "20", "30cm", "60kg")
a1.printMe()
a1.makeVoice

class Dog(Animal):
    #constructor của lớp con:
    def __init__(self, nameA, widthA, heightA, weightA, isChampionA):
        Animal.__init__(self, nameA, widthA, heightA, weightA,isChampionA)
    #gán thuộc tính bổ sung
        self.isChampion = isChampionA

dog1 = Dog("dog","cậu vàng", "80cm", "40cm", "20kg",)
dog2 = ("mật", "850cm", "100m", "50kg", True)
dog1.makeVoice()
dog1.printMe()
