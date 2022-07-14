import requests
from bs4 import BeautifulSoup


def task_two():

    def get_animals(page=None, list_of_animals=None):
        '''
        Функция производит сбор всех перечисленных животных на русском языке и латыни
        '''


        if page is None:
            url = "https://inlnk.ru/jElywR"
            page = requests.get(url).text
            list_of_animals = []

        navigation_links = ("Предыдущая страница", "Следующая страница")
        soup = BeautifulSoup(page, 'lxml')

        '''
        В список добавляются все ссылки, в тексте, которых назавания животных
        За исключение ссылок на предыдущую и следующую страницу
        '''
        animals = soup.find('div', id='mw-pages').find_all('a')
        for animal in animals:
            if animal.text not in navigation_links:
                list_of_animals.append(animal.text)
                count = len(list_of_animals)
                print(f'Collected {count} animals.')

        '''
        Переход на следуюущую страницу
        '''
        links = soup.find('div', id='mw-pages').find_all('a')
        for a in links:
            if a.text == 'Следующая страница':
                url = 'https://ru.wikipedia.org/' + a.get('href')
                page = requests.get(url).text
                get_animals(page, list_of_animals)
                return list_of_animals

    def count(list_of_names):

        '''
        Подсчет всех животных по первой букве в их названии
        '''
        count_dict = {"А": 0, "Б": 0, "В": 0, "Г": 0, "Д": 0, "Е": 0, "Ё": 0,
                      "Ж": 0, "З": 0, "И": 0, "Й": 0, "К": 0, "Л": 0, "М": 0,
                      "Н": 0, "О": 0, "П": 0, "Р": 0, "С": 0, "Т": 0, "У": 0,
                      "Ф": 0, "Х": 0, "Ц": 0, "Ч": 0, "Ш": 0, "Щ": 0, "Э": 0, "Ю": 0, "Я": 0,
                      "A": 0, "B": 0, "C": 0, "D": 0, "E": 0, "F": 0, "G": 0,
                      "H": 0, "I": 0, "J": 0, "K": 0, "L": 0, "M": 0, "N": 0,
                      "O": 0, "P": 0, "Q": 0, "R": 0, "S": 0, "T": 0, "U": 0,
                      "V": 0, "W": 0, "X": 0, "Y": 0, "Z": 0}

        for el in list_of_names:
            key = el[0]
            if key in count_dict:
                count = count_dict[key] + 1
                count_dict[key] = count

        count_string = ""
        for el in count_dict:
            string = f"{el}: {count_dict[el]} \n"
            count_string += string
        return count_string

    list_of_animals = get_animals()
    count_string = count(list_of_animals)
    return count_string


if __name__ == "__main__":
    print(task_two())
