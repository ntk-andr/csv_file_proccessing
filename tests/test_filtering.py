import pytest
from src.utils import filtering

tested_table = [['name', 'brand', 'price', 'rating'], ['iphone 15 pro', 'apple', '999', '4.9'],
                ['galaxy s23 ultra', 'samsung', '1199', '4.8'], ['redmi note 12', 'xiaomi', '199', '4.6'],
                ['poco x5 pro', 'xiaomi', '299', '4.4']]
columns = tested_table.pop(0)


def test_filtering_gr():
    result = filtering(table=tested_table, columns=columns, field='rating', operator='>', value=4.6)
    ex = [['iphone 15 pro', 'apple', '999', '4.9'], ['galaxy s23 ultra', 'samsung', '1199', '4.8']]
    assert result == ex


def test_filtering_lr():
    result = filtering(table=tested_table, columns=columns, field='rating', operator='<', value=4.8)
    ex = [['redmi note 12', 'xiaomi', '199', '4.6'], ['poco x5 pro', 'xiaomi', '299', '4.4']]
    assert result == ex


def test_filtering_eq():
    result = filtering(table=tested_table, columns=columns, field='rating', operator='=', value=4.6)
    ex = [['redmi note 12', 'xiaomi', '199', '4.6']]
    assert result == ex


def test_filtering_brand_eq():
    result = filtering(table=tested_table, columns=columns, field='brand', operator='=', value='xiaomi')
    ex = [['redmi note 12', 'xiaomi', '199', '4.6'], ['poco x5 pro', 'xiaomi', '299', '4.4']]
    assert result == ex
