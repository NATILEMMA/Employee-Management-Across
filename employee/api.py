from ast import Constant
import frappe
from frappe.utils import getdate
from frappe.utils import get_datetime
from datetime import datetime
from .permission_check import has_permission
from frappe.utils import get_site_name


VALID_RANGE_Longitude = 0.007

VALID_RANGE_Latitude= 0.017

#if the location of user is <= VALID_RANGE_Longitude

# VALID_RANGE_Longitude = 0.007

#VALID_RANGE_Latitude= 0.017

now = datetime.now()
datetm = now.strftime("%Y-%m-%d %H:%M:%S")
date = frappe.utils.getdate()


uid= frappe.session.user
print(uid)
email = frappe.db.get_value('User', {'username': uid}, ['email'])
employee = frappe.db.get_value('Employee', {'user_id': uid}, ['employee'])

company = frappe.db.get_value('Employee', {'user_id': uid}, ['company'])
if(not company):
    company = ""
location_db_response = frappe.db.get_value('Company', {'company_name': company}, ['location'])
NOT_IN_RANGE = "Not In Range!Get closer to the company : "+ company


@frappe.whitelist()
def check_location_and_fill_attendance(**args):
    location = eval(location_db_response)
    coordinates = location['features'][0]['geometry']['coordinates']
    print(coordinates)
    print(args.get('longitude'))
    difference = abs(float(coordinates[1]) - float(args.get('latitude')))
    print("&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&",difference)
    result = abs(float(coordinates[1]) - float(args.get('latitude'))) <= VALID_RANGE_Longitude 
    print ("result &&&&&&&&&&&&&&&&&&&&&&", result)
    if(abs(float(coordinates[0]) - float(args.get('longitude'))) <= VALID_RANGE_Longitude and abs(float(coordinates[1]) - float(args.get('latitude'))) <= VALID_RANGE_Latitude):
        status = args.get('status')
        return fill_attendance_function(status)
    else:
        return NOT_IN_RANGE
    
@frappe.whitelist()
def checkAttendanceFilled():
    now = datetime.now()
    datetm = now.strftime("%Y-%m-%d %H:%M:%S")
    date = frappe.utils.getdate()
    print("I am in the check")
    date = frappe.utils.getdate()
    


    uid= frappe.session.user    
    email = frappe.db.get_value('User', {'username': uid}, ['email'])
    employee = frappe.db.get_value('Employee', {'user_id': uid}, ['employee'])
    company = frappe.db.get_value('Employee', {'user_id': uid}, ['company'])

    Values  = {'email': email, 'date': date, 'employee': employee}

    last_punch_db_response = frappe.db.sql("""
    SELECT A.last_punch FROM `tabAttendance` AS A  WHERE (A.employee = %(employee)s)
    AND (attendance_date=%(date)s);""",values=Values, as_dict=0)

    attendance_name_db_response = frappe.db.sql("""
    SELECT A.name FROM `tabAttendance` AS A  WHERE (A.employee = %(employee)s)
    AND (attendance_date=%(date)s);""",values=Values, as_dict=0)

    first_unpack = []
    last_punch= 0


    for item in  last_punch_db_response:
        first_unpack = item

    for item in first_unpack:              # to unpack the array value from database 
        last_punch = item

    

    if(last_punch):  
        return True
    else:
        return False


