import string
import enum

from urllib.parse import parse_qsl
from wsgiref.simple_server import make_server

import student


class ErrorCodes(enum.Enum):
    HTTP_200 = '200 OK'


def load_template(name):
    with open(name, 'r') as template:
        source = string.Template(template.read())

    return source


def read_request_body(environment):
    try:
        request_body_size = int(environment.get('CONTENT_LENGTH', 0))

    except ValueError:
        request_body_size = 0

    request_body = environment['wsgi.input'].read(request_body_size)

    return request_body.decode()


def parse_request_body(request_body):
    parsed = parse_qsl(request_body)

    return dict(parsed)


def load_request(environment):
    request_body = read_request_body(environment=environment)
    parsed_body = parse_request_body(request_body=request_body)

    request = Request(
        path=environment['PATH_INFO'],
        data=parsed_body,
    )

    return request


class Request:
    def __init__(self, path, data):
        self.path = path
        self.data = data


class Response:
    def __init__(self, content, status_code=ErrorCodes.HTTP_200):
        self.content = content
        self.status_code = status_code

    def get_response_iter(self):
        yield self.content.encode()

    def __call__(self, start_response):
        headers = [
            ('Content-Type', 'text/html; charset=utf-8'),
        ]

        start_response(self.status_code.value, headers)

        return self.get_response_iter()


class Application:
    def __init__(self, routes):
        self.routes = routes

    def __call__(self, environment, start_response):
        request = load_request(environment=environment)

        response = self.dispatch_request(
            request=request,
        )

        return response(start_response)

    def dispatch_request(self, request):
        handler = self.routes[request.path]

        response = handler(request=request)

        return response


def index(request):
    template = load_template('index.html')

    response = Response(
        content=template.substitute(),
    )

    return response


def say_hello(request):
    name = request.data['name']

    response = Response(
        content=f'Hello, {name}',
    )

    return response


def average(request):
    name = request.data['name']
    grades = request.data['grades'].split(',')
    grades = [int(grade) for grade in grades]

    named_student = student.Student(
        name=name,
        grades=grades,
    )

    student_average = named_student.average()
    content = named_student.generate_report(average=student_average)

    response = Response(content=content)

    return response


routes = {
    '/': index,
    '/say_hello': say_hello,
    '/average': average,
}


SERVER_HOST = '127.0.0.1'
SERVER_PORT = 8000

application = Application(
    routes=routes,
)

with make_server(
        host=SERVER_HOST,
        port=SERVER_PORT,
        app=application,
) as wsgi_server:
    print(f'Starting server on {SERVER_PORT} port.')
    print(f"Serving at http://{SERVER_HOST}:{SERVER_PORT}")

    wsgi_server.serve_forever()