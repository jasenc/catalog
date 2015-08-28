# Import database
from sqlalchemy import create_engine, desc
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Users, Categories, Items

# Import our database variable.
from config import database

# Connect to database and create session
engine = create_engine("DATABASE_URL")
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


def category_list():
    return session.query(Categories).all()


def category_new(new_category):
    # Instantiate a new category object from the information stored in the
    # newCategory object passed through as an arguement.
    newCategory = Categories(name=new_category["name"],
                             image=new_category["image"],
                             description=new_category["description"],
                             user_id=new_category["user_id"])
    session.add(newCategory)
    session.commit()


def category_get(category_id):
    # Return all information for the category that has the id that was passed
    # through as an argument.
    return session.query(Categories).filter_by(id=category_id).one()


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
    return session.query(Items).filter_by(category_id=category_id)


def items_get_10():
    # Return all items assigned to the category_id passed as an argument.
    return session.query(Items).order_by(desc(Items.id)).limit(10).all()


def item_new(category_id, new_item):
    # Instantiate a new item object from the information stored in the
    # newItem object passed through as an arguement.
    newItem = Items(name=new_item["name"],
                    image=new_item["image"],
                    description=new_item["description"],
                    user_id=new_item["user_id"],
                    category_id=new_item["category_id"])
    session.add(newItem)
    session.commit()


def item_get(item_id):
    # Return the information for the item that matches the id passed as an
    # argument.
    return session.query(Items).filter_by(id=item_id).one()


def item_edit(edit_item):
    # Update the edited item in the DB.
    session.add(edit_item)
    session.commit()


def item_delete(delete_item):
    # Delete the item passed as an argument out of the DB.
    session.delete(delete_item)
    session.commit()
