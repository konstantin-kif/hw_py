from User_interface import get_info as gi

info = gi()
def writing_scv ():
    file = 'Phonebook.csv'
    with open (file, 'a', encoding = 'utf-8') as data:
        data.write(f'{info[0]}, {info[1]}, {info[2]}, {info[3]}, {info[4]}\n')

def writing_txt ():
    file = 'Phonebook.txt'
    with open (file, 'a', encoding = 'utf-8') as data:
        data.write(f'Фамилия: {info[0]}\n\n Имя: {info[1]}\n\n Дата рождения: {info[2]}\n\n Номер телефона: {info[3]}\n\n Место работы: {info[4]}\n\n\n')