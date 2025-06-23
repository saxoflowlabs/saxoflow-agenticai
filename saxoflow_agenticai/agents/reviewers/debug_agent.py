from saxoflow_agenticai.core.agent_base import BaseAgent
from saxoflow_agenticai.core.log_manager import get_logger

logger = get_logger()

class DebugAgent(BaseAgent):
    def __init__(self, verbose=False, log_to_file=None, override_provider=None, override_model=None):
        super().__init__(
            template_name="debug_prompt.txt",
            name="Debug Agent",
            description="Analyzes RTL/testbench code or simulation output and provides debugging suggestions.",
            agent_type="debug",  # Use 'debug' as key in your model config
            verbose=verbose,
            log_to_file=log_to_file,
            override_provider=override_provider,
            override_model=override_model,
        )

    def run(self, debug_input: str) -> str:
        """
        Analyze debug input (code, log, error, or simulation output) and provide debugging advice.
        """
        prompt = self.render_prompt({"debug_input": debug_input})
        logger.debug("[DebugAgent] Prepared debug prompt.")
        result = self.query_model(prompt)
        logger.info("[DebugAgent] Debugging output generated.")
        return result

    def improve(self, debug_input: str, feedback: str) -> str:
        """
        Use feedback to refine the debugging advice.
        """
        prompt = self.render_prompt({
            "debug_input": debug_input,
            "review": feedback
        })
        logger.debug("[DebugAgent] Prepared debug improvement prompt with feedback.")
        result = self.query_model(prompt)
        logger.info("[DebugAgent] Improved debugging output generated.")
        return result
