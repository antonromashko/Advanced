# + хотя бы один символ
# ? один или 0 символов [0;1]
# * любое ко-во вхожлений
# [abcd]+ "abc", "bbb", "bab" - OK, "ae" - NO
import re

# my_mail = 'romaha12@gmail.com.com'
# parse_string = re.search(r'(^[a-zA-Z\d.+_]+)@((?:[a-zA-Z\d]+\.){1,2}[a-zA-Z]+.?$)', my_mail)
# print(parse_string.groups())

# from flask import Flask
# from flask import request
#
# app = Flask(__name__)
# host = '1.0.0.1:5000'
# parse_string = re.search(r'((?:[0-255]+.){3}[0-254]+):(\d+$)', host)
# print(bool(parse_string))
#h = 'tap.com:0006'
# parse = re.search(r'^((?:(?:(?:0?(?:\d|[1-9]\d|1\d{2}|2[0-5]{2}|2[0-4]\d))\.){3}'
#                  r'(?:0?(?:\d|[1-9]\d|1\d{2}|2[0-5][0-4]|2[0-4]\d)))'
#                  r'|(?:[a-zA-Z]+(?:\.[a-zA-Z])*)):(\d+)$', h)
# print(bool(parse))
# print(parse)
# if parse is None:
# def host_parser(host):
#    parse = re.search(r'^((?:(?:(?:0?(?:\d|[1-9]\d|1\d{2}|2[0-5]{2}|2[0-4]\d))\.){3}'
#                      r'(?:0?(?:\d|[1-9]\d|1\d{2}|2[0-5][0-4]|2[0-4]\d)))'
#                      r'|(?:[a-zA-Z]+(?:\.(?:[a-zA-Z]*)*)):(\d+)$', host)
#    try:
#        return parse.groups()
#    except AttributeError:
#        return parse
#
# print(host_parser(h))


#from peewee import *
#
#database = SqliteDatabase('test.db')
#
#
#class BaseModel(Model):
#    created = DateField()
#    changed = DateField()
#
#    class Meta:
#        database = database
#
#
#class Vendor(BaseModel):
#    name = CharField()
#
#
#class CarModel(BaseModel):
#    name = CharField()
#    vendor = ForeignKeyField(Vendor)
#
#
#class CarBodyType(BaseModel):
#    name = CharField()
#
#
#class Car(BaseModel):
#    count_wheel = CharField()
#    vin = CharField()
#    issued = DateField()
#    model = ForeignKeyField(CarModel)
#    body_type = ForeignKeyField(CarBodyType)
#    color = CharField()
#database.create_tables([Car, CarModel, Vendor, CarBodyType])




