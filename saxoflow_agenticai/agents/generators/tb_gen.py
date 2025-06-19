from saxoflow_agenticai.core.agent_base import BaseAgent
from saxoflow_agenticai.core.log_manager import get_logger

logger = get_logger()

class TBGenAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            template_name="tbgen_prompt.txt",
            name="Testbench Generator",
            description="Generates SystemVerilog testbench code for the given RTL design."
        )

    def run(self, rtl_code: str) -> str:
        prompt = self.render_prompt({"rtl_code": rtl_code})
        logger.debug("[TBGenAgent] Prompt prepared for testbench generation.")
        result = self.query_model(prompt)
        logger.info("[TBGenAgent] Testbench generated successfully.")
        return result
