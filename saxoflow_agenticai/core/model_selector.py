import yaml
import os

from saxoflow_agenticai.gateway.groq import GroqGateway
from saxoflow_agenticai.gateway.openrouter import OpenRouterGateway
from saxoflow_agenticai.gateway.together import TogetherGateway
from saxoflow_agenticai.gateway.fireworks import FireworksGateway
from saxoflow_agenticai.gateway.googleaistudio import GoogleAIStudioGateway
from saxoflow_agenticai.gateway.mistral import MistralGateway  # Correct: provider is 'mistral'

_PROVIDER_MAP = {
    "groq": GroqGateway,
    "openrouter": OpenRouterGateway,
    "together": TogetherGateway,
    "fireworks": FireworksGateway,
    "googleaistudio": GoogleAIStudioGateway,
    "mistral": MistralGateway,   # Use 'mistral' as the key
}

class ModelSelector:
    @staticmethod
    def load_config():
        config_path = os.path.join(
            os.path.dirname(__file__), '..', 'config', 'model_config.yaml'
        )
        with open(config_path, 'r') as f:
            return yaml.safe_load(f)

    @classmethod
    def get_model(cls, agent_type=None, provider=None, model_name=None):
        """
        Returns a ModelGateway instance, selecting provider/model by:
        1. Explicit provider/model_name args (overrides all)
        2. Per-agent mapping in config (agent_models)
        3. Provider default in config (providers)
        4. Top-level defaults
        """
        config = cls.load_config()

        # Highest priority: explicitly supplied
        if provider and model_name:
            prov = provider.lower()
            if prov not in _PROVIDER_MAP:
                raise ValueError(f"Unsupported provider: {prov}")
            return _PROVIDER_MAP[prov](model_name=model_name)

        # Next: agent mapping
        agent_entry = config.get("agent_models", {}).get(agent_type, {}) if agent_type else {}
        prov = agent_entry.get("provider")
        modl = agent_entry.get("model")

        # Next: provider-level default
        if not prov:
            prov = config.get("default_provider", "groq")
        prov = prov.lower()

        if not modl:
            modl = config.get("providers", {}).get(prov, {}).get("model")
            # fallback: top-level default_model
            if not modl:
                modl = config.get("default_model")

        if prov not in _PROVIDER_MAP:
            raise ValueError(f"Unsupported provider: {prov}")

        return _PROVIDER_MAP[prov](model_name=modl)

    @classmethod
    def get_provider_and_model(cls, agent_type=None):
        """
        Returns (provider, model_name) for a given agent_type.
        """
        config = cls.load_config()
        agent_entry = config.get("agent_models", {}).get(agent_type, {}) if agent_type else {}
        prov = agent_entry.get("provider")
        modl = agent_entry.get("model")
        if not prov:
            prov = config.get("default_provider", "groq")
        if not modl:
            modl = config.get("providers", {}).get(prov, {}).get("model")
            if not modl:
                modl = config.get("default_model")
        return prov, modl
