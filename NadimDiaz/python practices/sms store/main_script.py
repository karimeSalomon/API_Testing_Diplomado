import sms_story
import datetime

my_inbox = sms_story.SMS_store()

my_inbox.add_new_arrival(76990445,datetime.datetime.now(),"ola ke ase")
my_inbox.add_new_arrival(76990446,datetime.datetime.now(),"aqui comiendo o ke ase")
my_inbox.add_new_arrival(76990447,datetime.datetime.now(),"shama shama")

print("Messages of my inbox: ", my_inbox.message_count()) #3

print("All indexes didn't read:", my_inbox.get_unread_indexes()) #all

print("Reading with invalid index: ", my_inbox.get_message(4)) #None

print("Reading with valid index: ", my_inbox.get_message(2)) #aqui comiendo o ke ase

print("All indexes didn't read:", my_inbox.get_unread_indexes()) #just first one and last one

#removing last message
my_inbox.delete(2)

print("Messages of my inbox: ", my_inbox.message_count()) #2

#removing all
my_inbox.clear()

print("Messages of my inbox: ", my_inbox.message_count()) #0

