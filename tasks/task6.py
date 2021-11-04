'''6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же, но с прописной первой буквой. 
    Например, print(int_func(‘text’)) -> Text.
    Продолжить работу над заданием. 
    В программу должна попадать строка из слов, разделенных пробелом. 
    Каждое слово состоит из латинских букв в нижнем регистре. 
    Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы. 
    Необходимо использовать написанную ранее функцию int_func().'''
class Main:
    def __call__(self):
        config = (({"in":"Введите слова из маленьких латинских букв, разделенных пробелом: ","out":"Результат = {0}", "def":self.FuncResult}))
        return config 

    # Используем стандартную функцию для установки заглавной буквы в слове
    def int_func_first(self, text):
        return text.capitalize()

    # Используем собственную реализацию для установки заглавной буквы в слове
    def int_func_second(self, text):
        length = len(text)
        if length<=0 or not text[0:1].isalpha():
            return text
        return text[0:1].upper()+text[1:length]

    # Используем стандартную функцию для установки заглавной буквы во всех словах в переданной строке (по сути почти вся наша программа)
    def int_func_third(self, text):
        return text.title()

    def FuncResult(self, value, out):
        words = value.split(" ")
        result = ""
        for word in words:
            result += self.int_func_first(word) + " "
        return out.format(result)
