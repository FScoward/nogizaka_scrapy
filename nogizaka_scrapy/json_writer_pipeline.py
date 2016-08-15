# -*- coding: utf-8 -*-

import json

class JsonWriterPipeline(object):

    def __init__(self):
        self.file = open('nogizaka.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False, indent=2) + ",\n"
        self.file.write(line)
        return item
