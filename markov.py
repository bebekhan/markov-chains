"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """
    expand_list = []
    with open(file_path) as file_name:
        for line in file_name:
            line = line.strip()
            sep_on_space = line.split()
            expand_list.extend(sep_on_space)

    return " ".join(expand_list)

open_and_read_file("green-eggs.txt")


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
    count = 0
    sep_on_space = text_string.split()

    while count < len(sep_on_space) - 4:
        turn_tuple = (sep_on_space[count], sep_on_space[count+1])

        if turn_tuple in chains.keys():
            chains[turn_tuple] += [sep_on_space[count + 2]]

        else:
            chains[turn_tuple] = [sep_on_space[count + 2]]

        count += 1

    return chains

print make_chains(open_and_read_file("green-eggs.txt"))

# def make_text(chains):
#     """Return text from chains."""

#     words = []

#     # your code goes here

#     return " ".join(words)


# input_path = "green-eggs.txt"

# # Open the file and turn it into one long string
# input_text = open_and_read_file(input_path)

# # Get a Markov chain
# chains = make_chains(input_text)

# # Produce random text
# random_text = make_text(chains)

# print random_text
