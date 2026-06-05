# backend/schemas.py

from pydantic import BaseModel, Field
from typing import List, Optional

class SkillsRecommendationRequest(BaseModel):
    skills: List[str] = Field(..., description="List of user's skills for job matching")
    experience_level: str = Field("Mid", description="Seniority level: 'Junior', 'Mid', or 'Senior'")

class JobCreateRequest(BaseModel):
    title: str = Field(..., example="Senior Data Engineer")
    company: str = Field(..., example="Fintech Corp")
    location: str = Field(..., example="Remote (US)")
    department: str = Field(..., example="Data Engineering")
    salary_range: str = Field(..., example="$130,000 - $160,000")
    experience_level: str = Field("Mid", example="Mid")
    description: str = Field(..., example="Build and scale database infrastructure...")
    required_skills: List[str] = Field(..., example=["Python", "SQL", "Docker", "AWS"])
