import os
import time
from openai import OpenAI
from env.environment import StartupEnv
from env.models import Action

# Initialize client
client = OpenAI(
    base_url=os.getenv("API_BASE_URL"),
    api_key=os.getenv("OPENAI_API_KEY"),
    timeout=30
)

# Model (fallback included)
MODEL = os.getenv("MODEL_NAME", "llama-3.1-8b-instant")

# Initialize environment
env = StartupEnv()

print("[START]")

obs = env.reset()
done = False
total_reward = 0.0
step_id = 0

while not done:

    # 🔥 LLM call (Groq-compatible via OpenAI client)
    response = client.responses.create(
        model=MODEL,
        input=[
            {
                "role": "system",
                "content": "You are an autonomous startup AI managing operations."
            },
            {
                "role": "user",
                "content": str({
                    "emails": [e.content for e in obs.emails],
                    "prs": [p.diff for p in obs.prs],
                    "metrics": obs.metrics.model_dump()
                })
            }
        ]
    )

    # ✅ Correct parsing for responses API
    if hasattr(response, "output_text") and response.output_text:
        response_text = response.output_text
    elif response.output:
        response_text = response.output[0].content[0].text
    else:
        response_text = "default response"

    # Deterministic action pattern
    action_type = "reply_email" if step_id % 2 == 0 else "approve_pr"

    action = Action(
        action_type=action_type,
        target_id="auto",
        content=response_text
    )

    # Step environment
    obs, reward, done, _ = env.step(action)
    time.sleep(2)

    total_reward += reward.score

    print(f"[STEP] step={step_id} reward={reward.score}")

    step_id += 1

print(f"[END] total_reward={total_reward}")