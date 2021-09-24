import re
text = input('Enter list of strings: ')
result = {}

text_result = re.split('[!.?]', text)
for line, texts in enumerate(text_result):
    words = re.findall(r'\b\w+\b', texts.lower())

    for word in words:
        if word in result:
            result[word][0] += 1
        else:
            result[word] = [1, line]

print('word', 'count', 'first line', sep='\t\t')
for word, word_result in result.items():
    print(f'{word:15} {word_result[0]:5} {word_result[1]:5d}')

