from pydantic import BaseModel


class AddressContext(BaseModel):
    address: str
