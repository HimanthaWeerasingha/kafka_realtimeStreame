# Import producer library
from kafka import KafkaProducer
import json

producer = KafkaProducer(value_serializer=lambda v: json.dumps(v).encode('utf-8'))

trans_id = 102

# loop to 
while True:
    user_input = input("Press enter to add a transaction (press 'n' to stop) : ")

    if (user_input == 'n'):
        print("Stopping the transaction")
        break
    else:
        atm_choise = input("Which ATM you want to transact in? 1 or 2 : ")
        if (atm_choise == '1' or atm_choise == '2'):
            producer.send("bankbranch", {'atmid': int(atm_choise), 'transid': trans_id})
            producer.flush()
            producer.send("bankbranch", value = "hello lamai")
            producer.flush()
            trans_id+=1
        
        else:
            print("Invalid ATM number")
            continue

producer.close()