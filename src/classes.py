
class hopital:
    def __init__(self, name, list_services=[] ,emergency_id="11",patient_id=1):
        self.name=name
        self.list_services= list_services
        self.list_urgence=[]
        self.salles_urgence=[]
        self.emergency_id = emergency_id
        self.patient_id = patient_id

    def add_service(self,service):
        self.list_services.append(service)
        pass

    def set_emergency_list(self,list_urgence):
        self.list_urgence = list_urgence

    def remove_service(self,service_name):
        service = search_service(self,service_name)
        if not service:
            print("Service %s doesn't exist" %(service))
            return
        self.list_services.remove(service)

    def search_service(self,service_name):
        for service in self.list_services:
            if service.name == service_name:
                return service
        return None

    #add urgence functions here
    def new_emergency_patient(self):
        patient_id = int(self.emergency_id + str(self.patient_id))
        self.list_urgence.append(patient_id)
        self.patient_id+=1
        return (patient_id,len(self.list_urgence)-1) #return id + number of waiting patients

    def emergency_patient_called(self):
        patient_id = self.list_urgence.pop(0)
        return patient_id

class service :
    service_index = "0"
    def __init__(self,name,id = 1):
        self.name=name
        self.list_checkins=[]
        self.id = id
        self.service_index = str(int(service.service_index)+1)
        service.service_index = self.service_index

            #checkin functions here
    def check_in(self):
        patient_id = int(self.service_index + str(self.id))
        self.list_checkins.append(patient_id)
        self.id+=1
        return (patient_id,len(self.list_checkins)-1) #return id + number of waiting patients


    def patient_called(self):
        if not self.list_checkins:
            return -1
        patient_id = self.list_checkins.pop(0)
        #call the patient to the doctos room
        return patient_id


class pharmacie:
    def __init__(self,name=None,position=None,list_medicaments=None):
        self.name=name
        self.position=position
        self.list_medicaments=list_medicaments

    def check_availability(self,ordonnance):
        # we check if the medicaments in ordonnance are available in list_medicaments
        pass

    def add_medicament(self,medicament):
        #we add medicament in list_medicaments, if it already exists we add in quantity
        pass

    def remove_medicament(self,medicament_name):
        #we delete a medicament when the stock runs out, or we decrement only if it doesnt run out
        pass



class medicament:
    def __init__(self,name,dose,quantity):
        self.name=name
        self.dose=dose
        self.quantity=quantity
