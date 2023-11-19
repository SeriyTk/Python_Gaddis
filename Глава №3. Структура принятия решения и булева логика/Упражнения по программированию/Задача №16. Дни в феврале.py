def Days_February():
    year = int(input("Введите год: "))

    if year % 100 == 0:
        if year % 400 == 0:  print(f"В феврале {year} года 29 дней.")
        else:  print(f"В феврале {year} года 28 дней.")
    else:
        if year % 4 == 0:  print(f"В феврале {year} года 29 дней.")
        else:  print(f"В феврале {year} года 28 дней.")


if __name__ == '__main__': Days_February = Days_February()
