# конкатенация
import colorama
from colorama import init
from colorama import Fore, Back, Style
# use Colorama to make Termcolor work on Windows too
init()
print(Fore.GREEN)
name = input("Как Тебя зовут? ")
print("Привет,", name)
age = input("Сколько тебе лет:")
print(age)
name = input("Что значит твое имя? ")
print(name + "," + "Cам придумал" +  "или кто-то помог" + "!")

