from pydantic import BaseModel, Field
from typing import Optional, Literal


class Intent(BaseModel):
    primary_goal: str
    urgency_level: Literal["low", "medium", "high"]
    decision_stage: Literal["awareness", "consideration", "decision"]


class BusinessValue(BaseModel):
    estimated_deal_size_usd: Optional[float]
    potential_ltv_usd: Optional[float]
    priority_score: int = Field(ge=1, le=10)


class RiskFactors(BaseModel):
    budget_risk: Literal["low", "medium", "high", "unknown"]
    churn_risk: Literal["low", "medium", "high", "unknown"]
    complexity_risk: Literal["low", "medium", "high", "unknown"]


class RecommendedAction(BaseModel):
    sales_motion: Literal[
        "self_service", "sales_assisted", "enterprise_sales", "reject"
    ]
    next_step: str
    recommended_owner: Literal["sales", "support", "marketing", "automation"]


class LeadAnalysis(BaseModel):
    lead_type: Literal["enterprise", "smb", "startup", "individual", "unknown"]
    intent: Intent
    business_value: BusinessValue
    risk_factors: RiskFactors
    recommended_action: RecommendedAction
    confidence: float = Field(ge=0.0, le=1.0)
