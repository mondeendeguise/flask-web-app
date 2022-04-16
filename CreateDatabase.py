import os
import pandas

class CreateDatabase:
    def __init__(self, name):
        self.name = name

    def make():
        with open(os.path.join('databases', f'{self.name}.json'), 'w+') as f:
            if not os.path.isfile(os.path.join('databases', f'{self.name}.json')):
                f.write()
            db = f.read_json()
        return db