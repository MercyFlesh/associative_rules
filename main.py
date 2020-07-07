import argparse
import json
import csv
import os
from assotiative_rules.apriori import apriori
from assotiative_rules.rules import get_associative_rules


def write_to_json(rules, path):
    name_path = os.path.splitext(path)[0]
    with open(f'{name_path}_rules.json', 'w') as file:
        to_json = {str(k): v for k, v in rules.items()}
        json.dump(to_json, file, indent=5)


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


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-P', '--path', help="path to database", type=str, required=True)
    parser.add_argument('-S', '--sup', help="minimum support", type=float, required=True)
    parser.add_argument('--conf', help="minimum confidience", type=float, required=False)
    parser.add_argument('--lift', help="minimum lift", type=float, required=False)
    parser.add_argument('--levar', help="minimum levarage", type=float, required=False)
    parser.add_argument('--conv', help="minimum conviction", type=float, required=False)
    parser.add_argument('-J', '--json', help="write rules to json file", action='store_const', const=True, required=False)
    args = parser.parse_args()

    try:
        support_items = apriori(args.path, args.sup)
        rules = get_associative_rules(support_items, 
                                    min_conf=args.conf, min_lift=args.lift, 
                                    min_levar=args.levar, min_conv=args.conv)
                                    
        if args.json:
            write_to_json(rules, args.path)
        else:
            write_to_csv(rules, args.path)

    except Exception as ex:
        print(ex.args[0])


if __name__ == "__main__":
    main()
