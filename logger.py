from dataCreate import nameData, surnameData, phoneData, addressData

def inputData():
  name = nameData()
  surname = surnameData()
  phone = phoneData()
  address = addressData()

  var = int(input(f'В каком формате записать данные\n\n'
  f'1 Вариант: \n'
  f'{name}\n{surname}\n{phone}\n{address}\n\n'
  f'2 Вариант: \n'
  f'{name};{surname};{phone};{address}\n'
  f'Выберите вариант: '))

  while var != 1 and var != 2:
    print('Неправильный ввод')
    var = int(input('Выберите вариант: '))

  if var == 1:
    with open('dataFirstVariant.csv', 'a', encoding='utf-8') as f:
      f.write(f'{name}\n{surname}\n{phone}\n{address}\n\n')
  elif var == 2:
    with open('dataSecondVariant.csv', 'a', encoding='utf-8') as f:
      f.write(f'{name};{surname};{phone};{address}\n\n')



def outputData():
  print('Вывод данных из 1-го файла:\n')
  with open('dataFirstVariant.csv', 'r', encoding='utf-8') as f:
    dataFirst = f.readlines()
    dataFirstList = []
    j = 0
    for i in range(len(dataFirst)):
      if dataFirst[i] == '\n' or i == len(dataFirst) - 1:
        dataFirstList.append(''.join(dataFirst[j:i+1]))
        j = i
    print(*dataFirstList)

  print('Вывод данных из 2-го файла:\n')
  with open('dataSecondVariant.csv', 'r', encoding='utf-8') as f:
    dataSecond = f.readlines()
    print(*dataSecond)


def changeData():
  flag = True
  name = '-1'
  surname = '-1'
  while(flag):
    command = int(input('Выберите параметр по которому будет осуществлен поиск данных: \n 1 - по имени\n 2 - по фамилии\nВведите число: '))
    if command == 1:
      name = nameData()
      flag = False
    elif command == 2:
      surname = surnameData()
      flag = False
    else:
      print("введена не правильная команда, повторите ввод: ")

  print('Введите новые данные: ')
  newName = nameData()
  newSurname = surnameData()
  newPhone = phoneData()
  newAddress = addressData()

  with open('dataFirstVariant.csv', 'r', encoding='utf-8') as f:
    dataFirst = f.readlines()
    dataFirstList = []
    j = 0
    for i in range(len(dataFirst)):
      if dataFirst[i] == '\n' or i == len(dataFirst) - 1:
        dataFirstList.append(''.join(dataFirst[j:i+1]))
        j = i
    indexToChange = -1
    for i in range(0, len(dataFirstList), 2):
      if name in dataFirstList[i] or surname in dataFirstList[i]:
        indexToChange = i

    if indexToChange >= 0:
      dataFirstList[indexToChange] = (f'{newName}\n{newSurname}\n{newPhone}\n{newAddress}\n\n')

    with open('dataFirstVariant.csv', 'w', encoding='utf-8') as f:
      for i in range(len(dataFirstList)):
        f.write(dataFirstList[i])
        

  with open('dataSecondVariant.csv', 'r', encoding='utf-8') as f:
    dataSecondList = f.readlines()

    indexToChange = -1
    for i in range(0, len(dataSecondList), 2):
      if name in dataSecondList[i] or surname in dataSecondList[i]:
        indexToChange = i

    if indexToChange >= 0:
      dataSecondList[indexToChange] = (f'{newName};{newSurname};{newPhone};{newAddress}\n\n')

    with open('dataSecondVariant.csv', 'w', encoding='utf-8') as f:
      for i in range(len(dataSecondList)):
        f.write(dataSecondList[i])


def deleteData():
  flag = True
  name = '-1'
  surname = '-1'
  while(flag):
    command = int(input('Выберите параметр по которому будет осуществлен поиск данных: \n 1 - по имени\n 2 - по фамилии\nВведите число: '))
    if command == 1:
      name = nameData()
      flag = False
    elif command == 2:
      surname = surnameData()
      flag = False
    else:
      print("введена не правильная команда, повторите ввод: ")

  with open('dataFirstVariant.csv', 'r', encoding='utf-8') as f:
    dataFirst = f.readlines()
    dataFirstList = []
    j = 0
    for i in range(len(dataFirst)):
      if dataFirst[i] == '\n' or i == len(dataFirst) - 1:
        dataFirstList.append(''.join(dataFirst[j:i+1]))
        j = i
    indexToDelete = -1
    for i in range(0, len(dataFirstList), 2):
      if name in dataFirstList[i] or surname in dataFirstList[i]:
        indexToDelete = i
    
    if indexToDelete >= 0:
      dataFirstList.pop(indexToDelete)
      
    with open('dataFirstVariant.csv', 'w', encoding='utf-8') as f:
      for i in range(len(dataFirstList)):
        f.write(dataFirstList[i])

  
  with open('dataSecondVariant.csv', 'r', encoding='utf-8') as f:
    dataSecondList = f.readlines()

    indexToDelete = -1
    for i in range(0, len(dataSecondList), 2):
      if name in dataSecondList[i] or surname in dataSecondList[i]:
        indexToDelete = i
        
    if indexToDelete >= 0:
      dataSecondList.pop(indexToDelete)

    with open('dataSecondVariant.csv', 'w', encoding='utf-8') as f:
      for i in range(len(dataSecondList)):
        f.write(dataSecondList[i])