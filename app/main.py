from fastapi import FastAPI

app = FastAPI(title="Oz Demo API")


@app.get("/")
def root():
    return {"message": "Hello from Oz Demo!"}


@app.get("/health")
def health():
    return {"status": "ok"}
