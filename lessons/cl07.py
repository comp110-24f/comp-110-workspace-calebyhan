def check_first_letter(word: str, letter: str) -> str:
    if word[0] == letter:
        return "match!"
    return "no match!"


print(check_first_letter(word="happy", letter="h"))
print(check_first_letter(word="happy", letter="s"))
