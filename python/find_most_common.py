"""Module for finding most common character in a string"""

SENTENCE = 'This is a common interview question'
CHARS = {}

for char in SENTENCE:
    if char in CHARS:
        CHARS[char] += 1
    else:
        CHARS[char] = 1

CHARS_SORTED = sorted(CHARS.items(), key=lambda kv: kv[1], reverse=True)

print(CHARS_SORTED[0])
