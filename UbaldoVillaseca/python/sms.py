import datetime

class SMS_store:
  def __init__(self):
    self.messages = []

  def add_new_arrival(self, from_number, time_arrived, text_of_SMS):
    self.messages.append(Message(from_number, time_arrived, text_of_SMS))
  
  def message_count(self):
    return len(self.messages)
  
  def get_unread_indexes(self):
    return [i for i,message in enumerate(self.messages) if message.has_been_viewed == False]
  
  def get_message(self, i):
    message = self.messages[i]
    message.has_been_viewed = True
    return message
  
  def delete(self, i):
    del self.messages[i]

class Message:
  def __init__(self, from_number, time_arrived, text_of_SMS):
    self.has_been_viewed = False
    self.from_number = from_number
    self.time_arrived = time_arrived
    self.text_of_SMS = text_of_SMS
    
store = SMS_store()
store.add_new_arrival('ubaldo@villaseca.com', datetime.datetime.now(), "What is it")
store.add_new_arrival('ub@villaseca.com', datetime.datetime.now(), "What is it")
store.add_new_arrival('uba@villaseca.com', datetime.datetime.now(), "What is it")
print(store.message_count())
print('[%s]' % ', '.join(map(str, store.get_unread_indexes())))
store.get_message(1)
print(store.message_count())
print('[%s]' % ', '.join(map(str, store.get_unread_indexes())))
store.delete(0)
store.delete(1)
print(store.message_count())
