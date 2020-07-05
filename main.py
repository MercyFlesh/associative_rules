import argparse
from assotiative_rules.apriori import apriori
from assotiative_rules.rules import get_associative_rules


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-P', '--path', help="path to database", type=str, required=True)
    parser.add_argument('-S', '--sup', help="minimum support", type=float, required=True)
    parser.add_argument('--conf', help="minimum confidience", type=float, required=False)
    parser.add_argument('--lift', help="minimum lift", type=float, required=False)
    parser.add_argument('--levar', help="minimum levarage", type=float, required=False)
    parser.add_argument('--conv', help="minimum conviction", type=float, required=False)
    args = parser.parse_args()

    try:
        support_items = apriori(args.path, args.sup)
        rules = get_associative_rules(support_items, 
                                    conf=args.conf, lift=args.lift, 
                                    levar=args.levar, conv=args.conv)
        print(rules)

    except Exception as ex:
        print(ex.args[0])


if __name__ == "__main__":
    main()
