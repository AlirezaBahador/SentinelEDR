from fastapi import FastAPI

app = FastAPI()

events = []

@app.get("/")
def home():
    return {"status": "SentinelEDR Server Running"}

@app.post("/event")
def receive_event(event: dict):
    events.append(event)

    print("[EVENT]", event)

    return {"message": "received"}

@app.get("/events")
def get_events():
    return events
