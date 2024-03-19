def sum(a, b):
    # print(f'{a} + {b} = {a + b}')
    return a + b

def quote():
    text = print('\"Don\'t let the noise of others\' opinions\n drown out your own inner voice.\"')
    print(text)

def all_odd(a, b):
    for i in range(a, b, 1):
        if i % 2 != 0:
            print(i)


num_1 = int(input('Початок діапазону:'))
num_2 = int(input('Кінець діапазону:'))

all_odd(num_1, num_2)

def find_max(a, b, c, d):
    return max(a, b, c, d)