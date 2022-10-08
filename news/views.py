from database.db import database

from .models import article, comment


async def get_article_list():
    return await database.fetch_all(query=article.select())


async def create_article(item):   
    art = article.insert().values({"title" : item.title, "text" : item.text, "image" : item.image})
    exec_ = await database.execute(art)
    return "Article created"


async def update_article(id, item):
    data = str(item).replace('"', '').replace(':', '=').replace('{', '').replace('}', '')
    query = f"UPDATE  SET {data} WHERE id = :id;"
    exec_ = await database.execute(query=query, values={"id" : id})
    return "Article updated"


async def delete_article(id):
    query = "DELETE FROM article WHERE id = :id;"
    try:
        exec_ = await database.execute(query=query, values={"id" : id})
    except ValueError: "No such article"
    else: return "Article deleted"





async def get_comment_list(id):
    query = "SELECT * from comment WHERE id = :id"
    return await database.fetch_all(query=query, values={"id":id})


async def create_comment(item, user):   
    com = article.insert().values({"text" : item.text, "article_id" : item.article_id, "user_email" : user[0]})
    exec_ = await database.execute(com)
    return "Created"



async def delete_comment(id):
    query = "DELETE FROM comment WHERE id = :id;"
    try:
        exec_ = await database.execute(query=query, values={"id" : id})
    except ValueError: "No such comment"
    else: return "Comment deleted"






# def foo(model, **kwargs):
#     ins = insert(model).values(**kwargs)

#  insert(model).values({getattr(model, key): value for key, value in kwargs.items()})




#  checkparams = {
#             'myid': 3,
#             'name': 'jack',
#             'description': 'mydescription'
#         }

#         self.astert_compile(insert(table1, (3, 'jack', 'mydescription')),
#                             'INSERT INTO mytable (myid, name, description) '
#                             'VALUES (:myid, :name, :description)',
#                             checkparams=checkparams)