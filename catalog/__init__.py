# Import Flask and initiate application.
from flask import Flask

app = Flask(__name__,  instance_relative_config=True)
app.config.from_object('config')
app.config.from_pyfile('config.py')

# Import Views
import catalog.views  # noqa

# Import models
import catalog.models  # noqa
