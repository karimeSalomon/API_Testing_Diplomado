# practice #13

# create a new class, SMS_store. the class will instantiate SMS_store objects,
# similar to an inbox or outbox on a cellphone:
#     my_inbox = SMS_store()
# this store can hold multiple SMS messages (i.e. its internal state will just
# be a list of messages). Each message will be represented as a tuple:
#     (has_been_viewed, from_number, time_arrived, text_of_SMS)
# the inbox object should provide these methods:
#     my_inbox.add_new_arrival(from_number, time_arrived, text_of_SMS) 
#             # Makes new SMS tuple, inserts it after other messages
#             # in the store. When creating this message, its
#             # has_been_viewed status is set False.
#     my_inbox.message_count()
#             # Returns the number of sms messages in my_inbox
#     my_inbox.get_unread_indexes() 
#             # Returns list of indexes of all not-yet-viewed SMS messages
#     my_inbox.get_message(i)
#             # Return (from_number, time_arrived, text_of_sms) for message[i] 
#             # Also change its state to "has been viewed".
#             # If there is no message at position i, return None
#     my_inbox.delete(i)
#             # Delete the message at index i
#     my_inbox.clear()
#             # Delete all messages from inbox
#
# write the class, create a message store object,
# write tests for these methods, and implement the methods.

from time import *

class SMS_Store:
    def __init__(self):
        self.messages = []

    def add_new_arrival(self,from_number,time_arrived,text_of_sms):
        self.messages.append((False,from_number,time_arrived,text_of_sms))

    def message_count(self):
        return len(self.messages)

    def get_unread_indexes(self):
        list = []
        for index,message in enumerate(self.messages):
            if not message[0]:
                list.append(index)
        return list

    def get_message(self,i):
        if 0 <= 0 and i < len(self.messages):
            message = self.messages[i]
            self.messages[i] = (True,message[1],message[2],message[3])
            return message

    def delete(self,i):
        if 0 <= 0 and i < len(self.messages):
            del self.messages[i]

    def clear(self):
        self.messages = []

    def print(self):
        for index,message in enumerate(self.messages):
            print('[{0}] {1} | {2}'.format(
                'X' if not message[0] else ' ',
                strftime('%Y-%m-%d %H:%M:%S',localtime(message[2])),
                message[1]))
            print('    {0}'.format(message[3]))

my_inbox = SMS_Store()

my_inbox.add_new_arrival('+591 645693450',time(),'Hello')
my_inbox.add_new_arrival('+591 645693450',time(),'Hello??')
my_inbox.add_new_arrival('+591 645693450',time(),'Moshi moshiii?')
my_inbox.print()

print()
print('Numero de mensajes:',my_inbox.message_count())
print()

unread = my_inbox.get_unread_indexes()
print('Mensajes sin leer:',unread)
print()

print('Leyendo mensaje {0}:'.format(unread[0]),my_inbox.get_message(unread[0]))
print()

my_inbox.print()
print()

unread = my_inbox.get_unread_indexes()
print('Mensajes sin leer:',unread)
print()

print('Leyendo mensaje {0}:'.format(unread[0]),my_inbox.get_message(unread[0]))
print()

my_inbox.print()
print()

my_inbox.delete(1)
print('Eliminando mensaje 1')
print()

my_inbox.print()
print()

my_inbox.clear()
print('Vaciando lista de mensajes')
print()

my_inbox.print()
print()

