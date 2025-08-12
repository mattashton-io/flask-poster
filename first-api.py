import flask 
import google 
import google.cloud
import google.cloud.storage
import google.cloud.storage.bucket
import google.cloud.storage.client
import google.genai
import os

#Hello World flask app to test functionality on cloudtop environment
api_app = flask.Flask("hello_world")

#decorator and function
@api_app.route("/")
def hello_router():
    return "Hello World"

#API KEY import
apikey = os.environ["APIKEY"]
print(apikey)
genai_client = google.genai.Client(api_key=apikey)

#decorator and route for genai response
@api_app.route("/gemini")
def gemini_router():
    response = genai_client.models.generate_content(
        model='gemini-2.0-flash-001', contents='generate a greeting based on what Chuck Norris would say in a 90s TV show style')
    return response.text

#decorator and route for post
@api_app.route("/post-hello", methods=['POST'])
def post_router():
    print(flask.request.method)
    print(flask.request.form)
    print(dir(flask.request))
    if flask.request.url == "http://127.0.0.1:5001/post-hello?password=123abc":
        return "success"
    else:
        return "access denied", 401

#decorator and route for post
@api_app.route("/get-greeting", methods=['GET'])
def get_router():
    if flask.request.url == "http://127.0.0.1:5001/get-greeting?password=123abc":
        return "here you go"
    else:
        return "access denied", 401
    
#run the app
if __name__=="__main__":
    api_app.run(debug=True, port=5001)