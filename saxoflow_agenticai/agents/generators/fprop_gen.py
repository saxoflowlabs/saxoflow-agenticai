from saxoflow_agenticai.core.agent_base import BaseAgent
from saxoflow_agenticai.core.log_manager import get_logger

logger = get_logger()

class FormalPropGenAgent(BaseAgent):
    def __init__(self, verbose=False, log_to_file=None, override_provider=None, override_model=None):
        super().__init__(
            template_name="fpropgen_prompt.txt",
            name="Formal Property Generator",
            description="Generates SystemVerilog Assertions for formal verification of RTL designs.",
            agent_type="fpropgen",
            verbose=verbose,
            log_to_file=log_to_file,
            override_provider=override_provider,
            override_model=override_model,
        )

    def run(self, spec: str, rtl_code: str) -> str:
        """
        Generate SystemVerilog formal properties (SVAs) for the given RTL code and design spec.
        """
        prompt = self.render_prompt({
            "spec": spec,
            "rtl_code": rtl_code,
        })
        logger.debug("[FormalPropGenAgent] Prompt prepared for formal property generation.")
        result = self.query_model(prompt)
        logger.info("[FormalPropGenAgent] Formal properties generated successfully.")
        return result

    def improve(self, spec: str, rtl_code: str, prev_fprops: str, review: str) -> str:
        """
        Use review feedback and previous properties to improve the formal properties.
        Uses fpropgen_improve_prompt.txt as template.
        """
        prompt = self.render_prompt(
            {
                "spec": spec,
                "rtl_code": rtl_code,
                "prev_fprops": prev_fprops,
                "review": review,
            },
            template_name="fpropgen_improve_prompt.txt"
        )
        logger.debug("[FormalPropGenAgent] Prompt prepared for formal property improvement with review feedback.")
        result = self.query_model(prompt)
        logger.info("[FormalPropGenAgent] Improved formal properties generated.")
        return result
