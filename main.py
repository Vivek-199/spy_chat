from spy_details import spy, Spy,ChatMessage,friends
from steganography.steganography import Steganography
from datetime import datetime
from termcolor import colored

STATUS_MESSAGES = ["sic parvis magna","i am batman","why so serious?"]

print "Welcome! Let\'s start."

question = "Do you want to continue as " + spy.salutation + ""+spy.name+"(Y/N)?"
existing = raw_input(question)
# Method for adding a status
def add_status():

    updated_status = None

    if spy.current_status != None:

        print "Your current status message is %s \n" % (spy.current_status)
    else:
        print "You don't have any status message currently."

    default = raw_input("Do you want to select from older status messages(Y/N)?")


    if default.upper() == "Y":

        item_position = 1

        for message in STATUS_MESSAGES:
            print "%d. %s" % (item_position, message)
            item_position = item_position + 1


        message_selection = int(raw_input("\nChoose from the above messages "))


        if len(STATUS_MESSAGES) >= message_selection:
            updated_status = STATUS_MESSAGES[message_selection - 1]

    elif default.upper() == "N":
        new_status = raw_input("What status you want to set?")

        if len(new_status) > 0:
            STATUS_MESSAGES.append(new_status)
            updated_status = new_status
    else:
        print "The option chosen is not valid! Press either y or n. "


    if updated_status:
        print "Your updated status message is: %s" % (updated_status)
    else:
        print "Currently you don't have a status update"


    return updated_status


# Method for adding a friend
def add_friend():

    new_friend = Spy("","",0,0.0)

    new_friend.name = raw_input("Please add your friend's name: ")
    new_friend.salutation = raw_input("Mr. or Ms. ?: ")

    new_friend.name = new_friend.salutation + "" + new_friend.name

    new_friend.age = int(raw_input("Age: "))

    new_friend.rating = float(raw_input("Rating: "))

    if len(new_friend.name) > 0 and new_friend.age > 16 and new_friend.rating >= spy.rating:
        friends.append(new_friend)
        print "Friend added"
    else:
        print "Invalid Entry. We can't add spy of given details"

    return len(friends)

#Method for selecting a friend
def select_a_friend():
    item_number = 0

    for friend in friends:
        print "%d. %s %s age %d with rating %.2f is online" % (item_number +1, friend.salutation,friend.name,
                                                                friend.age,friend.rating)
        item_number = item_number + 1

    friend_choice = raw_input("Choose a friend from your friends")

    friend_choice_position = int(friend_choice) - 1

    return friend_choice_position

#Method for sending a message
def send_message():

    friend_choice = select_a_friend()

    original_image = raw_input("What is the name of image?")
    output_path = "output.jpg"
    text = raw_input("What message do you want to send?")
    Steganography.encode(original_image,output_path,text)

    new_chat = ChatMessage(text,True)

    friends[friend_choice].chats.append(new_chat)

    print "Your message has been sent"

#Method for reading and saving a message
def read_message():

    sender = select_a_friend()

    output_path =raw_input("What is the file name? ")

    secret_text = Steganography.decode(output_path)

    new_chat = ChatMessage(secret_text,False)

    friends[sender].chats.append(new_chat)

    print "Your message has been saved"

#Method for showing message and chat history
def read_chat_history():

    read_chat = select_a_friend()



    for chat in friends[read_chat].chats:
        if chat.sent_by_me:
            print "[%s] %s: %s" % (chat.time.strftime("%d %B %Y"),'your message :' ,chat.message)

        else:
            print "[%s] %s's message: %s" % (chat.time.strftime("%d %B %Y"), friends[read_chat].name, chat.message)

# Method for starting a chat and providing user menu choices
def start_chat(spy):

    spy.name = spy.salutation +" "+ spy.name

    if spy.age > 18 and spy.age < 50:

        print "Authentication complete. Welcome "+spy.name+" age: "+str(spy.age)+"rating: "+str(spy.rating)\
              +" Nice to have you with us"

        show_menu = True

        while show_menu:
            menu_choices = "choose any one \n1. Add a status update \n2. Add a new friend \n3. Send a message " \
                           "\n4. Read a message \n5. Read Chats & chat history \n6. Close Application \n"
            menu_choice = raw_input(menu_choices)

            if len(menu_choice) > 0:
                menu_choice = int(menu_choice)

                if menu_choice == 1:
                    spy.current_status = add_status()
                elif menu_choice == 2:
                    number_of_friends = add_friend()
                    print "You have %d friends" % (number_of_friends)
                elif menu_choice == 3:
                    send_message()
                elif menu_choice == 4:
                    read_message()
                elif menu_choice == 5:
                    read_chat_history()
                else:
                    show_menu = False

    else:
        print "Your age is not valid for a spy"

if existing.upper() == "Y":
    start_chat(spy)
else:
    spy = Spy("","",0,0.0)

    spy.name = raw_input("Welcome to Spychat, you must tell me your spy name first: ")

    if len(spy.name) > 0:
        spy.salutation = raw_input("what should i call you Mr or Ms : ")

        spy.age = int(raw_input("What is your age :"))

        spy.rating = float(raw_input("What is your spy rating :"))

        start_chat(spy)
    else:
        print "Please add a valid name"

