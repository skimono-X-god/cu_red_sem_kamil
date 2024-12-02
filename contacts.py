import json
import os
import csv

class Contact:
    def __init__(self, id : int, name : str = None, phone : str = None, email : str = None):
        if not name:
            raise ValueError("Имя контакта - обязательное поле")
        self.id = id
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        return f"ID: {self.id}, Имя: {self.name}, Телефон: {self.phone}, Электронная почта: {self.email}"

    def to_dict(self):
        return dict(id = self.id, name = self.name, phone = self.phone, email = self.email)

    @staticmethod
    def from_dict(data: dict):
        return Contact(id = data['id'], name = data['name'], phone = data['phone'], email = data['email'])

    @staticmethod
    def load_contacts():
        if not os.path.exists('contacts.json'):
            return []
        with open('contacts.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
            return [Contact.from_dict(contact) for contact in data]

    @staticmethod
    def save_contacts(contacts):
        with open('contacts.json', 'w', encoding='utf-8') as file:
            data = [contact.to_dict() for contact in contacts]
            json.dump(data, file, ensure_ascii=False, indent=4)

    @staticmethod
    def create_contact(name : str = None, phone : str = None, email : str = None):
        contacts = Contact.load_contacts()
        contact_id = 1
        for contact in contacts:
            contact_id = max(contact_id, contact.id + 1)
        new_contact = Contact(contact_id, name, phone, email)
        contacts.append(new_contact)
        Contact.save_contacts(contacts)

    @staticmethod
    def find_contact(contact_id):
        contacts = Contact.load_contacts()
        for contact in contacts:
            if contact.id == contact_id:
                print(contact)
                return
        print(f"Контакт с ID{contact_id} не найден")

    @staticmethod
    def edit_contact(contact_id : int, new_name : str = None, new_phone : str = None, new_email : str = None):
        contacts = Contact.load_contacts()
        for i, contact in enumerate(contacts):
            if contact.id == contact_id:
                if new_name:
                    contact.name = new_name
                if new_phone:
                    contact.phone = new_phone
                if new_email:
                    contact.email = new_email
                Contact.save_contacts(contacts)
                print(f"Контакт с ID {contact_id} успешно изменен")
                return
        print(f"Контакт с ID {contact_id} не найден")

    @staticmethod
    def delete_contact(contact_id):
        contacts = Contact.load_contacts()
        l1 = len(contacts)
        contacts = [contact for contact in contacts if contact.id!= contact_id]
        l2 = len(contacts)
        Contact.save_contacts(contacts)
        if l1!= l2:
            print(f"Контакт с ID {contact_id} успешно удален")
        else:
            print(f"Контакта с ID {contact_id} не существует")

    @staticmethod
    def export_contacts_to_csv(file_name : str = None):
        if not file_name:
            file_name = "contacts.csv"
        contacts = Contact.load_contacts()
        with open(file_name, 'w', encoding='utf-8', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["ID", "Name", "Phone", "Email"])
            for contact in contacts:
                writer.writerow([contact.id, contact.name, contact.phone, contact.email])
        print(f"Контакты успешно экспортированы в {file_name}.")

    @staticmethod
    def import_contacts_from_csv(file_name : str = None):
        if not file_name:
            file_name = "contacts.csv"
        contacts = []
        with open(file_name, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                contact_id = row['ID'] if row['ID'] else None
                contact_name = row['Name'] if row['Name'] else None
                contact_phone = row['Phone'] if row['Phone'] else None
                contact_email = row['Email'] if row['Email'] else None
                contacts.append(Contact(int(contact_id), contact_name, contact_phone, contact_email))
            Contact.save_contacts(contacts)
