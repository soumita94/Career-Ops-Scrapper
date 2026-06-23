import asyncio

from services.sync_service import (
    sync_company
)


async def main():

    result = await sync_company(
        "https://www.airswift.com/"
    )

    print(result)


asyncio.run(main())