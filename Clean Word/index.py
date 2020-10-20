# recursion function (Clean Word)

def CleanWord(word):
    if len(word) == 1:
        return word
    
    elif word[0] == word[1]:
        return CleanWord(word[1:])
    
    else:
        return word[0] + CleanWord(word[1:])

print(CleanWord("wwwooooorrrrllddd"))
