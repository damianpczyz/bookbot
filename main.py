from stats import get_char_num, get_num_words, prepare_report

def get_book_text(filepath: str) -> str:
    with open(filepath) as book:
        book_content = book.read()
    return book_content    

def main():
    filepath = "books/frankenstein.txt"
    book_content = get_book_text(filepath)
    num_of_words = get_num_words(book_content)

    # print(f'{num_of_words} words found in the document')
    char_num_dict = get_char_num(book_content)

    prepare_report(char_num_dict, num_of_words, filepath)

main()