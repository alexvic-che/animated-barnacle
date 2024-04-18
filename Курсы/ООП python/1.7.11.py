class Viber:
    msg_list =[]

    @classmethod
    def add_message(cls, msg):
        cls.msg_list.append(msg)
    @classmethod
    def remove_message(cls, msg):
        cls.msg_list.remove(msg)
    @classmethod
    def set_like(cls ,msg):
        if msg.fl_like == False:
            msg.fl_like = True
        else:
            msg.fl_like = False
    @classmethod
    def show_last_message(cls, n):
        print(*[msg.text for msg in cls.msg_list[-n:]])
    @classmethod
    def total_messages(cls):
        return len(cls.msg_list)

class Message:

    def __init__(self, text):
        self.text = text
        self.fl_like = False

msg = Message("Всем привет!")
Viber.add_message(msg)
Viber.add_message(Message("Это курс по Python ООП."))
Viber.add_message(Message("Что вы о нем думаете?"))

Viber.show_last_message(2)
