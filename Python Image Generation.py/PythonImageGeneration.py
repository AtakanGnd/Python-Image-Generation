from openai import OpenAI

client = OpenAI(
  api_key="API-KEY",
)

response =  client.images.generate(
    model="dall-e-3",
    prompt="Ejderhalarla savaşan şövalyelerin resmini yap",
    size="1024x1024",
    n=1,
    response_format="url",
    quality="standard",
    )
    
print(f"Oluşan resmin URL: {response.data[0].url}")
