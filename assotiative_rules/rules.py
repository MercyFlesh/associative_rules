import itertools as it


def _get_keys_combinations(item):
    return map(tuple, [x for x in it.chain(*[it.combinations(item, i+1) for i in range(len(item)-1)])])


def _confidience(rules, sup_items_dict, min_conf=None):
    if min_conf and (min_conf < 0 or min_conf > 1):
        raise ValueError('Mininmum confidience must be a positive number within the interval [0, 1]. '
                        f'You enter {min_conf}.')

    """
    FORMAT DATA

    sup_items_dict
    {
        (item,): support,
        (item): support,
        ...
    }

    rules
    {
        ((fist_items), (second_items)): [fist_support, second_support, support, confidience, lift, levarage, conviction],
        ...
    }
    """

    """
    #Need to get rid of duplication code... but i stupid and don't know how implement in here...
    
    def get_conf():
        for k, v in sup_items_dict.items():
            if len(k) > 1:
                probable_rules = list(_get_keys_combinations(k))
                length = len(probable_rules)
                for i in len(length):
                    item = (probable_rules[i], probable_rules[length-1-i])    
                    item_support_first = sup_items_dict[item[0]] 
                    conf = v/item_support_first

                    yield [item_support_first, ]       
    """
    
    for k, v in sup_items_dict.items():
        if len(k) > 1:
            probable_rules = list(_get_keys_combinations(k))
            length = len(probable_rules)
            for i in range(length):
                item = (probable_rules[i], probable_rules[length-1-i])    
                item_support_first = sup_items_dict[item[0]] 
                
                conf = float(v/item_support_first)
                if min_conf:
                    if conf >= min_conf:
                        rules[item] = [
                            item_support_first, sup_items_dict[item[1]], v, conf
                        ]
                else:
                    rules[item] = [
                        item_support_first, sup_items_dict[item[1]], v, conf
                    ]
    

def _lift(rules, sup_items_dict, min_lift=None):
    if min_lift and min_lift < 0:
        raise ValueError('Mininmum lift must be a positive number within the interval [0, inf). '
                        f'You enter {min_lift}.')


def _levarage(rules, sup_items_dict, min_levar=None):
    if min_levar and (min_levar < -1 or min_levar > 1):
        raise ValueError('Mininmum levarage must be a number within the interval [-1, 1]. '
                        f'You enter {min_levar}.')


def _conviction(rules, sup_items_dict, min_conv=None):
    if min_conv and min_conv < 0:
        raise ValueError('Mininmum conviction must be a positive number within the interval [0, inf). '
                         f'You enter {min_conv}.')


def get_associative_rules(sup_items_dict, conf=None, lift=None, levar=None, conv=None):
    
    if any([conf, lift, levar, conv]):
        #temp_rules = {k: [v] for k, v in sup_items_dict.items() if len(k) > 1}
        rules = dict()
        _confidience(rules, sup_items_dict, conf)
        _lift(rules, sup_items_dict, lift)
        _levarage(rules, sup_items_dict, levar)
        _conviction(rules, sup_items_dict, conv)
        return rules           
     
    return sup_items_dict
