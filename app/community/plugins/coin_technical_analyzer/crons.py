from app.community.plugins.coin_technical_analyzer.data import ensure_data_store
from app.community.plugins.coin_technical_analyzer.helpers.data import (
    read_token_list,
    read_token_summary_list,
)
from app.community.plugins.coin_technical_analyzer.helpers.llm import (
    generate_token_tags_list,
)
from app.core.crons import BaseCron
from app.core.crons.registry import ensure_cron_registry

registry = ensure_cron_registry()


@registry.register
class CoinTechnicalsCron(BaseCron):
    name = "Coin Technicals"
    schedule = "* */1 * * *"
    token_list_path = "./data/coins-list.json"

    async def _process(self) -> None:
        data_store = ensure_data_store()
        token_list = read_token_list(self.token_list_path)
        token_summary_list = await read_token_summary_list(token_list)
        data_store.update_token_summaries(token_summary_list)
        token_tags_list = await generate_token_tags_list(token_summary_list)
        data_store.update_token_tags(token_tags_list)
