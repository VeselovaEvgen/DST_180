import numpy as np


"""Игра угадай число. Компьютер сам загадывает и угадывает число"""


def random_predict_3(number: int = 1) -> int:
    """
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """

    # Счетчик числа попыток
    count = 0
    predict = np.random.randint(1, 101) #генератор псевдослучайных чисел от 1 до 100

    # Переменная для списка сгенерированных чисел
    lst_predict = []
    for i in range(1, 101):
        lst_predict.append(np.random.randint(1, 101))
    #Сортировка списка
    lst_predict.sort()

    # low - для первого элемента списка, high - для последнего элемента
    low = lst_predict[0]
    high = len(lst_predict)-1
    
    # Цикл бинароного поиска для поиска загаданного числа number
    while low <= high:
        mid = (low + high) // 2
        if number == lst_predict[mid]:
            break
        if number < lst_predict[mid]:
            high = mid - 1
            count += 1
        else:  # number > lst_predict[mid]
            low = mid + 1
            count += 1


    return(count)


def score_game_3(random_predict_3) -> int:
    """За какое количество попыток в среднем за 10000 подходов угадывает наш алгоритм

    Args:
        random_predict_3 ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(1)  # фиксируем сид для воспроизводимости, чтобы получать одинаковый результат
    random_array = np.random.randint(1, 101, size=(10000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict_3(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попытки")

#RUN
if __name__ == '__main__':
    score_game_3(random_predict_3)