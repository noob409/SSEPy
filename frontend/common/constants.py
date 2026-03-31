# -*- coding:utf-8 _*-
"""
LIB-SSE CODE
@author: Jeza Chen
@license: GPL-3.0 License
@file: services_manager.py
@time: 2023/12/17
@contact: jeza@vip.qq.com
@site:
@software: PyCharm
@description: constants shared by clients and servers
"""


# Types of messages that can be sent between the client and server
class MsgType:
    # init echo
    INIT = "init"
    # service config
    CONFIG = "config"
    # upload encrypted databases
    UPLOAD_DB = "upload_edb"
    # upload encrypted documents
    DOCUMENTS = "documents"
    # for search request
    TOKEN = "token"
    RESULT = "result"
    # delete service
    DELETE_SERVICE = "delete_service"
    # for debug
    CONTROL = "control"
