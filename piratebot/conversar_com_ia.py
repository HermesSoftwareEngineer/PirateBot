from .app_model import app
from langchain_core.messages import HumanMessage

config = {'configurable': {'thread_id': 'conversa1'}}

def conversar(query):
    input_messages = [HumanMessage(query)]
    output = app.invoke({'messages': input_messages}, config)
    return output['messages'][-1].content

# stop = False
# print('Digite 0 para sair!')

# while(not stop):
#     message = input('Sua Mensagem: ')
#     if message != '0':
#         conversar(message)
#     else:
#         stop = True