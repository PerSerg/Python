class One:
   
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def multiplication(self,a,b):
        return a*b
    def amount(self,a,b):
        return a+b    
    def division(self,a,b):
        if b == 0:
            return "ERROR"
        else:
            return a/b
    def subtraction(self,a,b):
        return a-b
calc_mode = One(3,0)
print(calc_mode.multiplication(calc_mode.a, calc_mode.b))
print(calc_mode.amount(calc_mode.a, calc_mode.b))    
print(calc_mode.division(calc_mode.a, calc_mode.b))
print(calc_mode.subtraction(calc_mode.a, calc_mode.b))