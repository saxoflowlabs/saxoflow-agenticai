from saxoflow_agenticai.core.agent_manager import AgentManager
from saxoflow_agenticai.core.log_manager import get_logger

logger = get_logger()

class AgentOrchestrator:

    @staticmethod
    def full_pipeline(spec: str):
        """
        Complete end-to-end generation pipeline:
        RTLGen → TBGen → FormalPropGen → Reviews
        """
        logger.info("[Orchestrator] Starting full pipeline for given spec.")

        # Generation Phase
        logger.debug("[Orchestrator] Invoking RTLGenAgent...")
        rtlgen = AgentManager.get_agent("rtlgen")
        rtl_code = rtlgen.run(spec)
        logger.info("[Orchestrator] RTL generation complete.")

        logger.debug("[Orchestrator] Invoking TBGenAgent...")
        tbgen = AgentManager.get_agent("tbgen")
        testbench_code = tbgen.run(rtl_code)
        logger.info("[Orchestrator] Testbench generation complete.")

        logger.debug("[Orchestrator] Invoking FormalPropGenAgent...")
        fpropgen = AgentManager.get_agent("fpropgen")
        formal_properties = fpropgen.run(rtl_code)
        logger.info("[Orchestrator] Formal property generation complete.")

        # Review Phase
        logger.debug("[Orchestrator] Running RTL review...")
        rtlreview = AgentManager.get_agent("rtlreview")
        rtl_review_report = rtlreview.run(rtl_code)
        logger.info("[Orchestrator] RTL review complete.")

        logger.debug("[Orchestrator] Running TB review...")
        tbrev = AgentManager.get_agent("tb_review")
        tb_review_report = tbrev.run(testbench_code)
        logger.info("[Orchestrator] Testbench review complete.")

        logger.debug("[Orchestrator] Running FormalProp review...")
        fprev = AgentManager.get_agent("fprop_review")
        fprop_review_report = fprev.run(formal_properties)
        logger.info("[Orchestrator] Formal property review complete.")

        results = {
            "rtl_code": rtl_code,
            "testbench_code": testbench_code,
            "formal_properties": formal_properties,
            "rtl_review_report": rtl_review_report,
            "tb_review_report": tb_review_report,
            "fprop_review_report": fprop_review_report
        }

        logger.info("[Orchestrator] Full pipeline completed successfully.")
        return results
