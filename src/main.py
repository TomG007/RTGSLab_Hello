
import functions_framework

from markupsafe import escape
@functions_framework.http
def hello_http(request):
    """
    HTTP Cloud Function.

    Args:
        request (flask.Request): The request object.
        <https://flask.palletsprojects.com/en/1.1.x/api/#incoming-request-data>
    Returns:
        The response text, or any set of values that can be turned into a
        Response object using `make_response`
        <https://flask.palletsprojects.com/en/1.1.x/api/#flask.make_response>.
        
    Deploy CLI:
        gcloud functions deploy python-http-function \
            --gen2 \
            --runtime=python312 \
            --region=us-central1 \
            --source=. \
            --entry-point=hello_http \
            --trigger-http \
            --allow-unauthenticated
            
    Run examples:
        https://python-http-function-kx7s34om7q-uc.a.run.app
        https://python-http-function-kx7s34om7q-uc.a.run.app/?name=Bryan%20Runck

        curl -X GET https://python-http-function-kx7s34om7q-uc.a.run.app -H 'Content-Type: application/json'
        
        curl -X POST https://python-http-function-kx7s34om7q-uc.a.run.app -H 'Content-Type: application/json'
        curl -X POST https://python-http-function-kx7s34om7q-uc.a.run.app -H 'Content-Type: application/json' -d '{"name":"Bryan Runck"}'
    
    """
    request_json = request.get_json(silent=True)
    request_args = request.args

    if request_json and "name" in request_json:
        name = request_json["name"]
    elif request_args and "name" in request_args:
        name = request_args["name"]
    else:
        name = "World"
    return f"Hello {escape(name)}! Have a great day!"

