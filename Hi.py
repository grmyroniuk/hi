import colorama
from colorama import init
from colorama import Fore, Back, Style
init()
print(Fore.GREEN)
name = input("Как Тебя зовут? ")
print("Привет,", name)
age = input("Сколько тебе лет:")
print(age)
name = input("Что значит твое имя? ")
print(name + "," + "Cам придумал" +  "или кто-то помог" + "!")

