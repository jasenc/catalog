# Import application.
from catalog import app

if __name__ == '__main__':
    app.secret_key = 'this_is_my_super_secret_development_(not_production)_key'
    app.debug = True
    app.run()
