 
# def intersection(lst1, lst2): 
#     lst3 = [list(filter(lambda x: x in lst1, sublist)) for sublist in lst2] 
#     return lst3 
# people = [[1993,2019],[1985,2018],[1994,2020],[2000,2015],[2015,2019],[2016,2020],[1994,2018]]
# yob=list(map(lambda x: x[0], people))
# yod=list(map(lambda x: x[1], people))
# yobd=dict((k,1) for k in yob)
# yodd=dict((k,-1) for k in yod)
# print(yobd)
# print(yodd)
# yobd.update(yodd)
# linear_dict=sorted(yobd.items())
# #lst3 = [list(filter(lambda x: x in yob, sublist)) for sublist in yod]
# print(linear_dict)

from collections import Counter
import operator
def most_populated(population, single=True):
    birth = list(map(lambda x: x[0], population))
    death = list(map(lambda x: x[1] + 1, population))
    print(birth)
    print(death)
    b = Counter(birth)
    d = Counter(death)
    print(b)
    print(d)
    alive = 0
    years = {}
    i=0
    for year in range(min(birth), max(death) + 1):
        alive = alive + b[year] - d[year]
        years[year] = alive
        i+=1
    print (i)
    max_year_dict={}
    key=[max(years, key=lambda key: years[key])] if single else \
           [key for key, val in years.items() if val == max(years.values())]
    print(key)
    for i in key:
        max_year_dict.update({i:years[i]})
    return(max_year_dict)
data=[[1993,2019],[1985,2018],[1994,2020],[2000,2015],[2015,2019],[2016,2020],[1994,2018]]
res=most_populated(data,single=True)
print (res)