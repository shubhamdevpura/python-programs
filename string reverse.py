def reverse_sentence(sentence):
    words=sentence.split()
    reverse_sentence=''.join(reversed(words))
    return reverse_sentence

if __name__=="__main__":
    input='Hii Heloo'
    print (ReverseOfSentence(input))
