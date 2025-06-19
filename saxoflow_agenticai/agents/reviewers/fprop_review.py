from saxoflow_agenticai.core.agent_base import BaseAgent
from saxoflow_agenticai.core.log_manager import get_logger

logger = get_logger()

class FormalPropReviewAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            template_name="fpropreview_prompt.txt",
            name="Formal Property Reviewer",
            description="Reviews SystemVerilog Assertions for coverage, completeness, and corner cases."
        )

    def run(self, prop_code: str) -> str:
        prompt = self.render_prompt({"formal_properties": prop_code})
        logger.debug("[FormalPropReviewAgent] Prepared formal property review prompt.")
        result = self.query_model(prompt)
        logger.info("[FormalPropReviewAgent] Formal property review completed.")
        return result
