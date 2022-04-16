from flask import Flask, jsonify, request
import os
import pandas
import random

app = Flask(
    __name__,
    template_folder='templates',
    static_folder='static'
)
app.url_map.strict_slashes = None



if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=random.randint(2000,9000)
    )
