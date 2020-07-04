import csv
import itertools


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


def _lift():
    pass


def _confidience():
    pass


def _support(iterable, min_sup, set_items=set()):
    support_set = set()
    temp_dict = dict()
    n = 0

    for row in iterable:
        n += 1
        if set_items:
           for item in set_items:
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


def _levarage():
    pass


def _conviction():
    pass


def get_L_items(sets_items, size):
    temp_L_items = set()
    length = len(sets_items)

    for x, i in zip(sets_items[:length-1], range(length-1)):
        for y in sets_items[i:length]:
            if len(set(x).union(y)) == size:
                temp_L_items.add(tuple(set(x).union(y)))
    return temp_L_items


def apriori(db_path, min_sup=0.5):
    if min_sup <= 0 or min_sup > 1:
        raise ValueError(f'Minimum support must be a positive number within the interval (0, 1]. '
                         'U enter: {min_sup}.')

    sup_items = dict(_support(_csv_read(db_path), min_sup))
    
    n = 2
    L_items = sup_items.copy()
    while(L_items != set()):
        sup_items.update(L_items)
        L_items = get_L_items(list(L_items.keys()), n)
        if not L_items:
            break
        L_items = dict(_support(_csv_read(db_path), min_sup, L_items))
        n += 1
    
    return sup_items


def get_associative_rules(db_path, items, min_confid=0.6):
    if min_confid <= 0 or min_confid > 1:
        raise ValueError(f'mininmum confidience must be a positive number within the interval (0, 1]. '
                         'Got {min_confid}.')

    rules = {}
    return rules
