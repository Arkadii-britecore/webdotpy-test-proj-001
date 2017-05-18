import web
render = web.template.render('templates/')

urls = (
    '/(.*)', 'index'
)


class index:
    def GET(self, name):
        # name = 'Bob'
        # return render.index(name)

        # i = web.input(name=None)
        # return render.index(i.name)

        return render.index(name)


if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()