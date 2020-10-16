import os
# import tensorflow as tf
from flask import Flask

print('=========================================================================')
print(f'flask initialized ... path is {os.path.dirname(os.path.abspath("."))}')
# print(tf.__version__)
print('=========================================================================')
app = Flask(__name__)
print(f'wsgi init : initialized path is {os.path.dirname(os.path.abspath("."))}')
app.run(host='127.0.0.1', port=8080, debug=True)