from pydantic import BaseModel
from typing import List, Dict, Optional

class ToolCall(BaseModel):
    tool_name: str
    arguments: Dict[str, str]
    
class Email(BaseModel):
    id: str
    content: str
    urgency: int
    sentiment: str

class PR(BaseModel):
    id: str
    diff: str
    has_bug: bool
    security_risk: bool

class Task(BaseModel):
    id: str
    description: str
    priority: int
    completed: bool = False

class Metrics(BaseModel):
    revenue: float
    users: int
    satisfaction: float
    burn_rate: float

class Observation(BaseModel):
    emails: List[Email]
    prs: List[PR]
    tasks: List[Task]
    metrics: Metrics
    memory: List[str]

class Action(BaseModel):
    action_type: str
    target_id: Optional[str]
    content: Optional[str]
    tool: Optional[ToolCall] = None

class Reward(BaseModel):
    score: float
    breakdown: Dict[str, float]

