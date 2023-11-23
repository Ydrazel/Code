#-*- code: utf-8 -*-
from werkzeug.wrappers import Response

def application(environ, start_response):
    start_response("200 OK", [("Content-Type", "text/plain")])
    return ["Hello World!"]
