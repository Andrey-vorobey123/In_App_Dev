def print_result(func_t_d):
    
    def decorated(*args, **kwargs):
        func_t_d(*args, **kwargs)
        print(str(func_t_d.__name__))
        element = func_t_d(*args, **kwargs)
        if isinstance(element, str):
            print(element)
        elif isinstance(element, int):
            print(element)
        elif isinstance(element, dict):
            for key, value in element.items():
                print(key, '=', value)
        elif isinstance(element, list):
            for i in element:
                print(i)
        return element
    return decorated

@print_result
def test_1():
    return 1


@print_result
def test_2():
    return 'iu5'


@print_result
def test_3():
    return {'a': 1, 'b': 2}


@print_result
def test_4():
    return [1, 2]


if __name__ == '__main__':
    print('!!!!!!!!')
    test_1()
    test_2()
    test_3()
    test_4()