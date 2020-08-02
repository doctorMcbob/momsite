"""
This ones for you mom
"""
import waitress
from pyramid.config import Configurator
from pyramid.response import Response

from jinja2 import Environment, PackageLoader, select_autoescape

templates = Environment(
    loader=PackageLoader("momsite", "templates"),
    autoescape=select_autoescape(['html', 'xml'])
)

def debug(request):
    import pdb; pdb.set_trace()
    return main(request)

def main(request):
    return Response(templates.get_template("index.html").render())

if __name__ == """__main__""":
    with Configurator() as config:
        config.add_route("main", "/")
        config.add_view(main, route_name="main")
        config.add_route("debug", "/debug")
        config.add_view(debug, route_name="debug")

        config.add_static_view(name="/static", path="momsite:/static/")
        config.add_static_view(name="/static/css", path="momsite:/static/css/")
        config.add_static_view(name="static/js", path="momsite:/static/js/")

        config.scan()
        app = config.make_wsgi_app()

    waitress.serve(app, port=8000)
