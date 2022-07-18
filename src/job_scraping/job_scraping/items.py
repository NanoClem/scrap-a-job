from typing import Any, Optional

from pydantic import BaseModel


class AWItem(BaseModel):
    Id: int
    JobAdvertEntityId: int
    JobRef: int
    JobTitle: str
    Slug: str
    LeadIn: str
    Location: str
    JobCity: str
    WorkExtent: str
    OrderType: str
    Category: str
    StartingDate: Any
    JobTag: Optional[str]
    Requirements: Any
    CreatedDate: str
    ExtentOfWork: Any
    PublishDate: str
    Saved: bool
    Applied: bool
    NewLogoUrl: str
