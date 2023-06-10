import json
import csv
import datetime

# Функция для чтения списка заметок из файла
def read_notes_file(file_name):
    with open(file_name, 'r') as f:
        notes = json.load(f)
        return notes

# Функция для сохранения списка заметок в json формате
def save_notes_json(notes, file_name):
    with open(file_name, 'w') as f:
        json.dump(notes, f)

# Функция для сохранения списка заметок в csv формате
def save_notes_csv(notes, file_name):
    with open(file_name, 'w') as f:
        writer = csv.writer(f, delimiter=';')
    for note in notes:
        writer.writerow([note['id'], note['title'], note['body'], note['timestamp']])

# Функция для фильтрации заметок по дате
def filter_notes_by_date(notes, date):
    filtered_notes = []
    for note in notes:
        note_date = datetime.datetime.strptime(note['timestamp'], '%Y-%m-%d %H:%M:%S.%f')
        if note_date.date() == date:
            filtered_notes.append(note)
    return filtered_notes

# Функция для вывода на экран выбранной записи или всего списка заметок<br>
def print_notes(notes):
    if not notes:
        print('Заметок не найдено')
    else:
        for note in notes:
            print(f'ID: {note["id"]}')
            print(f'Заголовок: {note["title"]}')
            print(f'Тело заметки: {note["body"]}')
            print(f'Дата/время: {note["timestamp"]}')
            print('---')

# Функция для добавления новой записки
def add_note(notes):
    id = len(notes) + 1
    title = input('Введите заголовок: ')
    body = input('Введите тело заметки: ')
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
    new_note = {'id': id, 'title': title, 'body': body, 'timestamp': timestamp}
    notes.append(new_note)
    return notes

# Функция для редактирования записки
def edit_note(notes, id):
    for note in notes:
        if note['id'] == id:
            new_title = input(f'Введите новый заголовок (было: {note["title"]}): ')
        new_body = input(f'Введите новое тело заметки (было: {note["body"]}): ')
        note['title'] = new_title
        note['body'] = new_body
        note['timestamp'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
        break
    return notes

# Функция для удаления записки
def delete_note(notes, id):
    for note in notes:
        if note['id'] == id:
            notes.remove(note)
        break
    return notes

# Главная функция, которая выполняет все действия
def main():
    file_name = 'notes.json'
    notes = read_notes_file(file_name)

    while True:
        print('Выберите действие:')
        print('1. Вывести все заметки')
        print('2. Вывести заметки за определенную дату')
        print('3. Вывести конкретную заметку')
        print('4. Добавить новую заметку')
        print('5. Редактировать заметку')
        print('6. Удалить заметку')
        print('7. Выход')

        choice = input('Ваш выбор: ')

        if choice == '1':
            print_notes(notes)
        elif choice == '2':
            date_str = input('Введите дату в формате ГГГГ-ММ-ДД: ')
            date = datetime.datetime.strptime(date_str, '%Y-%m-%d').date()
            filtered_notes = filter_notes_by_date(notes, date)
            print_notes(filtered_notes)
        elif choice == '3':
            id = int(input('Введите ID заметки: '))
            note = [note for note in notes if note['id'] == id]
            print_notes(note)
        elif choice == '4':
            notes = add_note(notes)
            save_notes_json(notes, file_name)
        elif choice == '5':
            id = int(input('Введите ID заметки для редактирования: '))
            notes = edit_note(notes, id)
            save_notes_json(notes, file_name)
        elif choice == '6':
            id = int(input('Введите ID заметки для удаления: '))
            otes = delete_note(notes, id)
            save_notes_json(notes, file_name)
        elif choice == '7':
            break
        else:
            print('Недопустимый выбор')

if __name__ == '__main__':
    main()