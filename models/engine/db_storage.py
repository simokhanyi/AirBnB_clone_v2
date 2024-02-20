#!/usr/bin/python3
"""DATABASE engine"""

from os import getenv
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine
from models.base_model import Base
from models.state import State
from models.city import City
from models.user import User
from models.place import Place
from models.review import Review
from models.amenity import Amenity


class DBStorage:
    """Database engine"""

    __engine = None
    __session = None

    def __init__(self):
        """init"""
        user = getenv("HBNB_MYSQL_USER")
        pwd = getenv("HBNB_MYSQL_PWD")
        db = getenv("HBNB_MYSQL_DB")
        host = getenv("HBNB_MYSQL_HOST")
        env = getenv("HBNB_ENV")

        self.__engine = create_engine(
            "mysql+mysqldb://{}:{}@{}/{}".format(user, pwd, host, db),
            pool_pre_ping=True,
        )

        if env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """get all objects"""
        my_dict = {}
        if cls:
            if isinstance(cls, str):
                cls = eval(cls)
            if isinstance(cls, type):
                query = self.__session.query(cls)
                for q in query:
                    key = "{}.{}".format(type(q).__name__, q.id)
                    my_dict[key] = q
        else:
            class_list = [State, City, Place, Amenity, Review, User]
            for c in class_list:
                query = self.__session.query(c)
                for q in query:
                    key = "{}.{}".format(type(q).__name__, q.id)
                    my_dict[key] = q
        return my_dict

    def new(self, obj):
        """add new element"""
        if obj is not None:
            try:
                self.__session.add(obj)
                self.__session.flush()
                self.__session.refresh(obj)
            except Exception as e:
                self.__session.rollback()
                raise e

    def save(self):
        """save changes"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete element"""
        if obj:
            self.__session.query(type(obj)).filter(
                type(obj).id == obj.id
            ).delete()

    def reload(self):
        """reload"""
        Base.metadata.create_all(self.__engine)
        make_session = sessionmaker(
            bind=self.__engine, expire_on_commit=False
        )
        Session = scoped_session(make_session)
        self.__session = Session()

    def close(self):
        """Call remove() method on the private session attribute."""
        self.__session.close()
