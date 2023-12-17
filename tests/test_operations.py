def test_convert_date(all_operations):
    assert all_operations[6].convert_date("2019-03-23T01:09:46.296404") == "23.03.2019"


def test_convert_private_number(all_operations):
    assert all_operations[0].convert_private_number("Maestro 1596837868705199") == "Maestro 1596 83** **** 5199"
    assert all_operations[0].convert_private_number("Счет 64686473678894779589") == "Счет **9589"
