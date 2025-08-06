from google import generativeai
from google.generativeai import types
# from sentence_transformers import SentenceTransformer
import requests
from PIL import Image
import PyMuPDF
import chromadb
import io, re, os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("API_KEY")
client = generativeai.Client(api_key="API_KEY")

response = client.models.generate_content(
    model="gemini-2.0-flash", contents="Explain how AI works in a few words. Let's think step by step."
)
print(response.text)