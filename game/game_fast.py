import numpy as np

def binary_search_predict(number: int = 1) -> int:
    """Угадываем число с помощью бинарного поиска

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток!
    """
    count = 0
    left = 1
    right = 100

    while left <= right:
        count += 1
        middle = (left + right) // 2
        predict_number = middle

        if number < predict_number:
            right = middle - 1
        elif number > predict_number:
            left = middle + 1
        else:
            break

    return count

def score_game(binary_search_predict) -> int:
    """За какое количество попыток в среднем за 100 подходов угадывает наш алгоритм

    Args:
        binary_search_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(1)
    random_array = np.random.randint(1, 101, size=(1000))

    for number in random_array:
        count_ls.append(binary_search_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попыток")
    return score

if __name__ == "__main__":
    score_game(binary_search_predict)
