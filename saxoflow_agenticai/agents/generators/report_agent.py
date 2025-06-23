from saxoflow_agenticai.core.agent_base import BaseAgent
from saxoflow_agenticai.core.log_manager import get_logger

logger = get_logger()

class ReportAgent(BaseAgent):
    def __init__(self, verbose=False, log_to_file=None, override_provider=None, override_model=None):
        super().__init__(
            template_name="report_prompt.txt",
            name="Report Agent",
            description="Summarizes the actions and outputs of all agents during the development flow.",
            agent_type="report",  # Key for model_config.yaml, typically mapped to mistral
            verbose=verbose,
            log_to_file=log_to_file,
            override_provider=override_provider,
            override_model=override_model,
        )

    def run(self, phase_outputs: dict) -> str:
        """
        Summarize the outputs of all agents/phases for reporting.
        phase_outputs: dict mapping phase names to agent outputs (e.g., {'rtlgen': ..., 'tbgen': ..., ...})
        """
        # Flatten the dict for prompt rendering
        prompt_context = {"phases": phase_outputs}
        prompt = self.render_prompt(prompt_context)
        logger.debug("[ReportAgent] Prepared report summary prompt.")
        result = self.query_model(prompt)
        logger.info("[ReportAgent] Final pipeline summary generated.")
        return result

    def improve(self, phase_outputs: dict, feedback: str) -> str:
        """
        Use feedback to refine the phase summary.
        """
        prompt_context = {
            "phases": phase_outputs,
            "review": feedback
        }
        prompt = self.render_prompt(prompt_context)
        logger.debug("[ReportAgent] Prepared report improvement prompt with feedback.")
        result = self.query_model(prompt)
        logger.info("[ReportAgent] Improved report summary generated.")
        return result
