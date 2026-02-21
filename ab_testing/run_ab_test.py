from validation.model import LeadAnalysis
import json


def validate(output: str) -> LeadAnalysis:
    return LeadAnalysis.model_validate_json(output)


def compare(a: LeadAnalysis, b: LeadAnalysis) -> dict:
    return {
        "priority_delta": b.business_value.priority_score
        - a.business_value.priority_score,
        "confidence_delta": round(b.confidence - a.confidence, 2),
        "sales_motion_changed": (
            a.recommended_action.sales_motion
            != b.recommended_action.sales_motion
        ),
    }


if __name__ == "__main__":
    with open("results/comparison_example.json") as f:
        print(json.load(f))
