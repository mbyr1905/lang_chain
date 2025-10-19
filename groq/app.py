import streamlit as st
import os
from langchain_groq import ChatGroq
from langchain_community.document_loaders import WebBaseLoader
from langchain.embeddings import OllamaEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from lanchain.chains.combine_documnets import create_stuff_documents_chain
from langchain_core.prompts import ChtPromptTemplate
from langchain.chains import create_retrieval_chain
from langchain.llms import Ollama

from dotenv import load_dotenv
load_dotenv()

groq_api_key = os.environ['GROQ_API_KEY']

