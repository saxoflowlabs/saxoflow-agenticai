from jinja2 import Environment, FileSystemLoader
import os

class PromptManager:
    def __init__(self):
        base_path = os.path.dirname(os.path.dirname(__file__))  # go up from core/ to saxoflow_agenticai/
        template_dir = os.path.join(base_path, 'prompts')       # correct path to prompts/
        self.env = Environment(loader=FileSystemLoader(template_dir))

    def render(self, template_file, context):
        template = self.env.get_template(template_file)
        return template.render(context)
