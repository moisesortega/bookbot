def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    char_count = get_chars_dict(text)
    list_of_chars = []
    for key in char_count:
        if key.isalpha():
            list_of_chars.append({key: char_count[key]})
        else:
            pass
    list_of_chars.sort(reverse=True, key=sort_on)
    print("--- Begin report books/frankenstein.txt. ---")
    print(f"{num_words} words found in the document")
    # The printing
    for i in list_of_chars:
        for char, count in i.items():
            print(f"The '{char}' character was found {count} times")
    print("--- End report ---")
    
def sort_on(char_dict):
    key = list(char_dict.keys())[0]
    return char_dict[key]

def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()
    

main()