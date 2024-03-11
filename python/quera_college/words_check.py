import re


def words_check(text):
    words = text.split()
    result = {}
    for word in words:
        cleaned_word = re.sub("[^A-Za-z]", "", word).capitalize()
        word_length = len(word)
        cleaned_word_length = len(cleaned_word)
        if word_length - cleaned_word_length < 0.5 * word_length:
            if cleaned_word in result:
                result[cleaned_word] += 1
            else:
                result[cleaned_word] = 1
    return result


# Local Test
print(words_check("""hEllO My FriEnDs!!!
thIS is A tEsT For your #p#r#o#b#l#e#m a"""))
