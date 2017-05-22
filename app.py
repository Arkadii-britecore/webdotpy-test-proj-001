import string
import random
import web

from sqlalchemy.orm import scoped_session, sessionmaker
from model import *

render = web.template.render('templates/')

urls = (
    '/', 'index',
    '/company/(.*)', 'company_details',
    '/view', 'view'
)

def load_sqla(handler):
    web.ctx.orm = scoped_session(sessionmaker(bind=engine))
    try:
        return handler()
    except web.HTTPError:
       web.ctx.orm.commit()
       raise
    except:
        web.ctx.orm.rollback()
        raise
    finally:
        web.ctx.orm.commit()
        # If the above alone doesn't work, uncomment
        # the following line:
        #web.ctx.orm.expunge_all()


app = web.application(urls, locals())
app.add_processor(load_sqla)


# class add:
#     def GET(self):
#         web.header('Content-type', 'text/html')
#         fname = "".join(random.choice(string.letters) for i in range(4))
#         lname = "".join(random.choice(string.letters) for i in range(7))
#         u = User(name=fname
#                 ,fullname=fname + ' ' + lname
#                 ,password =542)
#         web.ctx.orm.add(u)
#         return "added:" + web.websafe(str(u)) \
#                             + "<br/>" \
#                             + '<a href="/view">view all</a>'

class index:
    def GET(self):
        '''
        Get list of companies
        :return: list of companies
        '''
        companies = web.ctx.orm.query(Company).all()
        print('DBG: found {} companies'.format(len(companies)))
        return render.index(companies)


class view:
    def GET(self):
        web.header('Content-type', 'text/plain')
        return "\n".join(map(str, web.ctx.orm.query(Employee).all()))

class company_details:
    def GET(self, company):
        '''
        Show company details
        :return: 
        '''
        # details = web.ctx.orm.query(Company).all()
        details = company

        # extend company details
        # todo - accept non-ASCII codepage
        print('DBG: company is:', type(company), company)
        count_employee = web.ctx.orm.query(Employee).\
            filter(Employee.company_id == Company.id). \
            filter(Company.title == company). \
            count()
        print('DBG: count_employee', count_employee)



        return render.company_details(details)


if __name__ == "__main__":
    app.run()