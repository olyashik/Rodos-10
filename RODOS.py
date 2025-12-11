from conditions import *

# Основное тело
if __name__ == "__main__":
    while True:
        # Сначала вводится номер реле, потом команда
        try:
            memory = input().split()
            numb_rel = memory[0]
            command = memory[1]
            c_list = ['s', 'n', 'f']
            n_list = ['0', '1', '2', '3']
            if (numb_rel in n_list) and (command in c_list):
                condition(numb_rel, command)
            else:
                print("Введено неверное значение")

        except Exception as e:
            print("Ошибка")

    
    
