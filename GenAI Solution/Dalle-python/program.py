# Note: DALL-E 3 requires version 1.0.0 of the openai-python library or later
import os
from openai import AzureOpenAI
import json
from dotenv import load_dotenv


load_dotenv()



load_dotenv()
client = AzureOpenAI(
                    api_version=os.getenv("Azure_OpenAI_Version"),
                    azure_endpoint=os.getenv("Azure_OpenAI_Endpoint"),
                    api_key=os.getenv("Azure_OpenAI_Key"))

result = client.images.generate(
    model="Dalle3", # the name of your DALL-E 3 deployment
    prompt="homesick",
    n=1
)

image_url = json.loads(result.model_dump_json())['data'][0]['url']
print(image_url)