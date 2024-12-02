class Patient:
   def __init__(self, name, age, gender, insurance,record):
       self.name = name
       self.age = age
       self.gender = gender
       self.insurance = insurance
       self.record = record

   def admit_patient (self, adm_date):
       self.record["admit"] = adm_date

   def add_insurance(self, addl_co, addl_acct):
       self.insurance["second"] = addl_co
       self.insurance["acct2"] = addl_acct

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

    patient_1.add_insurance("NuCo", "98765")
    print(patient_1.insurance)

    p2 = Pediatric_Patient("Sue",7,"F",{"co":"InsCo", "acct":"12345"}, {}, "Steve" )
    print(p2.guardian)