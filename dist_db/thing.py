import json
import time

class Thing:
    def __init__(self, id, value=None, timestamp=long(time.time() * 1000L)):
        self.id = id
        self.value = value
        self.timestamp = timestamp 

    @classmethod
    def from_json(cls, json):
        return cls(json['Id'],
                   json['Value'],
                   json['Timestamp'])

    def __str__(self):
        return json.dumps({'Id': self.id,
                           'Value': self.value,
                           'Timestamp': self.timestamp})
