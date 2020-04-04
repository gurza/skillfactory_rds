from math import ceil

import numpy as np

MIN_NUMBER = 1
MAX_NUMBER = 100


def game_core_v1(number):
    """Guesses the secret number (Version 1).

    Просто угадываем на random, никак не используя информацию о больше или меньше.

    :param number: the secret number.
    :type number: int
    :return: the number of guessing attempts.
    :rtype: int
    """
    count = 0
    while True:
        count += 1
        predict = np.random.randint(MIN_NUMBER, MAX_NUMBER + 1)
        if number == predict:
            return count


def game_core_v2(number):
    """Guesses the secret number (Version 2).

    Сначала устанавливаем любое random число, а потом уменьшаем или увеличиваем его в зависимости от того,
    больше оно или меньше нужного.

    :param number: the secret number.
    :type number: int
    :return: the number of guessing attempts.
    :rtype: int
    """
    count = 1
    predict = np.random.randint(MIN_NUMBER, MAX_NUMBER + 1)
    while number != predict:
        count += 1
        if number > predict:
            predict += 1
        elif number < predict:
            predict -= 1
    return count


def game_core_v3(number):
    """Guesses the secret number (Version 3 - my project).

    Binary search algorithm.

    :param number: the secret number.
    :type number: int
    :return: the number of guessing attempts.
    :rtype: int
    """
    min_predict = MIN_NUMBER
    max_predict = MAX_NUMBER
    predict = ceil((min_predict + max_predict - 1)/2)
    count = 1
    while number != predict:
        count += 1
        if number > predict:
            min_predict = predict + 1
        else:
            max_predict = predict - 1
        predict = ceil((min_predict + max_predict - 1)/2)
    return count


def score_game(game_core):
    """Calculates score for the given game core.

    :param game_core: game core function.
    :type game_core: function
    :return: score.
    :rtype: int
    """
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(MIN_NUMBER, MAX_NUMBER + 1, size=1000)
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    return score


if __name__ == '__main__':
    print('Алгоритм {core} угадывает число в среднем за {score} попыток'.format(
        core=game_core_v1, score=score_game(game_core_v1))
    )
    print('Алгоритм {core} угадывает число в среднем за {score} попыток'.format(
        core=game_core_v2, score=score_game(game_core_v2))
    )
    print('Алгоритм {core} угадывает число в среднем за {score} попыток'.format(
        core=game_core_v3, score=score_game(game_core_v3))
    )
