def merge_dict(dict1,dict2):
    mer_dict=dict1.copy()
    mer_dict.update(dict2)
    return mer_dict

dict_1={'a':1,'b':2}
dict_2={'c':3,'d':4}
merged_dict=merge_dict(dict_1,dict_2)
print("Merged dictornary =", merged_dict)

