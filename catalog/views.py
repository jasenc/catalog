from catalog import app
from catalog import models
from catalog import forms
from flask import (render_template, request, redirect, url_for,
                   make_response, flash, jsonify)
# To keep track of our user sessions we'll import the session dictionary and
# assign it a local name of login_session.
from flask import session as login_session
# We're going to generate a psuedorandom string to create a unique identifier
# for each user session so we'll need the following imports.
import random
import string
# For the Google+ sign in we'll want to access our oauth2 parameters stored
# in google_client_secrets.json, we can do this by creating a flow object.
from oauth2client.client import flow_from_clientsecrets, FlowExchangeError
# We'll use httplib2 as our HTTP client library.
import httplib2
# And requests as our URL Library.
import requests
# We'll import the JSON encoder and decoder for easy interaction with JSON.
import json


# Load up our app information for the Google+ sign in.
CLIENT_ID = json.loads(
    open('instance/google_client_secrets.json',
         'r').read())['web']['client_id']
APPLICATION_NAME = "Catalog App"


# Create index page that shows all categories.
@app.route('/')
@app.route('/index/')
@app.route('/category/')
def index():
    categories = models.category_list()
    items = models.items_get_10()
    if 'email' in login_session.keys():
        user_id = models.getUserID(login_session['email'])
        user = models.getUserInfo(user_id)
        return render_template('index.html', categories=categories,
                               items=items, user=user)
    else:
        # Create an anti-forgery state token by creatings a unique 32 char
        # string.
        state = ''.join(random.choice(string.ascii_uppercase + string.digits)
                        for x in xrange(32))
        # Save that state token to our login_session object.
        login_session['state'] = state
        # And return the template to log in, while passing along the state
        # string.
        return render_template('public.html', STATE=state,
                               categories=categories, items=items)


# Create new category page.
@app.route('/category/new', methods=['GET', 'POST'])
def newCategory():
    # If the user is logged in:
    if 'email' in login_session.keys():
        # Get the form for categories out of the forms module.
        form = forms.categoryForm(request.form)
        user_id = models.getUserID(login_session['email'])
        user = models.getUserInfo(user_id)
        # If the form is submitted via POST and is validated:
        if request.method == 'POST' and form.validate():
            # Create a new category object to store all data from the form.
            new_category = {
                "name": form.name.data,
                "image": form.image.data,
                "description": form.description.data,
                "user_id": models.getUserID(login_session['email'])
            }
            # Pass that object to the DB via the models module.
            models.category_new(new_category)
            # Redirect to the index page.
            return redirect(url_for('index'))
        else:
            # If the route is requested via GET, render the new category page.
            return render_template('categories/new.html', form=form, user=user)
    else:
        return redirect(url_for('index'))


# Create edit category page.
@app.route('/category/<int:category_id>/edit', methods=['GET', 'POST'])
def editCategory(category_id):
    # Adding logged in user verification to every route here on out.
    if 'email' in login_session.keys():
        # Get the category out of the DB.
        edit_category = models.category_get(category_id)
        # Let's make sure this user is the cateogory owner.
        user_id = models.getUserID(login_session['email'])
        if edit_category.user_id == user_id:
            # Get the form out of the form module.
            form = forms.categoryForm(request.form)
            # If the form is submitted via POST and is validated:
            if request.method == 'POST' and form.validate():
                # Update the category with the form data
                edit_category.name = form.name.data
                edit_category.image = form.image.data
                edit_category.description = form.description.data
                # Send the updated category back to the DB.
                models.category_edit(edit_category)
                # Redirect to the index page.
                return redirect(url_for('index'))
            else:
                # If the route is requested via GET render the edit page.
                user = models.getUserInfo(user_id)
                return render_template('categories/edit.html',
                                       category=edit_category,
                                       form=form, user=user)
        else:
            flash("You aren't the owner for that.")
            return redirect(url_for('index'))
    else:
        return redirect(url_for('index'))


# Create a delete comfirmation page.
@app.route('/category/<int:category_id>/delete', methods=['GET', 'POST'])
def deleteCategory(category_id):
    if 'email' in login_session.keys():
        # Get the category to be deleted out of the DB.
        delete_category = models.category_get(category_id)
        user_id = models.getUserID(login_session['email'])
        if delete_category.user_id == user_id:
            form = forms.deleteForm(request.form)
            if request.method == 'POST':
                # Delete the category out of the DB.
                models.category_delete(delete_category)
                # Redirect to the index page.
                return redirect(url_for('index'))
            else:
                # If the route is requested via GET render the delete page.
                user = models.getUserInfo(user_id)
                return render_template('categories/delete.html',
                                       category=delete_category, user=user,
                                       form=form)
        else:
            flash("You aren't the owner for that.")
            return redirect(url_for('index'))
    else:
        return redirect(url_for('index'))


