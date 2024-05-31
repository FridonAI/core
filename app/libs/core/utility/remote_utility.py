import json
import os
from abc import ABC

import requests

from app.libs.core.utility.base_utility import BaseUtility


class RemoteUtility(BaseUtility, ABC):
    def __init__(
            self,
            wallet_id: str,
            request_url: str = f"{os.environ['API_URL']}/blockchain/points",
            *args,
            **kwargs,
    ):
        self.wallet_id = wallet_id
        self.request_url = request_url

    def _get_remote_response(self, request):
        response = requests.post(self.request_url, json=request).json()
        if "statusCode" in response:
            if 500 > response["statusCode"] >= 400:
                return response.get("message", "Something went wrong!")
            if response["statusCode"] >= 500:
                return "Something went wrong! Please try again later."
        print("Got Response", response)
        return json.dumps(response['data'])
