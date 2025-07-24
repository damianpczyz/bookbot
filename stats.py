
from string import printable

def get_num_words(book_content: str) -> int:
    return len(book_content.split())

def get_char_num(book_content: str) -> dict:
    all_chars = printable[:36] + ' ' + printable[62:] 

    char_dict = {}
    
    for char in all_chars:
        char_num = book_content.lower().count(char)
        char_dict[char] = char_num

    return char_dict

def sort_on(char_dict_list: list):
    return char_dict_list["num"]

def sort_dict(char_dict: dict) -> list:
    char_dict_list = []

    for char_name in char_dict:
        count = char_dict[char_name]
        
        char_dict_list.append({
            'char': char_name,
            'num' : count})
    
    char_dict_list.sort(reverse = True, key = sort_on)

    return char_dict_list

def prepare_report(char_dict: dict, num_chars: int, filepath: str):
    sorted_dicts = sort_dict(char_dict)

    print('============ BOOKBOT ============\n'
          f'Analyzing book found at {filepath}\n'
          '----------- Word Count ----------\n'
          f'Found {num_chars} total words\n'
          '--------- Character Count -------')
    
    for position in range(0, len(sorted_dicts)):
        char = sorted_dicts[position]['char']
        num = sorted_dicts[position]['num']
        print(f'{char}: {num}')

    return None