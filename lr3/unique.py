from get_random import Get_Rand


# Итератор для удаления дубликатов
class Unique:
    def __init__(self, items, **kwargs):
        # Нужно реализовать конструктор
        # В качестве ключевого аргумента, конструктор должен принимать bool-параметр ignore_case,
        # в зависимости от значения которого будут считаться одинаковыми строки в разном регистре
        # Например: ignore_case = True, Aбв и АБВ - разные строки
        #           ignore_case = False, Aбв и АБВ - одинаковые строки, одна из которых удалится
        # По-умолчанию ignore_case = False
        self.used_elements = set()
        self.data = list(items)
        self.index = 0
        if 'ignore_case' in kwargs.keys():
            self.ignore_case = kwargs['ignore_case']
        else:
            self.ignore_case = False

    def __next__(self):
        while True:
            if self.index >= len(self.data):
                raise StopIteration
            else:
                current = self.data[self.index]
                self.index = self.index + 1
                if self.ignore_case:
                    if current.upper() not in self.used_elements:
                        self.used_elements.add(current.upper())
                        return current
                else:
                    if current not in self.used_elements:
                        self.used_elements.add(current)
                        return current

    def __iter__(self):
        return self

def UnSo(some):
    mas = []
    for i in Unique(some, ignore_case = True):
        mas.append(i)
    return sorted(mas)


if __name__ == '__main__':
    res = []
    for i in Unique([1, 3, 2, 1, 3, 2, 1, 3, 1, 2, 6, 6, 6]):
        res.append(i)
    print(sorted(res), "\n")
    res.clear()
    for i in Unique(Get_Rand(10, 1, 3)):
        res.append(i)
    print(sorted(res), "\n")
    res.clear()
    for i in Unique(['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']):
        res.append(i)
    print(sorted(res), "\n")
    res.clear()
    for i in Unique(['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B'], ignore_case = True):
        res.append(i)
    print(sorted(res), "\n")
    res.clear() 
