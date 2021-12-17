
class hopital:
    def __init__(self,name, list_services, list_urgence,salles_urgence):
        self.name=name
        self.list_services=list_services
        self.list_urgence=list_urgence
        self.salles_urgence=salles_urgence
    
    def add_service(self,service):
        #add new services
        pass
    
    def remove_service(self,service_name):
        #remove service
        pass

    #add urgence functions here


class service :
    def __init__(self,name,list_checkins=None):
        self.name=name
        self.list_checkins=list_checkins
    
    #checkin functions here



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
