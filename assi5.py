#!/usr/bin/env python
# coding: utf-8

# In[1]:


#A68; assignment:5
# Predefined knowledge base
knowledge_base = {
    "hello": "Hello! How can I assist you today?",
    "how are you": "I'm just a computer program, but I'm doing well. How can I help you?",
    "name": "I don't have a name, you can call me Chatbot.",
    "bye": "Goodbye! If you have more questions, feel free to ask."
}

# Function to get a response based on user input
def get_response(user_input):
    user_input = user_input.lower()  # Convert input to lowercase
    response = knowledge_base.get(user_input, "I'm sorry, I don't understand that.")

    return response

# Main chat loop
print("Chatbot: Hello! How can I assist you today? (Type 'bye' to exit)")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'bye':
        print("Chatbot: Goodbye!")
        break
    response = get_response(user_input)
    print("Chatbot:", response)


# In[ ]:





# In[ ]:




