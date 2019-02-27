class SMS_store(object):
  def __init__(self):
    self.messages = []

  def add_new_arrival(self, from_number, time_arrived, text_of_SMS):
    # Makes new SMS tuple, inserts it after other messages
	# in the store. When creating this message, its # has_been_viewed status is set False.
    new_message = (False, from_number, time_arrived, text_of_SMS)
    self.messages.append(new_message)

  def message_count(self):
     # Returns the number of sms messages in my_inbox
     return len(self.messages)

  def get_unread_indexes(self):
 	# Returns list of indexes of all not-yet-viewed SMS messages
     indexes = []
     aux = 0
     for j,k,m,n in self.messages:
         if j == False:
             indexes.append(aux)
             aux = aux + 1
     return indexes

  def get_message(self, i):
     # Return (from_number, time_arrived, text_of_sms) for message[i] 
     # Also change its state to "has been viewed".
     # If there is no message at position i, return None
    if i >= len(self.messages):
        return "None"
    else:
        message = self.messages[i]
        lst = list(message)
        lst[0] = True
        new_record_value = tuple(lst)
        #Tuples are immutable types in python.
        self.messages[i] = new_record_value
        return new_record_value

  def delete(self, i):
    # Delete the message at index i 
    if i >= len(self.messages):
        return "None"
    else:
        del self.messages[i]

  def clear(self):
      # Delete all messages from inbox
      self.messages.clear()