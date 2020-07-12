"""
Module of Apriori algorithm 

Used to search for sequences in the base satisfying, 
given minimum support
"""

import csv


def _csv_read(path):
    """Generator to read csv databse
    
    Args:
        path (str): csv file path

    Yields:
        (list): list from row fields csv file
    """

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
    """Calculation support

    Сalculation of support for sequences and 
    selection suitable for the minimum

    Args:
        iterable (iterable object): iterable object consisting of fields of the source database
        min_sup (float): minimum support
        list_items (set, optional): set of tuples of possible sequences that need 
                                to be checked for presence in the database and 
                                to calculate support. Defaults to set().

    Returns:
        (set): tuples of sequences matching minimal support {((item_1, ...), support), ...}
    """

    support_set = set()    # set of tuples items with support
    temp_dict = dict()     # dict of unique items with count
    transaction_counter = 0 
    
    for row in iterable:
        transaction_counter += 1
        if list_items:
            # counting occurrences possible items in the database 
            for item in list_items:
                if set(item).issubset(row):
                    temp_dict[item] = temp_dict.get(item, 0) + 1
        else:
            # counting occurrences of unique singleton items
            for x in row:
                key = (x,)
                temp_dict[key] = temp_dict.get(key, 0) + 1

    for key, val in temp_dict.items():
        # calculation and checking support
        support = val/transaction_counter
        if support >= min_sup:
            support_set.add((key, support))

    return support_set  


def _get_C_items(list_items, size):
    """
    Сreates possible potentially frequent items  given size from a given list

    Args:
        list_items (list): list current items len(item) = size-1
        size (int): len new items

    Returns:
        (set): new possible items
    """

    C_items = set()    # the set of potentially frequent size-element items.
    length = len(list_items)

    for x, i in zip(list_items[:length-1], range(length-1)):
        for y in list_items[i+1:length]:
            # bonding current sets to create new possible
            item = set(x).union(y) 
            if len(item) == size:
                C_items.add(tuple(sorted(item)))

    return C_items


def apriori(db_path, min_sup):
    """Start Apriori algorithm

    Args:
        db_path (str): path to csv database
        min_sup (float): given minimum support

    Returns:
        (dict): items {(item_1, ...): support, ...}
    """

    if min_sup < 0 or min_sup > 1:
        raise ValueError('Minimum support must be a positive number within the interval [0, 1]. '
                        f'You enter: {min_sup}.')

    # find support for single items
    sup_items = dict(_support(_csv_read(db_path), min_sup))
    
    n = 2                         # counter size for create new L_items
    L_items = sup_items.copy()    # a set of n-element sets whose support is not less than given
    while(L_items):
        sup_items.update(L_items)
        L_items = _get_C_items(list(L_items.keys()), n)
        if not L_items:
            break
        L_items = dict(_support(_csv_read(db_path), min_sup, L_items))
        n += 1
    
    return sup_items
