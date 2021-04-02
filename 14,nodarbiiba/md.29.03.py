from wsgiref.simple_server import make_server
from urllib.parse import parse_qs
import datetime


def index():
    response_content = f'<h3>Hello! Please use <a href="http://{HOST}:{PORT}"> </a></h3>'
    return [response_content.encode()]


def page(environ):
    method = environ["REQUEST_METHOD"]
    if method == "GET":
        response_content = """
        <table>
        <form action="" method="post">
        <tr>
            <th align="left">Title:</th><th align="left"> <input type="text" size=20px name="title" placeholder="Title"></th>
        </tr>
        <tr>
            <th align="left">Content:</th><th align="left"> <input type="text" size=20px name="content" placeholder="Content"></th>
        </tr>
            <tr>
            <th align="left"><input type="submit" value="Submit"></th></tr>
        </form> </table>
        """
        return [response_content.encode()]
    elif method == "POST":
        return result(environ)


def result(environ):
    try:
        length = int(environ["CONTENT_LENGTH"])
    except ValueError:
        length = 0

    wsgi_input = environ["wsgi.input"].read(length).decode()
    form_data = parse_qs(wsgi_input)
    time = datetime.datetime.now()
    response_content = f"""
    <h1>{form_data["title"][0]}</h1>
    <p>Time: {time}</p>
    <p>{form_data["content"][0]}</p>
    """
    return [response_content.encode()]


def application(environ, start_response):

    status = "200 OK"
    headers = [("Content-type", "text/html")]
    path = environ["PATH_INFO"]

    if path == "/":
        response_content = page(environ)
    else:
        response_content = index()
    start_response(status, headers)
    return response_content


HOST = "localhost"
PORT = 8000

with make_server(HOST, PORT, application) as server:
    print(f"Serving at http://{HOST}:{PORT}")
    server.serve_forever()