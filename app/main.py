from fastapi import FastAPI
app = FastAPI(title="finance-portfolio-api")

@app.get("/healthz")
def healthz():
    return {"status" : "ok"}