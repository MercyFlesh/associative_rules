import csv
import argparse
import apriori
from itertools import groupby


def csv_read(path, sort_col='year'):
    try:
        with open(path, 'r') as file:
            reader = csv.DictReader(file, delimiter=',')
            
            # i'm stupid and i dont know how to make grouping otherwise so that it looks normal
            sort_date = sorted(reader, key=lambda row: row[sort_col], reverse=False) 
            for row in sort_date:
                yield row
    
    except FileNotFoundError as ex:
        raise FileNotFoundError(ex)
    except csv.Error as ex:
        raise ValueError(ex)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-P', '--path', help="path to database", type=str, required=True)
    parser.add_argument('-S', '--support', type=float, required=False)
    parser.add_argument('-C', '--confidience', type=float, required=False)
    args = parser.parse_args()
    
    try:
        csv_reader_gen = csv_read(args.path)
        for row in csv_reader_gen:
            pass

    except Exception as ex:
        print(ex.args[0])


if __name__ == "__main__":
    main()
