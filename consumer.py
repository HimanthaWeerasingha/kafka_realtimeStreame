# import libraries

from kafka import KafkaConsumer
import json

consumer = KafkaConsumer('bankbranch', group_id = 'my-consumer-group', bootstrap_servers= ['localhost:9092'], 
                         auto_offset_reset = 'earliest',
                          value_deserializer=lambda m: json.loads(m.decode('utf-8') ))

print("hello. consumer waiting for receivings .....")
print(consumer)

for msg in consumer:

    # message = msg.value.decode('utf-8')
    message = msg.value
    
    print(message)
