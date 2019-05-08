#!/usr/bin/env python
import os
import sys
import json

from flask import (
    Flask,
    request
)

sys.path.append(os.path.join(os.path.dirname(__file__), os.pardir))

from render import Renderer


app = Flask(__name__)


@app.route('/', methods=['POST'])
def render_document():

    request_data = json.loads(request.data)
    template_name = request_data['template_name']

    CWD = os.getcwd()

    data_path = '{0}/{1}'.format(CWD, 'data.json')
    file = open(data_path, 'r')
    data_string = file.read()
    file.close()
    data = json.loads(data_string)

    renderer = Renderer(template_name, data)
    rendered_html_document = renderer.render_html()
    rendered_pdf_document = renderer.render_pdf(rendered_html_document)

    html_file_path = '{0}/output/{1}'.format(CWD, 'Rendered_{0}.html'.format(template_name))
    html_file = open(html_file_path, 'w')
    html_file.write(rendered_html_document)
    html_file.close()

    pdf_file_path = '{0}/output/{1}'.format(CWD, 'Rendered_{0}.pdf'.format(template_name))
    pdf_file = open(pdf_file_path, 'wb')
    pdf_file.write(rendered_pdf_document)
    pdf_file.close()

    return 'Documents Rendered!'


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
