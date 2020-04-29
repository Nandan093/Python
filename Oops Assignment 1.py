#Calculator

#Defining a class

class Calculator:

    a = 15 #Class valriable

    b  = 10 #class variable

    def __init__(self,a,b): #Init function for instance method
        self.a = a
        self.b = b

    def add(self): #Instance method 
        c = self.a + self.b
        return "Sum of {} and {} is {}".format(self.a,self.b,c)

    @staticmethod
    def sub(a,b): #Static method
        c = a - b
        return "Differance of {} and {} is {}".format(a,b,c)

    @classmethod
    def mul(cls): #Class method
        c = cls.a * cls.b
        return "Multiplication of {} and {} is {}".format(cls.a,cls.b,c)
    
    @classmethod
    def div(cls):
        c = cls.a / cls.b
        return "Division of {} and {} is {}".format(cls.a,cls.b,c)

    @staticmethod
    def modulus(a,b):
        c = a % b
        return "Modulus of {} and {} is {}".format(a,b,c)

    def power(self):
        c = self.a ** self.b
        return "Power of {} raise to  {} is {}".format(self.a,self.b,c)
        
    
sum1 = Calculator(2,3) #Instance method
print(sum1.add())
print(Calculator.sub(5,1))#Static method
print(Calculator.mul())#class method
print(Calculator.div())#class method
print(Calculator.modulus(5,3)) #Static method
power1 = Calculator(2,3)
print(power1.power())
