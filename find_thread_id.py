from src.fbchat import Client

username = "<username>"
password = "<password>"
chat_name = "<chat name>"

client = Client(username, password, max_tries=1)
threads = client.fetchThreadList()
id = [t.uid for t in threads if t.name == chat_name]

if id:
    print("Thread ID for chat name '{}' found successfully: ".format(chat_name),
          id)
else:
    print("Error: Thread ID for chat name '{}' could not be found: ".format(chat_name))
