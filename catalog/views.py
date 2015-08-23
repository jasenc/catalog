from catalog import app
from catalog import models
from flask import render_template, request, redirect, url_for
from catalog import forms


# Create index page that shows all categories.
@app.route('/')
@app.route('/index/')
@app.route('/category/')
def index():
    categories = 0
    return render_template('index.html', categories=categories)

'''
# Create new category page.
@app.route('/category/new', methods=['GET', 'POST'])
def newcategory():
    # Get the form for categories out of the forms module.
    form = forms.categoryForm(request.form)
    # If the form is submitted via POST and is validated:
    if request.method == 'POST' and form.validate():
        # Create a new category object to store all data from the form.
        new_category = {
            "name": form.name.data,
            "image": form.image.data,
            "description": form.description.data,
            "user_id": ???
        }
        # Pass that object to the DB via the models module.
        models.category_new(new_category)
        # Redirect to the index page.
        return redirect(url_for('index'))
    else:
        # If the route is requested via GET, render the new category page.
        return render_template('categories/new.html', form=form)


# Create edit category page.
@app.route('/category/<int:category_id>/edit', methods=['GET', 'POST'])
def editcategory(category_id):
    # Get the category out of the DB.
    edit_category = models.category_get(category_id)
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
        # If the route is requested via GET, render the edit category page.
        return render_template('categories/edit.html', category=edit_category,
                               form=form)


# Create a delete comfirmation page.
@app.route('/category/<int:category_id>/delete', methods=['GET', 'POST'])
def deletecategory(category_id):
    # Get the category to be deleted out of the DB.
    delete_category = models.category_get(category_id)
    if request.method == 'POST':
        # Delete the category out of the DB.
        models.category_delete(delete_category)
        # Redirect to the index page.
        return redirect(url_for('index'))
    else:
        # If the route is requested via GET, render the delete category page.
        return render_template('categories/delete.html',
                               category=delete_category)


# Create a page for each category.
@app.route('/category/<int:category_id>/')
def showcategory(category_id):
    # Get the selected category from the DB.
    category = models.category_get(category_id)
    # Get the items for that category out of the DB.
    items = models.items_get_by_category(category_id)
    # Show the information on the shetlers show page.
    return render_template('categories/show.html', category=category,
                           items=items)


# The following routes are essentially repeats of the previous ones but with
# more arguments passed around.
# Create a new page for items.
@app.route('/category/<int:category_id>/item/new', methods=['GET', 'POST'])
def newitem(category_id):
    category = models.category_get(category_id)
    items = models.items_get_by_category(category_id)
    form = forms.itemForm(request.form)
    if request.method == 'POST' and form.validate():
        new_item = {
            "name": form.name.data,
            "image": form.image.data,
            "description": form.description.data,
            "user_id": ???
        }
        models.item_new(category_id, new_item)
        return render_template('categories/show.html', category=category,
                               items=items)
    else:
        return render_template('items/new.html', category=category, form=form)


# Create a edit page for items.
@app.route('/category/<int:category_id>/item/<int:item_id>/edit',
           methods=['GET', 'POST'])
def edititem(category_id, item_id):
    category = models.category_get(category_id)
    items = models.items_get_by_category(category_id)
    edit_item = models.item_get(item_id)
    form = forms.itemForm(request.form)
    int_item_weight = int(edit_item.weight)
    if request.method == 'POST' and form.validate():
        edit_item.name = form.name.data
        edit_item.image = form.image.data
        edit_item.description = form.description.data
        models.item_edit(edit_item)
        return render_template('categories/show.html', category=category,
                               items=items, form=form)
    else:
        return render_template('items/edit.html', category=category,
                               item=edit_item, form=form,
                               int_item_weight=int_item_weight)


# Create a delete page for items.
@app.route('/category/<int:category_id>/item/<int:item_id>/delete',
           methods=['GET', 'POST'])
def deleteitem(category_id, item_id):
    delete_item = models.item_get(item_id)
    category = models.category_get(category_id)
    if request.method == 'POST':
        models.item_delete(delete_item)
        return redirect(url_for('showcategory', category_id=category.id))
    else:
        return render_template('items/delete.html', category=category,
                               item=delete_item)


# Create a page for each item.
@app.route('/category/<int:category_id>/item/<int:item_id>/')
def showitem(category_id, item_id):
    category = models.category_get(category_id)
    item = models.item_get(item_id)
    return render_template('items/show.html', category=category,
                           item=item)
'''
