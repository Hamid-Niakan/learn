from functools import reduce
import os


def csv_reader(path):
    with open(path) as csv:
        for row in csv.readlines():
            yield row.rstrip().split(',')


def process(path):
    cwd = os.getcwd()
    with open(f'{cwd}/ans.csv', 'w') as ans:
        for row in csv_reader(path):
            row.append(str(reduce((lambda x, y: int(x) + int(y)), row)))
            ans.write(','.join(row) + '\n')


process('python/quera_college/test.csv')
