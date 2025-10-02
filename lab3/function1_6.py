def reverse_words():
    sentence = input("Enter a sentence: ")
    words = sentence.split()
    reversed_sentence = " ".join(words[::-1])
    return reversed_sentence

print(reverse_words())
