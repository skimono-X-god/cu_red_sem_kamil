from financerecords import FinanceRecord
from contacts import Contact
from tasks import Task
from notes import Note

while True:
    print("Добро пожаловать в Персональный помощник!")
    print("Выберите действие:")
    print("1. Управление заметками")
    print("2. Управление задачами")
    print("3. Управление контактами")
    print("4. Управление финансовыми записями")
    print("5. Калькулятор")
    print("6. Выход")
    action = input("Введите номер действия: ")
    if action == "1":
        while True:
            print("Управление заметками:")
            print("1. Создание новой заметки")
            print("2. Просмотр списка заметок")
            print("3. Просмотр подробностей заметки")
            print("4. Редактирование заметки")
            print("5. Удаление заметки")
            print("6. Импорт заметок из CSV")
            print("7. Экспорт заметок в CSV")
            print("8. Назад")
            sub_action = input("Введите номер действия: ")
            if sub_action == "1":
                try:
                    title = input("Введите название заметки: ")
                    content = input("Введите содержимое заметки(необязательно): ")
                    Note.create_note(title, content)
                except Exception as error:
                    print(f"Технические шоколадки. Проверьте корректность ввода. {error}")
            elif sub_action == "2":
                try:
                    Note.show_notes()
                except Exception as error:
                    print(f"Технические шоколадки. Проверьте корректность ввода. {error}")
            elif sub_action == "3":
                try:
                    note_id = int(input("Введите ID заметки, которую хотите увидеть: "))
                    Note.show_note(note_id)
                except Exception as error:
                    print(f"Технические шоколадки. Проверьте корректность ввода. {error}")
            elif sub_action == "4":
                try:
                    note_id = int(input("Введите ID заметки, которую хотите отредактировать(целое число): "))
                    new_title = input("Введите новое название для заметки(необязательно): ")
                    new_content = input("Введите новое содержимое для заметки(необязательно): ")
                    Note.edit_note(note_id, new_title, new_content)
                except Exception as error:
                    print(f"Технические шоколадки. Проверьте корректность ввода. {error}")
            elif sub_action == "5":
                try:
                    note_id = int(input("Введите ID заметки, которую хотите удалить(целое число): "))
                    Note.delete_note(note_id)
                except Exception as error:
                    print(f"Технические шоколадки. Проверьте корректность ввода. {error}")
            elif sub_action == "6":
                try:
                    file_name = input("Введите имя файла для импорта заметок из CSV(по-умолчанию будет файл notes.csv): ")
                    Note.import_notes_from_csv(file_name)
                except Exception as error:
                    print(f"Технические шоколадки. Проверьте корректность ввода. {error}")
            elif sub_action == "7":
                try:
                    file_name = input("Введите имя файла для экспорта заметок в CSV(по-умолчанию будет файл notes.csv): ")
                    Note.export_notes_to_csv(file_name)
                except Exception as error:
                    print(f"Технические шоколадки. Проверьте корректность ввода. {error}")
            elif sub_action == "8":
                break
            else:
                print("Читать научись блять!")
    elif action == "2":
        while True:
            print("Управление задачами:")
            print("1. Создание новой задачи")
            print("2. Просмотреть задачи")
            print("3. Отметить задачу как выполненную")
            print("4. Редактировать задачу")
            print("5. Удалить задачу")
            print("6. Экспорт задач в CSV")
            print("7. Импорт задач из CSV")
            print("8. Назад")
            sub_action = input("Введите номер действия: ")
            if sub_action == "1":
                try:
                    title = input("Введите название задачи: ")
                    description = input("Введите описание задачи(необязательно): ")
                    done = input("Введите выполнена ли задача(True/False, по умолчанию False)")
                    if done == "True":
                        done = True
                    else:
                        done = False
                    priority = input("Укажите приоритет(Низкий, Средний, Высокий): ")
                    due_date = input("Укажите дедлайн(формат ДД-ММ-ГГГГ): ")
                    Task.create_task(title = title, description = description, priority = priority, done = done, due_date = due_date)
                except Exception as error:
                    print(f"Технические шоколадки. Проверьте корректность ввода. {error}")
            elif sub_action == "2":
                try:
                    Task.show_tasks()
                except Exception as error:
                    print(f"Технические шоколадки. Проверьте корректность ввода. {error}")
            elif sub_action == "3":
                try:
                    task_id = int(input("Введите ID задачи, которую хотите отметить, как выполненную(целое число): "))
                    Task.mark_task_as_done(task_id)
                except Exception as error:
                    print(f"Технические шоколадки. Проверьте корректность ввода. {error}")
            elif sub_action == "4":
                try:
                    task_id = int(input("Введите ID задачи, которую хотите отредактировать(целое число): "))
                    title = input("Введите новое название задачи(необязательно): ")
                    description = input("Введите новое описание задачи(необязательно): ")
                    done = input("Введите выполнена ли задача(True/False, по умолчанию False)")
                    if done == "True":
                        done = True
                    elif done == "False":
                        done = False
                    else:
                        done = None
                    priority = input("Укажите новый приоритет(Низкий, Средний, Высокий)(необязательно): ")
                    due_date = input("Укажите новый дедлайн(формат ДД-ММ-ГГГГ)(необязательно): ")
                    Task.edit_task(task_id = task_id, new_title = title, new_description = description, new_done = done, new_priority = priority, new_due_date = due_date)
                except Exception as error:
                    print(f"Технические шоколадки. Проверьте корректность ввода. {error}")
            elif sub_action == "5":
                try:
                    task_id = int(input("Введите ID задачи, которую хотите удалить(целое число): "))
                    Task.delete_task(task_id)
                except Exception as error:
                    print(f"Технические шоколадки. Проверьте корректность ввода. {error}")
            elif sub_action == "6":
                try:
                    file_name = input("Введите имя файла для экспорта задач в CSV(по-умолчанию будет файл tasks.csv): ")
                    Task.export_tasks_to_csv(file_name)
                except Exception as error:
                    print(f"Технические шоколадки. Проверьте корректность ввода. {error}")
            elif sub_action == "7":
                try:
                    file_name = input("Введите имя файла для импорта задач из CSV(по-умолчанию будет файл tasks.csv): ")
                    Task.import_tasks_from_csv(file_name)
                except Exception as error:
                    print(f"Технические шоколадки. Проверьте корректность ввода. {error}")
            elif sub_action == "8":
                break
            else:
                print("Читать научись блять!")
    elif action == "3":
        while True:
            print("Управление контактами:")
            print("1. Добавление нового контакта")
            print("2. Поиск контакта по имени или номеру телефона")
            print("3. Редактирование контакта")
            print("4. Удаление контакта")
            print("5. Экспорт контактов в CSV")
            print("6. Импорт контактов из CSV")
            print("7. Назад")
            sub_action = input("Введите номер действия: ")
            if sub_action == "1":
                try:
                    name = input("Введите имя контакта: ")
                    phone_number = input("Введите номер телефона контакта(необязательно): ")
                    email = input("Введите адрес электронной почты(необязательно): ")
                    Contact.create_contact(name, phone_number, email)
                except Exception as error:
                    print(f"Технические шоколадки. Проверьте корректность ввода. {error}")
            elif sub_action == "2":
                try:
                    contact_id = int(input("Введите ID контакта, который хотите увидеть(целое число): "))
                    Contact.find_contact(contact_id)
                except Exception as error:
                    print(f"Технические шоколадки. Проверьте корректность ввода. {error}")
            elif sub_action == "3":
                try:
                    contact_id = int(input("Введите ID контакта, который хотите отредактировать(целое число): "))
                    name = input("Введите новое имя контакта(необязательно): ")
                    phone = input("Введите новый номер телефона контакта(необязательно): ")
                    email = input("Введите новый email контакта(необязательно): ")
                    Contact.edit_contact(contact_id = contact_id, new_name = name, new_phone = phone, new_email = email)
                except Exception as error:
                    print(f"Технические шоколадки. Проверьте корректность ввода. {error}")
            elif sub_action == "4":
                try:
                    contact_id = int(input("Введите ID контакта, который хотите удалить(целое число): "))
                    Contact.delete_contact(contact_id)
                except Exception as error:
                    print(f"Технические шоколадки. Проверьте корректность ввода. {error}")
            elif sub_action == "5":
                try:
                    file_name = input("Введите имя файла для экспорта контактов в CSV(по-умолчанию будет файл contacts.csv): ")
                    Contact.export_contacts_to_csv(file_name)
                except Exception as error:
                    print(f"Технические шоколадки. Проверьте корректность ввода. {error}")
            elif sub_action == "6":
                try:
                    file_name = input("Введите имя файла для импорта контактов из CSV(по-умолчанию будет файл contacts.csv): ")
                    Contact.import_contacts_from_csv(file_name)
                except Exception as error:
                    print(f"Технические шоколадки. Проверьте корректность ввода. {error}")
            if sub_action == "7":
                break
    elif action == "4":
        while True:
            print("Управление финансовыми записями:")
            print("1. Добавить новую запись")
            print("2. Просмотреть все записи")
            print("3. Генерация отчёта")
            print("4. Удалить запись")
            print("5. Экспорт финансовых записей в CSV")
            print("6. Импорт финансовых записей из CSV")
            print("7. Назад")
            sub_action = input("Введите номер действия: ")
            if sub_action == "1":
                try:
                    amount = float(input("Введите сумму операции(положительное число для доходов, отрицательное для расходов): "))
                    category = input("Введите категорию: ")
                    date = input("Введите дату операции: ")
                    description = input("Введите описание операции: ")
                    FinanceRecord.create_record(amount=amount, category=category, date=date, description=description)
                except Exception as error:
                    print(f"Технические шоколадки. Проверьте корректность ввода. {error}")
            elif sub_action == "2":
                try:
                    FinanceRecord.show_records()
                except Exception as error:
                    print(f"Технические шоколадки. Проверьте корректность ввода. {error}")
            elif sub_action == "3":
                try:
                    start_data = input("Введите начальную дату (ДД-ММ-ГГГГ): ")
                    end_data = input("Введите конечную дату (ДД-ММ-ГГГГ): ")
                    FinanceRecord.generate_report(start_data, end_data)
                except Exception as error:
                    print(f"Технические шоколадки. Проверьте корректность ввода. {error}")
            elif sub_action == "4":
                try:
                    contact_id = int(input("Введите ID записи, которую хотите удалить(целое число): "))
                    FinanceRecord.delete_record(contact_id)
                except Exception as error:
                    print(f"Технические шоколадки. Проверьте корректность ввода. {error}")
            elif sub_action == "5":
                try:
                    file_name = input("Введите имя файла для экспорта записей в CSV(по-умолчанию будет файл records.csv): ")
                    FinanceRecord.export_records_to_csv(file_name)
                except Exception as error:
                    print(f"Технические шоколадки. Проверьте корректность ввода. {error}")
            elif sub_action == "6":
                try:
                    file_name = input("Введите имя файла для экспорта записей из CSV(по-умолчанию будет файл records.csv): ")
                    FinanceRecord.import_records_from_csv(file_name)
                except Exception as error:
                    print(f"Технические шоколадки. Проверьте корректность ввода. {error}")
            elif sub_action == "7":
                break
            else:
                print("Читать научись блять!")
    elif action == "5":
        while True:
            print("Калькулятор:")
            print("1. Арифметическая операция")
            print("2. Назад")
            sub_action = input("Введите номер действия: ")
            if sub_action == "1":
                try:
                    expression = input("Введите арифметическое выражение: ").strip()
                    allowed_chars = "0123456789+-*/(). "
                    if not all(char in allowed_chars for char in expression):
                        raise ValueError("Выражение содержит недопустимые символы.")
                    result = eval(expression)
                    print(f"Результат: {result}")
                except ZeroDivisionError:
                    print("Ошибка: Деление на ноль.")
                except ValueError as error:
                    print(f"Ошибка: {error}")
                except Exception as error:
                    print(f"Произошла ошибка: {error}")
            elif sub_action == "2":
                break
            else:
                print("Читать научись блять!")
    elif action == "6":
        print("Adios Payasos!")
        break
    else:
        print("Читать научись блять!")