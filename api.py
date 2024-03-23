from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from inference import inference
app = FastAPI()

@app.get("/")
async def home():
    return "hello" 

@app.get("/translator/{text}")
async def translate(text:str):
    vi = inference(text)
    return vi[0]["translation_text"]

@app.get("/items/")
async def read_items():
    html_content = """
    <html>
        <head>
            <title>Some HTML in here</title>
        </head>
        <body>
            <h1>Look ma! HTML!</h1>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)