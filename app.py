# import string

# import random

# import decimal

import re

import web

from sqlalchemy.orm import scoped_session, sessionmaker

# from sqlalchemy import create_engine, Column, Integer, ForeignKey, Numeric, DateTime, func
from sqlalchemy import func

from model import *

render = web.template.render('templates/')

urls = (
    '/', 'index',
    '/company/(.*)', 'company_details',
    '/employees', 'employees',
    '/employee/(.*)', 'employee_details',

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


class company_details:
    def GET(self, company_id):
        '''
        Show company details by id
        :return: 
        '''
        company = web.ctx.orm.query(Company).filter(Company.id == company_id).first()
        # company_id = str(company, 'utf-8')

        # extend company details
        # todo - accept non-ASCII codepage
        print('DBG: company is:', type(company), company)
        count_employee = web.ctx.orm.query(Employee).\
            filter(Employee.company_id == Company.id). \
            filter(Company.id == company_id). \
            count()
        # print('DBG: count_employee', count_employee)  #  ok

        # extend company details for total salary
        total_slr = web.ctx.orm.query(Employee.salary).\
            filter(Employee.company_id == Company.id). \
            filter(Company.id == company_id). \
            all()
        try:
            total_salary = web.ctx.orm.query(
                func.sum(Employee.salary)).filter(Employee.company_id == company_id).all()

            # total_salary = total_salary.with_entities(func.sum(Employee.salary)).scalar()

            print('DBG 102 : total_salary', total_salary)
        except Error as e:
            print('ERR : could not count total_salary', type(e), e)

        print('DBG 106: total_salary', type(total_salary), type(total_salary[0]),
              str(total_salary[0]), str(re.findall(r'\d+', str(total_salary[0]))))
        total_salary = float(re.findall(r'\d+', str(total_salary[0]))[0])

        # extend company info with list of workers
        staff = web.ctx.orm.query(Employee).\
            filter(Employee.company_id == Company.id). \
            filter(Company.id == company_id).all()
        print('DBG: staff:', type(staff), len(staff), staff)

        return render.company_details(company, count_employee, total_salary, staff)


class employees:
    def GET(self):
        # web.header('Content-type', 'text/plain')
        employees = web.ctx.orm.query(Employee).all()
        print('DBG employees:', len(employees), type(employees))

        # return "\n".join(map(str, web.ctx.orm.query(Employee).all()))
        return render.employees(employees)


class employee_details:
    def GET(self, id):
        """
        Show employee details by id
        :return: 
        """

        employee_id = id
        employee = web.ctx.orm.query(Employee).filter(Employee.id == employee_id).first()
        print('DBG: employee is:', type(employee), employee)
        return render.employee_details(employee)


if __name__ == "__main__":
    app.run()
