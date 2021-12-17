#hospital list
from classes import hopital, medicament, pharmacie, service
import math


def calcul_distance(position_a, position_b):
    return math.sqrt((position_a[0]-position_b[0])**2 + (position_a[1]-position_b[1])**2)

def minmax(tup,max1,max2):
    return [tup[0]/max1,tup[1]/max2]

    
def get_route(position_1, list_pharma, ordonance):
    list_dist_disp=[]
    for ph in list_pharma:
        
        if ph.check_availability(ordonance)==len(ordonance):
            return (ph,ph.return_intersection(ordonance))
    
        list_dist_disp.append((calcul_distance(position_1,ph.position),ph.check_availability(ordonance)))
    
    score_ph=[]
    i=0
    for tuple in list_dist_disp:
        tuple=minmax(tuple,max(list_dist_disp[0]),len(ordonance))
        if(tuple[1]==0):
            tuple[1]=0.0001
        score_ph.append(tuple[0]+(1/tuple[1]))
        i+=1
    
    min_score=min(score_ph)
    min_index=score_ph.index(min_score)

    if min_score>= 10000 :
        return (None,ordonance)

    new_list=list_pharma.copy()
    new_list.remove(list_pharma[min_index])
    new_ordonnance=list_pharma[min_index].return_intersection_bar(ordonance)

    return ((list_pharma[min_index],list_pharma[min_index].return_intersection(ordonance)),get_route(list_pharma[min_index].position,new_list,new_ordonnance))
    




if __name__ == '__main__':

    list_hospital=[hopital('h1',[150,15],{service('s1',{'S12','S13','S14'}),service('s2',{'S21','S23'})},{'u1','u2','u3'},{'salle1','salle2'}),
            hopital('h2',[115,85],{service('s3',{'S12','S13','S14'}),service('s4',{'S21','S23'})},{'u1','u2','u3'},{'salle1','salle2'}),
            hopital('h3',[200,1],{service('s4',{'S12','S13','S14'}),service('s5',{'S21','S23'})},{'u1','u2','u3'},{'salle1','salle2'})
    ]

list_medicaments=[medicament('doliprane',250,20),medicament('catalgine',500,5),
    medicament('charbonel',500,2),medicament('dafalgon',150,10), medicament('spasfon',1000,100)]

ordonance=[medicament('doliprane',250,20),medicament('catalgine',500,5),medicament('charbonel',150,10),medicament('dafalgon',150),medicament('creme',150)]

list_pharmacies=[pharmacie('p1',[14,16],[medicament('doliprane',250,20),medicament('catalgine',500,5)]),
     pharmacie('p2',[250,69],[medicament('catalgine',500,5),medicament('charbonel',150,10)]),
     pharmacie('p3',[300,2],[medicament('catalgine',500,5),medicament('charbonel',150,10),medicament('doliprane',200,10)]),
     pharmacie('p4',[45,45],[medicament('spasfon',1000,5),medicament('dafalgon',150,10)])]

'''
for pharma in list_pharmacies:
    pharma.remove_medicament(list_medicaments[1])
    pharma.add_medicament(medicament('doliprane',10,2))
    print(pharma.name)
    print(pharma.check_availability(ordonance))
    print('LIST : ')
    for med in pharma.list_medicaments:
        print(med.name,'  ',med.quantity)
'''
    
#print(calcul_distance(list_hospital[0].position,list_pharmacies[0].position))

returned=get_route(list_hospital[0].position,list_pharmacies,ordonance)

for obj in returned:
    print(obj[0],'  ',obj[1])
