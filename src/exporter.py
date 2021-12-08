import os
from typing import List, Optional, Dict, Any

from jinja2 import Template

from models import Scientist


class TableExporter:

    @classmethod
    def render(cls, objects: List[Scientist]):
        root_dir = os.path.dirname(os.path.realpath(__file__))
        resources_dir = os.path.join(root_dir, "resources")
        filepath = os.path.join(resources_dir, "export_template.html")

        with open(filepath) as f:
            template = Template(f.read())
        rendered = template.render(scientists=objects)

        return rendered

    @classmethod
    def export(cls, objects: List[Scientist], output_filepath: str) -> str:
        html = cls.render(objects)
        with open(output_filepath, "w+") as f:
            f.write(html)
        return html
