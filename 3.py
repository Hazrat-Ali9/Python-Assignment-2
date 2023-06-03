class Numbers:
    def __init__(self,a, b, c) -> None:
        self.a = a
        self.b = b
        self.c = c

    def sum(self):
        result = self.a + self.b + self.c
        return result
    
    def factorial(self):
        fact = 1
        for i in range(1, self.b + 1):
            fact *= i
        return fact
    

my_num = Numbers(3, 5, 7)

print(my_num.sum())

print(my_num.factorial())
