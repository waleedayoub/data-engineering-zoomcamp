import csv
import json
from typing import List, Dict
<<<<<<< HEAD

from kafka.errors import KafkaTimeoutError

from ride import Ride
from kafka import KafkaProducer

=======
from kafka import KafkaProducer
from kafka.errors import KafkaTimeoutError

from ride import Ride
>>>>>>> class/main
from settings import BOOTSTRAP_SERVERS, INPUT_DATA_PATH, KAFKA_TOPIC


class JsonProducer(KafkaProducer):
    def __init__(self, props: Dict):
<<<<<<< HEAD
        self.resources = './resources/rides.csv'
        self.producer = KafkaProducer(**props)
        self.topic = KAFKA_TOPIC
=======
        self.producer = KafkaProducer(**props)
>>>>>>> class/main

    @staticmethod
    def read_records(resource_path: str):
        records = []
        with open(resource_path, 'r') as f:
            reader = csv.reader(f)
            header = next(reader)  # skip the header row
            for row in reader:
                records.append(Ride(arr=row))
        return records

<<<<<<< HEAD
    def publish_rides(self, messages: List[Ride]):
        for ride in messages:
            try:
                record = self.producer.send(topic=self.topic, key=ride.pu_location_id, value=ride)
=======
    def publish_rides(self, topic: str, messages: List[Ride]):
        for ride in messages:
            try:
                record = self.producer.send(topic=topic, key=ride.pu_location_id, value=ride)
>>>>>>> class/main
                print('Record {} successfully produced at offset {}'.format(ride.pu_location_id, record.get().offset))
            except KafkaTimeoutError as e:
                print(e.__str__())


if __name__ == '__main__':
    # Config Should match with the KafkaProducer expectation
    config = {
        'bootstrap_servers': BOOTSTRAP_SERVERS,
        'key_serializer': lambda key: str(key).encode(),
        'value_serializer': lambda x: json.dumps(x.__dict__, default=str).encode('utf-8')
    }
    producer = JsonProducer(props=config)
    rides = producer.read_records(resource_path=INPUT_DATA_PATH)
<<<<<<< HEAD
    producer.publish_rides(messages=rides)
=======
    producer.publish_rides(topic=KAFKA_TOPIC, messages=rides)
>>>>>>> class/main
