from datetime import datetime


class SmsStore:
    def __init__(self):
        self.__messages = []

    def add_new_arrival(self, from_number, time_arrived, text_of_sms):
        message = (False, from_number, time_arrived, text_of_sms)
        self.__messages.append(message)

    def message_count(self):
        return len(self.__messages)

    def get_unread_indexes(self):
        unread_indexes = []
        for index, message in enumerate(self.__messages):
            if not message[0]:
                unread_indexes.append(index)
        return unread_indexes

    def get_message(self, index):
        if self.__message_exists(index):
            message = self.__messages[index]
            to_return = message[1:]
            new_message = (True, *to_return)
            self.__messages[index] = new_message
            return to_return

    def delete(self, index):
        if self.__message_exists(index):
            self.__messages.pop(index)

    def clear(self):
        self.__messages.clear()

    def __message_exists(self, index):
        return 0 <= index < self.message_count()


# call store implementations
sms_store = SmsStore()
print(sms_store.message_count())
print("adding one message")
sms_store.add_new_arrival(12345, datetime.today(), "message1")
print(sms_store.message_count())
print(sms_store.get_unread_indexes())
print(sms_store.get_message(0))
print(sms_store.get_unread_indexes())
print("deleting message")
sms_store.delete(0)
print(sms_store.get_message(0))
print(sms_store.get_unread_indexes())
print(sms_store.message_count())
print("adding other message")
sms_store.add_new_arrival(12345, datetime.today(), "message2")
print(sms_store.get_message(0))
print(sms_store.get_unread_indexes())
print(sms_store.message_count())
print("clearing list")
sms_store.clear()
print(sms_store.get_message(0))
print(sms_store.get_unread_indexes())
print(sms_store.message_count())
