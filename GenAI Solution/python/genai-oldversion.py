import os
from dotenv import load_dotenv
import openai
load_dotenv()

openai.api_type = "azure"
openai.api_key = os.getenv("Azure_OpenAI_Key")
openai.api_version = os.getenv("Azure_OpenAI_Version")
openai.api_base = os.getenv("Azure_OpenAI_Endpoint")



model_name = os.getenv("Azure_OpenAI_Model")
response = openai.ChatCompletion.create(
              engine = model_name,
              messages = [
                  {"role":"system","content":"You are being helpful"},
                  {"role":"user","content":"write a slogan for a computer programmer."}
            ],
            max_tokens = 100,
            temperature = 1.0,
            n = 2
)

print (response.choices[0].message.content)
print (response.choices[1].message.content)
