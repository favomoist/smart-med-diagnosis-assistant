from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="Smart Medical Diagnosis Assistant API",
    description="Symptom intake, triage, and possible-condition guidance API.",
    version="0.1.0",
)


class SymptomCheckRequest(BaseModel):
    symptoms: list[str]
    age: int | None = None
    sex: str | None = None


class SymptomCheckResponse(BaseModel):
    urgency: str
    possible_conditions: list[str]
    disclaimer: str = (
        "This is not a medical diagnosis. Please consult a licensed "
        "healthcare provider for professional medical advice."
    )


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/api/v1/symptom-check", response_model=SymptomCheckResponse)
def symptom_check(payload: SymptomCheckRequest):
    # Placeholder rule-based logic — to be replaced with the real
    # triage/diagnosis engine.
    urgency = "self-care"
    if "chest pain" in [s.lower() for s in payload.symptoms]:
        urgency = "emergency"

    return SymptomCheckResponse(
        urgency=urgency,
        possible_conditions=["Placeholder condition A", "Placeholder condition B"],
    )
