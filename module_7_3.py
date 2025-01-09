# Задача "Найдёт везде"

class WordsFinder:
    def __init__(self, *args):
        self.file_names = []
        for i in args:
            self.file_names.append(i)

    def get_all_words(self):
        all_words = {}
        no_char = [',', '.', '=', '!', '?', ';', ':', '-']
        for i in self.file_names:
            with open(i, 'r', encoding = 'utf-8') as file:
                file_read = []
                for line in file:
                    line2 = ''
                    for char in line:
                        if not (char in no_char):
                            line2 += char
                    line2 = line2.lower().split()
                    file_read += line2
                all_words [i] = file_read
        return all_words

    def find(self, word):
        num_word = {}
        for a, b in self.get_all_words().items():
            c = 0
            for i in b:
                c += 1
                if i.lower() == word.lower():
                    num_word[a] = c
                    break
        return num_word

    def count(self, word):
        count_word = {}
        for a, b in self.get_all_words().items():
            c = 0
            for i in b:
                if i.lower() == word.lower():
                    c += 1
            count_word[a] = c
        return count_word





finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))  # 3 слово по счёту
print(finder2.count('teXT'))  # 4 слова teXT в тексте всего
