from wsgiref.simple_server import make_server
from urllib.parse import parse_qs

def index():
    response_content = f'<h3>Hello! Please use <a href="http://{HOST}:{PORT}/university"> </a></h3>'
    return [response_content.encode()]

def request_body(environment):
    try:
        request_body_size = int(environment.get('CONTENT_LENGTH',0))
    except ValueError:
        request_body_size = 0
    request_body = environment['wsgi.input'].read(request_body_size)
    return request_body.decode()


def page(environ):
    method = environ["REQUEST_METHOD"]
    if method == "GET":
        response_content = """
        <table>
        <form action="" method="post">
        <tr>
            <th align="left">Full name:</th><th align="left"> <input type="text" size=20px name="title" placeholder="Full name"></th>
        </tr>
        <tr>
            <th align="left">Mathematics:</th><th align="left"> <input type="text" size=20px name="mathematics" placeholder="Mathematics"></th>
        </tr>
          <th align="left">Latvian language:</th><th align="left"> <input type="text" size=20px name="latvian language" placeholder="Latvian language"></th>
         <tr>
            <th align="left">Foreign language:</th><th align="left"> <input type="text" size=20px name="foreign language" placeholder="Foreign language"></th>
        </tr>  
            <tr>
            <th align="left"><input type="submit" value="Submit"></th></tr>
        </form> </table>
        """
        return [response_content.encode()]
    elif method == "POST":
        return result(environ)

def result(request_body):
    if int(input.mathematics) <=40 and int(input.latvian_language) <=40 and \
        (input.foreign_language)<=40:
        return (input.title), "cannot apply for University"
    else:
        return (input.title), "can apply for University"

def application(environ, start_response):

    status = "200 OK"
    headers = [("Content-type", "text/html")]
    path = environ["PATH_INFO"]

    if path == "/university":
        response_content = page(environ)
    else:
        response_content = index()
    start_response(status, headers)
    return response_content
    request_body = read_request_body(environment)

HOST = "localhost"
PORT = 8000

with make_server(HOST, PORT, application) as server:
    print(f"Serving at http://{HOST}:{PORT}/university")
    server.serve_forever()