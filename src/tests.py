import classes as classes

def reserve(service_name,hospital):
    for service in hospital.list_services:
        if(service.name == service_name):
            new_patient(service.check_in())

def new_patient(information):
    patient_id , len = information
    print("your id is %d and there is %d people before you in line" %(patient_id,len))

def new_emergency_patient(information):
    patient_id , len = information
    if len > reasonable_waiting_time:
        # nearby_hospitals_available()
        pass
    else:
        print("your id is %d and there is %d people before you in  line" %(patient_id,len))

def patient_called(service_name,hospital):
    for service in hospital.list_services:
        if(service.name == service_name):
            patient_id = service.patient_called()
    print("patient %d please procced to the doctor" %(patient_id))

reasonable_waiting_time = 5

services = []
services.append(classes.service("dentist"))
services.append(classes.service("ophtalmologue"))
h1 = classes.hopital("hopital 1", services)


reserve("dentist",h1)
reserve("ophtalmologue",h1)
reserve("ophtalmologue",h1)
reserve("ophtalmologue",h1)
patient_called("ophtalmologue",h1)
patient_called("ophtalmologue",h1)
reserve("dentist",h1)
reserve("dentist",h1)
reserve("ophtalmologue",h1)
#
# new_emergency_patient(h1.new_emergency_patient())
# reserve("ophtalmologue",h1)
# reserve("ophtalmologue",h1)
# patient_called("ophtalmologue",h1)
# patient_called("ophtalmologue",h1)
# reserve("dentist",h1)
# reserve("dentist",h1)
# reserve("ophtalmologue",h1)
# patient_called("ophtalmologue",h1)
# reserve("dentist",h1)
# reserve("ophtalmologue",h1)
# reserve("dentist",h1)
# reserve("ophtalmologue",h1)
# patient_called("ophtalmologue",h1)
