''' Напишите код, который выводит на экран следующее:
I will be a Python developer
Вопросы к этому заданию
'''
# print('I will be a Python developer')
'''
Выполните задание, следуя инструкциям в вопросах
Вопросы к этому заданию
Выведите на экран результат произведения чисел 3 и 7
Выведите на экран результат возведения числа 4 в степень 3
Выведите на экран результат вычисления остатка от деления числа 29 на 5
'''
# print(3 * 7)
# print(4 ** 3)
# print(29 % 5)
'''
Выполните задание, следуя инструкциям в вопросах
Вопросы к этому заданию

Создайте переменные, описывающие автомобиль - модель, цвет, год, количество дверей. Поместите в них значения. Затем поменяйте цвет автомобиля, присвоив ниже в коде новое значение соответствующей переменной. Выведите на экран все значения.  При создании имён переменных используйте подходящие по смыслу слова. Воспользуйтесь Google переводчиком, если нужно.

Создайте переменные, в которые будете помещать возраст людей. Также создайте переменную, в которой будет храниться количество людей.  Вычислите и выведите на экран средний возраст человека исходя из данных о возрасте этих пятерых людей. Если не знаете формулу вычисления среднего арифметического значения, воспользуйтесь поиском информации в интернете. При создании имён переменных используйте подходящие по смыслу слова. Воспользуйтесь Google переводчиком, если нужно.
'''
# car_model = 'Chevrolett Lacetti'
# car_color = 'black'
# year = 2011
# numbers_of_doors = 5

# i_am = 35
# my_wife = 35
# my_son = 15
# my_daughter = 12
# my_masya = 8
# count = 5
# average_age = (i_am + my_wife + my_son + my_daughter 
#                     + my_masya) / count
# print(average_age)
'''
Выполните задание, следуя инструкциям в вопросах
Вопросы к этому заданию
Создайте переменные, поместите в них значения - имя, фамилию и возраст. Выведите на экран следующее предложение: "Hi! My name is имя фамилия, I'm возраст years old." Используйте конкатенацию переменных и строк.
Выведите на экран текст детской песенки:
Baa, baa, black sheep,
Have you any wool?
Yes sir, yes sir,
Three bags full
One for the master,
One for the dame,
And one for the little boy
Who lives down the lane
Baa, baa, black sheep,
Have you any wool?
Yes sir, yes sir,
Three bags full
Отступите от левого края расстояние, равное двум табуляциям. Выполните перенос текста на новую строку двумя способами
'''
# my_first_name = 'Dmitry'
# my_second_name = 'Tygyshev'
# my_age = 35
# print('Hi! My name is', my_first_name, my_second_name + ', I\'m ' + str(my_age) + ' years old')
# print('''\tBaa, baa, black sheep,
# \tHave you any wool?
# \tYes sir, yes sir,
# \tThree bags full
# \tOne for the master,
# \tOne for the dame,
# \tAnd one for the little boy
# \tWho lives down the lane
# \tBaa, baa, black sheep,
# \tHave you any wool?
# \tYes sir, yes sir,
# \tThree bags full''')
'''
Выполните задание, следуя инструкциям в вопросах
Вопросы к этому заданию
Создайте список, содержащий разные типы данных
Создайте список, извлеките из него элементы с 1 по 3, поместите их в новый список и распечатайте
'''
# my_list = [1, -9, 'evgen', 45, 'loch', 6.87]
# my_second_list = [my_list[:3]]
# print(my_second_list)
'''
Создайте объект dictionary, содержащий пары ключей и значений, выведите на экран одно значение
Создайте объект dictionary, описывающий компьютер
'''
# my_sklad_dict = {'Evgen':'loch',
#                  'Sosok':'daun',
#                  'Yakov':'foggot'}
# print(my_sklad_dict['Sosok'])
'''
Создайте объект tuple, описывающий компьютер и распакуйте его в соответствующие переменные. Выведите переменные вызвав функцию print() один раз
'''                  
# comp = ('processor', 'ram', 'hdd', 'video')
# el_1, el_2, el_3, el_4 = comp
# print(el_1, el_2, el_3, el_4, sep='\n')
'''
Создайте множество при помощи функции set() из текста, чтобы получить уникальные символы, содержащиеся в тексте. Присвойте результат переменной. Выведите переменную на экран. Выведите тип значения переменной на экран. При необходимости найдите информацию в интернете
'''
# string = 'Evgen is foggot and retard'
# string_set = set(string)
# print(string_set)
# print(type(string_set))
'''
Создайте 2 переменных, содержащие числовые значения. Сравните их при помощи всех операторов сравнения и выведите результат на экран
Сравните две одинаковых буквы, но одна из них должна быть заглавной, при помощи операторов сравнения ">" и выведите результат на экран. Выведите на экран ASCII код каждой из букв
'''
# x = 5
# y = 10
# print(x > y)
# print(x < y)
# print(x == y)
# print(x != y)

