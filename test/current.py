__author__ = 'root'

from hello import app
from flask import current_app

app_ctx = app.app_context()
app_ctx.push()
print current_app.name
print app.url_map
app_ctx.pop()
