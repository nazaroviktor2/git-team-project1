"""Main file."""

from functions.encryption import encrypt_by_tsezar
from functions.file import save_text_to_file

if __name__ == '__main__':
    commands = {
        "0": "Список команд",
        "1": 'Шифрование методом Цезаря',
    }
    print("Список команд: ")
    for name_com, text_com in commands.items():
        print("{0} - {1}".format(name_com, text_com))
    user_input = input('Введите номер команды из списка, чтобы запустить ее (q to exit): ')
    while True:
        if user_input == "q":
            print("Конец работы ")
            break
        elif user_input == "0":
            print("Список команд: ")
            for name, text in commands.items():
                print("{0} - {1}".format(name, text))

        elif user_input == "1":
            print("Введите текст для шифрования (поддерживает только англиский язык)")
            text_for_encrypt = input()
            print("Введите ключ для шифрование (число)")
            try:
                key = int(input())
            except ValueError:
                print("Введен не верный ключ! Ключем может быть любое число ")
            else:
                encrypt_text = encrypt_by_tsezar(text_for_encrypt, key)
                print("Зашифрованный текст: ")
                print(encrypt_text)
                file_name = input("Для сохрание текста в файл, ввидете имя файла иначе нажмите enter: ")
                if file_name != "":
                    file_path = save_text_to_file(encrypt_text, file_name)
                    print("Файл сохранен в {0}".format(file_path))
        else:
            print("Не известная команда")

        user_input = input('Введите номер команды из списка, чтобы запустить ее (q to exit): ')
