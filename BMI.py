class Bmi:
    def __init__(self,weight, high):
        self.__weight = weight
        self.__high = high / 100
        self.__bmi = self.__weight / (self.__high**2)

    def calculate_and_showData(self):
        print(f"ค่าBMIของคุณ = {self.__bmi:.2f}")

    def checkBMI(self):
        if self.__bmi < 18.50:
            return ("ซึ่งน้อยกว่าเกณฑ์")
        elif self.__bmi < 22.90:
            return ("ซึ่งปกติดี")
        elif self.__bmi < 24.90:
            return ("ซึ่งเป็นโรคอ้วนระดับ1")
        elif self.__bmi < 29.90:
            return ("ซึ่งเป็นโรคอ้วนระดับ2")
        else: 
            return ("ซึ่งเป็นโรคอ้วนม่กระดับ3")
w = float(input("Please insert Weight:"))
h = float(input("Please insert High:"))

bmi = Bmi(weight=w, high=h)
bmi.calculate_and_showData()
print(bmi.checkBMI())