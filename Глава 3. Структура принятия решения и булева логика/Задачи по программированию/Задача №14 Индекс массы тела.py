def Body_mass_index():
    weight = float(input('Масса тела в кг.: '))
    height = float(input("Рост в метрах: "))
    b_m_i = weight / height
    if 18.5 <= b_m_i <= 25: print("Масса тела оптимальна.")
    elif 18.5 > b_m_i: print('Масса ниже нормы.')
    elif 25 < b_m_i: print('Масса выше нормы.')


Body_mass_index()
