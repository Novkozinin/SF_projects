import numpy as np


def random_predict(number_: int=np.random.randint(1, 101)) -> int:
    """ Угадываем число при помощи алгоритма бинарого поиска.
        Формула с текстовым ответом для самостоятельного запуска.

    Args:
        number_ (int, optional): Загаданное число. По умолчанию рандомно\
загадывается компьютером в диапазоне 1-100.

    Returns:
        int: Число попыток (шагов)
    """

    # Проверка загаданного числа, в случае пользовательского ввода
    if number_ == int(number_) and 1 < number_ < 100:
        pass
    else:
        return print('Ошибка: загаданное число должно быть целым числом \
от 1 до 100')

    count_ = 0
    lst_num_ = np.array(list(range(1, 101)))
    np_lst_ = np.array(lst_num_)  # конвертируем список в numpy array
    # расчет максимального количествава попыток
    max_rounds_ = int(np.log2(np_lst_[-1])) + 1
    print(f'Алгоритм угадает загаданное число максимум за {max_rounds_} \
попыток\n...')
    comment_ = ''

    while True:
        count_ += 1
        predict_number_ = int(np.mean(np_lst_))
        half_ = round((len(np_lst_))/2)
        if number_ == predict_number_:
            break  # выход из цикла, если угадали
        elif predict_number_ < number_:
            np_lst_ = np_lst_[half_:]
        else:
            np_lst_ = np_lst_[:half_]

    if max_rounds_ == count_:
        comment_ = 'как и планировалось!'
    elif max_rounds_ - count_ == 1:
        comment_ = f'это на {max_rounds_ - count_} ход лучше прогноза!'
    elif max_rounds_ - count_ >= 6:
        comment_ = f'это на {max_rounds_ - count_} ходов лучше прогноза!'
    else:
        comment_ = f'это на {max_rounds_ - count_} хода лучше прогноза!'

    answer_dict_ = {
        1: 'попытку',
        2: 'попытки',
        3: 'попытки',
        4: 'попытки',
        5: 'попыток',
        6: 'попыток',
        7: 'попыток'
        }

    return print(f'Алгоритм угадал загаданное число за {count_} \
{answer_dict_[count_]} - {comment_}')


def random_predict_score(number: int = 1) -> int:
    """ Угадываем число при помощи алгоритма бинарого поиска.
        Формула с выводом количества попыток для вызова в качестве аргумента \
        функции score_game()

    Args:
        number (int, optional): Загаданное число. По умолчанию рандомно \
        загадывается компьютером в диапазоне 1-100.

    Returns:
        int: Число попыток (шагов)
    """

    count = 0
    lst_num = np.array(list(range(1, 101)))
    np_lst = np.array(lst_num)  # конвертируем список в numpy array

    while True:
        count += 1
        predict_number = int(np.mean(np_lst))
        half = round((len(np_lst))/2)
        if number == predict_number:
            break  # выход из цикла, если угадали
        elif predict_number < number:
            np_lst = np_lst[half:]
        else:
            np_lst = np_lst[:half]

    return count


def score_game(random_predict_score) -> int:
    """Среднее количество попыток на угадывание числа из интервала 1-100 \
    за 1000 подходов

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """

    count_ls = []  # список для сохранения количества попыток
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    # загадали список чисел
    random_array = np.random.randint(1, 101, size=(1000))

    for number in random_array:
        count_ls.append(random_predict_score(number))

    score = int(np.mean(count_ls))  # находим среднее количество попыток

    return print(f'Алгоритм угадал задуманное число из интервала 1-100 \
в среднем за {score} попыток!')


# RUN
if __name__ == '__main__':
    score_game(random_predict_score)

