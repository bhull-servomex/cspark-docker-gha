import os
from flask import Flask, render_template_string

app = Flask(__name__)


@app.route('/')
def index():
  return "Hello world"

@app.route('/bindmount')
def mount():
  directory = '/data'
  html_content = "<html><head><title>Index of {}</title></head><body>".format(directory)
  html_content += "<h1>Index of {}</h1><ul>".format(directory)

  for item in os.listdir(directory):
      item_path = os.path.join(directory, item)
      if os.path.isdir(item_path):
          html_content += '<li><a href="{}/">{}/</a></li>'.format(item, item)
      else:
          html_content += '<li><a href="{}">{}</a></li>'.format(item, item)

  html_content += "</ul></body></html>"
  
  return render_template_string(html_content)
