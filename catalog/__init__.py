# Import Flask and initiate application.
from flask import Flask

app = Flask(__name__)

# Import Views
import catalog.views  # noqa

# Import models
import catalog.models  # noqa
