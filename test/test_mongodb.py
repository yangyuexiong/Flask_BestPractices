# -*- coding: utf-8 -*-
# @Time    : 2023/11/12 18:28
# @Author  : yangyuexiong
# @Email   : yang6333yyx@126.com
# @File    : test_mongodb.py
# @Software: PyCharm


from config.config import config_obj


def mg_init(collection_name="test_collection"):
    """init"""

    # Mongodb example
    MG = config_obj['new'].MG
    print(MG)

    # select database
    current_db = MG["test_db"]
    print(current_db)

    # get collection list
    collection_names = current_db.list_collection_names()
    print(collection_names)

    # create collection
    if collection_name not in collection_names:
        current_db.create_collection("test_collection")

    # select collection
    collection = current_db[collection_name]
    print(collection)
    return collection


def test_insert_one(collection):
    """test_insert_one"""

    # insert document
    document_data = {
        "id": 1,
        "username": "yangyuexiong",
        "password": "123456"
    }

    result = collection.insert_one(document_data)

    print(f"Inserted document ID: {result.inserted_id}")


def test_insert_many(collection):
    """test_insert_many"""

    documents = [
        {
            "id": 1,
            "username": "y1",
            "password": "111111"
        },
        {
            "id": 2,
            "username": "y2",
            "password": "222222"
        },
        {
            "id": 3,
            "username": "y3",
            "password": "333333"
        }
    ]

    result = collection.insert_many(documents)
    print(result)


def test_query_all():
    """test_query_all"""

    # query all
    documents = collection.find()

    # remove '_id' field
    # documents = collection.find({}, {"_id": 0})

    documents_list = list(documents)
    for doc in documents_list:
        print(doc)


def test_query_filter():
    """test_query_filter"""

    # filter
    query = {"id": 1}
    specific_document = collection.find_one(query)
    # specific_document = collection.find_one({}, {"_id": 0})
    print("Specific Document:", specific_document)


if __name__ == '__main__':
    collection = mg_init()
    test_insert_one(collection)
    test_insert_many(collection)
    test_query_all()
    test_query_filter()
