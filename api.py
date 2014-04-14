#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: Gonzalo Chacaltana @gchacaltanab
from flask import Flask, request
from flask.ext import restful
from ErrorMessage import ErrorMessage

app = Flask(__name__)
api = restful.Api(app)

#array de clientes
customers = {
    '1': {
        'company_name': 'Laboratorios AdHoc S.A',
        'ruc': '20987876261',
        'billing_contact': 'Gonzalo Chacaltana'
        },
    '2': {
        'company_name': 'Química Suecia Inc',
        'ruc': '20769823211',
        'billing_contact': 'Steve Jhonson'
        },
    '3': {
        'company_name': 'Produce Labs EIRL',
        'ruc': '20226578291',
        'billing_contact': 'Manuel Gutierrez'
        },
    '4': {
        'company_name': 'Rockets Science S.A.C',
        'ruc': '20769823211',
        'billing_contact': 'Eugenia Rodriguez'
        },
    '5': {
        'company_name': 'Laboratorios del Perú S.A.C',
        'ruc': '20650081111',
        'billing_contact': 'Martín Saavedra'
        },
    '6': {
        'company_name': 'Estudios Químicos S.A.C',
        'ruc': '20925600181',
        'billing_contact': 'Mike Salvatierra'
        },
    '7': {
        'company_name': 'Proctect & Handlers EIRL',
        'ruc': '20186709201',
        'billing_contact': 'Carl Wiston'
        },
    '8': {
        'company_name': 'Compu Labs EIRL',
        'ruc': '20986722561',
        'billing_contact': 'Eduardo García'
        },
}


#Clase Clientes
class Customers(restful.Resource):

    def get(self, id):
        if self.validCustomers(id) is False:
            return ErrorMessage.printError(
                400, 'The customer does not exist.'
                )

        return customers[id]

    def put(self, id):
        if self.validCustomers(id) is False:
            return ErrorMessage.printError(
                400, 'The customer does not exist.'
                )

        customers[id][request.form['field']] = request.form['value']
        return customers[id]

    def validCustomers(self, id):
        if id in customers:
            return True
        else:
            return False

#ruteo
api.add_resource(Customers, '/customers/<string:id>')

if __name__ == '__main__':
    app.run(debug=True)
