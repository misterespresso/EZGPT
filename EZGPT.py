from openai import OpenAI
from pathlib import Path

client = OpenAI(api_key = "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")

#Message history array. This is your chats context.
message_history = []
status = True
total_tokens = 0

while status:
  #Checks to see if there is any context.
  if len(message_history) != 0:

    #Creates a prompt by declaring context via the message_history array.
    message = "Here is a history of our conversation which we are continuing:\n"
    message += str(message_history)
    
    #Adds clear instruction of a new message and gathers users new message
    message += "Here is my new message:\n"
    newmessage = input("Enter a Message: ")

    #Check to see if the user wants to quit.
    if newmessage == 'q': 
      status = False 
      break

    #Appends the new message to context and history
    message+= newmessage
    message_history.append(newmessage)

    #The completion request
    completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
      {"role": "developer", "content": "You are a helpful assistant."},
      {"role": "user", "content": "{}".format(message)}
    ])

    #Appends the response
    message_history.append(completion.choices[0].message.content)

    #Response
    print("ChatGPT:", completion.choices[0].message.content)

    #Checks tokens used for this message and total context. 
    tokens = completion.usage.total_tokens 
    total_tokens+= tokens
    print("Tokens used: ", tokens, "Total Chat Tokens: ", total_tokens)
    print('#'*30)
  else:

    message = input("Welcome enter a message to start or press \'q\' to quit: ")

    message_history.append(message)
    completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
      {"role": "developer", "content": "You are a helpful assistant."},
      {"role": "user", "content": "{}".format(message)}
    ])

    #Appends the response.
    message_history.append(completion.choices[0].message.content)
    
    #Response
    print("ChatGPT:", completion.choices[0].message.content)

    #Checks tokens used for this message and total context. 
    tokens = completion.usage.total_tokens 
    total_tokens+= tokens
    print("Tokens used: ", tokens, "Total Chat Tokens: ", total_tokens)
    print('#'*30)
  
