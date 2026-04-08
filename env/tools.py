def send_email(state, email_id):
    state["metrics"].satisfaction += 0.1
    return "email_sent"

def deploy_code(state):
    state["metrics"].users += 20
    state["metrics"].revenue += 100
    return "deployed"

def schedule_meeting(state):
    state["metrics"].burn_rate += 10
    return "meeting_scheduled"