@frappe.whitelist()
def punchAttendance():

    now = datetime.now()
    datetm = now.strftime("%Y-%m-%d %H:%M:%S")
    date = frappe.utils.getdate()

    print("Below is the correct datetime value printed from the Employee.API.api.py")
    print(datetm)
    uid= frappe.session.user    
    email = frappe.db.get_value('User', {'username': uid}, ['email'])
    employee = frappe.db.get_value('Employee', {'user_id': uid}, ['employee'])
    company = frappe.db.get_value('Employee', {'user_id': uid}, ['company'])

    Values  = {'email': email, 'date': date, 'employee': employee}

    last_punch_db_response = frappe.db.sql("""
    SELECT A.last_punch FROM `tabAttendance` AS A  WHERE (A.employee = %(employee)s)
    AND (attendance_date=%(date)s);""",values=Values, as_dict=0)

    attendance_name_db_response = frappe.db.sql("""
    SELECT A.name FROM `tabAttendance` AS A  WHERE (A.employee = %(employee)s)
    AND (attendance_date=%(date)s);""",values=Values, as_dict=0)

    first_unpack = []
    attendance_first = []
    last_punch= 0
    attendance_name = 0

    for item in  last_punch_db_response:
        first_unpack = item

    for item in first_unpack:              # to unpack the array value from database 
        last_punch = item
    
    for item in  attendance_name_db_response:
        attendance_first= item

    for item in attendance_first:              # to unpack the array value from database 
        attendance_name = item
    print("last punch in punch attendance")
    print(last_punch)
    
    if(last_punch == "1"):
        print("I am in ==1")

        doc = frappe.get_doc('Attendance',attendance_name)
        
        doc.out_time = datetm
        doc.last_punch = 2
        doc.save()
        return "punched Out at time " + datetm



    elif(last_punch == "2"):
        return "Punch for the day already satisfied!!!"
    elif(last_punch == "A"):
        return "You are Absent today can't Punch!!!"
    elif(last_punch == "W"):
        doc = frappe.get_doc('Attendance',attendance_name)
        
        doc.out_time = datetm
        doc.last_punch = 2
        doc.save()
        return "punched Out at time " + datetm
       
    else:
        return "Please fill todays attendance first."
    '''
        if(last_punch == 1):
        print("I am in ==1")

        doc = frappe.get_doc('Attendance',attendance_name)
        
        doc.out_time_morning = datetm
        doc.last_punch = 2
        doc.save()
        return "punched Out at time " + datetm

    elif(last_punch == 2):
        doc = frappe.get_doc('Attendance',attendance_name)
        doc.in_time_afternoon = datetm
        doc.last_punch = 3
        doc.save()
        return "punched In at time"+ datetm

    elif(last_punch == 3):
        doc = frappe.get_doc('Attendance',attendance_name)
        doc.out_time_afternoon = datetm
        doc.last_punch = 4
        doc.save()
        return "punched Out at time" + datetm

    elif(last_punch == 4):
        return "Punch for the day already satisfied!!!"
    else:
        return "Please fill todays attendance first."
        
    '''


@frappe.whitelist()
def fill_attendance(**args):
    status = args.get('status')
    return fill_attendance_function(status)
    
   
   
def fill_attendance_function(status):
    Values  = {'email': email, 'date': date}
    data = frappe.db.sql("""    
        SELECT A.status FROM `tabAttendance` AS A, `tabEmployee`,`tabUser` WHERE (user_id=%(email)s) AND (attendance_date=%(date)s);""",values=Values, as_dict=0)

    attendance_name = frappe.db.sql("""
    SELECT A.name FROM `tabAttendance` AS A, `tabEmployee`,`tabUser` WHERE (user_id=%(email)s) AND (attendance_date=%(date)s);
    """,values=Values, as_dict=0)

    try:
        if (not len(data)):
            if(status == "Present"):
                # create a new document
                doc = frappe.get_doc({
                    'doctype': 'Attendance',
                    'employee': employee,
                    'attendance_date': date,
                    'company': company,
                    'status':status,
                    'in_time': datetm,
                    'last_punch':1,
                
        
                })
                doc.insert()
                print("i am here in === status present")
                doc.save()
                frappe.db.commit()
                print(doc.name)
            elif (status == "Absent"):
                # create a new document
                doc = frappe.get_doc({
                        'doctype': 'Attendance',
                    'employee': employee,
                    'attendance_date': date,
                    'company': company,
                    'status':status,
                    'last_punch': "A",
                
        
                })
                doc.insert()
                print("i am here in === status present")
                doc.save()
                frappe.db.commit()
                print(doc.name)
            elif (status == "Work From Home"):
                # create a new document
                doc = frappe.get_doc({
                    'doctype': 'Attendance',
                    'employee': employee,
                    'attendance_date': date,
                    'company': company,
                    'status':status,
                    'in_time': datetm,
                    'last_punch': "W",
                
        
                })
                doc.insert()
                print("i am here in === status present")
                doc.save()
                frappe.db.commit()
                print(doc.name)
                
            else: 
                return "Invalid Attendance"   
            return "New attendance created!"
        
    except:
         return "Attendance already exists! You already filled Attendance. contact the HR manager for further information. "   

@frappe.whitelist(allow_guest = True)
def check_permission():
    site_name = get_site_name(frappe.local.request.host)    
    user= frappe.session.user
    print("site name: ***********************************************************************************")  
    print(site_name)
    print("user: ***********************************************************************************")  
    print(user == "Guest")
    if(user == "Guest"):
        relocate = True
        relocation_url = "https://"+site_name+"/employee_dashboard/login.html"
    else:
        permission = has_permission("Attendance",raise_exception= False)
        if(not permission):
            permission = has_permission("Attendance",raise_exception= False)
            relocate = True
            relocation_url = "https://"+site_name+"/employee_dashboard/chart.html"
        else:
            relocate = False
            relocation_url = None
    response = {"relocate":relocate,"relocation_url":relocation_url}
    return response
    