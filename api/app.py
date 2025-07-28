from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langserve import add_routes
import uvicorn
import os
from langchain_community.llms import Ollama
from dotenv import load_dotenv

load_dotenv()
os.environ["LANGCHAIN_TRACING_V2"]="true"
app = FastAPI(
    title='LangChain Server',
    version="1.0",
    description="Simple Api Server"
)

llama_model = Ollama(model='llama2')
gemma_model = Ollama(model='gemma')

prompt1 = ChatPromptTemplate.from_template("Write me an essay about {topic} with 100 words")
prompt2 = ChatPromptTemplate.from_template("Write me an poem about {topic} with 100 words")

add_routes(
    app,
    prompt1|llama_model,
    path='/essay'
)
add_routes(
    app,
    prompt2|gemma_model,
    path='/poem'
)

if __name__ =='__main__':
    uvicorn.run(app, host="localhost", port=8000)