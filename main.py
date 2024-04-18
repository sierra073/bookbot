def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        # print(file_contents)
        words = file_contents.split()
        print('--- Begin report of books/frankenstein.txt ---')
        print(f"{len(words)} words found in the document")
        letters_dict = count_letters(file_contents)
        list_dict = [{"character": k, "num": v} for k, v in letters_dict.items()]
        list_dict.sort(reverse=True, key=sort_on)
        for d in list_dict:
            if d["character"].isalnum():
                print(f"The '{d["character"]}' character was found {d["num"]} times")


def count_letters(s: str) -> dict:
    result = {}
    s = s.lower()
    for char in s:
        if result.get(char):
            result[char] += 1
        else:
            result[char] = 1
    return result

def sort_on(dict):
    return dict["num"]


main()
