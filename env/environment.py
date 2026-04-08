import random
from turtle import done
random.seed(42)
from env.models import *
from env.generators import *
from env.reward import compute_reward
from env.memory import Memory
from env.events import generate_event, apply_event
from env.agents import CEOAgent, EngineerAgent, SupportAgent
from env.tools import *

class StartupEnv:

    def __init__(self):
        self.memory = Memory()
        self.ceo = CEOAgent()
        self.engineer = EngineerAgent()
        self.support = SupportAgent()
        self.reset()

    def reset(self):
        self.state_data = self._init_state()
        obs = self.state()
        score, breakdown = compute_reward(self.state_data, None, self.memory)
        reward_obj = Reward(score=score, breakdown=breakdown)
        done = False

        return obs.dict(), reward_obj.dict(), done, {}

    def state(self):
        return Observation(
            emails=self.state_data["emails"],
        prs=self.state_data["prs"],
        metrics=self.state_data["metrics"]
        )

    def step(self, action: Action):
        self.state_data["step"] += 1

        # 🔥 1. APPLY EVENT (UPDATED WITH STEP)
        event = generate_event(self.state_data["step"])
        apply_event(self.state_data, event)

        # 🔥 2. MULTI-AGENT AUTO ACTIONS
        for pr in self.state_data["prs"]:
            decision = self.engineer.review_pr(pr)
            if decision == "approve_pr":
                deploy_code(self.state_data)

        for email in self.state_data["emails"]:
            decision = self.support.handle_email(email)
            if decision == "reply_email":
                send_email(self.state_data, email.id)

        # 🔥 3. TOOL EXECUTION (NEW - ADD HERE)
        if action.tool:
            if action.tool.tool_name == "deploy_code":
                deploy_code(self.state_data)

            elif action.tool.tool_name == "send_email":
                send_email(self.state_data, action.target_id)

            elif action.tool.tool_name == "schedule_meeting":
                schedule_meeting(self.state_data)

        # 🔥 4. APPLY USER ACTION
        self.apply_action(action)

        # 🔥 5. MEMORY UPDATE
        self.memory.add(f"{action.action_type}:{action.target_id}")

        # 🔥 6. REWARD (AFTER EVERYTHING)
        score, breakdown = compute_reward(self.state_data, action, self.memory)

        # 🔥 7. DONE CONDITION
        done = self.state_data["step"] >= 20

        return self.state(), Reward(score=score, breakdown=breakdown), done, {}

    def apply_action(self, action):
        m = self.state_data["metrics"]

        if action.action_type == "reply_email": # pyright: ignore[reportUndefinedVariable]
            m.satisfaction += 0.1

        elif action.action_type == "approve_pr":
            m.users += 15
            m.revenue += 80

        elif action.action_type == "schedule":
            m.burn_rate += 20

        elif action.action_type == "ignore":
            m.satisfaction -= 0.2