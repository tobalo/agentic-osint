from pydantic import BaseModel, Field
from datetime import datetime

class IntelligenceReport(BaseModel):
    subject: str = Field(..., description="The subject of the intelligence report")
    bottom_line_up_front: str = Field(
        ..., alias="BLUF", description="The bottom line up front in brevity and to the point"
    )
    analysis: str = Field(..., description="Detailed analysis and findings of the report")
    metadata: dict = Field(
        default_factory=dict, description="Additional metadata associated with the report such as sources, links, etc."
    )
    created_at: datetime = Field(
        default_factory=datetime.utcnow, description="Timestamp when the report was created"
    )
    updated_at: datetime | None = Field(
        None, description="Timestamp when the report was last updated"
    )

class FinancialIntelligenceReport(BaseModel):
    subject: str = Field(..., description="The subject of the financial intelligence report")
    bottom_line_up_front: str = Field(
        ..., alias="BLUF", description="The bottom line up front in brevity and to the point"
    )
    quantitative_elements: dict = Field(
        ..., description="Key quantitative metrics and data points relevant to the report"
    )
    macroeconomics: str = Field(
        ..., description="Macroeconomic factors and context influencing the analysis"
    )
    analysis: str = Field(..., description="Detailed analysis and findings of the financial report")
    guidance: str = Field(
        ..., description="Recommendations and strategic guidance based on the analysis"
    )
    metadata: dict = Field(
        default_factory=dict, description="Additional metadata associated with the report"
    )
    created_at: datetime = Field(
        default_factory=datetime.utcnow, description="Timestamp when the report was created"
    )
    updated_at: datetime | None = Field(
        None, description="Timestamp when the report was last updated"
    )
