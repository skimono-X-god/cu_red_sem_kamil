import json
import os
import csv
from datetime import datetime

class FinanceRecord:
    def __init__(self, id : int, amount : float = 0.0, category : str = None, date : str = None, description : str = None):
        self.id = id
        self.amount = amount
        self.category = category
        self.date = date
        self.description = description

    def __str__(self):
        return f"ID: {self.id}, Сумма: {self.amount}, Категория: {self.category}, Дата: {self.date}, Описание: {self.description}"

    def to_dict(self):
        return dict(id = self.id, amount = self.amount, category = self.category, date = self.date, description = self.description)

    @staticmethod
    def from_dict(data : dict):
        return FinanceRecord(data['id'], data['amount'], data['category'], data['date'], data['description'])

    @staticmethod
    def load_records():
        if not os.path.exists('finance.json'):
            return []
        with open('finance.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
            return [FinanceRecord.from_dict(record) for record in data]

    @staticmethod
    def save_records(records):
        with open('finance.json', 'w', encoding='utf-8') as file:
            data = [record.to_dict() for record in records]
            json.dump(data, file, ensure_ascii=False, indent=4)

    @staticmethod
    def create_record(amount : float, category : str = None, date : str = None, description : str = None):
        records = FinanceRecord.load_records()
        record_id = 1
        for record in records:
            record_id = max(record_id, record.id + 1)
        new_record = FinanceRecord(record_id, amount, category, date, description)
        records.append(new_record)
        FinanceRecord.save_records(records)

    @staticmethod
    def show_records():
        records = FinanceRecord.load_records()
        if len(records) == 0:
            print('Записей в базе нет')
        else:
            for record in records:
                print(record)

    @staticmethod
    def delete_record(record_id):
        records = FinanceRecord.load_records()
        l1 = len(records)
        records = [record for record in records if record.id != record_id]
        l2 = len(records)
        FinanceRecord.save_records(records)
        if l1 != l2:
            print(f'Запись с ID {record_id} успешно удалена')
        else:
            print(f'Записи с ID {record_id} не существует')

    @staticmethod
    def filter_records_by_date(start_date: str, end_date: str):
        records = FinanceRecord.load_records()
        start_date = datetime.strptime(start_date, "%d-%m-%Y")
        end_date = datetime.strptime(end_date, "%d-%m-%Y")
        filtered_records = []
        for record in records:
            if record.date:
                record_date = datetime.strptime(record.date, "%d-%m-%Y")
                if start_date <= record_date <= end_date:
                    filtered_records.append(record)
        return filtered_records

    @staticmethod
    def generate_report(start_date: str, end_date: str):
        filtered_records = FinanceRecord.filter_records_by_date(start_date, end_date)
        income = sum(record.amount for record in filtered_records if record.amount > 0)
        expense = sum(record.amount for record in filtered_records if record.amount < 0)
        balance = income + expense
        print(f"Финансовый отчёт за период с {start_date} по {end_date}:")
        print(f" - Общий доход: {income} руб.")
        print(f" - Общий расход: {expense} руб.")
        print(f" - Баланс: {balance} руб.")

    @staticmethod
    def export_records_to_csv(file_name : str = None):
        if not file_name:
            file_name = "records.csv"
        records = FinanceRecord.load_records()
        with open(file_name, 'w', encoding='utf-8', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["ID", "Amount", "Category", "Date", "Description"])
            for record in records:
                writer.writerow([record.id, record.amount, record.category, record.date, record.description])
        print(f"Контакты успешно экспортированы в {file_name}.")

    @staticmethod
    def import_records_from_csv(file_name : str = None):
        if not file_name:
            file_name = "records.csv"
        records = []
        with open(file_name, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                record_id = row['ID'] if row['ID'] else None
                record_amount = row['Amount'] if row['Amount'] else None
                record_category = row['Category'] if row['Category'] else None
                record_date = row['Date'] if row['Date'] else None
                record_description = row['Description'] if row['Description'] else None
                records.append(FinanceRecord(int(record_id), float(record_amount), record_category, record_date, record_description))
            FinanceRecord.save_records(records)
