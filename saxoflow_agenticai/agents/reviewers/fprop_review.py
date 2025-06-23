from saxoflow_agenticai.core.agent_base import BaseAgent
from saxoflow_agenticai.core.log_manager import get_logger

logger = get_logger()

class FormalPropReviewAgent(BaseAgent):
    def __init__(self, verbose=False, log_to_file=None, override_provider=None, override_model=None):
        super().__init__(
            template_name="fpropreview_prompt.txt",
            name="Formal Property Reviewer",
            description="Reviews SystemVerilog Assertions for coverage, completeness, and corner cases.",
            agent_type="fpropreview",
            verbose=verbose,
            log_to_file=log_to_file,
            override_provider=override_provider,
            override_model=override_model,
        )

    def run(self, prop_code: str) -> str:
        """
        Review SystemVerilog formal properties for coverage and completeness.
        """
        prompt = self.render_prompt({"formal_properties": prop_code})
        logger.debug("[FormalPropReviewAgent] Prepared formal property review prompt.")
        result = self.query_model(prompt)
        logger.info("[FormalPropReviewAgent] Formal property review completed.")
        return result

    def improve(self, prop_code: str, feedback: str) -> str:
        """
        Re-run the review or escalate based on new feedback.
        """
        logger.info("[FormalPropReviewAgent] Re-running formal property review with feedback context (if any).")
        return self.run(prop_code)
