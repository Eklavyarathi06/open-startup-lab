import random

def compute_reward(state, action, memory):

    score = 0
    breakdown = {}

    if action.action_type == "reply_email":
        score += 0.15 + random.uniform(0.05, 0.15)

    if action.action_type == "approve_pr":
        score += 0.2 + random.uniform(0.05, 0.2)

    # memory penalty
    score -= memory.get_penalties()

    # dynamic business logic
    m = state["metrics"]

    if m.satisfaction < 0.5:
        score -= 0.1

    if m.revenue > 1500:
        score += 0.1

    return round(score, 3), breakdown