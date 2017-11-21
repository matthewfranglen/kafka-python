from datetime import datetime
from elasticsearch import Elasticsearch

def write(server, index, document_type, source):
    writer = Elasticsearch([server])

    for message in source:
        document = {
            'text': message,
            'timestamp': datetime.now()
        }

        writer.index(index=index, doc_type=document_type, body=document)
        print(f'Written: {message}')
