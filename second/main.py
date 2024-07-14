import os


def count_word_frequency(filename):
    with open(filename) as file:
        word_count = {}
        for line in file:
            for word in line.split():
                frequency = word_count.get(word, 0)
                word_count[word] = frequency + 1
    return word_count


def sort_word_frequency(word_frequency):
    word_frequency_sorted = dict(sorted(word_frequency.items(), key=lambda item: (-item[1], item[0])))
    return word_frequency_sorted.items()


if __name__ == '__main__':
    script_dir = os.path.dirname(os.path.abspath(__file__))
    word_frequency = count_word_frequency(os.path.join(script_dir, 'words.txt'))
    for word, frequency in sort_word_frequency(word_frequency):
        print(f"{frequency} {word}")
