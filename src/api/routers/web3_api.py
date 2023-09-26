from fastapi import APIRouter

from src.models import AddressContext, Approvals
from src.services import Web3Service


router = APIRouter()


@router.post("/approvals_by_address", response_model=Approvals)
async def get_approvals_by_address(body: AddressContext):
    web3_service = Web3Service()
    return web3_service.get_address_approvals(body.address)
