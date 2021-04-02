import requests
from wsgiref.simple_server import make_server
from urllib.parse import parse_qs
def index():
    response_content = "<h1>Hello!</h1>"
    return [response_content.encode()]

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
        return university_response(environ)

def university_response():
    if "Mathematics" <= 40 and "Latvian_language" <= 40 and "Forign_language" <=40:
        response_content = """
    <p>
    Full_name can not apply to University
    """
    else:
        response_content = """
        <p>
        Full_name can apply to University
        """
    return [response_content()]

def application(environ, start_response):

    status = "200 OK"
    headers = [("Content-type", "text/html")]
    path = environ["PATH_INFO"]

    if path == "/":
        response_content = university_response()
    else:
        response_content = index()
    start_response(status, headers)
    return response_content


HOST = "localhost"
PORT = 8000

with make_server(HOST, PORT, application) as server:
    print(f"Serving at http://{HOST}:{PORT}")
    server.serve_forever()
