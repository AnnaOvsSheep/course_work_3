import json

from classes.operations_class import Operation


def get_list_operations(path):
    """
    Функция вызова списка операций
    :param path: путь к файлу
    :return: список операций
    """
    with open(path, encoding="utf-8") as file:
        return json.load(file)


def get_operations(operations):
    """
    Функция вызова выполненных операций из списка операций
    :param operations: список операций
    :return: экземпляры класса Operation
    """
    all_operations = []
    for operation in operations:
        if operation and operation['state'] == 'EXECUTED':
            operation = Operation(
                pk=operation['id'],
                state=operation['state'],
                date=operation['date'],
                operation_amount=operation['operationAmount'],
                description=operation['description'],
                whence=operation.get('from', ''),
                to=operation['to']
            )
            all_operations.append(operation)
    return all_operations


def get_operation_date(operation):
    """Вызов даты операции"""
    return operation.date


def sort_by_date(operations):
    """Сортировка операций по дате (по убыванию)"""
    return sorted(operations, key=get_operation_date, reverse=True)
