#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import xml.etree.ElementTree as ET

from textblob import TextBlob

def parse_xml():
    tree = ET.parse('./romeo_and_juliet_moby.xml')
    root = tree.getroot()
    acts = root.findall('ACT')
    romeo_array = []
    for act in acts:
        for scene in act.findall('SCENE'):
            for speech in scene.findall('SPEECH'):
                for line in speech.findall('LINE'):
                    line_text = ''
                    for ll in line.itertext():
                        line_text = line_text + ll

                    if not line_text:
                        line_text = ''

                    text_blob = TextBlob(line_text)
                    romeo_array.append({
                        'act': act.find('TITLE').text,
                        'scene': scene.find('TITLE').text,
                        'speaker': speech.find('SPEAKER').text,
                        'line': line_text,
                        'line_polarity': text_blob.sentiment.polarity,
                        'line_subjectivity': text_blob.sentiment.subjectivity
                    })

    return romeo_array

if __name__ == "__main__":
    romeo_array = parse_xml()

    with open('romeo_sentiment_array.json', 'w') as romeo_file:
        json.dump(romeo_array, romeo_file, indent=4)
