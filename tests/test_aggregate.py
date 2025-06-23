import pytest
from src.utils import aggregate


tested_table = [['name', 'brand', 'price', 'rating'], ['iphone 15 pro', 'apple', '999', '4.9'],
                ['galaxy s23 ultra', 'samsung', '1199', '4.8'], ['redmi note 12', 'xiaomi', '199', '4.6'],
                ['poco x5 pro', 'xiaomi', '299', '4.4']]
columns = tested_table.pop(0)


def test_aggregate_avg():
    result = aggregate(table=tested_table, columns=columns, field='rating', operation='avg')
    ex = [['avg'], [4.675]]
    assert result == ex


def test_aggregate_min():
    result = aggregate(table=tested_table, columns=columns, field='rating', operation='min')
    ex = [['min'], [4.4]]
    assert result == ex


def test_aggregate_max():
    result = aggregate(table=tested_table, columns=columns, field='rating', operation='max')
    ex = [['max'], [4.9]]
    assert result == ex
