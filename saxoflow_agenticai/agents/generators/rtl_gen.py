from saxoflow_agenticai.core.agent_base import BaseAgent
from saxoflow_agenticai.core.log_manager import get_logger

logger = get_logger()

class RTLGenAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            template_name="rtlgen_prompt.txt",
            name="RTL Generator",
            description="Generates synthesizable RTL code from a design specification."
        )

    def run(self, spec: str) -> str:
        prompt = self.render_prompt({"spec": spec})
        logger.debug("[RTLGenAgent] Prompt prepared for RTL generation.")
        result = self.query_model(prompt)
        logger.info("[RTLGenAgent] RTL code generated successfully.")
        return result
