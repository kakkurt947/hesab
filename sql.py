#  !/usr/bin/env python3
#  -*- coding: utf-8 -*-
#  Name     : broadcast-bot [ Telegram ]
#  Repo     : https://github.com/m4mallu/broadcast-bot
#  Author   : Renjith Mangal [ https://t.me/space4renjith ]
#  Licence  : GPL-3

import os
import threading
from sqlalchemy import create_engine
from sqlalchemy import Column, TEXT, Numeric
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

def start() -> scoped_session:
    engine = create_engine("postgres://visrynupdovxwp:906d6e3f0995150173028f03e64002a4cb14fb0a0308301fa6b23b82fe764621@ec2-3-230-238-86.compute-1.amazonaws.com:5432/d63r3fugndsia5", client_encoding="utf8")
    BASE.metadata.bind = engine
    BASE.metadata.create_all(engine)
    return scoped_session(sessionmaker(bind=engine, autoflush=False))


BASE = declarative_base()
SESSION = start()

INSERTION_LOCK = threading.RLock()

class Broadcast(BASE):
    __tablename__ = "broadcast"
    id = Column(Numeric, primary_key=True)
    user_name = Column(TEXT)

    def __init__(self, id, user_name):
        self.id = id
        self.user_name = user_name

Broadcast.__table__.create(checkfirst=True)


# ------------------------------------ Add user details ----------------------------- #
async def add_user(id, user_name):
    with INSERTION_LOCK:
        msg = SESSION.query(Broadcast).get(id)
        if not msg:
            usr = Broadcast(id, user_name)
            SESSION.add(usr)
            SESSION.commit()
        else:
            pass

async def query_msg():
    try:
        query = SESSION.query(Broadcast.id).order_by(Broadcast.id)
        return query
    finally:
        SESSION.close()
