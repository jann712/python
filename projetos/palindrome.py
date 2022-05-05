word = input('Type a word: ')
word_inverted = ''

print()

for num in range(-1, -len(word) -1, -1):
	word_inverted += word[num]

print('word: {}'.format(word))
print('inverted: {}'.format(word_inverted))

print()

if word == word_inverted: print('Palindrome Alert')
else: print('Normal Word Alert')