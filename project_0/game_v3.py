"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def binar_predict(number: int = 1, start_range: int = 1,
                   end_range = 100) -> int:
    """Угадываем число методом деления допустимого
       интервала пополам

    Args:
        number (int, optional): Загаданное число. Defaults to 1.
        start_range (int, optional): Начало интервала из которого
                                     загадывается числа.
                                     Defaults to 1.
        end_range (int, optional): Конец интервала из которого
                                   загадывается числа.
                                   Defaults to 100.

    Returns:
        int: Число попыток
    """
    
    count = 0

    while True:
        count += 1
        predict_number = (start_range+end_range) // 2  # предполагаемое число
        if predict_number > number:
            end_range = predict_number - 1
        elif predict_number < number:
            start_range = predict_number + 1
        else:
            break #конец игры выход из цикла
    return count


def score_game(binar_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        binar_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(5)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(binar_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(binar_predict)
