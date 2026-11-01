words = ['python', 'cat', 'programming', 'dog', 'computer', 'hi']
result = (word.upper() if len(word) > 5 else len(word) for word in words)
print(result.__next__())
print('Начало цикла')
for a in result:
    print(a)
# print(result.__next__())

def cubes(num:int):
    temp = []
    for x in range(num):
        temp.append(x**3)
    return temp

b = cubes(11)
print(b, type(b), type(cubes))

def cubes2(num:int):
    for x in range(num):
        yield x**3 #сохраняет обьект генератора

c = cubes2(11)
print(c, type(c), type(cubes2))
for x in c:
    print(x)