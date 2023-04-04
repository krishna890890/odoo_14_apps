# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
from odoo import _
import base64
import unicodedata


class AttachmentUpload(http.Controller):

    def add_attachment(self, ufile, res_model, res_id):
        partner = request.env.user.partner_id
        Model = request.env['ir.attachment']
        filename = ufile.filename
        if request.httprequest.user_agent.browser == 'safari':
            # Safari sends NFD UTF-8 (where é is composed by 'e' and [accent])
            # we need to send it the same stuff, otherwise it'll fail
            filename = unicodedata.normalize('NFD', ufile.filename)
        if ufile.filename:
            attachment = Model.sudo().create({
                    'name': ufile.filename,
                    'datas': base64.encodebytes(ufile.read()),
                    'store_fname': ufile.filename,
                    'res_model': res_model,
                    'res_id': res_id or False,
                    'ajax_uploaded_file': True,
                })
            return str(attachment.id)
        return None

    @http.route(['/upload/attachment/onchange'], type='http', auth="public", website=True, csrf=False)
    def upload_attachment_onchange(self, attachments, res_id, res_model, **kw):
        file_ids = kw.get('file_ids', [])
        survey = kw.get('survey', False)
        if survey:
            attachments = kw.get(attachments)
        if attachments:
            return self.add_attachment(attachments, res_model, res_id)

    @http.route(['/upload/attachment/onload'], type='json', auth="public", website=True, csrf=False)
    def uploaded_files(self, **kw):
        partner = request.env.user.partner_id
        files_ids = kw.get('files_ids', None)
        res_id = kw.get('res_id', '')
        res_model = kw.get('res_model', '')
        if res_id and res_model:
            domain = [
                ('res_model', '=', res_model),
                ('res_id', '=', res_id),
                ('res_field', '=', False),
                ('ajax_uploaded_file', '=', True),
            ]
            attachment_ids = request.env['ir.attachment'].sudo().search(domain)
            attachments = []
            for attach in attachment_ids:
                attachments.append({'path': attach.id, 'name': attach.name, 'size': attach.file_size})
            return attachments
        elif files_ids:
            files_ids = map(int, files_ids.split(','))
            attachment_ids = request.env['ir.attachment'].sudo().browse(files_ids)
            attachments = []
            for attach in attachment_ids:
                attachments.append({'path': attach.id, 'name': attach.name, 'size': attach.file_size})
            return attachments
        return {}


    def delete_attachment(self, attachment_id, res_model):
        if attachment_id:
            Model = request.env['ir.attachment']
            if type(attachment_id) != list:
                attachment_id = [int(attachment_id)] 
            domain = [
                ('id', 'in', attachment_id),
                ('res_model', '=', res_model),
                ('res_field', '=', False),
                ('ajax_uploaded_file', '=', True),
            ]
            attachment_id = Model.sudo().search(domain)
            size = attachment_id.file_size
            attachment_id.sudo().unlink()
            return size


    @http.route(['/upload/attachment/delete'], type='json', auth="public", website=True, csrf=False)
    def uploaded_files_delete(self, attachment_id, res_model, **kw):
        res = self.delete_attachment(attachment_id, res_model)
        if type(attachment_id) == list:
            attachment_id = attachment_id[0]
        if res:
            return attachment_id, res
