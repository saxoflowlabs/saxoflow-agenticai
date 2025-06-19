from saxoflow_agenticai.core.agent_base import BaseAgent
from saxoflow_agenticai.core.log_manager import get_logger

logger = get_logger()

class TBReviewAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            template_name="tbreview_prompt.txt",
            name="Testbench Reviewer",
            description="Reviews SystemVerilog testbench for stimulus quality and coverage."
        )

    def run(self, testbench_code: str) -> str:
        prompt = self.render_prompt({"testbench_code": testbench_code})
        logger.debug("[TBReviewAgent] Prepared testbench review prompt.")
        result = self.query_model(prompt)
        logger.info("[TBReviewAgent] Testbench review completed.")
        return result
