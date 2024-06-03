from app.community.plugins.greeter.tools import TOOLS
from app.core.plugins import BasePlugin
from app.core.plugins.registry import ensure_plugin_registry
from app.core.plugins.tools import BaseTool

plugin_registry = ensure_plugin_registry()

@plugin_registry.register("greeter")
class GreeterPlugin(BasePlugin):
    name = "greeter"
    description = "A simple plugin that greets the user"
    tools: type[list[BaseTool]] = TOOLS
