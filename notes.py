from datetime import datetime
import json
import os
import csv

class Note:
    def __init__(self, id : int, title : str, content : str, timestamp = None):
        if not title:
            raise ValueError("Заголовок заметки - обязательное поле")
        self.id = id
        self.title = title
        self.content = content if content else None
        self.timestamp = datetime.strptime(timestamp, "%d-%m-%Y %H:%M:%S") if timestamp else datetime.now()

    def to_dict(self):
        return  dict(id = self.id, title = self.title, content = self.content, timestamp = self.timestamp.strftime("%d-%m-%Y %H:%M:%S"))

    @staticmethod
    def from_dict(data : dict):
        return Note(data['id'], data['title'], data['content'], data['timestamp'])

    def __str__(self):
        return f"Заметка с ID: {self.id}, Заголовок: {self.title}, Содержимое: {self.content}, Время создания/Изменения: {self.timestamp}"

    @staticmethod
    def load_notes():
        if not os.path.exists('notes.json'):
            return []
        with open('notes.json', 'r', encoding="utf-8") as file:
            data = json.load(file)
            return [Note.from_dict(note) for note in data]

    @staticmethod
    def save_notes(notes):
        with open('notes.json', 'w', encoding='utf-8') as file:
            data = [note.to_dict() for note in notes]
            json.dump(data, file, ensure_ascii=False, indent=4)

    @staticmethod
    def create_note(title, content : str = None):
        notes = Note.load_notes()
        note_id = 1
        for note in notes:
            note_id = max(note_id, note.id + 1)
        new_node = Note(note_id, title, content)
        notes.append(new_node)
        Note.save_notes(notes)

    @staticmethod
    def show_notes():
        notes = Note.load_notes()
        if len(notes) == 0:
            print('Заметок нет')
        else:
            for note in notes:
                print(note)

    @staticmethod
    def show_note(note_id : int):
        notes = Note.load_notes()
        for note in notes:
            if note.id == note_id:
                print(note)
                return
        print(f'Заметка с ID {note_id} не найдена')

    @staticmethod
    def edit_note(note_id : int, new_title : str = None, new_content : str = None):
        notes = Note.load_notes()
        for i, note in enumerate(notes):
            if note.id == note_id:
                if new_title:
                    note.title = new_title
                if new_content:
                    note.content = new_content
                note.timestamp = datetime.now()
                Note.save_notes(notes)
                print(f'Заметка с ID {note_id} успешно изменена')
                return
        print(f'Заметка с ID {note_id} не найдена')

    @staticmethod
    def delete_note(note_id : int):
        notes = Note.load_notes()
        l1 = len(notes)
        notes = [note for note in notes if note.id != note_id]
        l2 = len(notes)
        Note.save_notes(notes)
        if l1 != l2:
            print(f'Заметка с ID {note_id} успешно удалена')
        else:
            print(f'Заметки с ID {note_id} не существует')

    @staticmethod
    def export_notes_to_csv(file_name):
        if not file_name:
            file_name = "notes.csv"
        notes = Note.load_notes()
        with open(file_name, 'w', encoding = 'utf-8', newline = '') as file:
            writer = csv.writer(file)
            writer.writerow(["ID", "Title", "Content", "Timestamp"])
            for note in notes:
                writer.writerow([note.id, note.title, note.content, note.timestamp.strftime("%d-%m-%Y %H:%M:%S")])
        print(f"Заметки успешно экспортированы в {file_name}.")

    @staticmethod
    def import_notes_from_csv(file_name):
        if not file_name:
            file_name = "notes.csv"
        notes = []
        with open(file_name, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                content = row['Content'] if row['Content'] else None
                timestamp = row['Timestamp'] if row['Timestamp'] else datetime.now().strftime("%d-%m-%Y %H:%M:%S")
                notes.append(Note(int(row['ID']), row['Title'], content, timestamp))
        Note.save_notes(notes)
        print(f"Заметки успешно импортированы из {file_name}.")
