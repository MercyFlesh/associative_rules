
def _confidience(rules, sup_items_dict, min_conf=None):
    if min_conf < 0 or min_conf > 1:
        raise ValueError('Mininmum confidience must be a positive number within the interval [0, 1]. '
                        f'You enter {min_conf}.')


def _lift(rules, sup_items_dict, min_lift=None):
    if min_lift < 0:
        raise ValueError('Mininmum lift must be a positive number within the interval [0, inf). '
                        f'You enter {min_lift}.')


def _levarage(rules, sup_items_dict, min_levar=None):
    if min_levar < -1 or min_levar > 1:
        raise ValueError('Mininmum levarage must be a number within the interval [-1, 1]. '
                        f'You enter {min_levar}.')


def _conviction(rules, sup_items_dict, min_conv=None):
    if min_conv < 0:
        raise ValueError('Mininmum conviction must be a positive number within the interval [0, inf). '
                         f'You enter {min_conv}.')


def get_associative_rules(sup_items_dict, conf=None, lift=None, levar=None, conv=None):
    
    if any([conf, lift, levar, conv]):
        temp_rules = {k: [v] for k, v in sup_items_dict.items() if len(k) > 1}
        
        _confidience(temp_rules, sup_items_dict, conf)
        _lift(temp_rules, sup_items_dict, lift)
        _levarage(temp_rules, sup_items_dict, levar)
        _conviction(temp_rules, sup_items_dict, conv)              
    else:
        return sup_items_dict
    
    rules = {}

    return rules
