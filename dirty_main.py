from application.salary import *
from application.db.people import *


if __name__ == '__main__':
    print(get_employees('Дмитрий'))
    print(calculate_salary(3000, 50000, 500))