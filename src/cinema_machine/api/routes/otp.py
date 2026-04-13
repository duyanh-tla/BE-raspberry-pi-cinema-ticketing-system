from fastapi import APIRouter, HTTPException
from api.schemas.otp import SendOTPRequest, VerifyOTPRequest, MessageResponse
from services.otpService import create_and_send_otp, verify_otp

router = APIRouter(prefix="/otp", tags=["OTP"])


@router.post("/send", response_model=MessageResponse)
def send_otp(data: SendOTPRequest):
    try:
        create_and_send_otp(data.email)
        return {"message": "OTP sent"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/verify", response_model=MessageResponse)
def verify(data: VerifyOTPRequest):
    success, message = verify_otp(data.email, data.otp)

    if not success:
        raise HTTPException(status_code=400, detail=message)

    return {"message": message}