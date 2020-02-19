'''Березовська А.О
Дано символи - s1, s2, .... Відомо, що символ s1 відмінний від пробілу і що серед
s2, s3, ... є хоча б один пробіл. Розглядаються s1, ..., sn - символи, що передують першому
пробілу (n заздалегідь не відомо). З послідовності s1, ..., sn сформувати множину, в якій
видалити всі символи, що не є буквами або цифрами, і замінити кожну велику букву на
однойменну малу'''
while True:
    s = input('Enter the sequence: ').split()
    if len(s) > 1:
        s_set = set(s[0])
        s_new = set()
        for i in s_set:
            if i.isalnum():
                s_new.add(i.lower())
        print(f'The required set is: {s_new}')
    else:
        print('You should enter the sequence with at least one gap!')

        answer = input('Do you want to rerun the program? Yes (1), No (something)')
        if answer == '1':
            continue
        else:
            break
