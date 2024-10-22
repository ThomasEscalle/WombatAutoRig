
from wombatAutoRig.src.core import FileHelper
import json

# The Preferences class is used to store user preferences in a JSON file. 
# It has methods to load, save, get, and set preferences.
class Preferences:
    def __init__(self):
        self.preferences = {}
        self.load()

    # Load preferences from a JSON file.
    def load(self):
        path = FileHelper.getPreferencesPath()
        if not path:
            return

        try:
            with open(path, "r") as file:
                self.preferences = json.load(file)
        except FileNotFoundError:
            self.save()

    # Save preferences to a JSON file.
    def save(self):
        path = FileHelper.getPreferencesPath()

        if not path:
            return
        
        with open(path, "w") as file:
            json.dump(self.preferences, file)

    # Get a preference by key.
    # @param key The key of the preference.
    # @param default The default value if the preference is not found.
    # @return The value of the preference.
    def get(self, key ,default=None):
        if key in self.preferences:
            return self.preferences[key]
        else:
            self.set(key, default)
        return default

    # Set a preference by key.
    # @param key The key of the preference.
    # @param value The value of the preference.
    def set(self, key, value):
        self.preferences[key] = value
        self.save()