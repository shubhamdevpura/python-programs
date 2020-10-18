def reverse_sentence(sentence):
    words=sentence.split()
    reverse_sentence=''.join(reversed(words))
    # string reverse ho gayi bc
    return reverse_sentence

if __name__=="__main__":
    input='Hii Heloo'
    print (reverse_sentence(input))
