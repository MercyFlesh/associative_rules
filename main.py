import argparse
import json
import csv
import os
import time
from associative_rules.apriori import apriori
from associative_rules.rules import get_associative_rules


def write_to_json(rules, path):
    name_path = os.path.splitext(path)[0]
    with open(f'{name_path}_rules.json', 'w') as file:
        to_json = {str(k): v for k, v in rules.items()}
        json.dump(to_json, file, indent=5)

    print(f'[\033[32m+\033[0m] Rules are written in {name_path}_rules.json')


def write_to_csv(rules, path):
    name_path = os.path.splitext(path)[0]
    data_list = [
        [
            'fist_items', 'second_items', 'fist_support', 
            'second_support', 'item_support', 'confidience', 
            'lift', 'levarage', 'conviction',
        ]
    ]
    
    for k, v in rules.items():
        temp_list = list()
        for item in k:
            temp_list.append(str(item))
        temp_list.extend(v)
        data_list.append(temp_list)    
    
    with open(f'{name_path}_rules.csv', 'w', newline='') as file:
        writer = csv.writer(file, delimiter=',')
        writer.writerows(data_list)

    print(f'[\033[32m+\033[0m] Rules are written in {name_path}_rules.csv')


def main():
    parser = argparse.ArgumentParser()
    mendatory_group = parser.add_argument_group('Mendatory')
    rule_coeffs = parser.add_argument_group('Rule sorting coefficients')
    output_flags = parser.add_argument_group('Output flags')

    mendatory_group.add_argument('-P', '--path', help="path to database", type=str, required=True)
    mendatory_group.add_argument('-S', '--sup', help="minimum support", type=float, required=True)
    rule_coeffs.add_argument('--conf', help="minimum confidience", type=float, required=False)
    rule_coeffs.add_argument('--lift', help="minimum lift", type=float, required=False)
    rule_coeffs.add_argument('--levar', help="minimum levarage", type=float, required=False)
    rule_coeffs.add_argument('--conv', help="minimum conviction", type=float, required=False)
    output_flags.add_argument('-J', '--json', help="write rules to json file", action='store_const', const=True, required=False)
    args = parser.parse_args()
    
    try:
        print('[\033[32m+\033[0m] Finding items suitables of min support is started...')
        start_time = time.perf_counter()
        support_items = apriori(args.path, args.sup)
        
        print('[\033[32m+\033[0m] All items matching minimal support found')
        print('[\033[32m+\033[0m] Finding rules in items')

        rules = get_associative_rules(support_items, 
                                    min_conf=args.conf, min_lift=args.lift, 
                                    min_levar=args.levar, min_conv=args.conv)

        if args.json:
            write_to_json(rules, args.path)
        else:
            write_to_csv(rules, args.path)

        print(f'[\033[32m*\033[0m] Runtime: {round(time.perf_counter() - start_time, 4)} sec.')

    except Exception as ex:
        print(f'[\033[31m-\033[0m] Error: {ex.args[0]}')

    
if __name__ == "__main__":
    main()
