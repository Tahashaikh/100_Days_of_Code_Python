import json
import os
from flask import Flask, request

app = Flask(__name__)

def load_stubs(directory):
    stubs = []
    for filename in os.listdir(directory):
        if filename.endswith(".json"):
            with open(os.path.join(directory, filename)) as f:
                stubs.extend(json.load(f))
    return stubs

@app.route("/stub/<path:path>", methods=["GET"])
def stub_handler(path):
    stubs = load_stubs("D:\WireMock\mappings")
    for stub in stubs:
        if stub["request"]["url"] == request.path and stub["request"]["method"] == request.method:
            if "body" in stub["request"].keys() and request.data.decode("utf-8") != stub["request"]["body"]:
                continue
            return (stub["response"]["body"], stub["response"]["status"], stub["response"]["headers"])
    return "No matching stub found", 404

if __name__ == "__main__":
    stubs = load_stubs("D:\WireMock\mappings")
    for stub in stubs:
       print(stub)
  #  app.run(debug=True, host="0.0.0.0", port=8080)