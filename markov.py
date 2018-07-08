"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
	"""Take file path as string; return text as string.

	Takes a string that is a file path, opens the file, and turns
	the file's contents as one string of text.
	"""

	# your code goes here
	green_eggs = open(file_path)

	return(green_eggs.read())

	# return "Contents of your file as one long string"


def make_chains(text_string):
	"""Take input text as string; return dictionary of Markov chains.

	A chain will be a key that consists of a tuple of (word1, word2)
	and the value would be a list of the word(s) that follow those two
	words in the input text.

	For example:

		>>> chains = make_chains("hi there mary hi there juanita")

	Each bigram (except the last) will be a key in chains:

		>>> sorted(chains.keys())
		[('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

	Each item in chains is a list of all possible following words:

		>>> chains[('hi', 'there')]
		['mary', 'juanita']
		
		>>> chains[('there','juanita')]
		[None]
	"""

	chains = {}


	words = text_string.split()

	for i in range(len(words)-2):
		bi_gram_tuple = (words[i], words[i+1])
		if bi_gram_tuple in chains:
			chains[bi_gram_tuple].append(words[i+2])
		else: 
			chains[bi_gram_tuple] = [words[i+2]]

	# print(chains.items())

	# for k, v in chains.items(): 
	# 	print(k, ": ", v)	

	return chains


def make_text(chains):
	"""Return text from chains."""

	words = []

	# your code goes here
	
	random_key = choice(list(chains.keys())) # picks a random key & turns it into a list
											 # so we can index it for the 2nd index for 
											 # new key
	words.extend(random_key) # adds works in tuple as individual items to the words list

	# print("this is the random key", random_key)
	while random_key in chains:
		
		new_link = random_key[1] # this becomes the first index in the new tuple key

		# words.append(new_link) # adds the second index to the words list bc it's the second 
							   # word in the original tuple key from random key
		
		value_at_key = chains[random_key] # gives me the list at that key
		
		random_new_word = choice(value_at_key) # picks a random word from the list to make 
											   # new key tuple
		words.append(random_new_word) #add this word to the list to keep building sentence
		
		random_key = (new_link, random_new_word) # reassigning new to new key we generated

	# print("this is words", words)

	return " ".join(words)
	# print(" ".join(words))


input_path = "green-eggs.txt"

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

# print random_text
print(random_text)