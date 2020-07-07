import itertools as it

def _get_keys_combinations(item):
    return map(sorted, (set(x) for x in it.chain(*[it.combinations(item, i+1) for i in range(len(item)-1)])))


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
        ((fist_items), (second_items)): [fist_support, second_support, item_support, confidience, lift, levarage, conviction],
        ...
    }
    """

    for k, v in sup_items_dict.items():
        if len(k) > 1:
            probable_rules = list(_get_keys_combinations(k))
            length = len(probable_rules)
            for i in range(length):
                item = (tuple(probable_rules[i]), tuple(probable_rules[length-1-i]))    
                item_support_first = sup_items_dict[item[0]] 
                
                conf = round(v/item_support_first, 4)
                if min_conf:
                    if conf >= min_conf:
                        rules[item] = [
                            item_support_first, sup_items_dict[item[1]], v, conf
                        ]
                else:
                    rules[item] = [
                        item_support_first, sup_items_dict[item[1]], v, conf
                    ]
    

def _lift(rules, min_lift=None):
    if min_lift and min_lift < 0:
        raise ValueError('Mininmum lift must be a positive number within the interval [0, inf). '
                        f'You enter {min_lift}.')

    for item, coef in rules.items():
        lift = round(coef[3]/coef[1], 4)
        if min_lift:
            if lift >= min_lift:
                coef.append(lift)
        else:
            coef.append(lift)


def _levarage(rules, sup_items_dict, min_levar=None):
    if min_levar and (min_levar < -1 or min_levar > 1):
        raise ValueError('Mininmum levarage must be a number within the interval [-1, 1]. '
                        f'You enter {min_levar}.')

    for item, coef in rules.items():
        levar = round(coef[2] - coef[0]*coef[1], 4)
        if min_levar:
            if levar >= min_levar:
                coef.append(levar)
        else:
            coef.append(levar)

def _conviction(rules, sup_items_dict, min_conv=None):
    if min_conv and min_conv < 0:
        raise ValueError('Mininmum conviction must be a positive number within the interval [0, inf). '
                         f'You enter {min_conv}.')

    for item, coef in rules.items():
        denom = 1 - coef[3]
        if (denom > 0):
            conv = round((1 - coef[1])/denom, 4)
        else:
            conv = 'inf'

        if min_conv:
            if type(conv) == str or conv >= min_conv:
                coef.append(conv)
        else:
            coef.append(conv)


def get_associative_rules(sup_items_dict, min_conf=None, min_lift=None, min_levar=None, min_conv=None):
    
    if any([min_conf, min_lift, min_levar, min_conv]):
        #temp_rules = {k: [v] for k, v in sup_items_dict.items() if len(k) > 1}
        rules = dict()
        _confidience(rules, sup_items_dict, min_conf)
        _lift(rules, min_lift)
        _levarage(rules, sup_items_dict, min_levar)
        _conviction(rules, sup_items_dict, min_conv)
        return rules           
     
    return sup_items_dict
