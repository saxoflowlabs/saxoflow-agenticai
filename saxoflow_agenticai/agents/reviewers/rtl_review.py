from saxoflow_agenticai.core.agent_base import BaseAgent
from saxoflow_agenticai.core.log_manager import get_logger

logger = get_logger()

class RTLReviewAgent(BaseAgent):
    def __init__(self, verbose=False, log_to_file=None, override_provider=None, override_model=None):
        super().__init__(
            template_name="rtlreview_prompt.txt",
            name="RTL Review Agent",
            description="Performs structural and style reviews of RTL code.",
            agent_type="rtlreview",
            verbose=verbose,
            log_to_file=log_to_file,
            override_provider=override_provider,
            override_model=override_model,
        )

    def run(self, rtl_code: str) -> str:
        """
        Review RTL code for structural, style, and synthesizability issues.
        """
        prompt = self.render_prompt({"rtl_code": rtl_code})
        logger.debug("[RTLReviewAgent] Prepared RTL review prompt.")
        result = self.query_model(prompt)
        logger.info("[RTLReviewAgent] RTL review completed.")
        return result

    def improve(self, rtl_code: str, feedback: str) -> str:
        """
        Optionally, suggest improvements based on feedback, or pass for now.
        """
        logger.info("[RTLReviewAgent] Re-running review with feedback context (if any).")
        return self.run(rtl_code)
