def reverse_sentence(sentence):
    words=sentence.split()
    reverse_sentence=''.join(reversed(words))
    return reverse_sentence

if __name__=="__main__":
    sentence=input("Enter sentence here:")
    print (Reserve_sentences(sentence))
