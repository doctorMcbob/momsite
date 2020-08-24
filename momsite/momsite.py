"""
This ones for you mom
"""
import waitress
from pyramid.config import Configurator
from pyramid.response import Response

import smtplib
from email.message import EmailMessage

from jinja2 import Environment, PackageLoader, select_autoescape

import os

SENDEMAIL = "wootenwesley@gmail.com"
LOGINEMAIL = "pymessager666@gmail.com"
PASSWORD = os.environ["EMAILPASS"]

templates = Environment(
    loader=PackageLoader("momsite", "templates"),
    autoescape=select_autoescape(['html', 'xml'])
)

def main(request):
    return Response(templates.get_template("index.html").render())

def contact(request):
    return Response(templates.get_template("contact.html").render())

def about(request):
    return Response(templates.get_template("about.html").render())

def services(request):
    return Response(templates.get_template("services.html").render())

def email(request):
    try:
        name = request.POST["name"]
        email = request.POST["email"]
        message = request.POST["message"]
    except KeyError:
        return Response("400 Bad Request")

    mail = EmailMessage()
    mail["To"] = SENDEMAIL
    mail["From"] = email
    mail["Subject"] = "Contact from " + str(name)
    message = "Respond to: " + str(email) + "\n" + message
    mail.set_content(message)

    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.ehlo()
    s.starttls()

    s.login(LOGINEMAIL, PASSWORD)
    
    s.send_message(mail)
    s.quit()
    return Response("200 OK")


if __name__ == """__main__""":
    with Configurator() as config:
        config.add_route("main", "/")
        config.add_view(main, route_name="main")
        config.add_route("contact", "/contact")
        config.add_view(contact, route_name="contact")
        config.add_route("services", "/services")
        config.add_view(services, route_name="services")
        config.add_route("about", "/about")
        config.add_view(about, route_name="about")
        config.add_route("email", "/email")
        config.add_view(email, route_name="email")

        

        config.add_static_view(name="/static", path="momsite:/static/")
        config.add_static_view(name="/static/css", path="momsite:/static/css/")
        config.add_static_view(name="/static/fonts", path="momsite:/static/fonts/")
        config.add_static_view(name="static/js", path="momsite:/static/js/")
        config.add_static_view(name="static/img", path="momsite:/static/img/")

        config.scan()
        app = config.make_wsgi_app()

    waitress.serve(app, port=8000)
