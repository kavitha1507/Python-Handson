def intersec_set(set1,set2):
    inter_set=set1.intersection(set2)
    return inter_set

set_a={1,2,3,4}
set_b={3,4,5,6}
result_set=intersec_set(set_a,set_b)
print("Intersedtion of sets =", result_set)