#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import nltk

def open_book():
    with open('books/Moby_Dick.asciidoc', 'r') as moby_dick:
        moby = moby_dick.read()
    return moby.replace('\n', ' ')

class SentenceStats:
    def __init__(self, sentence):
        self.sentence = sentence

    def characters(self):
        return len(self.sentence)

    def words(self):
        tokens = nltk.word_tokenize(self.sentence)
        return len(tokens)

def main():
    moby = open_book()

    sent_detector = nltk.data.load('tokenizers/punkt/english.pickle')
    sentences = sent_detector.tokenize(moby)
    sentence_data = []
    for index, sentence in enumerate(sentences):
        sentence_stats = SentenceStats(sentence)
        sentence_data.append([
            index,
            sentence,
            sentence_stats.words(),
            sentence_stats.characters()
        ])
    with open('01_sentence_generation/moby_sentence_stats.json', 'w') as moby_json:
        json.dump(sentence_data, moby_json)


if __name__ == "__main__":
    main()