# letter_1 = 'A'
# letter_2 = 'a'
# print(letter_1 > letter_2)
# print(ord(letter_1), ord(letter_2), sep='\n')
'''
Напишите код, который выводит сообщение: 'Enter any number'. Если было введено число 7, должно выводиться сообщение: '7 is a lucky number! Today is your lucky day!', если введено что-то другое - должно выводиться сообщение 'Thank you! Have a nice day!'

Напишите код, который выводит сообщение: 'Enter an integer number'. Если было введено чётное число, должно выводиться сообщение: 'The number is even', если было введено нечётное число, должно выводиться сообщение 'The number is odd'
'''
# lucky_number = int(input('Enter any number \n'))
# if lucky_number == 7:
#   print('7 is a lucky number! Today is lucky day')
# else:
#   print('Thank you! Have a nice day')

# int_number = int(input('Enter an integer number\n'))
# if int_number % 2 == 0:
#   print('The number is even')
# else:
#   print('The number is ood')      
'''
Используйте цикл for для вычисления всех чётных чисел в диапазоне от 10 до 30 (включая крайние значения). Выведите результат на печать

Получите от пользователя число на вводе и используйте цикл for для вывода на экран текста 'Hello!' столько же раз
'''
# summ = 0
# for i in range(10, 31):
#   if i % 2 == 0:
#     summ += i
# print(summ)

# count = int(input('Enter a number\n'))
# for _ in range(count):
#   print('Hello')
'''
При помощи функции randint() из модуля  random генерируйте числа в диапазоне от 1 до 10 и помещайте в список, до тех пор пока не будет сгенерировано число 7. Распечатайте содержимое списка.
'''
# import random
# number_list = []
# while True:
#   num = random.randint(1, 10)
#   if num != 7:
#     number_list.append(num)
#   else:
#     break
# print(number_list)
'''
»з исходного списка greetings = ['hello', 'hi', 'hey', 'hola'] создайте новый список содержащий вторую букву из каждой строки исходного списка. ¬ыведите новый список на печать.

–ешите задание двум¤ способами - при помощи List Comprehension и без него.

»з исходного списка digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] создайте новый список содержащий нечетные числа исходного списка. ¬ыведите новый список на печать.

–ешите задание двум¤ способами - при помощи List Comprehension и без него.
'''
# greetings = ['hello', 'hi', 'hey', 'hola']
# new_list = []
# for i in greetings:
#   new_list.append(i[1])
# print(new_list)

# new_list_1 = [i[1] for i in greetings]
# print(new_list_1)

# digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# new_digits = []
# for i in digits:
#   if i % 2 != 0:
#     new_digits.append(i)
# print(new_digits)

# new_digits_1 = [i for i in digits  if i % 2 != 0]
# print(new_digits_1)

