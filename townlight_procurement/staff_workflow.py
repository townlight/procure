"""Staff-authored proposals and award records for the desktop suite."""
from typing import Annotated
from uuid import UUID

import sqlalchemy as sa
from pydantic import BaseModel, ConfigDict, Field

from townlight_procurement.persistence import metadata, rfp_draft_records

ShortText = Annotated[str, Field(min_length=1, max_length=255)]
Notes = Annotated[str, Field(max_length=8000)]

proposals = sa.Table(
    "staff_proposals", metadata,
    sa.Column("id", sa.Uuid, primary_key=True),
    sa.Column("solicitation_id", sa.String(36), sa.ForeignKey(rfp_draft_records.c.draft_id), nullable=False),
    sa.Column("vendor_name", sa.String(255), nullable=False),
    sa.Column("summary", sa.Text, nullable=False),
    sa.Column("staff_score", sa.Integer, nullable=False),
    sa.Column("staff_exceptions", sa.Text, nullable=False),
    sa.CheckConstraint("staff_score BETWEEN 0 AND 100", name="staff_proposal_score_range"),
    schema=rfp_draft_records.schema,
)

awards = sa.Table(
    "staff_award_decisions", metadata,
    sa.Column("solicitation_id", sa.String(36), sa.ForeignKey(rfp_draft_records.c.draft_id), primary_key=True),
    sa.Column("proposal_id", sa.Uuid, sa.ForeignKey(proposals.c.id), nullable=False),
    sa.Column("decision_reference", sa.String(255), nullable=False),
    sa.Column("decision_note", sa.Text, nullable=False),
    sa.Column("recorded_by", sa.Uuid, nullable=False),
    sa.Column("recorded_at", sa.DateTime(timezone=True), nullable=False),
    schema=rfp_draft_records.schema,
)


class RfpInput(BaseModel):
    model_config = ConfigDict(extra="forbid", str_strip_whitespace=True)

    title: ShortText
    procurement_type: ShortText
    city_need: Annotated[str, Field(min_length=1, max_length=8000)]


class ProposalInput(BaseModel):
    model_config = ConfigDict(extra="forbid", str_strip_whitespace=True)

    vendor_name: ShortText
    summary: Annotated[str, Field(min_length=1, max_length=8000)]
    staff_score: Annotated[int, Field(ge=0, le=100, strict=True)]
    staff_exceptions: Notes = ""


class AwardInput(BaseModel):
    model_config = ConfigDict(extra="forbid", str_strip_whitespace=True)

    proposal_id: UUID
    decision_reference: ShortText
    decision_note: Annotated[str, Field(min_length=1, max_length=8000)]
