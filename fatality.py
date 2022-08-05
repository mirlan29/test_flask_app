import requests

#for i in range (0,10):
#    response = requests.get('https://api.kanye.rest/')
#    quote = (response.text)
#    print(quote)
from re import *
import requests
import ast
from peewee import *
  
db = PostgresqlDatabase(
    'quotes',
    host = 'localhost',
    port = '5434',
    user = 'mirlan',
    password = 'qwe123'
)

db.connect()

unique_list = []
for i in range(10):
    response = requests.get('https://api.kanye.rest/')
    quote = response.text
    quote = ast.literal_eval(quote)
    quote = quote.get('quote')
    if quote in unique_list:
        continue
    class BaseModel(Model):
        class Meta:
            database = db


    class quotes(BaseModel):
        kanye = CharField(max_length=255, unique=False)


    db.create_tables([quotes])

    quotes.create(
        kanye = quote
    )


    db.close()

    unique_list.append(quote)