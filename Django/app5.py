import google.generativeai as genai

genai.configure(api_key="AIzaSyDvkUlEkTF590PKhNXZ98Gti6MdW1J30Oo")

for model in genai.list_models():
    print(model.name)