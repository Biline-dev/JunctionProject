
class hopital:
    def __init__(self, name, emergency_id="11",patient_id=1):
        self.name=name
        self.list_services=[]
        self.list_urgence=[]
        self.salles_urgence=[]
        self.emergency_id = emergency_id
        self.patient_id = patient_id

    def add_service(self,service):
        self.list_services.append(service)
        pass

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
        
    def __repr__(self):
        return (self.name)
    
    def check_availability(self,ordonnance):
        # we check if the medicaments in ordonnance are available in list_medicaments
        cmp=0
        for med in ordonnance:
            for lst in self.list_medicaments:
                if med.if_same_med(lst):
                    cmp+=1
                

        return cmp

    def return_intersection(self,ordonnance):
        #we return intersection between dispo medics and medics in ordonnance
        intersect=[]
        for med in ordonnance:
            if med.if_med_inlist(self.list_medicaments):
                intersect.append(med)

        return intersect
    
    def return_intersection_bar(self,ordonnance):
        #we return intersection between dispo medics and medics in ordonnance
        intersect=[]
        for med in ordonnance:
            if not(med.if_med_inlist(self.list_medicaments)):
                intersect.append(med)

        return intersect


    def add_medicament(self,medicament):
        #we add medicament in list_medicaments, if it already exists we add in quantity
        bool=False
        for medic in self.list_medicaments:
            if medic.if_same_med(medicament):
                medic.quantity+=1
                bool=True
                break
        
        if bool==False:
            self.list_medicaments.append(medicament)



    def remove_medicament(self,medicament):
        #we delete a medicament when the stock runs out, or we decrement only if it doesnt run out
        for medic in self.list_medicaments:
            if medic.if_same_med(medicament):
                if medic.quantity==1 or medic.quantity==0:
                    self.list_medicaments.remove(medic)
                
                else:
                    medic.quantity-=1
            



class medicament:
    def __init__(self,name,dose=None,quantity=None):
        self.name=name
        self.dose=dose
        self.quantity=quantity

    def __repr__(self):
        return 'name=' + str(self.name) + ', dose='+ str(self.dose)
    
    def if_same_med(self, medicament):
        if self.name==medicament.name and self.dose==medicament.dose:
            return True
        
        return False


    def if_med_inlist(self, list_med):

        for medec in list_med:
            if self.if_same_med(medec):
                return True

        return False
