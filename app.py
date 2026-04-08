from fastapi import FastAPI
from env.environment import StartupEnv
from env.models import Action

app = FastAPI()

env = StartupEnv()

@app.post("/reset")
def reset():
    obs = env.reset()
    return obs.dict()

@app.post("/step")
def step(action: dict):
    action_obj = Action(**action)
    obs, reward, done, _ = env.step(action_obj)

    return {
        "obs": obs.dict(),
        "reward": reward.score,
        "done": done
    }

@app.get("/state")
def state():
    return env.get_state_dict()