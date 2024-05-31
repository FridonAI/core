import os
import uuid
from abc import ABC

import requests
from dependency_injector.wiring import Provide

from app.libs.core.utility.base_utility import BaseUtility
from app.schema import ResponseDto
from app.utils.redis import Publisher


class BlockchainUtility(BaseUtility, ABC):
    def __init__(
            self,
            chat_id: str,
            wallet_id: str,
            request_url: str = f"{os.environ['API_URL']}/blockchain/defi-operation",
            pub: Publisher = Provide["publisher"],
            queue_getter=Provide["queue_getter"],
            *args,
            **kwargs,
    ):
        self.chat_id = chat_id
        self.wallet_id = wallet_id
        self.request_url = request_url
        self.pub = pub
        self.queue_getter = queue_getter

    def _generate_tx(self, request):
        resp = requests.post(self.request_url, json=request).json()

        if "statusCode" in resp:
            if 500 > resp["statusCode"] >= 400:
                return resp.get("message", "Something went wrong!")
            if resp["statusCode"] >= 500:
                return "Something went wrong! Please try again later."

        return resp["data"]["serializedTx"]

    async def _send_and_wait(self, tx):
        queue_name = str(uuid.uuid4())

        await self.pub.publish(
            "response_received",
            str(ResponseDto.from_params(
                self.chat_id,
                self.wallet_id,
                None,
                tx,
                queue_name,
                {}))
        )

        print("Waiting for response", queue_name)
        response = await self.queue_getter.get(queue_name=queue_name)
        print("Got Response", response)
        return response
