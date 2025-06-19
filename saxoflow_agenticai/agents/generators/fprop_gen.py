from saxoflow_agenticai.core.agent_base import BaseAgent
from saxoflow_agenticai.core.log_manager import get_logger

logger = get_logger()

class FormalPropGenAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            template_name="fpropgen_prompt.txt",
            name="Formal Property Generator",
            description="Generates SystemVerilog Assertions for formal verification of RTL designs."
        )

    def run(self, rtl_code: str) -> str:
        prompt = self.render_prompt({"rtl_code": rtl_code})
        logger.debug("[FormalPropGenAgent] Prompt prepared for formal property generation.")
        result = self.query_model(prompt)
        logger.info("[FormalPropGenAgent] Formal properties generated successfully.")
        return result
