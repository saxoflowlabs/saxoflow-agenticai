from saxoflow_agenticai.core.agent_base import BaseAgent
from saxoflow_agenticai.core.log_manager import get_logger

logger = get_logger()

class TBReviewAgent(BaseAgent):
    def __init__(self, verbose=False, log_to_file=None, override_provider=None, override_model=None):
        super().__init__(
            template_name="tbreview_prompt.txt",
            name="Testbench Reviewer",
            description="Reviews SystemVerilog testbench for stimulus quality and coverage.",
            agent_type="tbreview",
            verbose=verbose,
            log_to_file=log_to_file,
            override_provider=override_provider,
            override_model=override_model,
        )

    def run(self, testbench_code: str) -> str:
        """
        Review a SystemVerilog testbench for stimulus quality and coverage.
        """
        prompt = self.render_prompt({"testbench_code": testbench_code})
        logger.debug("[TBReviewAgent] Prepared testbench review prompt.")
        result = self.query_model(prompt)
        logger.info("[TBReviewAgent] Testbench review completed.")
        return result

    def improve(self, testbench_code: str, feedback: str) -> str:
        """
        Re-run the review or escalate based on new feedback.
        """
        logger.info("[TBReviewAgent] Re-running testbench review with feedback context (if any).")
        return self.run(testbench_code)