'''Создайте функции cat_voice() and dog_voice(), которые выводят на экран 'Meow!' и 'Woof!' соответственно. Сделайте по одному вызову каждой из функций

Создайте функции cat_voice() and dog_voice(), которые возвращают значения 'Meow!' и 'Woof!' соответственно. Выведите на экран 'Meow!' и 'Woof!' по 2 раза

Создайте функцию get_voice() которая возвращает передаваемый ей в качестве параметра текст c восклицательным знаком.

Создайте функцию, которая генерирует последовательность нечетных чисел в диапазоне от a до b (a и b включительно). Значения a и b должны передаваться в качестве параметров. Результирующая последовательность должна возвращаться в форме объекта list. Решите задание двумя способами - при помощи List Comprehension  и без него
'''

# def cat_voice():
#   print('Meow')


# def dog_voice():
#   print('Woof')

# cat_voice()
# dog_voice()  

# def cat_voice():
#   return 'Meow'


# def dog_voice():
#   return 'Woof'

# print(cat_voice())
# print(dog_voice())  

# def get_voice(text):
#   return text + '!'
# print(get_voice('Hello'))

# def get_list(a, b):
#   my_list = []
#   for i in range(a, b + 1):
#     if i % 2 != 0:
#       my_list.append(i)
#   return my_list

# print(get_list(1, 10))

# def get_list(a, b):
#   my_list = [num for num in range(a, b + 1) if num % 2 != 0]
#   return my_list

# print(get_list(1, 101))
'''Создайте класс BlogPost с атрибутами user_name, text, number_of_likes. Создайте два объекта этого класса. После создания измените атрибут number_of_likes одного из объектов. Распечатайте атрибут number_of_likes каждого из объектов
'''
# class BlogPost:


#   def __init__(self, user_name, text, number_of_likes):
#     self.user_name = user_name
#     self.text = text
#     self.number_of_likes = number_of_likes

# post_1 = BlogPost('evgen', 'evgen is foggot', 10)
# post_2 = BlogPost('kobez', 'kobez is retard', 5)

# post_1.number_of_likes = 88
# print(post_1.number_of_likes)
# print(post_2.number_of_likes)
'''Создайте класс BankAccount с атрибутами client_id, client_first_name, client_last_name, balance и методами add() и withdraw(), при помощи которых можно пополнять счет и выводить средства со счета соответственно. Атрибут balance должен инициализироваться по умолчанию значением 0.0 и меняться при срабатывании методов add() и withdraw().
'''

# class BankAccount:


#   def __init__(self,client_id, client_first_name, client_last_name, balance=0.0 ):
#     self.client_id = client_id
#     self.client_first_name = client_first_name
#     self.client_last_name = client_last_name
#     self.balance = balance

#   def add(self, money):
#     self.balance = self.balance + money
  
#   def withdraw(self, money):
#     self.balance = self.balance - money

# iam = BankAccount(1, 'Dmitry', 'Tygushev')
# iam.add(100)
# iam.add(48596079)
# iam.add(1)
# iam.withdraw(400000000)
# print(iam.balance)
'''Создайте класс GameCharacter с атрибутами name, health, level и методом speak(), который выводит на печать 'Hi, my name is (значение атрибута name)'.

Создайте класс Villain, наследник класса GameCharacter с теми же атрибутами, методом speak(), который выводит на печать 'Hi, my name is (значение атрибута name) and I will kill you', методом kill(), который принимает в качестве параметра объект класса GameCharacter, присваивает атрибуту health этого объекта значение 0 и  выводит на печать 'Bang-bang, now you're dead'
'''
class GameCharacter:
  def __init__(self, name, health, level):
    self.name = name
    self.health = health
    self.level = level

  def speak(self):
    print('Hi, my name is {}'.format(self.name))

iam = GameCharacter('nachtgast', 100, 10)
iam.speak()

class Villian(GameCharacter):
  def __init__(self, name, health, level):
    GameCharacter.__init__(self, name, health, level)

  def speak(self):
    print('Hi, my name is {} and I will kill you'.format(self.name))

  def kill(self, other):
    other.health = 0
    print('Bang-bang, now you\'re dead')

you = Villian('hz', 10, 10)
you.kill(iam)
print(iam.health)    

