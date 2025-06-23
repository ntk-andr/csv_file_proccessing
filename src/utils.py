import csv
import os

from exceptions import EmptyVariableError


def read_file(filepath: str) -> list:
    if not os.path.exists(filepath):
        raise FileNotFoundError(f'Файл {filepath} не найден')
    with open(file=filepath) as csvfile:
        table: list = [row for row in csv.reader(csvfile)]
    return table


def filtering(table: list, columns: list, field: str, operator: str, value: str | float) -> list:
    if not table:
        raise EmptyVariableError('table')
    field = columns.index(field)

    if operator == '>':
        return [item for item in table if float(item[field]) > float(value)]
    elif operator == '=':
        return [item for item in table if item[field] == str(value)]
    elif operator == '<':
        return [item for item in table if float(item[field]) < float(value)]
    else:
        raise ValueError(f'Введен не корректный оператор {operator}')


def aggregate(table: list, columns: list, field: str, operation: str) -> list:
    if not table:
        raise EmptyVariableError('table')
    if not columns:
        raise EmptyVariableError('columns')

    index = columns.index(field)
    items = [float(item[index]) for item in table]

    table = [[operation]]

    if operation == 'avg':
        table.append([sum(items) / len(items)])
    elif operation == 'min':
        table.append([min(items)])
    elif operation == 'max':
        table.append([max(items)])
    else:
        raise ValueError(f'Введен не корректный оператор {operation}')

    return table
