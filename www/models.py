# -*- coding: utf-8 -*-
#!/usr/bin/env python3
#models.py

__author__ = 'lynings'

import time, uuid

from orm import Model, StringField, BooleanField, FloatField, TextField

def next_id():
	return '%015d%s000' % (int(time.time() * 1000), uuid.uuid4().hex)

class User(Model):
	__table__ = 'users'

	id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
	email = StringField(ddl='varchar(50)')
	passwd = StringField(ddl='varchar(50)')
	admin = BooleanField()
	name = StringField(ddl='varcahr(50)')
	image = StringField(ddl='varchat(500)')
	create_time = FloatField(default=time.time)

class Bolg(Model):
	__table__ = 'blogs'

	id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
	blog_id = StringField(ddl='varchar(50)')
	user_id = StringField(ddl='varchar(50)')
	user_name = StringField(ddl='varchar(50)')
	user_image = StringField(ddl='varchar(500)')
	name = StringField(ddl='varchar(50)')
	summary = StringField(ddl='varchar(200)')
	content = TextField()
	create_time = FloatField(default=time.time)

class Comment(Model):
	__table__ = 'comments'

	id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
	blog_id = StringField(ddl='varchar(50)')
	user_id = StringField(ddl='varchar(50)')
	user_name = StringField(ddl='varchar(50)')
	user_image = StringField(ddl='varchar(500)')
	content = TextField()
	create_time = FloatField(default=time.time)



	
