
from logger import changeData, deleteData, inputData, outputData

def interface():
    command = int(input("Добрый день!\n" "Выберите функцию: \n" "1 - запись данных\n" "2 - вывод данных\n" "3 - изменение данных\n" "4 - удаление данных\n" "Введите число: "))
    if command == 1:
      inputData()
    elif command == 2:
      outputData()
    elif command == 3:
      changeData()
    elif command == 4:
      deleteData()
    else:
      print("введена не правильная команда, повторите ввод: ")

