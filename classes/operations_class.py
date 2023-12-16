from datetime import datetime


class Operation:
    def __init__(self, pk, state, date, operation_amount, description, whence, to):
        self.pk = pk
        self.state = state
        self.date = self.convert_date(date)
        self.operation_amount = operation_amount
        self.description = description
        if whence:
            self.whence = self.convert_private_number(whence)
        else:
            self.whence = ''
        self.to = self.convert_private_number(to)

    def convert_date(self, date):
        """Конвертация даты"""
        return datetime.fromisoformat(date)

    def convert_private_number(self, private_number):
        """
        Функция маскирует номер счета или карты
        :param private_number: номер счета или карты
        :return: замаскированный номер счета или карты
        """
        if private_number.startswith('Счет'):
            private_number = private_number[:5] + '**' + private_number[-4:]
        else:
            private_num = private_number.split()[-1][:6] + (len(private_number.split()[-1][6:-4]) * '*') + \
                          private_number.split()[-1][-4:]
            chunks = len(private_number.split()[-1])
            chunk_size = len(private_number.split()[-1]) // 4
            private_number = private_number[:-16] + " ".join(
                [private_num[i:i + chunk_size] for i in range(0, chunks, chunk_size)])
        return private_number

    def __str__(self):
        return (
            f'{datetime.strftime(self.date, "%d.%m.%Y")} Перевод организации \n'
            f'{self.whence} -> {self.to} \n'
            f'{self.operation_amount["amount"]} {self.operation_amount["currency"]["name"]}'
        )
