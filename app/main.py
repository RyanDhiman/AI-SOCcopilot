from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {
        "message": "AI SOC Copilot Started Successfully!"
    }