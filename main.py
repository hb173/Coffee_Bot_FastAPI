from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello Dukes"}

if __name__ == '__main__':
    uvicorn.run(app, port=8080, host='0.0.0.0')
