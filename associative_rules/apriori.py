import csv

def _csv_read(path):
    try:
        with open(path, 'r') as file:
            reader = csv.reader(file, delimiter=',')
            for row in reader:
                yield row

    except FileNotFoundError as ex:
        raise FileNotFoundError(ex)
    except csv.Error as ex:
        raise ValueError(ex)
    except StopIteration as ex:
        raise StopIteration(ex)


def _support(iterable, min_sup, list_items=set()):
    support_set = set()
    temp_dict = dict()
    n = 0

    for row in iterable:
        n += 1
        if list_items:
           for item in list_items:
               if set(item).issubset(row):
                   temp_dict[item] = temp_dict.get(item, 0) + 1
        else:
            for x in row:
                key = (x,)
                temp_dict[key] = temp_dict.get(key, 0) + 1

    for key, val in temp_dict.items():
        support = val/n
        if support >= min_sup:
            support_set.add((key, support))

    return support_set  


def _get_L_items(list_items, size):
    temp_L_items = set()
    length = len(list_items)

    """
    def check_duble(new_item):
        for x in temp_L_items:
            if new_item == set(x):
                return True
        return False
    """
    for x, i in zip(list_items[:length-1], range(length-1)):
        for y in list_items[i+1:length]:
            item = set(x).union(y)
            if len(item) == size: # and not check_duble(item):
                temp_L_items.add(tuple(sorted(item)))

    return temp_L_items


def apriori(db_path, min_sup=0.5):
    if min_sup < 0 or min_sup > 1:
        raise ValueError('Minimum support must be a positive number within the interval [0, 1]. '
                        f'You enter: {min_sup}.')

    sup_items = dict(_support(_csv_read(db_path), min_sup))
    
    n = 2
    L_items = sup_items.copy()
    while(L_items):
        sup_items.update(L_items)
        L_items = _get_L_items(list(L_items.keys()), n)
        if not L_items:
            break
        L_items = dict(_support(_csv_read(db_path), min_sup, L_items))
        n += 1
    
    return sup_items
