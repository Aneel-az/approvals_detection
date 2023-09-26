from fastapi import Request, status
from requests import HTTPError
from starlette.responses import JSONResponse

from src.exceptions import Web3ConnectionError


def handle_http_exception(request: Request, e: HTTPError) -> JSONResponse:
    return JSONResponse(
        status_code=e.response.status_code,
        content=e.response.reason
    )


def handle_web3_connection_exception(request: Request, e: Exception) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_502_BAD_GATEWAY,
        content="Failed to connect to the Web3 blockchain"
    )


def handle_exception(request: Request, e: Exception) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content="General Error"
    )


exception_handlers = {
    HTTPError: handle_http_exception,
    Web3ConnectionError: handle_web3_connection_exception,
    Exception: handle_exception
}
