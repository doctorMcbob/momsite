"""
This ones for you mom
"""
import waitress
from pyramid.config import Configurator
from pyramid.response import Response

import smtplib
from email.message import EmailMessage

from jinja2 import Environment, PackageLoader, select_autoescape

templates = Environment(
    loader=PackageLoader("momsite", "templates"),
    autoescape=select_autoescape(['html', 'xml'])
)

def main(request):
    return Response(templates.get_template("index.html").render())

def contact(request):
    return Response(templates.get_template("contact.html").render())

def email(request):
    try:
        name = request.POST["name"]
        email = request.POST["email"]
        message = request.POST["message"]
    except KeyError:
        return Response("400 Bad Request")
    return Response("200 OK")


if __name__ == """__main__""":
    with Configurator() as config:
        config.add_route("main", "/")
        config.add_view(main, route_name="main")
        config.add_route("contact", "/contact")
        config.add_view(contact, route_name="contact")
        config.add_route("email", "/email")
        config.add_view(email, route_name="email")

        

        config.add_static_view(name="/static", path="momsite:/static/")
        config.add_static_view(name="/static/css", path="momsite:/static/css/")
        config.add_static_view(name="static/js", path="momsite:/static/js/")

        config.scan()
        app = config.make_wsgi_app()

    waitress.serve(app, port=8000)
