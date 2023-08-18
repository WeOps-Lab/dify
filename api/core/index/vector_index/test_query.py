import base64
import binascii
import hashlib
import math
import secrets
from os import environ

import numpy as np
import qdrant_client
from langchain.embeddings import MiniMaxEmbeddings, OpenAIEmbeddings
from langchain.vectorstores import Milvus
from numpy import average

from core.index.vector_index.qdrant import Qdrant

OPENAI_API_KEY = ""  # example: "sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
## Set up environment variables
environ["OPENAI_API_KEY"] = OPENAI_API_KEY
environ["MINIMAX_GROUP_ID"] = ""
environ["MINIMAX_API_KEY"] = ""

def test_query():
    #embeddings = MiniMaxEmbeddings()
    embeddings = OpenAIEmbeddings(model="text-embedding-ada-002")
    query = '电影排名:4'
    # search_params = {"metric_type": "IP", "params": {"level": 2}}
    # docs = Milvus(embedding_function=embeddings, collection_name='jytest4').similarity_search(query)
    result = Milvus(embedding_function=embeddings, collection_name='jytest5', connection_args={"uri": 'https://in01-7af631b9d591cb7.aws-us-west-2.vectordb.zillizcloud.com:19541',
                           'user': 'db_admin', 'password': 'difyai123!'}).similarity_search(query, param={"metric_type": "IP"})
    print(result)
    print(result)
    client = qdrant_client.QdrantClient(
        "https://7cceb067-61b5-4d74-9a4c-c82b683ed4d5.eu-central-1-0.aws.cloud.qdrant.io",
        api_key="xA7RZJa2-uJIPMHoCRiZf8t4Se7J_CAHezeaGKbnx6qcglg9ssEjRA",  # For Qdrant Cloud, None for local instance
    )
    result = Qdrant(embeddings=embeddings, client=client, collection_name="texts2").similarity_search(query)
    print(result)
