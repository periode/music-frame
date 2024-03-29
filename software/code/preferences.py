import yaml
import os
from logger import Logger

class Preferences:
    def __init__(self):
        # defaults
        self.composition = None
        self.volume = 1.0
        self.debug = False
        self.web = True
        self.port = "2046"
        self.host = "0.0.0.0"

        self.prefs = vars(self)
        self.debug = False
        self.logger = Logger()
        
    def load(self, _type, _input):
        self.logger.debug(f"loading prefs as {_type} from {_input}")

        if _type == "yaml":
            try:
                path = os.path.join(os.path.dirname(__file__), f"{_input}")
                self.logger.debug(f"loading preferences from: {path}")
                loaded = yaml.safe_load(open(path))
                self.logger.debug(f"loaded: {loaded}")

            except:
                exit(f"no preferences found.")

            self.composition = loaded['composition']
            self.volume = loaded['volume']
            self.debug = loaded['debug']
            self.web = loaded['web']
            self.port = loaded['port']
            self.host = loaded['host']

            self.prefs = loaded
        elif _type == "args":
            self.composition = _input.composition
            self.volume = _input.volume
            self.debug = _input.debug
            self.web = _input.web
            self.port = _input.port
            self.host = _input.host

            self.prefs = vars(_input)

        
        self.logger.debug(f"set preferences: {self.prefs}")

    def save(self):
        success = True
        with open('preferences.yml', 'w') as file:
            yaml.dump(self.prefs, file)
        
        return success
    
    def update(self, _key, _value):
        self.prefs[_key] = _value