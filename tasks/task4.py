'''4. Программа принимает действительное положительное число x и целое отрицательное число y. 
    Необходимо выполнить возведение числа x в степень y. 
    Задание необходимо реализовать в виде функции my_func(x, y). 
    При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
Подсказка: попробуйте решить задачу двумя способами. 
    Первый — возведение в степень с помощью оператора **. 
    Второй — более сложная реализация без оператора **, предусматривающая использование цикла.'''
class Main:
    def __call__(self):
        config = (
            ({"in":"Введите действительное положительное число x: ", "def":self.FuncSetX, "type":(float,int)}),
            ({"in":"Введите целое отрицательное число y: ", "def":self.FuncSetY, "type":int}),
            ({"out":"Первый способ результат = {0}", "def":self.FuncGetFirst}),
            ({"out":"Второй способ результат = {0}", "def":self.FuncGetSecond}))
        return config

    def FuncSetX(self, value, out):
        if value<=0:
            raise Exception("PositiveNumber")
        self.x = value

    def FuncSetY(self, value, out):
        if value>=0:
            raise Exception("NegativeNumber")
        self.y = value

    def FuncGetFirst(self, value, out):
        return self.FuncFirst(self.x, self.y)

    def FuncGetSecond(self, value, out):
        return self.FuncSecond(self.x, self.y)           

    def FuncFirst(self, x, y):
        return x ** y

    def FuncSecond(self, x, y):
        result = x
        i = abs(y)
        while i > 1:
            result*=x
            i-=1
        if y<0:
            return 1/result
        else:
            return result
