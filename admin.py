# import libraries
from kafka.admin import KafkaAdminClient, NewTopic

#configure admin client
admin_client = KafkaAdminClient(bootstrap_servers="localhost:9092", client_id='test')

#list of topics
topic_list = []

#create a topic
new_topic = NewTopic(name = 'bankbranch', num_partitions = 2, replication_factor = 1)

#append the topic
topic_list.append(new_topic)

admin_client.create_topics(new_topics=topic_list)



