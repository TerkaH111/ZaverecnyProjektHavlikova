class InsuranceDatabase:
    def __init__(self):
        self.insured_people = []

    def add_insured_person(self, person):
        self.insured_people.append(person)

    def search_by_name(self, first_name, last_name):
        for person in self.insured_people:
            if person.first_name == first_name and person.last_name == last_name:
                return person
        return None

    def display_all(self):
        for person in self.insured_people:
            print(person)



