from wsgiref.simple_server import make_server


def index():
    response_content = "<h1>Hello!</h1>"
    return [response_content.encode()]


def latin():
    response_content = """
    <p>
    Lorem ipsum dolor sit amet, consectetur adipiscing <br>
    Pellentesque eu euismod diam. Suspendisse blandit sagittis ornare. <br>
    Quisque eu justo ultrices, tincidunt odio non, hendrerit sem. Quisque vel commodo nibh.
    </p>
    """
    return [response_content.encode()]


def application(environ, start_response):

    status = "200 OK"
    headers = [("Content-type", "text/html")]

    path = environ["PATH_INFO"]

    if path == "/latin":
        response_content = latin()
    else:
        response_content = index()

    start_response(status, headers)

    return response_content


HOST = "localhost"
PORT = 8000

with make_server(HOST, PORT, application) as server:
    print(f"Serving at http://{HOST}:{PORT}/")
    server.serve_forever()

def application(environ, start_response):

    status = "200 OK"
    headers = [("Content-type", "text/html")]

    path = environ["PATH_INFO"]

    if path == "/latin":
        response_content = latin()
    else:
        response_content = index()

    start_response(status, headers)

    return response_content


HOST = "localhost"
PORT = 8000

with make_server(HOST, PORT, application) as server:
    print(f"Serving at http://{HOST}:{PORT}/")
    server.serve_forever()