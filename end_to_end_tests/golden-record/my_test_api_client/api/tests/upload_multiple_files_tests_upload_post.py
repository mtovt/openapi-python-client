from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import Client
from ...models import HTTPValidationError
from ...types import File, Response


def _get_kwargs(
    *,
    client: Client,
    multipart_data: List[File],
) -> Dict[str, Any]:
    url = "{}/tests/upload/multiple".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    multipart_multipart_data = []
    for multipart_data_item_data in multipart_data:
        multipart_data_item = multipart_data_item_data.to_tuple()

        multipart_multipart_data.append(multipart_data_item)

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "files": multipart_multipart_data,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, HTTPValidationError]]:
    if response.status_code == 200:
        response_200 = cast(Any, response.json())
        return response_200
    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, HTTPValidationError]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    multipart_data: List[File],
) -> Response[Union[Any, HTTPValidationError]]:
    """Upload multiple files

     Upload several files in the same request

    Args:
        multipart_data (List[File]):

    Returns:
        Response[Union[Any, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        client=client,
        multipart_data=multipart_data,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    multipart_data: List[File],
) -> Optional[Union[Any, HTTPValidationError]]:
    """Upload multiple files

     Upload several files in the same request

    Args:
        multipart_data (List[File]):

    Returns:
        Response[Union[Any, HTTPValidationError]]
    """

    return sync_detailed(
        client=client,
        multipart_data=multipart_data,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    multipart_data: List[File],
) -> Response[Union[Any, HTTPValidationError]]:
    """Upload multiple files

     Upload several files in the same request

    Args:
        multipart_data (List[File]):

    Returns:
        Response[Union[Any, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        client=client,
        multipart_data=multipart_data,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    multipart_data: List[File],
) -> Optional[Union[Any, HTTPValidationError]]:
    """Upload multiple files

     Upload several files in the same request

    Args:
        multipart_data (List[File]):

    Returns:
        Response[Union[Any, HTTPValidationError]]
    """

    return (
        await asyncio_detailed(
            client=client,
            multipart_data=multipart_data,
        )
    ).parsed
