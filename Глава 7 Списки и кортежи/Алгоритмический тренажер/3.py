def numbers1_list():
    numbers1 = []
    for i in range(1,101):
        numbers1.append(i)
    return numbers1
numbers2 = []        
def copy_list(par1,par2):
    par2 += par1
    return par2

print(copy_list(numbers1_list(),numbers2))
    