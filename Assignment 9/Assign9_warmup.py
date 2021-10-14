def find_threes(start,end):
    z = []
    for i in range(start,end+1):
        if '3' in str(i):
            z += [i]

    return z



def get_salary(emp):
    return emp[1]
    
def top_n(LL,num):
    LL.sort(key=get_salary)
    res1, res2 = map(list, zip(*LL))
    res1.reverse()
    x = res1[0:num]
    return x



def sum_max(numbers):
    total = 0
    for i in numbers:
        x = max(i)
        total += x
    return total
