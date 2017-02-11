import nltk

def open_book():
    with open('books/Moby_Dick.asciidoc', 'r') as moby_dick:
        moby = moby_dick.read()
    return moby


def write_sentences():
    moby = open_book()
    # replace newlines with spaces
    moby = moby.replace('\n', ' ')
    sent_detector = nltk.data.load('tokenizers/punkt/english.pickle')
    moby_sents = sent_detector.tokenize(moby)
    moby_sents_file = open('01_sentence_generation/moby_sents.txt', 'w')
    for sentence in moby_sents:
        moby_sents_file.write(sentence)
        moby_sents_file.write('\n')
    moby_sents_file.close()


def main():
    print("Writing out a list of sentences from Moby Dick")
    write_sentences()

if __name__ == "__main__":
    main()
