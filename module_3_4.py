def single_root_words(root_word, *other_words):
    same_words = []
    for word in other_words:
        if is_intersection(root_word, word, 4):
            same_words.append(word)
    return same_words

def is_intersection(word1, word2, count):
    result = False
    for i in range(0, len(word1) - count + 1):
        test_str = (word1[i: i + count]).upper()
        if test_str in word2.upper():
            result = True
            break
    return result

result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')

print(result1)
print(result2)