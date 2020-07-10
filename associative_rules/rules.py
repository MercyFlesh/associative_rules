"""
Module for finding associative rules

"""

import itertools as it


def _get_keys_combinations(sequence):
    """Get pairs of item

    Сreates unique combinations for rules 
    from the passed sequence

    Args:
        sequence (tuple): sequence to get pairs of combinations 

    Returns:
        (map object): object from sequence of combinations
    """
    
    return map(sorted, (set(x) for x in it.chain(*[it.combinations(sequence, i+1) for i in range(len(sequence)-1)])))


def _confidience(rules, sup_items_dict, min_conf=None):
    """Calculate confidience
    and selection of rules by confidience

    Args:
        rules (dict): dict for write rules
        sup_items_dict (dict): dict with support of items in wich keys are sequences, values - support
        min_conf (float, optional): given minimum confidience for selection rules. Defaults to None.
    """

    if min_conf and (min_conf < 0 or min_conf > 1):
        raise ValueError('Mininmum confidience must be a positive number within the interval [0, 1]. '
                        f'You enter {min_conf}.')

    for k, v in sup_items_dict.items():
        if len(k) > 1:
            # for rules need sequences of len > 1
            probable_rules = list(_get_keys_combinations(k))
            length = len(probable_rules)
            for i in range(length):
                item = (tuple(probable_rules[i]), tuple(probable_rules[length-1-i]))    # make a rule from combinations 
                item_support_first = sup_items_dict[item[0]]                             
                                                                                        
                conf = round(v/item_support_first, 4)                                   # confidience(a->b) = support(a->b)/support(a)
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
    """Calculate lift
    and selection of rules by lift

    Args:
        rules (dict): dict for write rules
        min_lift (float, optional): given minimum lift. Defaults to None.
    """

    if min_lift and min_lift < 0:
        raise ValueError('Mininmum lift must be a positive number within the interval [0, inf). '
                        f'You enter {min_lift}.')

    for item, coef in rules.items():
        lift = round(coef[3]/coef[1], 4)    # lift(a->b) = conf(a->b)/support(b)
        if min_lift:
            if lift >= min_lift:
                coef.append(lift)
        else:
            coef.append(lift)


def _levarage(rules, min_levar=None):
    """Calculate levarage
    and selection of rules by levarage

    Args:
        rules (dict): dict for write rules
        min_lift (float, optional): given minimum levarage. Defaults to None.
    """

    if min_levar and (min_levar < -1 or min_levar > 1):
        raise ValueError('Mininmum levarage must be a number within the interval [-1, 1]. '
                        f'You enter {min_levar}.')

    for item, coef in rules.items():
        levar = round(coef[2] - coef[0]*coef[1], 4)    # support(a->b) - support(a)*support(b)
        if min_levar:
            if levar >= min_levar:
                coef.append(levar)
        else:
            coef.append(levar)


def _conviction(rules, min_conv=None):
    """Calculate conviction
    and selection of rules by conviction

    Args:
        rules (dict): dict for write rules
        min_lift (float, optional): given minimum conviction. Defaults to None.
    """

    if min_conv and min_conv < 0:
        raise ValueError('Mininmum conviction must be a positive number within the interval [0, inf). '
                         f'You enter {min_conv}.')

    for item, coef in rules.items():
        denom = 1 - coef[3]
        if (denom > 0):
            conv = round((1 - coef[1])/denom, 4)    # conv(a->b) = (1 - support(b))/(1 - conf(a->c))
        else:
            conv = 'inf'

        if min_conv:
            if type(conv) == str or conv >= min_conv:
                coef.append(conv)
        else:
            coef.append(conv)


def get_associative_rules(sup_items_dict, min_conf=None, min_lift=None, min_levar=None, min_conv=None):
    """Organization of calculation of rule coefficients

    Args:
        sup_items_dict (dict): dict of sequence with support {(item,): support, ...}
        min_conf (float, optional): . Defaults to None.
        min_lift (float, optional): . Defaults to None.
        min_levar (float, optional): . Defaults to None.
        min_conv (float, optional): . Defaults to None.

    Returns:
        (dict): rules - { ((first_items), (second_items)): [first_support, second_support, 
                                                            item_support, confidience, lift, 
                                                            levarage, conviction], ...}
    """

    rules = dict()
    _confidience(rules, sup_items_dict, min_conf)
    _lift(rules, min_lift)
    _levarage(rules, min_levar)
    _conviction(rules, min_conv)

    return rules 
