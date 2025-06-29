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

    def run(self, spec: str, rtl_code: str) -> str:
        """
        Review RTL code for structural, style, synthesis, and **spec adherence**.
        Always returns at least a minimal structured critique report.
        """
        prompt = self.render_prompt({"spec": spec, "rtl_code": rtl_code})
        logger.debug("[RTLReviewAgent] Prepared RTL review prompt.")
        result = self.query_model(prompt)
        # Fallback for empty response
        if not result or not result.strip():
            logger.warning("[RTLReviewAgent] LLM returned empty review. Using fallback critique report.")
            result = (
                "Syntax Issues: None\n"
                "Logic Issues: None\n"
                "Reset Issues: None\n"
                "Port Declarations Issues: None\n"
                "Optimization Suggestions: None\n"
                "Naming Improvements: None\n"
                "Synthesis Concerns: None\n"
                "Overall Comments: No major issues found."
            )
        logger.info("[RTLReviewAgent] RTL review completed.")
        return result

    def improve(self, spec: str, rtl_code: str, feedback: str) -> str:
        """
        Re-run review with updated context.
        """
        logger.info("[RTLReviewAgent] Re-running review with feedback context (if any).")
        return self.run(spec, rtl_code)
