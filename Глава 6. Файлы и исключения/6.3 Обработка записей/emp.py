def save_emp_records():
    with open('employees.txt', 'w') as emp_file:
        for count in range(int(input('C�o���o ������� � ����������� �� ������ �������?: '))):
            print(f'������� ������ � ���������� �{count + 1}')
            print(input('���: '), file=emp_file)
            print(input('����������������� �����: '), file=emp_file)
            print(input('�����: '), file=emp_file)

    print('������ �  ����������� ��������� � ernployees.txt.')

def read_emp_records():
    with open('employees.txt') as emp_file:
        while True:
            name = emp_file.readline().rstrip()
            if not name: break
            else:
                id_num = emp_file.readline().rstrip()
                dept = emp_file.readline().rstrip()

                print(f'���: {name}')
                print(f'��: {id_num}')
                print(f'�����: {dept}')
                print()