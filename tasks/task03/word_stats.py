import re
text = input('Enter list of strings: ')
text = text.lower()
words = text.split()
words = [word.strip('.,?!;()[]') for word in words]
texts = re.split('[!.?]', text)

word_count = {i:words.count(i) for i in words}
word = list(word_count)
print('word           count      first line')
for i in word:
    for a in texts:
        if re.search(i, a):
            print(f'{i:10} {word_count[i]:5} {texts.index(a):10d}')
            # print(i, word_count[i], texts.index(a))
            break

