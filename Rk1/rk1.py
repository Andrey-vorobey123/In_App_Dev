# Кобяк Андрей ИУ5-52Б
from operator import itemgetter

class File:
    """Файл"""
    def __init__(self, id, name, f_size, katalog_id):
        self.id = id
        self.name = name
        self.f_size = f_size
        self.katalog_id = katalog_id


class Katalog:
    """Каталог"""
    def __init__(self, id, name):
        self.id = id
        self.name = name


class FilesKatalogs:
    """
     'Файл каталога' для реализации
     связи многие-ко-многим
     """
    def __init__(self, katalog_id, file_id):
        self.katalog_id = katalog_id
        self.file_id = file_id


# Каталоги
katalogs = [
    Katalog(1, 'Учеба'),
    Katalog(2, 'Работа'),
    Katalog(3, 'Хобби'),
]
# Файлы
files = [
    File(1, 'Программирование', 2500, 1),
    File(2, 'Задача_от_того-то', 3500, 2),
    File(3, 'Машина', 4500, 3),
    File(4, 'Документы', 3500, 2),
    File(5, 'Для_этого-то', 2500, 1),
]
files_katalogs = [
    FilesKatalogs(1, 1),
    FilesKatalogs(1, 2),
    FilesKatalogs(1, 5),
    FilesKatalogs(2, 2),
    FilesKatalogs(2, 4),
    FilesKatalogs(2, 5),
    FilesKatalogs(3, 1),
    FilesKatalogs(3, 3),
    FilesKatalogs(3, 5),
]


def main():
    """Основная функция"""
    # Соединение данных один-ко-многим
    one_to_many = [(e.name, e.f_size, d.name)
                   for d in katalogs
                   for e in files
                   if e.katalog_id == d.id]

    # Соединение данных многие-ко-многим
    many_to_many_temp = [(d.name, ed.katalog_id, ed.file_id)
                         for d in katalogs
                         for ed in files_katalogs
                         if d.id == ed.katalog_id]

    many_to_many = [(e.name, e.f_size, d_name)
                    for d_name, d_id, emp_id in many_to_many_temp
                    for e in files if e.id == emp_id]
                    
    print('Задание Б1')
    res_11 = sorted(one_to_many, key=itemgetter(0))
    print(res_11)
    print('\n Задание Б2 ')
    res_12_unsorted = []
    for d in katalogs:
        # Список
        d_files = list(filter(lambda i: i[2] == d.name, one_to_many))
        # Если не пустой
        if len(d_files) > 0:
            res_12_unsorted.append((d.name, len(d_files)))

    res_12 = sorted(res_12_unsorted, key=itemgetter(1), reverse=True)
    print(res_12)

    print('\n Задание Б3')
    res_13 = {}
    # Перебираем все каталоги
    for d in files:
        if d.name[-1] == 'о':
            d_es = list(filter(lambda i: i[0] == d.name, many_to_many))
            # print(d_es) 
            d_es_names = [x for _, _, x in d_es]      
            res_13[d.name] = d_es_names

    print(res_13)


if __name__ == '__main__':
    main()
