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

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None  
        self.prev = None    

class DoublyLinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, value):
        
        new_node = Node(value)
        if not self.head:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def pop(self):
        
        if not self.tail:
            return None
        value = self.tail.value
        if self.head == self.tail:
            self.head = self.tail = None
        else:

            self.tail = self.tail.prev
            self.tail.next = None
        return value

    def unshift(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def shift(self):
        if not self.head: 
            return None
        value = self.head.value
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        return value

    def __iter__(self):
        current = self.head
        while current:
            yield current.value
            current = current.next

dll = DoublyLinkedList()
dll.push(1)     
dll.push(2)     
dll.unshift(0)
print(list(dll))
dll.pop()
dll.shift()
print(list(dll))

def query_word_distribution(queries):

    total_queries = len(queries)
    word_count_dict = {}

    for query in queries:
        word_count = len(query.split())
        word_count_dict[word_count] = word_count_dict.get(word_count, 0) + 1

    for word_count in sorted(word_count_dict):
        count = word_count_dict[word_count]
        percentage = (count / total_queries) * 100
        print(f"{word_count} слово: {percentage:.2f}%")

search_queries = [
    "watch new movies",
    "coffee near me",
    "how to find the determinant",
    "python",
    "data science jobs in UK",
    "courses for data science",
    "taxi",
    "google",
    "yandex",
    "bing",
    "foreign exchange rates USD/BYN",
    "Netflix movies watch online free",
    "Statistics courses online from top universities"
]

query_word_distribution(search_queries)
