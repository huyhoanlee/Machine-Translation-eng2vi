from transformers import pipeline

def inference(text):
    translator = pipeline("translation", model="./translator_model")
    return translator(text)

# print(inference("Hello"))
# text = "i like to play video game online. In evening i usually go outside with my friend to the coffe shop."
# print(inference(text))