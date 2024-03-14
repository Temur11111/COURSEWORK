import pytest
import json
import datetime
from src.utills import add_initial_data, delete_none, executed_operations_only, crypto, secret_card, slice_operations, sort_operations, date_format
import json
def test_add_initial_data():
    data = add_initial_data()
    assert isinstance(data, list)



def test_delete_none_return_type():
    result = delete_none()
    assert isinstance(result, list)

def test_delete_none_content():
    result = delete_none()
    initial_data = add_initial_data()
    for item in result:
        assert item in initial_data
        assert "id" in item

#####Эти тесты проверяют тип возвращаемого значения функции и убеждаются, что возвращенный список содержит только операции с состоянием "EXECUTED"
def test_executed_operations_only_return_type():
    result = executed_operations_only()
    assert isinstance(result, list)

def test_executed_operations_only_content():
    result = executed_operations_only()
    for item in result:
        assert item["state"] == "EXECUTED"


def test_secret_card_type():
    ###проверяет, что результат, возвращаемый функцией, является списком
    result = secret_card()
    assert isinstance(result, list)





def test_sort_operations_returns_list():
    assert isinstance(sort_operations(), list)

def test_sort_operations_sorted_by_date():
    result = sort_operations()
    dates = [operation["date"] for operation in result]
    assert dates == sorted(dates, reverse=True)



def test_date_format_returns_list():
    assert isinstance(date_format(), list)

def test_date_format_date_formatting():
    result = date_format()
    for operation in result:
        assert len(operation["date"]) == 10
        date_parts = operation["date"].split(".")
        assert len(date_parts) == 3
        day, month, year = map(int, date_parts)
        assert datetime.datetime(year, month, day) is not None
