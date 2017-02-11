#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import xml.etree.ElementTree as ET

import textblob

def parse_xml():
    tree = ET.parse('./romeo_and_juliet_moby.xml')
    root = tree.getroot()
    acts = root.findall('ACT')
    romeo_data = []
    for act in acts:
        act_data = {'title': act.find('TITLE').text, 'scenes': []}
        for scene in act.findall('SCENE'):
            scene_data = {'title': scene.find('TITLE').text, 'speaches': []}
            for speech in scene.findall('SPEECH'):
                speaker = speech.find('SPEAKER').text
                speech_data = {'speaker': speaker, 'lines': []}
                for line in speech.findall('LINE'):
                    speech_data['lines'].append(line.text)

                scene_data['speaches'].append(speech_data)
            act_data['scenes'].append(scene_data)
        romeo_data.append(act_data)
    return romeo_data

if __name__ == "__main__":
    romeo_data = parse_xml()
    with open('romeo_with_sentiment.json', 'w') as romeo_json:
        json.dump(romeo_data, romeo_json)
