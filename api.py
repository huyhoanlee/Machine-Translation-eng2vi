from fastapi import FastAPI, Form, Request, HTTPException
from fastapi.responses import HTMLResponse
from inference import inference

app = FastAPI()

@app.get("/")
async def home():
    return "Hello"

# @app.post("/translator/")
# async def translate(text: str):
#     vi = inference(text)
#     return vi

@app.get("/text")
async def receive_text(request: Request):
    try:
        text = await request.body()
        received_text = text.decode("utf-8")
        #print(received_text)
        vi = inference(received_text)
        #print(vi)
        return vi[0]['translation_text']
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing text: {str(e)}")
    

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