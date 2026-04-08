import random
from env.models import Email, PR, Task

def generate_email(i):
    samples = [
        ("App crashed!", 3, "angry"),
        ("Refund request", 2, "neutral"),
        ("Love your app!", 1, "happy")
    ]
    c = random.choice(samples)
    return Email(id=f"e{i}", content=c[0], urgency=c[1], sentiment=c[2])

def generate_pr(i):
    return PR(
        id=f"p{i}",
        diff="code changes",
        has_bug=random.choice([True, False]),
        security_risk=random.choice([True, False])
    )

def generate_task(i):
    return Task(
        id=f"t{i}",
        description="Task work",
        priority=random.randint(1, 3)
    )