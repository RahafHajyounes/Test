from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello from FastAPI in GitHub repo!"}

@app.get("/ar")
def read_root():
    return {"رسالة": "مرحبا"}

# I will push this code to my branch then make a PR to merge it with main