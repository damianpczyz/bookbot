from stats import get_char_num, get_num_words, prepare_report
from sys import argv, exit

def get_book_text(filepath: str) -> str:
    with open(filepath) as book:
        book_content = book.read()
    return book_content    

def show_help() -> None:
    print('Usage: python3 main.py <path_to_book>')

def main():

    if(len(argv) != 2):
        show_help()
        exit(1)    
    else:
        filepath = argv[1]
        book_content = get_book_text(filepath)
        num_of_words = get_num_words(book_content)
        char_num_dict = get_char_num(book_content)

        prepare_report(char_num_dict, num_of_words, filepath)

main()