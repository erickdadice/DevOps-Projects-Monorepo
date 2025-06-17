from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "ArgoCD Demo App in Python"}

@app.get("/health")
def health():
    return {"status": "ok"}
