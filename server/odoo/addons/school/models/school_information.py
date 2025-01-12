from odoo import models, fields, api

class SchoolInformation(models.Model):
    _name = 'school.information'
    _description = 'School Information'

    name = fields.Char(string='Tên trường')
    type = fields.Selection([('private', 'Dân lập'), ('public', 'Công lập')], default='public', string='Loại trường')
    email = fields.Text(string='Email')
    address = fields.Text(string='Địa chỉ')
    phone = fields.Char(string='Số điện thoại')
    hasOnline = fields.Boolean(string='Có lớp online hay không?', default=False)
    rank = fields.Integer(string='Xếp hạng')
    establishDay = fields.Date('Ngày thành lập')
    document = fields.Binary(string='Tài liệu về trường')
    document_name = fields.Char(string='Tên tài liệu')