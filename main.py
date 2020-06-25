#!/usr/bin/env python3
import csv
import argparse
import apriori


def csv_read(path):
    try:
        with open(path, 'r') as file:
            reader = csv.DictReader(file, delimiter=',')
            for row in reader:
                yield row

    except FileNotFoundError as ex:
        raise FileNotFoundError(ex)
    except csv.Error as ex:
        raise ValueError(ex)


def main():
    try:
        path = 'assseqRules.csv'
        csv_row_gen = csv_read(path)
    
    except Exception as ex:
        print(ex.args[0])
    

if __name__ == "__main__":
    main()
