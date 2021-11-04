'''5. Программа запрашивает у пользователя строку чисел, разделенных пробелом. 
    При нажатии Enter должна выводиться сумма чисел. 
    Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter. 
    Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме. 
    Но если вместо числа вводится специальный символ, выполнение программы завершается. 
    Если специальный символ введен после нескольких чисел, то вначале нужно добавить сумму этих чисел к полученной ранее сумме и после этого завершить программу.'''
class Main:

    def __init__(self):
        self.sum=0

    def __call__(self):
        config = (({"in":"Введите строку чисел, разделенных пробелом (или все кроме числа для выхода): ","out":"Сумма чисел = {0}", "def":self.FuncSum}))
        return config 

    def FuncSum(self, value, out):
        values=value.split(" ")

        for number in values:
            if number=="":
                continue

            try:
                number=float(number)
                self.sum+=number
            except:
                print(out.format(self.sum))
                self.sum=0
                return#raise Exception("ProgramStop")

        print(out.format(self.sum))
        raise Exception("Repeat")
