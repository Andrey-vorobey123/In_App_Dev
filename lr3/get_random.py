import random


def Get_Rand(count, begin, end):
    for counter in range(count):
        yield random.randint(begin, end)


if __name__ == '__main__':
    random_str = Get_Rand(6, 1, 6)
    print(list(random_str))

""" while True:
    try:
        i = random_str.__next__()
        print(i)
    except StopIteration:
        break
 """
