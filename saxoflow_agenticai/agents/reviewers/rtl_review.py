from saxoflow_agenticai.core.agent_base import BaseAgent
from saxoflow_agenticai.core.log_manager import get_logger

logger = get_logger()

class RTLReviewAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            template_name="rtlreview_prompt.txt",
            name="RTL Review Agent",
            description="Performs structural and style reviews of RTL code."
        )

    def run(self, rtl_code: str) -> str:
        prompt = self.render_prompt({"rtl_code": rtl_code})
        logger.debug("[RTLReviewAgent] Prepared RTL review prompt.")
        result = self.query_model(prompt)
        logger.info("[RTLReviewAgent] RTL review completed.")
        return result
