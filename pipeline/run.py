from validation.model import LeadAnalysis
import json


def validate_llm_output(raw_json: str) -> LeadAnalysis:
    parsed = json.loads(raw_json)
    return LeadAnalysis.model_validate(parsed)


if __name__ == "__main__":
    with open("../examples/output_example.json") as f:
        raw_output = f.read()

    validated = validate_llm_output(raw_output)
    print("Validated output:", validated)
