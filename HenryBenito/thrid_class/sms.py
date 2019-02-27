from datetime import datetime


class SMS_store:
    def __init__(self):
        self.message_list = list()

    def add_new_arrival(self, from_number, time_arrived, text_of_SMS):
        self.message_list.append({"has_been_viewed": False,
                                  "from_number": from_number,
                                  "time_arrived": time_arrived,
                                  "text_of_SMS": text_of_SMS
                                  })

    def message_count(self):
        return len(self.message_list)

    def get_unread_indexes(self):
        result = list()
        for message_index in range(len(self.message_list)):
            if not self.message_list[message_index]["has_been_viewed"]:
                result.append(message_index)
        return result

    def get_message(self, i):
        if int(i) > len(self.message_list or int(i) < 0):
            return None
        self.message_list[i]["has_been_viewed"] = True
        previous_result = self.message_list[i].copy()
        del previous_result["has_been_viewed"]
        return previous_result

    def delete(self, i):
        del self.message_list[int(i)]

    def clear(self):
        self.message_list = list()


sms_store = SMS_store()
sms_store.add_new_arrival(70725852, str(datetime.now()), "Test")
sms_store.add_new_arrival(76478998, str(datetime.now()), "Other Test")
sms_store.add_new_arrival(64778998, str(datetime.now()), "Third Test")

print("Number of messages: {}".format(sms_store.message_count()))

print(sms_store.get_message(1))
print(sms_store.get_message(35))

print(sms_store.get_unread_indexes())

sms_store.delete(2)

sms_store.clear()
print("Number of messages: {}".format(sms_store.message_count()))
