import yaml
import os
from saxoflow_agenticai.gateway.openrouter import OpenRouterGateway
from saxoflow_agenticai.gateway.groq import GroqGateway

class ModelSelector:
    @staticmethod
    def load_config():
        config_path = os.path.join(
            os.path.dirname(__file__), '..', 'config', 'model_config.yaml'
        )
        with open(config_path, 'r') as f:
            return yaml.safe_load(f)

    @classmethod
    def get_model(cls):
        config = cls.load_config()
        provider = config.get("default_provider", "").lower()

        if provider == "openrouter":
            model_name = config["openrouter"]["model"]
            return OpenRouterGateway(model_name=model_name)
        elif provider == "groq":
            model_name = config["groq"]["model"]
            return GroqGateway(model_name=model_name)
        else:
            raise ValueError(f"Unsupported provider: {provider}")
