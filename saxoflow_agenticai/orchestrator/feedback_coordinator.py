class AgentFeedbackCoordinator:
    @staticmethod
    def iterate_improvements(agent, initial_input, feedback_agent, max_iters=1):
        """
        agent: generator agent (e.g., RTLGenAgent)
        initial_input: main input for the generator (e.g., spec or rtl_code)
        feedback_agent: corresponding reviewer agent
        max_iters: maximum refinement cycles
        """
        output = agent.run(initial_input)
        for i in range(max_iters):
            feedback = feedback_agent.run(output).strip()
            # Heuristic: stop if feedback shows "no issues"
            lower_feedback = feedback.lower()
            if any(
                key in lower_feedback
                for key in [
                    "no major issue", "no issues found",
                    "no issues detected", "no issue", "no issues identified"
                ]
            ):
                break
            output = agent.improve(initial_input, feedback)
        return output, feedback
