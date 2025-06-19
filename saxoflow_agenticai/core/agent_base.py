from abc import ABC, abstractmethod
from saxoflow_agenticai.core.model_selector import ModelSelector
from saxoflow_agenticai.core.prompt_manager import PromptManager
from saxoflow_agenticai.core.log_manager import get_logger

logger = get_logger()

class BaseAgent(ABC):
    def __init__(self, template_name: str, name: str = None, description: str = None):
        self.name = name or self.__class__.__name__
        self.description = description or "No description provided."
        self.model = ModelSelector.get_model()
        self.prompt_manager = PromptManager()
        self.template_name = template_name

    @abstractmethod
    def run(self, input_data: str) -> str:
        pass

    def render_prompt(self, context: dict) -> str:
        prompt = self.prompt_manager.render(self.template_name, context)
        logger.debug(f"[{self.name}] Prompt rendered using template '{self.template_name}'")
        return prompt

    def query_model(self, prompt: str) -> str:
        logger.info(f"[{self.name}] Querying model with prompt.")
        return self.model.query(prompt)
