from saxoflow_agenticai.agents.generators.rtl_gen import RTLGenAgent
from saxoflow_agenticai.agents.generators.tb_gen import TBGenAgent
from saxoflow_agenticai.agents.generators.fprop_gen import FormalPropGenAgent

from saxoflow_agenticai.agents.reviewers.rtl_review import RTLReviewAgent
from saxoflow_agenticai.agents.reviewers.tb_review import TBReviewAgent
from saxoflow_agenticai.agents.reviewers.fprop_review import FormalPropReviewAgent

class AgentManager:
    @staticmethod
    def get_agent(agent_name: str):
        agents = {
            "rtlgen": RTLGenAgent,
            "tbgen": TBGenAgent,
            "fpropgen": FormalPropGenAgent,
            "rtlreview": RTLReviewAgent,
            "tb_review": TBReviewAgent,
            "fprop_review": FormalPropReviewAgent,
        }

        if agent_name in agents:
            return agents[agent_name]()
        else:
            raise ValueError(f"Unknown agent: {agent_name}")
