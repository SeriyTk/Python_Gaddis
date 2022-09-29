import PersonCustmer as p_c

def main():
    name = input('Имя: ')
    adress = input('Адрес: ')
    phone = input('Телефонный номер: ')
    num = input('Номер клиента: ')
    answer = input('Хотите быть в списке рассылки д/н: ')
    per_cust = p_c.Custmer(name, adress, phone, num, answer)
    print(per_cust)
    if per_cust.get_answer() == 'д': print("Вы в списке")
    elif per_cust.get_answer() == "н": print("Вы не в списке.")

if __name__ == '__main__': main()