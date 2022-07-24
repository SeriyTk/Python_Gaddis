import sets

def main():
    baseball = set(['Джоди', 'Кармен', 'Аида', 'Алиция'])
    basketball = set(['Эва', 'Кармен', 'Алиция', 'Сара'])
    sets.get_name_baseball(baseball)
    print()
    print()
    sets.get_name_basketball(basketball)
    print()
    print()
    sets.get_intеrsесtiоn_names(baseball, basketball)
    print()
    print()
    sets.get_union_names(baseball, basketball)
    print()
    print()
    sets.get_difference_baseball(baseball, basketball)
    print()
    print()
    sets.get_difference_basketball(baseball, basketball)
    print()
    print()
    sets.get_symmetric_names(baseball, basketball)


main()
