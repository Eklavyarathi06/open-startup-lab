import random

def generate_event(step):
    if step % 5 == 0:
        return {"type": "major_crisis", "impact": -0.5}
    return {"type": "normal", "impact": 0}


def apply_event(state, event):

    if event["type"] == "major_crisis":
        state["metrics"].satisfaction -= 0.5
        state["metrics"].revenue -= 300

        # persists in system
        state["crisis"] = True

    if state.get("crisis"):
        state["metrics"].satisfaction -= 0.05  # ongoing damage