from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate #initial chat prompt is given here
from langchain_core.output_parsers import StrOutputParser #default poutput parser whev ever an output is received from llms
from langchain_community.llms import Ollama
import streamlit as st
import os
from dotenv import load_dotenv
from langchain.callbacks.tracers.langchain import LangChainTracer

load_dotenv()

#os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")
#langsmith tracking 

os.environ["LANGCHAIN_TRACING_V2"]="true"

print("LANGCHAIN_API_KEY:", os.getenv("LANGCHAIN_API_KEY"))
print("LANGCHAIN_PROJECT:", os.getenv("LANGCHAIN_PROJECT"))
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are an AI assistant"),
        ("user", "Question:{question}")
    ]
)

# stramlit franework
st.title('Langchain Demo with opensourceApi')
input_text = st.text_input("Serach the topic you want")

#llm = ChatOpenAI(model = "gpt-3.5-turbo")
llm=Ollama(model='llama2')
output_parser = StrOutputParser()
chain = prompt|llm|output_parser

tracer = LangChainTracer()
chain_with_tracing = chain.with_config({"callbacks": [tracer]})

if input_text:
    st.write(chain.invoke({'question':input_text}))