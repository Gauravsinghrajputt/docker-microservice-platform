from fastapi import FastAPI
import socket

app = FastAPI()

@app.get("/")
def home():
	return{
		"message":"Platform Engineering Demo",
		"hoatname": socket.gethostname()
	}

@app.get("/health")
def health():
	return {"status": "healthy"}
