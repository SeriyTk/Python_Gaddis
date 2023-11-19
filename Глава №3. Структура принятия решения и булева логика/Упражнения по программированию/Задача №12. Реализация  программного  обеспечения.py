RETAIL = 99
def Software_implementation():
    num_pack_purch = int(input('Количество приобретенных пакетов: '))
    total_sum = num_pack_purch * RETAIL
    if 1 <= num_pack_purch < 10:  print(total_sum)
    elif 10 <= num_pack_purch < 20: discount_amount = RETAIL * 0.10; print(f'{total_sum - discount_amount:,.2f}')
    elif 20 <= num_pack_purch < 50: discount_amount = RETAIL * 0.20; print(f'{total_sum - discount_amount:,.2f}')
    elif 50 <= num_pack_purch < 99: discount_amount = RETAIL * 0.30; print(f'{total_sum - discount_amount:,.2f}')
    elif num_pack_purch >= 100: discount_amount = RETAIL * 0.40; print(f'{total_sum - discount_amount:,.2f}')


if __name__ == '__main__': Software_implementation = Software_implementation()
