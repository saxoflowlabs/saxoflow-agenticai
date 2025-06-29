from saxoflow_agenticai.core.agent_base import BaseAgent
from saxoflow_agenticai.core.log_manager import get_logger

logger = get_logger()

class RTLGenAgent(BaseAgent):
    def __init__(self, verbose=False, log_to_file=None, override_provider=None, override_model=None):
        super().__init__(
            template_name="rtlgen_prompt.txt",
            name="RTL Generator",
            description="Generates synthesizable RTL code from a design specification.",
            agent_type="rtlgen",
            verbose=verbose,
            log_to_file=log_to_file,
            override_provider=override_provider,
            override_model=override_model,
        )

    def run(self, spec: str) -> str:
        """
        Generate RTL code from a design specification.
        """
        prompt = self.render_prompt({"spec": spec})
        logger.debug("[RTLGenAgent] Prompt prepared for RTL generation.")
        result = self.query_model(prompt)
        logger.info("[RTLGenAgent] RTL code generated successfully.")
        return result

    def improve(self, spec: str, prev_rtl_code: str, review: str) -> str:
        """
        Use review feedback to improve the existing RTL code.
        Uses rtlgen_improve_prompt.txt as template.
        """
        prompt = self.render_prompt(
            {"spec": spec, "prev_rtl_code": prev_rtl_code, "review": review},
            template_name="rtlgen_improve_prompt.txt"
        )
        logger.debug("[RTLGenAgent] Prompt prepared for RTL improvement with review feedback.")
        result = self.query_model(prompt)
        logger.info("[RTLGenAgent] Improved RTL code generated.")
        return result
