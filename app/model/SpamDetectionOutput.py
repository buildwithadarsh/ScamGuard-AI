from typing import Literal
from pydantic import BaseModel, Field

class SpamDetectionOutput(BaseModel):
    is_scam: bool = Field(description= "its a boolean field, value could only be true or false, based on if a email is detected as spam or not. Spam as true, else false.")
    scam_type: str = Field(description= "its a scam_type field, which should only contain the type of the scam type: OTP Fraud, Loan Scam, Urgency etc")
    risk_level: str = Field(description= "risk level could be: low, medium, high")
    confidence_score: int = Field(description = "This is the confidence score for a email detection as spam. the higher the score the  higher chances of this being a spam.")
    explanation: str = Field(description = "A short description of the email why its spam or not a spam, in simple language")
    