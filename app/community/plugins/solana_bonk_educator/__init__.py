from app.community.plugins.solana_bonk_educator.tools import TOOLS
from app.core.plugins import BasePlugin
from app.core.plugins.registry import ensure_plugin_registry
from app.core.plugins.tools import BaseTool

plugin_registry = ensure_plugin_registry()

@plugin_registry.register("solana-bonk-educator")
class SolanaBonkEducatorPlugin(BasePlugin):
    name = "Solana Bonk Educator"
    description = "Plugin for solana-bonk education with bonk examples."
    owner = "2snYEzbMckwnv85MW3s2sCaEQ1wtKZv2cj9WhbmDuuRD"
    tools: type[list[BaseTool]] = TOOLS