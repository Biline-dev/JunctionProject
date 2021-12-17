
class hopital:
    def __init__(self,name,position, list_services, list_urgence,salles_urgence):
        self.name=name
        self.position=position
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