# Create a page for each category.
@app.route('/category/<int:category_id>/')
def showCategory(category_id):
    # Get the selected category from the DB.
    category = models.category_get(category_id)
    # Get the items for that category out of the DB.
    items = models.items_get_by_category(category_id)
    # Show the information on the shetlers show page.
    if 'email' in login_session.keys():
        user_id = models.getUserID(login_session['email'])
        user = models.getUserInfo(user_id)
        return render_template('categories/show.html', category=category,
                               items=items, user=user)
    else:
        state = ''.join(random.choice(string.ascii_uppercase + string.digits)
                        for x in xrange(32))
        login_session['state'] = state
        return render_template('categories/public.html',
                               category=category, items=items, STATE=state)


# The following routes are essentially repeats of the previous ones but with
# more arguments passed around.
# Create a new page for items.
@app.route('/category/<int:category_id>/item/new', methods=['GET', 'POST'])
def newItem(category_id):
    if 'email' in login_session.keys():
        form = forms.itemForm(request.form)
        user_id = models.getUserID(login_session['email'])
        user = models.getUserInfo(user_id)
        category = models.category_get(category_id)
        if request.method == 'POST' and form.validate():
            new_item = {
                "name": form.name.data,
                "image": form.image.data,
                "description": form.description.data,
                "user_id": models.getUserID(login_session['email']),
                "category_id": category_id
            }
            models.item_new(category_id, new_item)
            items = models.items_get_by_category(category_id)
            return render_template('categories/show.html', category=category,
                                   items=items, user=user)
        else:
            return render_template('items/new.html', category=category,
                                   form=form, user=user)
    else:
        return redirect(url_for('showCategory', category_id=category_id))


# Create a edit page for items.
@app.route('/category/<int:category_id>/item/<int:item_id>/edit',
           methods=['GET', 'POST'])
def editItem(category_id, item_id):
    if 'email' in login_session.keys():
        edit_item = models.item_get(item_id)
        user_id = models.getUserID(login_session['email'])
        if edit_item.user_id == user_id:
            form = forms.itemForm(request.form)
            user = models.getUserInfo(user_id)
            category = models.category_get(category_id)
            if request.method == 'POST' and form.validate():
                edit_item.name = form.name.data
                edit_item.image = form.image.data
                edit_item.description = form.description.data
                models.item_edit(edit_item)
                items = models.items_get_by_category(category_id)
                return render_template('categories/show.html',
                                       category=category,
                                       items=items, user=user)
            else:
                return render_template('items/edit.html', category=category,
                                       item=edit_item, form=form, user=user)
        else:
            flash("You aren't the owner for that.")
            return redirect(url_for('showCategory', category_id=category_id))
    else:
        return redirect(url_for('showCategory', category_id=category_id))


# Create a delete page for items.
@app.route('/category/<int:category_id>/item/<int:item_id>/delete',
           methods=['GET', 'POST'])
def deleteItem(category_id, item_id):
    if 'email' in login_session.keys():
        delete_item = models.item_get(item_id)
        user_id = models.getUserID(login_session['email'])
        if delete_item.user_id == user_id:
            form = forms.deleteForm(request.form)
            category = models.category_get(category_id)
            user = models.getUserInfo(user_id)
            if request.method == 'POST':
                models.item_delete(delete_item)
                return redirect(url_for('showCategory',
                                        category_id=category.id))
            else:
                return render_template('items/delete.html', category=category,
                                       item=delete_item, user=user, form=form)
        else:
            flash("You aren't the owner for that.")
            return redirect(url_for('showCategory', category_id=category_id))
    else:
        return redirect(url_for('showCategory', category_id=category_id))


# Create a page for each item.
@app.route('/category/<int:category_id>/item/<int:item_id>/')
def showItem(category_id, item_id):
    category = models.category_get(category_id)
    item = models.item_get(item_id)
    if 'email' in login_session.keys():
        user_id = models.getUserID(login_session['email'])
        user = models.getUserInfo(user_id)
        return render_template('items/show.html', category=category,
                               item=item, user=user)
    else:
        return render_template('items/public.html',
                               category=category, item=item)


