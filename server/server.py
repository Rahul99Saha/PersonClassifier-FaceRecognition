from flask import Flask,request,jsonify
import util

app = Flash(__name__)

if __name__ == "__main__":
    app.run(port=5000)