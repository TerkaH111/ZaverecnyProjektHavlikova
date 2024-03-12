from insured_person import InsuredPerson
from insurance_database import InsuranceDatabase
import re


class InsuranceApp:
    def __init__(self):
        self.database = InsuranceDatabase()

    def valid_name(self, name):
        pattern = r"^(?!.*([A-Za-zÁáČčĎďÉéĚěÍíŇňÓóŘřŠšŤťÚúŮůÝýŽž\s])\1{2})[A-Za-zÁáČčĎďÉéĚěÍíŇňÓóŘřŠšŤťÚúŮůÝýŽž\s]{2,}$"
        return bool(re.match(pattern, name))

    def phone_number_validation(self, phone_number):
        pattern = r"^\d{9}$"
        return bool(re.match(pattern, phone_number))

    def running(self):
        while True:
            print("Evidence pojištěných:")
            print("1. Přidat nového pojištěnce")
            print("2. Vypsat všechny pojištěnce")
            print("3. Vyhledat pojištěného")
            print("4. Konec")
            choice = input("Vyberte si akci: ")

            if choice == '1':

                while True:
                    first_name = input("Zadejte křestní jméno: ")
                    last_name = input("Zadejte příjmení: ")
                    if self.valid_name(first_name) and self.valid_name(last_name):
                        break
                    else:
                        print("Neplatné jméno. Zadejte znovu. ")

                while True:
                    age = input("Zadejte věk: ")
                    if age.isdigit():
                        break
                    else:
                        print("Neplatný věk, zadejte znovu")

                while True:
                    phone_number = input("Zadejte telefonní číslo: ")
                    if self.phone_number_validation(phone_number):
                        break
                    else:
                        print("Neplatné telefonní číslo. Zadejte znovu. ")

                person = InsuredPerson(first_name, last_name, age, phone_number)
                self.database.add_insured_person(person)
                print("Data byla uložena.")

            elif choice == '2':
                print("Seznam pojištěnců:")
                self.database.display_all()

            elif choice == '3':
                first_name = input("Zadejte jméno: ")
                last_name = input("Zadejte příjmení: ")
                person = self.database.search_by_name(first_name, last_name)
                if person:
                    print(person)
                else:
                    print("Osoba nenalezena.")

            elif choice == '4':
                print("Ukončuji aplikaci.")
                break

            else:
                print("Neplatná volba. Zadejte znovu.")




