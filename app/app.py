from flask import Flask
from prometheus_client import start_http_server, Summary

app = Flask(__name__)

# Define a metric to track request duration
REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')

@app.route("/")
@REQUEST_TIME.time()
def hello():
    return "Hello, Flask Observability Demo!"

if __name__ == "__main__":
    # Start Prometheus metrics server on port 8000
    start_http_server(8000)
    app.run(host="0.0.0.0", port=5000)
