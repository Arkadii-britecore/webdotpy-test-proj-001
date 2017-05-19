import web
render = web.template.render('templates/')

urls = (
    # '/(.*)', 'index'  # for "return render.index(name)"
    '/', 'index',
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
        todos = db.select('todozero')
        return render.index(todos)



if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()