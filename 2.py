'''Березовська А.О
Визначити середній бал оцінок з усіх предметів, і вивести відомості про
студентів, середній бал яких складає більше 75б. Поля структури: Прізвище, Група,
Фізика, Алгоритмізація та програмування, Вища математика.'''

surname = ['Alby', 'Becker', 'Chester', 'Graham', 'Hale', 'Kirby', 'Lincoln', 'Mitchell', 'Norton', 'Perry']
p = [86, 79, 91, 60, 89, 100, 73, 87, 92, 84]
m = [100, 75, 87, 70, 90, 100, 91, 98, 70, 85]
r = [87, 68, 91, 64, 67, 97, 74, 78, 90, 84]

group = {a: b for (a,b) in zip(surname, ['A', 'B', 'C', 'A', 'A', 'B', 'C', 'F', 'C', 'A'])}
physics = {a: b for (a,b) in zip(surname, p)}
math = {a: b for (a,b) in zip(surname, m)}
programming = {a: b for (a,b) in zip(surname, r)}

for i in range(len(surname)):
    if ((p[i] + m[i] + r[i])/3) > 75:
        print(f'{surname[i]} - group {group[surname[i]]}: Physics {physics[surname[i]]}, Math {math[surname[i]]}, Programming {programming[surname[i]]}')

