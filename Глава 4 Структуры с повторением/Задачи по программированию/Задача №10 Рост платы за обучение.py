def Rising_tuition_fees(START, RAISE, years):
    print('Семестр\tПлата')
    print('-------------------')
    for year in range(years):
        print(f' {year + 1} \t\t    {START + (START * RAISE) * year:,.2f}')


Rising_tuition_fees(45000, 0.03, 6)
