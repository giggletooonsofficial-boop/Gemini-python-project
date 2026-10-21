from typing import List, Optional
from datetime import datetime
from sqlmodel import SQLModel, Field
from pydantic import BaseModel

class MeetingBase(SQLModel):
    objective: str
    status: str = Field(default="pending") # pending, active, completed, failed
    created_at: datetime = Field(default_factory=datetime.utcnow)

class Meeting(MeetingBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

class AgentBase(SQLModel):
    name: str
    role: str
    provider: str
    meeting_id: int = Field(foreign_key="meeting.id")

class Agent(AgentBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

class MessageBase(SQLModel):
    meeting_id: int = Field(foreign_key="meeting.id")
    agent_name: str
    phase: str
    content: str
    timestamp: datetime = Field(default_factory=datetime.utcnow)

class Message(MessageBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

# API Response Models
class MeetingResponse(MeetingBase):
    id: int
    agents: List[AgentBase] = []
    messages: List[MessageBase] = []
