def single_root_words(root_word, *other_words):
    same_words = []
    root_word = root_word.lower()
    for other_word in other_words:
        other_word = other_word.lower()
        if other_word in root_word or root_word in other_word:
            same_words.append(other_word)
    return same_words

result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)