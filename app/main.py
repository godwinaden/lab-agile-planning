from fastapi import FastAPI
import uvicorn
import config

settings = config.get_settings()

app = FastAPI(
	title="Counter Machine",
    description="A microservice for counter",
    version="0.1.0",
)


@app.get("/add")
def increment():
    presentCount = settings.counter1
    settings.counter1 = settings.counter1 + 1
    return {"initial": presentCount, "counter": settings.counter1}


@app.get("/add/{by}")
def increment_by(by: int):
    presentCount = settings.counter1
    settings.counter1 = settings.counter1 + by
    return {"initial": presentCount, "counter": settings.counter1}


@app.get("/decrease")
def decrease():
    presentCount = settings.counter1
    settings.counter1 = settings.counter1 - 1
    return {"initial": presentCount, "counter": settings.counter1}


@app.get("/decrease/{by}")
def decrease_by(by: int):
    presentCount = settings.counter1
    settings.counter1 = settings.counter1 - by
    return {"initial": presentCount, "counter": settings.counter1}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
