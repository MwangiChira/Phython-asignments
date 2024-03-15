user_input = input("Enter a list of words (separated by spaces): ")
words = user_input.split()
odd_length_words = [word for word in words if len(word) % 2 != 0]
print("Words with odd character count:")
for word in odd_length_words:
    print(word)