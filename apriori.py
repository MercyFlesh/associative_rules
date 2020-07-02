import csv
import collections
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
    
    for row in iterable:
        n += 1
        for x in row:
            temp_dict[x] = temp_dict.get(x, 0) + 1
            
    for key, val in temp_dict.items():
        support = val/n
        if support >= min_sup:
            support_set.add((key, support)) 

    return n, support_set


def apriori(db_path, min_sup=0.5):
    if min_sup <= 0 or min_sup > 1:
        raise ValueError(f'minimum support must be a positive number within the interval (0, 1]. '
                         'Got {min_sup}.')
    
    n, support_set = _support(_csv_read(db_path), min_sup)

    items = {}
    #need to implement the receipt of pairs of N elements...

    return items


def get_associative_rules(db_path, items, min_confid=0.6):
    if min_confid <= 0 or min_confid > 1:
        raise ValueError(f'mininmum confidience must be a positive number within the interval (0, 1]. '
                         'Got {min_confid}.')

    rules = {}
    return rules
