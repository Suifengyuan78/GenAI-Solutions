import os
from dotenv import load_dotenv
from openai import AzureOpenAI

load_dotenv()
azure_openai_version = os.getenv("Azure_OpenAI_Version")
azure_openai_endpoint = os.getenv("Azure_OpenAI_Endpoint")
azure_openai_key = os.getenv("Azure_OpenAI_Key")
model_name = os.getenv("Azure_OpenAI_Model")


azure_search_endpoint = os.getenv("Search_endpoint")
azure_search_index = os.getenv("Search_index")
azure_search_key = os.getenv("Search_key")


client = AzureOpenAI(
                     base_url       = f"{azure_openai_endpoint}/openai/deployments/{model_name}/extensions",
                     api_key        = azure_openai_key, 
                     api_version    = azure_openai_version,
                     )

extra_config = dict(dataSources = [{
                                    "type"       : "AzureCognitiveSearch",
                                    "parameters" : {"endpoint"  : azure_search_endpoint, 
                                                    "key"       : azure_search_key, 
                                                    "indexName" : azure_search_index
                                                    }
                                    }]
                    )
                                                    
response = client.chat.completions.create(
                                          model     = model_name,
                                          messages  = [
                                                    {"role":"system" , "content":"You are being helpful"},
                                                    {"role":"user"   , "content":"What is the new name for Microsfot power virtual agents?"},
                                                     ],
                
         
                                         max_tokens  = 100,
                                         temperature = 1.0,
                                         n=2,
                                         extra_body = extra_config
                                         )

print (response.choices[0].message.content)
print (response.choices[1].message.content)
