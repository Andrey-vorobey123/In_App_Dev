goods = [
    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
    {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'},
    {'title': 'Диван НЕ для отдыха', 'price': 500, 'color': 'white'},
    {'title': 'Шкаф', 'price': 10000}
]


def field(items, *args):
    assert len(args) > 0
    if len(args) == 1:
        for elem in items:
            if args[0] in elem and elem[args[0]] is not None:
                yield elem[args[0]]
    else:
        for elem in items:
            result = {}
            for key in args:
                if key in elem and elem[key] is not None:
                    result[key] = elem[key]
            yield result


test = field(goods, 'title', 'price')
while True:
    try:
        i = test.__next__()
        print(i)
    except StopIteration:
        break
