import csv
import itertools


class Transaction:
    def __init__(self, *args):
        pass


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



def _support(iterable, min_sup):
    support_set = set()
    temp_dict = dict()
    n = 0

    count_colls = len(iterable.send(None))
    for row in iterable:
        n += 1
        for x, i in zip(row, range(count_colls)):
            temp_dict[x] = temp_dict.get(x, 0) + 1            
            for j in range(i+2, count_colls+1):
                key = tuple(row[i:j])
                temp_dict[key] = temp_dict.get(key, 0) + 1
    
    for key, val in temp_dict.items():
        support = val/n
        if support >= min_sup:
            support_set.add((key, support)) 

    return support_set

"""
def get_L_items(items_set, size):
    L_items = set()
    length = len(items_set)

    for x, i in zip(items_set[:length-1], range(length-1)):
        for y in items_set[i:length]:
            if len(x.union(y)) == size:
                L_items.add(x.union(y))
    return L_items
"""

def apriori(db_path, min_sup=0.5):
    if min_sup <= 0 or min_sup > 1:
        raise ValueError(f'minimum support must be a positive number within the interval (0, 1]. '
                         'Got {min_sup}.')

    sup_items_set = _support(_csv_read(db_path), min_sup)


    """
    Need to try rewriting the implementation support for original apriori using sets instead tuple, maybe it will be faster,
    need watch time...
    
    But then you will need to store support in some container or just drop it...

    n = 2
    L_items = sup_items_set.copy()
    C_items = set()
    while(L_items != set()):
        C_items.add(L_items)
        L_items = get_L_items(L_items, n)
        L_items = _support(L_items, min_sup)
        n += 1
    """
    


    
    return sup_items_set


def get_associative_rules(db_path, items, min_confid=0.6):
    if min_confid <= 0 or min_confid > 1:
        raise ValueError(f'mininmum confidience must be a positive number within the interval (0, 1]. '
                         'Got {min_confid}.')

    rules = {}
    return rules
