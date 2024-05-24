# Employee Management System

Это приложение представляет собой систему управления сотрудниками и филиалами компании.

## Функциональность

- Добавление и редактирование сотрудников.
- Добавление и редактирование филиалов.
- Экспорт списка сотрудников в форматы XLSX и DOCX.

## Структура проекта

- **db**: Каталог с базой данных SQLite.
- **output_files**: Каталог для сохранения экспортированных файлов.
- **src**: Сам проект.
### SQL
```sql
CREATE TABLE Branches (
    branch_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    director_id INTEGER DEFAULT NULL,
    FOREIGN KEY (director_id) REFERENCES Employees(employee_id)
);

CREATE TABLE Employees (
    employee_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    position TEXT NOT NULL,
    branch_id INTEGER,
    FOREIGN KEY (branch_id) REFERENCES Branches(branch_id)
);

```

## Требования к установке

Для работы приложения необходимо установить следующие зависимости:

- Python 3
- PyQt5
- openpyxl
- python-docx

Вы можете установить зависимости с помощью pip:

```bash
pip install -r requirements.txt
```

## Запуск приложения

1. Клонируйте репозиторий:

```bash
git clone https://github.com/s1zzen/contest_employee_managment
```

2. Перейдите в каталог проекта:

```bash
cd contest_employee_management
```

3. Устанавливаете зависимости:

```bash
pip install -r requirements.txt
```

4. Запустите приложение:

```bash
python main.py
```
