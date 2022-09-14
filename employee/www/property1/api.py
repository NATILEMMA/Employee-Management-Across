import frappe

@frappe.whitelist()
def fill_attendance(**args):
    # create a new document
    doc = frappe.get_doc({
        'doctype': 'Attendance',
        'employee': 'HR-EMP-00011',
        'attendance_date': '2022-08-24',
        'company': 'Gagarian',
        'status': 'Absent',
 
    })
    doc.insert()
    doc.submit()
    frappe.db.commit()
    doc.save()
 


    return
