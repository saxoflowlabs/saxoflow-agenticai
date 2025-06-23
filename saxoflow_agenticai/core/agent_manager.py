from saxoflow_agenticai.agents.generators.rtl_gen import RTLGenAgent
from saxoflow_agenticai.agents.generators.tb_gen import TBGenAgent
from saxoflow_agenticai.agents.generators.fprop_gen import FormalPropGenAgent
from saxoflow_agenticai.agents.generators.report_agent import ReportAgent

from saxoflow_agenticai.agents.reviewers.rtl_review import RTLReviewAgent
from saxoflow_agenticai.agents.reviewers.tb_review import TBReviewAgent
from saxoflow_agenticai.agents.reviewers.fprop_review import FormalPropReviewAgent
from saxoflow_agenticai.agents.reviewers.debug_agent import DebugAgent

class AgentManager:
    """
    Returns agent instances by string key.
    Supported keys:
        - "rtlgen", "tbgen", "fpropgen", "report"
        - "rtlreview", "tbreview", "fpropreview", "debug"
    """
    @staticmethod
    def get_agent(agent_name: str, verbose: bool = False, log_to_file: str = None):
        agents = {
            "rtlgen": RTLGenAgent,
            "tbgen": TBGenAgent,
            "fpropgen": FormalPropGenAgent,
            "report": ReportAgent,

            "rtlreview": RTLReviewAgent,
            "tbreview": TBReviewAgent,
            "fpropreview": FormalPropReviewAgent,
            "debug": DebugAgent,
        }
        if agent_name in agents:
            return agents[agent_name](verbose=verbose, log_to_file=log_to_file)
        else:
            raise ValueError(f"Unknown agent: {agent_name}")
