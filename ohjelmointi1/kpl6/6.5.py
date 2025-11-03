list = []
checked_list=[]

def list_filler(n):
    loop = 0

    while loop < n:
        list.append(int(input("Anna luku")))
        loop += 1

    return list

def list_checker(list):
    for i in list:
        if i % 2 == 0:
            checked_list.append(i)

    return checked_list

def main():
    n = int(input("Montako lukua listaan?"))
    list_filler(n)
    list_checker(list)
    return checked_list


main()
print(checked_list)
