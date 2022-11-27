import numpy as np
number = np.random.randint(1, 101) # загадываем число
count = 0
 
while True:
    count += 1
    predict_number = int(input('Угадай число от 1 до 100: '))
    
    if predict_number > number:
        print(f'Попытка: {count}, Ваш ответ: {predict_number}')
        print('Ответ неверный. Загаданное число меньше')
        
    elif predict_number < number:
        print(f'Попытка: {count}, Ваш ответ: {predict_number}')
        print('Ответ неверный. Загаданное число больше')
    
    else:
        print(f'Вы угадали! Это число = {number}, за {count} попыток')
        break # конец игры, выход из цикла
