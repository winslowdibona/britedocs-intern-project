import os
from jinja2 import (
    BaseLoader,
    TemplateNotFound
)
from functools import partial


class Loader(BaseLoader):
    """
    A Jinja loader

    See https://github.com/pallets/jinja/blob/master/jinja2/loaders.py
    for complete reference of jinja loaders.
    """

    def get_document(self, template_name, **kwargs):
        file_path = '{0}/templates/{1}.html'.format(os.getcwd(), template_name)
        try:
            file = open(file_path, 'r')
            html = file.read()
            return html
        except IOError as e:
            print('Unable to open template {0}'.format(template_name))
            print(e)
            raise TemplateNotFound(template_name)

    def include_template(self, env, template_name, **kwargs):
        html = self.get_document(template_name, **kwargs)
        rendered = env.from_string(html)
        return_value = rendered.render(var_data=kwargs)
        return return_value

    def get_source(self, environment, template):

        environment.globals.update(include_template=partial(self.include_template, environment))

        html = self.get_document(template)

        return html, template, lambda: True
