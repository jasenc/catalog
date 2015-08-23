# Import database
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Users, Categories, Items

# Connect to database and create session
engine = create_engine('sqlite:///catalogitems.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


def createUser(login_session):
    newUser = Users(name=login_session['username'],
                    email=login_session['email'],
                    picture=login_session['picture'])
    session.add(newUser)
    session.commit()
    user = session.query(Users).filter_by(email=login_session['email']).one()
    return user.id


def getUserInfo(user_id):
    user = session.query(Users).filter_by(id=user_id).one()
    return user


def getUserID(email):
    try:
        user = session.query(Users).filter_by(email=email).one()
        return user.id
    except:
        return None


'''
def category_list():
    return session.query(category).all()


def category_new(new_category):
    # Instantiate a new category object from the information stored in the
    # newcategory object passed through as an arguement.
    newCategory = category(name=new_category["name"],
                           address=new_category["address"],
                           city=new_category["city"],
                           state=new_category["state"],
                           zipCode=new_category["zipCode"],
                           website=new_category["website"])
    session.add(newcategory)
    session.commit()


def category_get(category_id):
    # Return all information for the category that has the id that was passed
    # through as an argument.
    return session.query(category).filter_by(id=category_id).one()


def category_edit(edit_category):
    # Update the edited category in the DB.
    session.add(edit_category)
    session.commit()


def category_delete(delete_category):
    # Delete the category passed as an argument out of the DB.
    session.delete(delete_category)
    session.commit()


def items_get_by_category(category_id):
    # Return all items assigned to the category_id passed as an argument.
    return session.query(item).filter_by(category_id=category_id)


def item_new(category_id, new_item):
    # Instantiate a new item object from the information stored in the
    # newitem object passed through as an arguement.
    newItem = item(name=new_item["name"],
                   gender=new_item["gender"],
                   dateOfBirth=new_item["dateOfBirth"],
                   picture=new_item["picture"],
                   category_id=category_id,
                   weight=new_item["weight"])
    session.add(newitem)
    session.commit()


def item_get(item_id):
    # Return the information for the item that matches the id passed as an
    # argument.
    return session.query(item).filter_by(id=item_id).one()


def item_edit(edit_item):
    # Update the edited item in the DB.
    session.add(edit_item)
    session.commit()


def item_delete(delete_item):
    # Delete the item passed as an argument out of the DB.
    session.delete(delete_item)
    session.commit()
'''
