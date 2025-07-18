from saxoflow_agenticai.core.agent_base import BaseAgent
from saxoflow_agenticai.core.log_manager import get_logger

logger = get_logger()

class TBGenAgent(BaseAgent):
    def __init__(self, verbose=False, log_to_file=None, override_provider=None, override_model=None):
        super().__init__(
            template_name="tbgen_prompt.txt",
            name="Testbench Generator",
            description="Generates SystemVerilog testbench code for the given RTL design.",
            agent_type="tbgen",
            verbose=verbose,
            log_to_file=log_to_file,
            override_provider=override_provider,
            override_model=override_model,
        )

    def run(self, spec: str, rtl_code: str) -> str:
        """
        Generate a SystemVerilog testbench for the given RTL code, using the design spec.
        """
        prompt = self.render_prompt({"spec": spec, "rtl_code": rtl_code})
        logger.debug("[TBGenAgent] Prompt prepared for testbench generation.")
        result = self.query_model(prompt)
        logger.info("[TBGenAgent] Testbench generated successfully.")
        return result

    def improve(self, spec: str, prev_tb_code: str, review: str, rtl_code: str) -> str:
        """
        Use review feedback to improve the testbench code.
        Uses tbgen_improve_prompt.txt as template.
        """
        prompt = self.render_prompt(
            {
                "spec": spec,
                "prev_tb_code": prev_tb_code,
                "review": review,
                "rtl_code": rtl_code,
            },
            template_name="tbgen_improve_prompt.txt"
        )
        logger.debug("[TBGenAgent] Prompt prepared for testbench improvement with review feedback.")
        result = self.query_model(prompt)
        logger.info("[TBGenAgent] Improved testbench generated.")
        return result
