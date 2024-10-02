def get_unique_sorted(int_list):
    # Я бы мог еще использовать sorted и set тогда вообще решение было бы в 2 строчки. Но наверное нельзя.
    unique_values = []
    for num in int_list:
        if num not in unique_values:
            unique_values.append(num)

    for i in range(len(unique_values)):
        for j in range(len(unique_values) - 1):
            if unique_values[j] > unique_values[j + 1]:
                unique_values[j], unique_values[j + 1] = unique_values[j + 1], unique_values[j]

    return unique_values



numbers = [4, 2, 5, 2, 3, 4, 1]
result = get_unique_sorted(numbers)
print(result)

def cosine_distance(vec1, vec2):
    """
    По Вашей ссылке я ничего не понял)) Сделал по этой ссылке: https://habr.com/ru/companies/sberbank/articles/726532/
    """

    if len(vec1) != len(vec2):
        print("Невозможно вычислить: векторы разной длины.")
        return

    if not any(vec1) or not any(vec2):
        print("Невозможно вычислить: один из векторов является нулевым.")
        return


    dot_product = sum(a * b for a, b in zip(vec1, vec2))

    norm1 = sum(a ** 2 for a in vec1) ** 0.5
    norm2 = sum(b ** 2 for b in vec2) ** 0.5

    cos_similarity = dot_product / (norm1 * norm2)
    cos_distance = 1 - cos_similarity

    print(f"Косинусное расстояние: {cos_distance}")

vector1 = [1, 2, 3]
vector2 = [4, 5, 6]
cosine_distance(vector1, vector2)

from datetime import datetime

def days_difference(date1_str, date2_str):
    # task 3
    date_format = "%Y-%m-%d"
    try:
        date1 = datetime.strptime(date1_str, date_format)
        date2 = datetime.strptime(date2_str, date_format)
        delta = date2 - date1
        days = abs(delta.days)
        print(f"Difference in days: {days}")
    except ValueError as e:
        print(f"Error parsing dates: {e}")

days_difference("2023-05-01", "2023-05-10")  
