import logging
from fastapi import FastAPI, HTTPException, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
import uuid
from .models import Receipt
from .logic.points import calc_points

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)

app = FastAPI()

receipts: dict[str, int] = {}

# override the RequestValidationError so it can raise 400 
@app.exception_handler(RequestValidationError)
def validation_exception_handler(request: Request, exc: RequestValidationError):
        logger.info(exc.errors())
        return JSONResponse(
            status_code=400,
            content={"detail": "The receipt is invalid."}
        )

@app.post("/receipts/process")
def process_receipt(receipt: Receipt):
    receipt_id = str(uuid.uuid4())
    try:
        receipts[receipt_id] = calc_points(receipt)
    except Exception:
        raise HTTPException(status_code=400, detail="The receipt is invalid.")
    return {"id": receipt_id}

@app.get("/receipts/{receipt_id}/points")
def get_receipt_points(receipt_id: str):
    if receipt_id in receipts:
        return {"points": receipts[receipt_id]}
    raise HTTPException(status_code=404, detail="No receipt found for that ID.")
