from app.libs.core.utility.blockchain_utility import BlockchainUtility
from app.libs.core.utility.remote_utility import RemoteUtility

class KaminoBorrowLendUtility(BlockchainUtility):
    def __init__(*args, **kwargs):
        super().__init__(*args, **kwargs)

    async def __call__(
            self,
            operation: str,
            currency: str,
            amount: float,
    ):
        request = {
            "plugin": "kamino",
            "function": "borrowlend",
            "args": {
                "walletAddress": self.wallet_id,
                "operation": operation,
                "currency": currency,
                "amount": amount,
            }
        }

        tx = self._generate_tx(request)
        return await self._send_and_wait(tx)


class KaminoBalanceUtility(RemoteUtility):
    def __init__(*args, **kwargs):
        super().__init__(*args, **kwargs)

    async def __call__(self, currency: str):
        request = {
            "plugin": "kamino",
            "function": "balance",
            "walletAddress": self.wallet_id,
        }

        return self._get_remote_response(request)



