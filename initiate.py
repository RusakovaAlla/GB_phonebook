import add_contact
import export_phb
import import_phb

if __name__ == "__main__":
    answer = input("Работаем со справочником? Да/нет ")
    while answer != 'нет':
        action = input("Какое действие выполним? добавить/экспорт/импорт/ ")
        if action == "добавить":
            add_contact.add_contact_manual_user()
        elif action == "экспорт":
            export_phb.export_format()
        elif action == "импорт":
            file_to_import = input("Укажите путь к файлу: ")
            import_phb.lets_import(file_to_import)
        else:
            break
    else:
        print("В другой раз")
