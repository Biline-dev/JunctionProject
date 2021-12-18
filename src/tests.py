import classes as classes

def reserve(service_name,hospital):
    for service in hospital.list_services:
        if(service.name == service_name):
            patient_id , len = service.check_in()
            # print("your id is %d and there is %d people before you in line" %(patient_id,len))


def new_emergency_patient(hospital):
    patient_id , lenght = hospital.new_emergency_patient()
    print("your id is %d and there is %d people before you in line" %(patient_id,lenght))
    if lenght > reasonable_waiting_time:
        proposed_hospital = hospital
        for nearby_hospital in  hospitals_list:
            if nearby_hospital != hospital and lenght > len(nearby_hospital.list_urgence):
                proposed_hospital = nearby_hospital
        if(proposed_hospital != hospital):
            print("we suggest you go to %s where the waiting line for emergency is %s" %(proposed_hospital.name,len(proposed_hospital.list_urgence)))

def patient_called(service_name,hospital):
    for service in hospital.list_services:
        if(service.name == service_name):
            patient_id = service.patient_called()
    # print("patient %d please procced to the %s" %(patient_id,service_name))

reasonable_waiting_time = 2

services = []
h1 = classes.hopital("Hospital Aïn Naadja",[150,50],[],[],[])
h2 = classes.hopital("Hospital Mohamad Lamine",[15,150],[],[],[])
h3 = classes.hopital("Hospital Salim Zmirli",[100,75],[],[],[])
h1.add_service(classes.service("dentist"))
h1.add_service(classes.service("ophtalmologue"))
h2.add_service(classes.service("ophtalmologue"))
h3.add_service(classes.service("ophtalmologue"))
h2.set_emergency_list([111,112,113,114,115,116])
h3.set_emergency_list([111])

hospitals_list = [h1 , h2, h3]

reserve("dentist",h1)
reserve("ophtalmologue",h1)
reserve("ophtalmologue",h1)
reserve("ophtalmologue",h1)
patient_called("ophtalmologue",h1)
patient_called("ophtalmologue",h1)
reserve("dentist",h1)
reserve("dentist",h1)
reserve("ophtalmologue",h1)
new_emergency_patient(h1)
new_emergency_patient(h1)
new_emergency_patient(h1)
new_emergency_patient(h1)
