# -*- coding: utf-8 -*-

import json

class JsonWriterPipeline(object):

    def __init__(self):
        self.file = open('nogizaka.json', 'w', encoding='utf-8')
        self.seen = set()

    def process_item(self, item, spider):
        target = dict(item)
        entry_title = target['entry_title'][0]
        if entry_title in self.seen:
            pass
        else:
            self.seen.add(entry_title)
            # line = json.dumps(target, ensure_ascii=False, indent=2) + ",\n"
            line = json.dumps(target, ensure_ascii=False) + ",\n"
            self.file.write(line)
        return item
