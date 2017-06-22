from datetime import datetime

# class Spy is declared
class Spy:

    def __init__(self,name,salutation,age,rating):
        self.name = name
        self.salutation = salutation
        self.age = age
        self.rating = rating
        self_is_online = True
        self.chats = []
        self.current_status = None
#declaring class ChatMessage
class ChatMessage:

    def __init__(self,message,sent_by_me):
        self.message = message
        self.time = datetime.now()
        self.sent_by_me = sent_by_me


spy = Spy("Hunt","Mr.",20,5.8)

friend_one = Spy("Wick","Mr.",21,5.2)
friend_two = Spy("L","Mr.",24,4.9)
friend_three = Spy("Bourne","Mr.",20,5.4)

#Implementing list
friends = [friend_one,friend_two,friend_three]
