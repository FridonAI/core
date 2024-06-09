from contextvars import ContextVar

from pydantic.v1 import BaseModel

from app.core.crons.base import BaseCron


class CronRegistry(BaseModel):
    crons: list[BaseCron] = []

    def register(self, cron: type[BaseCron]) -> type[BaseCron]:
        print(cron)
        self.crons.append(cron())
        return cron

    def start_crons(self) -> None:
        print(self.crons)
        for cron in self.crons:
            cron.start()

var_cron_registry = ContextVar("cron_registry", default=CronRegistry())

def ensure_cron_registry() -> CronRegistry:
    return var_cron_registry.get()
