from tests.conftest import operations

from utils import get_operations, get_operation_date, sort_by_date


def test_get_operations(operations):
    all_operations = get_operations(operations)
    assert len(all_operations) == 12
    operation1 = all_operations[0]
    assert operation1.pk == 441945886
    assert operation1.state == 'EXECUTED'
    assert operation1.date == '26.08.2019'
    assert operation1.operation_amount == {'amount': '31957.58', 'currency': {'code': 'RUB', 'name': 'руб.'}}
    assert operation1.description == 'Перевод организации'
    assert operation1.whence == 'Maestro 1596 83** **** 5199'
    assert operation1.to == 'Счет **9589'
    operation2 = all_operations[3]
    assert operation2.pk == 587085106
    assert operation2.state == 'EXECUTED'
    assert operation2.date == '23.03.2018'
    assert operation2.operation_amount == {'amount': '48223.05', 'currency': {'code': 'RUB', 'name': 'руб.'}}
    assert operation2.description == 'Открытие вклада'
    assert operation2.whence == ''
    assert operation2.to == 'Счет **2431'



