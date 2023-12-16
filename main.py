from setting import OPERATIONS_PATH
from utils import get_list_operations, get_operations, sort_by_date


def main():
    list_operations = get_list_operations(OPERATIONS_PATH)
    all_operations = get_operations(list_operations)
    sort_operations = sort_by_date(all_operations)
    for operation in sort_operations[:5]:
        print(operation)
        print()


if __name__ == '__main__':
    main()