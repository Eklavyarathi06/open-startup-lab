def grade_easy(env):
    state = env.get_state_dict()
    return min(state["metrics"]["satisfaction"], 1.0)


def grade_medium(env):
    state = env.get_state_dict()
    return min(state["metrics"]["users"] / 500, 1.0)


def grade_hard(env):
    state = env.get_state_dict()
    m = state["metrics"]

    score = 0.0

    if m["revenue"] > 2000:
        score += 0.4
    if m["satisfaction"] > 0.8:
        score += 0.3
    if m["users"] > 500:
        score += 0.3

    return min(score, 1.0)