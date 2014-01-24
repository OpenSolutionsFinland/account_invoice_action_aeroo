from osv import osv, fields
from openerp.tools.translate import _

class aeroo_invoice(osv.osv):
    _name="account.invoice"
    _inherit="account.invoice"
    
    def invoice_print(self, cr, uid, ids, context=None):
        assert len(ids) == 1, 'This option should only be used for a single id at a time.'
        
        self.write(cr, uid, ids, {'sent': True}, context=context)
        
        # check aeroo.invoice exists
        reportID = self.pool.get('ir.actions.report.xml').search(cr, uid, [('report_name', '=', 'aeroo.invoice')])
        if len(reportID) == 0:
            raise osv.except_osv('Error', _('Report not found! Install a report with service name aeroo.invoice'))
        
        datas = {
            'ids': ids,
            'model': 'account.invoice',
            'form': self.read(cr, uid, ids[0], context=context)
        }
        return {
            'type': 'ir.actions.report.xml',
            'report_name': 'aeroo.invoice',
            'datas': datas,
            'nodestroy' : True
        }

aeroo_invoice()