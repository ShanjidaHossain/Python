# Write a function that asks the user for a long string containing multiple words.
# Print back to the user the same string, except with the words in backwards order.
# For example, Input:
#   My name is Michele
# Output:
#  Michele is name My

# Function to reverse words of string

def rev_sentence(sentence):
    words = sentence.split(' ')
    reverse_sentence = ' '.join(reversed(words))
    return reverse_sentence


if __name__ == "__main__":
    input = 'geeks quiz practice code'
    print(input)
    print(rev_sentence(input))
