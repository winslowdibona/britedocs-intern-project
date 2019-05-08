import os
import sys

from jinja2.sandbox import SandboxedEnvironment
from weasyprint import (
    HTML,
    CSS
)

sys.path.append(os.path.join(os.path.dirname(__file__), os.pardir))

from loader import Loader


class Renderer(object):

    def __init__(self, template_name, data):
        self.env = self._get_default_environment()
        self.template = self.env.get_template(template_name)
        self.data = data

    def _get_default_environment(self):
        return SandboxedEnvironment(extensions=['jinja2.ext.loopcontrols', 'jinja2.ext.do'],
                                    loader=Loader())

    def render_html(self):
        return self.template.render(self.data)

    def render_pdf(self, html):
        weasy = HTML(file_obj=html, encoding='utf-8')
        data = weasy.write_pdf(stylesheets=[CSS(string='')])
        return data
