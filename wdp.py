from mysql.connector import MySQLConnection, Error

import web

render = web.template.render('templates/')
db = web.database(dbn='mysql',
                  db='todo',
                  user='wdp',
                  password='kajhzbn7vceW',
                  buffered=True)

urls = (
    # '/(.*)', 'index'  # for "return render.index(name)"
    '/', 'index',
    '/add', 'add'
)


class index:
    # def GET(self, name):
    #     # name = 'Bob'
    #     # return render.index(name)
    #
    #     # i = web.input(name=None)
    #     # return render.index(i.name)
    #
    #     return render.index(name)

    def GET(self):
        # some dbg
        # print('DBG web.database ...', db, '\n', dir(db), '\n', db.select('todozero'), '\n')
        try:
            todos = db.select('todozero', what='*')
        except Error as e:
            print('Error:', type(e), e)
            # todos = ['a','b']
        return render.index(todos)


class add:
    def POST(self):
        i = web.input()
        n = db.insert('todozero', todozero_text=i.todozero_text)
        raise web.seeother('/')


if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()