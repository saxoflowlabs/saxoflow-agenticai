from saxoflow_agenticai.core.agent_base import BaseAgent
from saxoflow_agenticai.core.log_manager import get_logger

logger = get_logger()

class TBReviewAgent(BaseAgent):
    def __init__(self, verbose=False, log_to_file=None, override_provider=None, override_model=None):
        super().__init__(
            template_name="tbreview_prompt.txt",
            name="Testbench Reviewer",
            description="Reviews SystemVerilog testbench for stimulus quality, coverage, and DUT instantiation.",
            agent_type="tbreview",
            verbose=verbose,
            log_to_file=log_to_file,
            override_provider=override_provider,
            override_model=override_model,
        )

    def run(self, spec: str, rtl_code: str, testbench_code: str) -> str:
        """
        Review a SystemVerilog testbench for stimulus quality, coverage, and correct RTL instantiation, using spec and RTL code as reference.
        """
        prompt = self.render_prompt({
            "spec": spec,
            "rtl_code": rtl_code,
            "testbench_code": testbench_code
        })
        logger.debug("[TBReviewAgent] Prepared testbench review prompt.")
        result = self.query_model(prompt)
        logger.info("[TBReviewAgent] Testbench review completed.")
        return result

    def improve(self, spec: str, rtl_code: str, testbench_code: str, feedback: str) -> str:
        """
        Optionally re-run the review or escalate based on new feedback, with full context.
        """
        logger.info("[TBReviewAgent] Re-running testbench review with feedback context (if any).")
        return self.run(spec, rtl_code, testbench_code)
