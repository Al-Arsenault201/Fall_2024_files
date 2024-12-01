"""
Starter code for CMSC 201 Section 60 Homework 6. This code begins the definition of the class "Patient"
and its subclass, "Pediatric_Patient".  An init method and one other method are defined for
each class.
"""




class Patient:
   def __init__(self, name, age, gender, insurance,record):
       self.name = name
       self.age = age
       self.gender = gender
       self.insurance = insurance
       self.record = record


   def admit_patient (self, adm_date):
       self.record["admit"] = adm_date


# def discharge_patient(self, discharge_date):
# write the body of this method:
# add a field to "record" - call it "discharge" and give it the value "discharge_date"


class Pediatric_Patient(Patient):
   def __init__(self, name, age, gender, insurance, record, guardian):
       super().__init__(name, age, gender, insurance, record)
       self.guardian = guardian




if __name__ == "__main__":


   #create a patient named "Joe"
   patient_1 = Patient("Joe", 54, "M", {"co":"InsCo", "acct":"12345"}, {})
   # now add an admission date
   patient_1.admit_patient("02/15/2024")


   # now check to see if it worked
   print(patient_1.record)


   p2 = Pediatric_Patient("Sue",7,"F",{"co":"InsCo", "acct":"12345"}, {}, "Steve" )
   print(p2.guardian)


