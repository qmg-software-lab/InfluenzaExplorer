

# ["Geo_Code","Geo_Label","Population","Year","Cohort","Eventname","Event_Label","Observed","Crude_Rate","Adjusted_Rate","Expected","Expected_Adjusted","OE_Crude_Ratio","OE_Adjusted_Ratio","Std_Error","Std_Error_Adjusted","Uppercl","Lowercl","Percentile","Short_label","cohort_web_label","Geo_Name"]

# def transpose():
m = [[1,2],[3,4],[5,6]]
for row in m:
    print(row)
rez = [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]
print("\n")
for row in rez:
    print(row)



# error class defs
def error_class_hierarchy():

    class Error(Exception):
        pass
    class Warning(Exception):
        pass
    class InterfaceError(Error):
        pass
    class DatabaseError(Error):
        pass
    class InternalError(DatabaseError):
        pass
    class OperationalError(DatabaseError):
        pass
    class ProgrammingError(DatabaseError):
        pass
    class IntegrityError(DatabaseError):
        pass
    class DataError(DatabaseError):
        pass
    class NotSupportedError(DatabaseError):
        pass
    class_hierarchy_param_dict = {
            'Error': 'Exception',
            'Warning': 'Exception',
            'InterfaceError': 'Error',
            'DatabaseError': 'Error',
            'InternalError': 'DatabaseError',
            'OperationalError': 'DatabaseError',
            'ProgrammingError': 'DatabaseError',
            'IntegrityError': 'DatabaseError',
            'DataError': 'DatabaseError',
            'NotSupportedError': 'DatabaseError'
        }

    return class_hierarchy_param_dict


class_hierarchy_param_dict = error_class_hierarchy()
print(class_hierarchy_param_dict)


# api for bid sample dataset
influenza_who_xmart_enpoint = 'https://xmart-api-public.who.int/FLUMART/VIW_FID?$format=csv'