# Create POST route for logging in through Google
@app.route('/gconnect', methods=['POST'])
def gconnect():
    # First we should validate that the state token the server sent to the
    # client matches the state token the client sent to the server.
    # If the state variable returned by the request arguments does not equal
    # the state variable we assigned above:
    if request.args.get('state') != login_session['state']:
        # We'll respond accordingly.
        response = make_response(json.dumps('Invalid state parameter.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    # Otherwise let's grab the authorization code.
    code = request.data

    try:
        # Upgrade the authorization code into a credentials object.
        oauth_flow = (flow_from_clientsecrets
                      ('instance/google_client_secrets.json', scope=''))
        # Somehow the following line of code indicates that this is the
        # one-time-use code the server will be sending off.
        oauth_flow.redirect_uri = 'postmessage'
        # The exchange is initiated.
        credentials = oauth_flow.step2_exchange(code)
    except FlowExchangeError:
        response = make_response(
            json.dumps('Failed to upgrade the authoerization code.'), 401)
        response.headers['Content-Type'] = 'applications/json'
        return response

    # Now that we have the credentials lets verify some things.
    # First that we were provided with a valid access token.
    access_token = credentials.access_token
    # This is the url where we can check the access_token.
    url = ('https://www.googleapis.com/oauth2/v1/tokeninfo?access_token={0}'
           .format(access_token))
    # We'll create an Http() object.
    h = httplib2.Http()
    # We'll store our result in a variable.
    result = json.loads(h.request(url, 'GET')[1])
    print result
    # The only way we know if the access token wasn't valid is if an error
    # is returned.
    if result.get('error') is not None:
        response = make_response(json.dumps(result.get('error')), 500)
        response.headers['Content-Type'] = 'application/json'

    # And we can verify that the access token is being used appropriately.
    gplus_id = credentials.id_token['sub']
    if result['user_id'] != gplus_id:
        response = make_response(
            json.dumps("Token's client ID does not match app's."), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is valid for this app.
    if result['issued_to'] != CLIENT_ID:
        response = make_response(
            json.dumps("Token's client ID does not match app's."), 401)
        print "Token's client ID does not match app's."
        response.headers['Content-Type'] = 'application/json'
        return response

    # And let's make sure the user isn't already logged in.
    stored_credentials = login_session.get('credentials')
    stored_gplus_id = login_session.get('gplus_id')
    if stored_credentials is not None and gplus_id == stored_gplus_id:
        response = make_response(json.dumps('Current user is already \
                                 connected.'), 200)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Store the access token in the session for later use.
    login_session['credentials'] = credentials.access_token
    print login_session['credentials']
    login_session['gplus_id'] = gplus_id

    # Get the user's info
    userinfo_url = "https://www.googleapis.com/oauth2/v1/userinfo"
    params = {'access_token': credentials.access_token, 'alt': 'json'}
    answer = requests.get(userinfo_url, params=params)

    data = answer.json()

    login_session['username'] = data['name']
    login_session['picture'] = data['picture']
    login_session['email'] = data['email']
    # Let's add how the user signed in.
    login_session['provider'] = 'google'

    # We can check if the user is in our database, and if not add them.
    user_id = models.getUserID(data["email"])
    if not user_id:
        user_id = models.createUser(login_session)
    login_session['user_id'] = user_id

    output = "SUCCESS!"

    return output


@app.route('/gdisconnect')
def gdisconnect():
    # Only disconnect a connected user.
    credentials = login_session.get('credentials')
    if credentials is None:
        response = make_response(
            json.dumps('Current user not connected.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    access_token = credentials
    url = ('https://accounts.google.com/o/oauth2/revoke?token={0}'
           .format(access_token))
    h = httplib2.Http()
    result = h.request(url, 'GET')[0]
    if result['status'] == '200':
        # Reset the user's session.
        del login_session['credentials']
        del login_session['gplus_id']
        del login_session['username']
        del login_session['email']
        del login_session['picture']

        response = make_response(json.dumps('Successfully disconnected.'), 200)
        response.headers['Content-Type'] = 'application/json'
        flash("Can't believe you're leaving me, again...")
        return redirect(url_for('index'))
    else:
        # For whatever reason, the given token was invalid.
        response = make_response(
            json.dumps('Failed to revoke token for given user.', 400))
        response.headers['Content-Type'] = 'application/json'
        flash("Log out unsuccessful!")
        return redirect(url_for('index'))


# Making API Endpoints
@app.route('/category/<int:category_id>/JSON')
def categoryJSON(category_id):
    # Get the selected category from the DB.
    category = models.category_get(category_id)
    # Get the items for that category out of the DB.
    items = models.items_get_by_category(category_id)
    return jsonify(CatalogItems=[i.serialize for i in items])


@app.route('/category/<int:category_id>/item/<int:item_id>/JSON')
def itemJSON(category_id, item_id):
    category = models.category_get(category_id)
    item = models.item_get(item_id)
    return jsonify(CatalogItems=[item.serialize])
