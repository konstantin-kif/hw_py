import display 
import fileio

def menu(data):
    while True:
        answer = display.display_menu()
        if answer == 0:
            display.display_data(data)
        elif answer == 1:
            str_data = input("Please enter your data delimited by ; : ")
            row = str_data.split(";")
            data.append([row[0], row[1], row[2]])
        elif answer == 2:
            str_to_del = input("Please enter ID: ")
            for i in range(len(data)):
                if data[i][0] == str_to_del:
                    del (data[i])
        elif answer == 3:
            fileio.write_data("data.csv", data)
        elif answer == 4:
            print('goodbay')
            break
        else:
            print("Повторите выбор")