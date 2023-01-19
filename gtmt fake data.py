from faker import Faker
import unidecode
import random

class GtmtFake :
    def __init__(self):
        self.fake = Faker(locale="fr_FR")

    def person(self, count, id):
        msg = f"Email;Nom;Prenom;Societe;Adresse;Ville;Code Postal;Telephone;ID\n"
        for i in range(count):
            email = self.fake.email()
            nom = self.fake.last_name()
            prenom = self.fake.first_name()
            societe = self.fake.company()
            adresse = self.fake.street_address().replace(",","")
            adresse.strip(",")
            ville = self.fake.city()
            codePostal = self.fake.postcode()
            telephone = self.fake.phone_number()
            # contactKey = id + str(10**(len(str(count))-1)+ i + 1) # need to delete 1
            # contactKey = id + str(i) # need to delete 1
            contactKey = 1200 + i 

            
            msg += f"{email};{nom};{prenom};{societe};{adresse};{ville};{codePostal};{telephone};{contactKey}\n"
            msg = unidecode.unidecode(msg)

            if (count > 100) & ((i % (count / 100)) == 0):
                percentage = i / (count / 100)
                print(f"{percentage}%", end='\r')
        return msg

if __name__ == '__main__':
    f = GtmtFake()
    # r = random
    count = 500      # number of contacts
    numLists = 1        # number of csv files
    fileName = "500"     # file marker
    date = "221109"     # date

    for i in range(numLists):
        data = f.person(count, f"{date}{i+1}")
 
        with open(f"gtmt_contacts_hw_{fileName}_p{1200}.csv", "w") as d:
            d.write(data)
