import yaml
import random
import os
import voluptuous as vol

from homeassistant.components.sensor import SensorEntity
from homeassistant.const import CONF_NAME
import homeassistant.helpers.config_validation as cv

DEFAULT_NAME = "Prattler Greeting"

PLATFORM_SCHEMA = vol.Schema({
    vol.Required("platform"): "prattler",
    vol.Optional(CONF_NAME, default=DEFAULT_NAME): cv.string,
})

def setup_platform(hass, config, add_entities, discovery_info=None):
    name = config.get(CONF_NAME)
    add_entities([PrattlerGreetingSensor(name)])

class PrattlerGreetingSensor(SensorEntity):
    def __init__(self, name):
        self._name = name
        self._state = None
        self._greetings = self._load_greetings()

    def _load_greetings(self):
        path = os.path.join(
            os.path.dirname(__file__),
            "greeting.yaml"
        )
        try:
            with open(path, "r", encoding="utf-8") as file:
                return yaml.safe_load(file).get("time_based", {})
        except Exception as e:
            print(f"Failed to load greetings: {e}")
            return {}

    def update(self):
        hour = self._get_hour()
        time_of_day = self._get_time_of_day(hour)
        greetings_list = self._greetings.get(time_of_day, [])
        self._state = random.choice(greetings_list) if greetings_list else "Hello, Automation Wizard!"

    def _get_hour(self):
        from datetime import datetime
        return datetime.now().hour

    def _get_time_of_day(self, hour):
        if 0 <= hour < 5:
            return "late_night"
        elif 5 <= hour < 12:
            return "morning"
        elif 12 <= hour < 17:
            return "afternoon"
        elif 17 <= hour < 21:
            return "evening"
        else:
            return "night"

    @property
    def name(self):
        return self._name

    @property
    def state(self):
        return self._state
