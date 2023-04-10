def capitalize(text):
	if text == '':
		return ''

	first_char, *other_chars = text
	first_char = first_char.upper()
	rest_substring = ''.join(other_chars)
	return f'{first_char}{rest_substring}'
