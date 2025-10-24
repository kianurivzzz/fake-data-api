from pydantic import BaseModel, Field
from typing import Optional, Any, List


class BaseResponse(BaseModel):
    timestamp: float
    datetime: str


class ProfileResponse(BaseResponse):
    profile: dict


class NameResponse(BaseResponse):
    full_name: str
    first_name: str
    last_name: str


class AddressResponse(BaseResponse):
    address: str
    city: Optional[str] = None
    country: Optional[str] = None
    zipcode: Optional[str] = None


class EmailResponse(BaseResponse):
    email: str


class JobResponse(BaseResponse):
    job: str


class TextResponse(BaseResponse):
    text: str


class IPResponse(BaseResponse):
    ipv4_address: str


class MACResponse(BaseResponse):
    mac_address: str


class PhoneResponse(BaseResponse):
    phone_number: str


class CompanyResponse(BaseResponse):
    company: str


class URLResponse(BaseResponse):
    url: str


class CreditCardResponse(BaseResponse):
    provider: str
    number: str
    expire: str
    security_code: str


class UserAgentResponse(BaseResponse):
    user_agent: str


class AllDataResponse(BaseResponse):
    profile: dict
    full_name: str
    first_name: str
    last_name: str
    address: str
    email: str
    job: str
    text: str
    ipv4: str
    mac_address: str
    phone_number: str
    company: str
    url: str


class BatchResponse(BaseModel):
    data: List[Any]
    count: int
    timestamp: float
    datetime: str
