
class SMS_store:
    def __init__(self):
        self.store = []
    def add_new_arrival(self, from_number, time_arrived, text_of_SMS):
        new_message = (False, from_number, time_arrived, text_of_SMS)
        self.store.append(new_message)
    def message_count(self):
        return len(self.store)
    def get_unread_indexes(self):
        return [index for index in range(len(self.store)) if not self.store[index][0]]
    def get_message(self, i):
        if i > len(self.store) or i < len(self.store) : return None
        updated_message = (True, self.store[i][1], self.store[i][2], self.store[i][3])
        self.store[i] = updated_message
        return self.store[i]



my_inbox = SMS_store()
my_inbox.add_new_arrival(123456, '2-18-2019 18:00', 'Message')
num = my_inbox.message_count()
unread_message = my_inbox.get_unread_indexes()
print('[+] Message number:', num)
print('[+] Unread message:', unread_message)
