from fastapi import APIRouter, HTTPException
from src.database import MeetDocument  # updated name
from src.schemas.space_name import MeetDocumentSpaceNameUpdate

router = APIRouter()

@router.get("/document/{meet_key}/space_name", response_model=str, tags=["Space"])
def get_space_name(meet_key: str):
    document = MeetDocument.objects(meet_key=meet_key).first()
    if not document:
        raise HTTPException(status_code=404, detail="MeetDocument not found")
    return document.space_name


@router.put("/document/{meet_key}/space_name", response_model=str, tags=["Space"])
def update_space_name(meet_key: str, update: MeetDocumentSpaceNameUpdate):
    document = MeetDocument.objects(meet_key=meet_key).first()
    if not document:
        raise HTTPException(status_code=404, detail="MeetDocument not found")
    document.space_name = update.space_name
    document.save()
    return "Success"
