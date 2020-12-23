import json
import sys
from print_result import print_result
from cm_timer import cm_timer_1
from time import sleep
from unique import UnSo
from get_random import Get_Rand

way = "lr3/data_light.json"


global data
with open(way, 'r', encoding='utf-8') as f:
    data = json.load(f)


@print_result
def f1(source):
    return UnSo([some['job-name'] for some in source])

@print_result
def f2(source):
    return list(filter(lambda n: "программист" in n, source))

@print_result
def f3(source):
    return list(map(lambda i: i + 'с опытом Python', source))

@print_result
def f4(source):
    return list(map(lambda i: i + ', зарплата ' + str(*Get_Rand(1, 100_000, 200_000)) + ' рублей', source))

if __name__ == '__main__':
    with cm_timer_1():
        f4(f3(f2(f1(data))))
        sleep(1.5)
