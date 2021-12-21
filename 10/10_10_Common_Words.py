def count_words(filename, word):
	"""count the approximate number of words in a file."""

	try:
		with open(filename, encoding='utf-8') as f:
			contents = f.read()
	except FileNotFoundError:
		pass
	else:
		word_count = contents.lower().count(word)
		msg = f"'{word}' appears in {filename} about {word_count} times."
		print(msg)

		

filename = 'book.txt'
count_words(filename, 'the')
