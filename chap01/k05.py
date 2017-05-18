# coding: utf-8
#文字n-gram
def ngram_char(string, n):
    ngrams = [string[i:i+n] for i in range(len(string) - (n - 1))]
    return ngrams

#単語n-gram
def ngram_word(words, n):
    ngrams = [''.join(words[i:i+n]) for i in range(len(words) - (n - 1))]
    return ngrams

if __name__ == '__main__':
    string = "I am an NLPer"
    words = string.split(' ')
    print(ngram_char(string, 2))
    print(ngram_word(words, 2))
