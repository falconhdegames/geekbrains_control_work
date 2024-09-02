import json

class JsonFile:
    def __init__(self, file):
        self.path = file
        self.data = json.load(open(self.path, encoding='utf-8'))
    def writeValue(self, key, value):
        self.data[key] = value
        self.writeAll()
    def readValue(self, key):
        return self.data[key]
    def readAll(self):
        return self.data
    def writeAll(self):
        json.dump(self.data, open(self.path, 'w', encoding='utf-8'))
    def clear(self):
        open(self.path, 'w', encoding='utf-8').close()
    def writeValueInDict(self, key_0, key_1, value):
        self.data[key_0][key_1] = value
        self.writeAll()
    def removeValue(self, key):
        del self.data[key]
        self.writeAll()