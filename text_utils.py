# Preprocessing functions for text data

import re


def striphtml(text):
    """
	remove html formating (e.g. <b> <\b>, <a </a>) from a string

	>>> striphtml('Hi! <b> Important <\b>  click here <a> link </a>')
	'Hi!  Important   click here  link '

	"""
    p = re.compile(r'<.*?>')
    return p.sub('', text)


def remove_words(words_to_remove, list_of_strings):
    """
	words_to_remove: list of words to remove
	list_of_strings: list of string from which to remove words

	>>> remove_words(['bye'], ['hello, bye', 'bye, hi'])
	['hello, ', ', hi']

	"""
    for word in words_to_remove:
        list_of_strings = [s.replace(word, '') for s in list_of_strings]
    return list_of_strings


# test the functions
if __name__ == '__main__':
    import doctest
    doctest.testmod()
