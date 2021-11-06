'''3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух аргументов.'''
class Main:
    def __call__(self):
        config = (({"out":"Сумма двух наибольших аргументов = {0}", "def":self.FuncOut}))
        return config

    def FuncOut(self, value, out):
        return out.format(self.my_func(*[7,5,9]))

    def my_func(self, *args):
        return sum(sorted(args, reverse=True)[0:2])
