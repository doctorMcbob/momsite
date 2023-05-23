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

SENDEMAIL = "sherry@herenowpsychotherapycounseling.com"
LOGINEMAIL = "sherry@herenowpsychotherapycounseling.com"
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

def EMDR(request):
    return Response(templates.get_template("emdr.html").render())

def children(request):
    return Response(templates.get_template("childrenandadolescents.html").render())

def somatic(request):
    return Response(templates.get_template("somatictherapies.html").render())

def substance(request):
    return Response(templates.get_template("substanceusedisorders.html").render())

def internalfamily(request):
    return Response(templates.get_template("internalfamily.html").render())

def cognitive(request):
    return Response(templates.get_template("cognitivebehavioral.html").render())

def acceptance(request):
    return Response(templates.get_template("acceptance.html").render())

def gender(request):
    return Response(templates.get_template("sexualityandgender.html").render())

def psychodynamic(request):
    return Response(templates.get_template("psychodynamictherapy.html").render())

def deepbrain(request):
    return Response(templates.get_template("deepbrainreorienting.html").render())

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
        config.add_route("emdr", "/EMDR")
        config.add_view(EMDR, route_name="emdr")
        config.add_route("children", "/childrenandadolescents")
        config.add_view(children, route_name="children")
        config.add_route("somatic", "/somatictherapies")
        config.add_view(somatic, route_name="somatic")
        config.add_route("substance", "/substanceusedisorders")
        config.add_view(substance, route_name="substance")
        config.add_route("internalfamily", "/internalfamilysystems")
        config.add_view(internalfamily, route_name="internalfamily")
        config.add_route("cognitive", "/cognitivebehavioraltherapy")
        config.add_view(cognitive, route_name="cognitive")
        config.add_route("acceptance",
                         "/acceptanceandcommitmenttherapy")
        config.add_view(acceptance, route_name="acceptance")
        config.add_route("gender", "/sexualityandgender")
        config.add_view(gender, route_name="gender")
        config.add_route("psychodynamic", "/psychodynamictherapy")
        config.add_view(psychodynamic, route_name="psychodynamic")
        config.add_route("deepbrain", "/deepbrainreorienting")
        config.add_view(deepbrain, route_name="deepbrain")

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
