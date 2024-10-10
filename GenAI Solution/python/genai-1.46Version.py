import os
from dotenv import load_dotenv
from openai import AzureOpenAI

load_dotenv()


client = AzureOpenAI(api_key= os.getenv("Azure_OpenAI_Key"), 
                     api_version=os.getenv("Azure_OpenAI_Version"),
                     azure_endpoint=os.getenv("Azure_OpenAI_Endpoint"))

model_name = os.getenv("Azure_OpenAI_Model")
response = client.chat.completions.create(
              model= model_name,
              messages= [
                  {"role":"system","content":"You are being helpful"},
                  {"role":"user","content":"Describe a hamburger."},
                  {"role":"assistant","content":"Food."},
                  {"role":"user","content":"Describe a Gin."},
                  {"role":"assistant","content":"Alcohol."},
                  {"role":"user","content":"Describe a printer."},
                  {"role":"assistant","content":"device."},
                  {"role":"user","content":"Describe a dress."},
                  {"role":"assistant","content":"Clothes."},




                  {"role":"user","content":"Describe a daisy."}
            ],
            max_tokens=100,
            temperature=1.0,
            n=2
)

print (response.choices[0].message.content)
print (response.choices[1].message.content)
