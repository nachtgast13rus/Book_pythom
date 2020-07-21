# name = 'Evgen'
# aka = 'foggot'
# who_is = 'Our {0} is {1} !'.format(name, aka)
# print(who_is)

my_list = list(range(11))
print(my_list)


def plus_one(num):
  return num + 1


for i in my_list:
  print(plus_one(i))


print(list(map(plus_one, my_list)))
print(list(map(lambda num: num + 1, my_list)))
