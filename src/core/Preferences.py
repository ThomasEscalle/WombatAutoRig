
import json


# The Preferences class is used to store user preferences in a JSON file. 
# It has methods to load, save, get, and set preferences.
class Preferences:
    def __init__(self):
        self.preferences = {}
        self.load()

    # Load preferences from a JSON file.
    def load(self):
        try:
            with open("preferences.json", "r") as file:
                self.preferences = json.load(file)
        except FileNotFoundError:
            self.save()

    # Save preferences to a JSON file.
    def save(self):
        with open("preferences.json", "w") as file:
            json.dump(self.preferences, file)

    # Get a preference by key.
    # @param key The key of the preference.
    # @param default The default value if the preference is not found.
    # @return The value of the preference.
    def get(self, key ,default=None):
        if key in self.preferences:
            return self.preferences[key]
        return default

    # Set a preference by key.
    # @param key The key of the preference.
    # @param value The value of the preference.
    def set(self, key, value):
        self.preferences[key] = value
        self.save()