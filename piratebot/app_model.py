import os
from langgraph.graph import StateGraph, MessagesState, START
from langchain_google_vertexai import ChatVertexAI
from langgraph.checkpoint.memory import MemorySaver
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'C:\Users\Asus\PROJETOS_DEV\keys_APIs\key_google.json'
os.environ['LANGSMITH_TRACING'] = 'true'
os.environ['LANGSMITH_API_KEY'] = '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'

model = ChatVertexAI(model='gemini-1.5-flash')

workflow = StateGraph(state_schema=MessagesState)

prompt_template = ChatPromptTemplate(
    [
        ('system', 'Você é um pirata! Responda da melhor maneira possível. Não utilize linguagem markdown nas respostas. Seja curto nas respostas, use no máximo de 3 frases.'),
        MessagesPlaceholder(variable_name='messages')
    ]
)

def call_model(state: MessagesState):
    prompt = prompt_template.invoke(state)
    response = model.invoke(prompt)
    return {'messages': response}

workflow.add_edge(START, 'model')
workflow.add_node('model', call_model)

memory = MemorySaver()
app = workflow.compile(checkpointer=memory)