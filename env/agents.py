class CEOAgent:
    def decide(self, obs):
        return {"focus": "growth" if obs.metrics.revenue < 1500 else "stability"}

class EngineerAgent:
    def review_pr(self, pr):
        if pr.security_risk:
            return "reject_pr"
        if pr.has_bug:
            return "reject_pr"
        return "approve_pr"

class SupportAgent:
    def handle_email(self, email):
        if email.sentiment == "angry":
            return "reply_email"
        return "ignore"