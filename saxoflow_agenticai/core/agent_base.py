import click
from abc import ABC, abstractmethod
from saxoflow_agenticai.core.model_selector import ModelSelector
from saxoflow_agenticai.core.prompt_manager import PromptManager
from saxoflow_agenticai.core.log_manager import get_logger

logger = get_logger()

class BaseAgent(ABC):
    # Class-level color mapping for log types
    _LOG_COLORS = {
        "PROMPT SENT TO LLM": "blue",
        "LLM RESPONSE": "magenta",
        "REVIEW FEEDBACK": "yellow",
        "INFO": "green",
        "WARNING": "red"
    }

    def __init__(
        self,
        template_name: str,
        name: str = None,
        description: str = None,
        agent_type: str = None,
        verbose: bool = False,
        log_to_file: str = None,
        override_provider: str = None,
        override_model: str = None,
    ):
        """
        agent_type: Used for model selection. Defaults to self.__class__.__name__.lower()
        override_provider / override_model: (Advanced) Override config per instantiation.
        """
        self.name = name or self.__class__.__name__
        self.description = description or "No description provided."
        self.agent_type = agent_type or self.name.lower()
        self.verbose = verbose
        self.log_to_file = log_to_file

        # Select model using agent_type + config (or explicit override)
        self.model = ModelSelector.get_model(
            agent_type=self.agent_type,
            provider=override_provider,
            model_name=override_model
        )

        self.prompt_manager = PromptManager()
        self.template_name = template_name

        # Banner in log file at session start
        if self.log_to_file:
            with open(self.log_to_file, 'a') as f:
                import datetime
                f.write(f"\n\n========== NEW SESSION: {datetime.datetime.now()} ({self.name}) ==========\n")
        # Log the model/provider used
        provider, model = ModelSelector.get_provider_and_model(self.agent_type)
        logger.info(f"[{self.name}] Using LLM provider={provider}, model={model}")
        if self.verbose:
            click.secho(f"\n[{self.name}] Using LLM provider: {provider}, model: {model}\n", fg="green", bold=True)
            if self.log_to_file:
                with open(self.log_to_file, 'a') as f:
                    f.write(f"[{self.name}] Using LLM provider: {provider}, model: {model}\n")

    @abstractmethod
    def run(self, input_data: str) -> str:
        pass

    def improve(self, input_data: str, feedback: str) -> str:
        raise NotImplementedError(f"{self.name} has no improve() implemented.")

    def _log_block(self, title: str, content: str):
        color = self._LOG_COLORS.get(title, "white")
        header = f"\n========== [{self.name} | {title}] =========="
        footer = "\n" + "="*len(header)
        block = f"{header}\n{content.strip()}{footer}\n"
        # Colorful terminal output
        click.secho(header, fg=color, bold=True)
        click.secho(content.strip(), fg=color)
        click.secho(footer + "\n", fg=color)
        # Also export to log file if enabled
        if self.log_to_file:
            with open(self.log_to_file, 'a') as f:
                f.write(block)
                f.flush()

    def render_prompt(self, context: dict) -> str:
        prompt = self.prompt_manager.render(self.template_name, context)
        logger.debug(f"[{self.name}] Prompt rendered using template '{self.template_name}'")
        if self.verbose:
            self._log_block("PROMPT SENT TO LLM", prompt)
        return prompt

    def query_model(self, prompt: str) -> str:
        logger.info(f"[{self.name}] Querying model with prompt.")
        result = self.model.query(prompt)
        if self.verbose:
            self._log_block("LLM RESPONSE", result)
        return result
