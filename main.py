import csv
import argparse
from apriori import apriori, get_associative_rules


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-P', '--path', help="path to database", type=str, required=True)
    parser.add_argument('-S', '--support', type=float, default=0.5, required=False)
    parser.add_argument('-C', '--confidience', type=float, default=0.6, required=False)
    args = parser.parse_args()

    try:
        sets_satisfying_min_sup = apriori(args.path, args.support) 
        rules = get_associative_rules(args.path, sets_satisfying_min_sup, args.confidience)

    except Exception as ex:
        print(ex.args[0])


if __name__ == "__main__":
    main()
