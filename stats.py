def get_book_text(book):
        with open(book) as b:
            book_contents = b.read()
        return book_contents

def count_words(book):
    words = get_book_text(book).split()
    count = 0
    for word in words:
        count += 1
    return count

def count_characters(book):
    words = get_book_text(book).lower()
    character_counts = {}
    for character in words:
        if character not in character_counts:
                    character_counts[character] = 0
        character_counts[character] += 1
    return character_counts

def list_sorter(book):
    dictionary = count_characters(book)
    list = []
    for character, character_count in dictionary.items():
        list.append({"char":character, "num":character_count})
    def get_num(item):
        return item["num"]
    list.sort(reverse = True, key = get_num)
    return list
