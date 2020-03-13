import os
from glob import glob
import re
import xml.etree.ElementTree as ElTree
from datetime import datetime

timez = datetime.now().strftime('%Y-%m-%d_%H-%M')
root = os.getcwd()  # папка запуска скрипта. (Скрипт размещать в корне папки с игрой, рядом с папкой game)
orig_dir = bak_dir = ''
suffix_orig = '_orig.txt'  # дописывается к имени текстового файла с оригинальной дорожкой
suffix_tran = '_tran.txt'  # дописывается к имени текстового файла с переводом
                           # (или таким должно быть окончание файла-источника перевода)
suffix_old = '.bak'  # дописывается к имени файла резервной копии
include_voice = False  # вытаскивать строки голоса в файл (по умолчанию - пропускаем [False])
source_lang = 'russian'  # исходный язык (для xliff-файлов)
lang = 'english'  # язык назначения, совпадает с именем папки в tl
copy_dir_structure = False  # копировать структуру папок в виде дерева
                            # или прописывать в имени файла, разделяя символом "-"
compare_without_emotion = True  # сравнивать имена без эмоций при подстановке из старых tl-файлов

# возвращает текст между кавычками
def only_text(st):
    first = st.find('"')
    end = st.rfind('"')
    return st[first + 1:end]


# стоп-слово для приостановки работы скрипта
def stop():
    a = input('Press Enter to continue or "s" to stop\n')
    if a == "s":
        exit()


# вытаскивает оригинальную дорожку в текстовый файл
def parser(filename):
    FILENAME = filename
    if copy_dir_structure:
        rel_path = os.path.split(filename)[0].replace(root + "\\game\\tl\\" + lang, orig_dir)
        cur_file = rel_path + '\\' + os.path.splitext(os.path.split(filename)[1])[0] + suffix_orig
        try:
            os.makedirs(rel_path)
        except FileExistsError:
            pass
    else:
        rel_path = os.path.split(filename)[0].replace(root + "\\game\\tl\\" + lang, '').replace("\\", "-")[1:]
        if rel_path != '':
            cur_file = orig_dir + '\\' + rel_path + "-" + os.path.splitext(os.path.split(filename)[1])[0] + suffix_orig
        else:
            cur_file = orig_dir + '\\' + os.path.splitext(os.path.split(filename)[1])[0] + suffix_orig

    with open(FILENAME, "r", encoding='utf-8') as f:
        massiv = f.readlines()

    f2 = open(cur_file, 'w', encoding='utf-8')
    f2.close()

    for i, line in enumerate(massiv, start=0):
        if ".rpy:" in line:
            if "translate" in massiv[i + 1]:
                st = i + 3
                len_block = 0
                while re.match(r'^\s+#', massiv[st]) is not None:
                    if re.match(r'^\s+# voice', massiv[st]) and not include_voice:
                        len_block += 1
                    else:
                        with open(cur_file, 'a', encoding='utf-8') as f2:
                            f2.write(massiv[st + len_block])
                    st += 1

            elif "old" in massiv[i + 1]:
                with open(cur_file, 'a', encoding='utf-8') as f2:
                    f2.write(massiv[i + 1])

    print('Создан файл {}'.format(cur_file))


# вытаскивает дорожку перевода в текстовый файл
def parser_tran(filename):
    FILENAME = filename
    if copy_dir_structure:
        rel_path = os.path.split(filename)[0].replace(root + "\\game\\tl\\" + lang, orig_dir)
        cur_file = rel_path + '\\' + os.path.splitext(os.path.split(filename)[1])[0] + suffix_tran
        try:
            os.makedirs(rel_path)
        except FileExistsError:
            pass
    else:
        rel_path = os.path.split(filename)[0].replace(root + "\\game\\tl\\" + lang, '').replace("\\", "-")[1:]
        if rel_path != '':
            cur_file = orig_dir + '\\' + rel_path + "-" + os.path.splitext(os.path.split(filename)[1])[0] + suffix_tran
        else:
            cur_file = orig_dir + '\\' + os.path.splitext(os.path.split(filename)[1])[0] + suffix_tran
            rel_path = orig_dir

    with open(FILENAME, "r", encoding='utf-8') as f:
        massiv = f.readlines()

    f2 = open(cur_file, 'w', encoding='utf-8')
    f2.close()

    for i, line in enumerate(massiv, start=0):
        if ".rpy:" in line:
            if "translate" in massiv[i + 1]:
                st = i + 3
                len_block = 0
                while re.match(r'^\s+#', massiv[st]) is not None:
                    if re.match(r'^\s+# voice', massiv[st]) and not include_voice:
                        len_block += 1
                    else:
                        with open(cur_file, 'a', encoding='utf-8') as f2:
                            f2.write(massiv[st + 1 + len_block])
                    st += 1

            elif "old" in massiv[i + 1]:
                with open(cur_file, 'a', encoding='utf-8') as f2:
                    f2.write(massiv[i + 2])

    print('Создан файл {}'.format(cur_file))


# проверка на непарные кавычки
def check(filename):
    a = [filename, ]
    with open(filename, 'r', encoding='utf-8') as f:
        # проверка на кавычки
        for i, line in enumerate(f.readlines(), start=1):
            if line.count('"') % 2 != 0:
                a.extend((i, line))
    # вывод строк с непарными кавычками
    if len(a) > 1:
        print(filename)
        for x in range(1, len(a), 2):
            print(a[x], a[x + 1])
            stop()


# проверка на русские буквы в строках перевода
def miss_letter(filename):
    a = True
    print(filename)
    with open(filename, "r", encoding='utf-8') as f:
        massiv = f.readlines()

    for i, line in enumerate(massiv, start=0):
        if ".rpy:" in line:
            if "translate" in massiv[i + 1]:
                st = i + 3
                len_block = 0
                while re.match(r'^\s+#', massiv[st]) is not None:
                    if re.match(r'^\s+# voice', massiv[st]) and not include_voice:
                        len_block += 1
                    else:
                        if re.match(r'.*[а-яА-ЯёЁ]+.*', massiv[st + 1 + len_block]):
                            print(st + 1 + len_block, massiv[st + 1 + len_block])
                            a = False
                    st += 1
            elif "old" in massiv[i + 1]:
                if re.match(r'.*[а-яА-ЯёЁ]+.*', massiv[i + 2]):
                    print(i + 2, massiv[i + 2])
                    a = False
    if a: print("Ok")


# вставляет дорожку перевода из текствого файла в исходный rpy-файл
def reverse(filename):
    try:
        os.makedirs(bak_dir)
    except FileExistsError:
        pass

    try:
        FILENAME = filename
        if copy_dir_structure:
            rel_path = os.path.split(filename)[0].replace(root + "\\game\\tl\\" + lang, orig_dir)
            TRANS_TXT = rel_path + '\\' + os.path.splitext(os.path.split(filename)[1])[0] + suffix_tran
            OLDFILENAME = os.path.split(filename)[0].replace(root + "\\game\\tl\\" + lang, bak_dir) + '\\' + \
                          os.path.split(filename)[1] + suffix_old
        else:
            rel_path = os.path.split(filename)[0].replace(root + "\\game\\tl\\" + lang, '').replace("\\", "-")[1:]
            if rel_path != '':
                TRANS_TXT = orig_dir + '\\' + rel_path + "-" + os.path.splitext(os.path.split(filename)[1])[
                    0] + suffix_tran
                OLDFILENAME = bak_dir + '\\' + rel_path + "-" + os.path.split(filename)[1] + suffix_old
            else:
                TRANS_TXT = orig_dir + '\\' + os.path.splitext(os.path.split(filename)[1])[0] + suffix_tran
                OLDFILENAME = bak_dir + '\\' + os.path.split(filename)[1] + suffix_old

        str_f = str_tr = 0

        with open(FILENAME, "r", encoding='utf-8') as f:
            massiv = f.readlines()
            for i, line in enumerate(massiv, start=0):
                if ".rpy:" in line:
                    if "translate" in massiv[i + 1]:
                        st = i + 3
                        while re.match(r'^\s+#', massiv[st]) is not None:
                            if include_voice:
                                str_f += 1
                            else:
                                if re.match(r'^\s+# voice', massiv[st]) is None:
                                    str_f += 1
                            st += 1
                    elif "old" in massiv[i + 1]:
                        str_f += 1

        with open(TRANS_TXT, "r", encoding='utf-8') as tr:
            trans = tr.readlines()
            str_tr = len(trans)

        # проверка на равенство строк
        if str_f == str_tr:
            for i, line in enumerate(massiv, start=0):
                if ".rpy:" in line:
                    if "translate" in massiv[i + 1]:
                        st = i + 3
                        len_block = 0
                        while re.match(r'^\s+#', massiv[st]) is not None:
                            if re.match(r'^\s+# voice', massiv[st]) and not include_voice:
                                len_block += 1
                            else:
                                str_zamena = trans.pop(0)
                                # удаление хеша из строки
                                str_zamena = str_zamena[:4] + str_zamena[5:]
                                massiv.pop(st + len_block + 1)
                                massiv.insert(st + len_block + 1, str_zamena)
                            st += 1
                    elif "old" in massiv[i + 1]:
                        str_zamena = trans.pop(0)
                        # замена old на new в строке
                        str_zamena = str_zamena[:4] + 'new' + str_zamena[7:]
                        massiv.pop(i + 2)
                        massiv.insert(i + 2, str_zamena)

            # возвращаем список в файл
            try:
                os.rename(FILENAME, OLDFILENAME)
                with open(FILENAME, 'w', encoding='utf-8') as frev:
                    frev.writelines(massiv)
            except FileExistsError:
                print('Ошибка записи в этот файл: {}'.format(FILENAME))

            print('\nОбработан файл {}\nOK'.format(FILENAME))
        elif str_f == 0 or str_tr == 0:
            print("Файлы пусты")
        else:
            print('{}\n{}:{}\n{}:{}\n'.format('File length mismatch!',
                                              FILENAME, str_f,
                                              TRANS_TXT, str_tr))
            exit()

    except FileNotFoundError:
        print('Файл {} не найден'.format(TRANS_TXT))


# вытаскивает дорожку оригинальную дорожку в xliff
# если установлен inc_trans, вытаскивает дорожку перевода (если там есть текст)
def parser_xliff(filename, inc_trans=False):
    FILENAME = filename
    if copy_dir_structure:
        rel_path = os.path.split(filename)[0].replace(root + "\\game\\tl\\" + lang, orig_dir)
        xlf_file = rel_path + '\\' + os.path.splitext(os.path.split(filename)[1])[0] + ".xliff"
        try:
            os.makedirs(rel_path)
        except FileExistsError:
            pass
    else:
        rel_path = os.path.split(filename)[0].replace(root + "\\game\\tl\\" + lang, '').replace("\\", "-")[1:]
        if rel_path != '':
            xlf_file = orig_dir + '\\' + rel_path + "-" + os.path.splitext(os.path.split(filename)[1])[0] + ".xliff"
        else:
            xlf_file = orig_dir + '\\' + os.path.splitext(os.path.split(filename)[1])[0] + ".xliff"

    with open(FILENAME, "r", encoding='utf-8') as f:
        massiv = f.readlines()

    count_block = 0

    XLIFF = ElTree.Element('xliff', {'version': "1.2", 'xmlns': "urn:oasis:names:tc:xliff:document:1.2"})
    x_file = ElTree.SubElement(XLIFF, 'file', {
        'source-language': source_lang,
        'target-language': lang,
        'datatype': "RenPy translation",
        'original': os.path.split(filename)[1]})
    body = ElTree.SubElement(x_file, 'body')

    for i, line in enumerate(massiv, start=0):
        if ".rpy:" in line:
            if "translate" in massiv[i + 1]:
                st = i + 3
                len_block = 0
                block_name = re.match(r'(.* )(\w+:$)', massiv[i + 1]).group(2)[:-1]
                while re.search(r'^\s+#', massiv[st]) is not None:
                    if re.search(r'^\s+# voice', massiv[st]) and not include_voice:
                        len_block += 1
                    else:
                        count_block += 1
                        unit = ElTree.SubElement(body, 'trans-unit', {'id': str(count_block) + ": " + block_name})
                        source = ElTree.SubElement(unit, 'source')
                        source.text = massiv[st + len_block].strip()
                        if inc_trans:
                            # нужно добавить еще и перевод
                            if len(only_text(massiv[st + 1 + len_block].strip())) > 0:  # если текст перевода есть
                                target = ElTree.SubElement(unit, 'target')
                                target.text = "# " + massiv[st + 1 + len_block].strip()
                    st += 1

            elif "old" in massiv[i + 1]:
                count_block += 1
                unit = ElTree.SubElement(body, 'trans-unit', {'id': str(count_block)})
                source = ElTree.SubElement(unit, 'source')
                source.text = massiv[i + 1].strip()
                if inc_trans:
                    # нужно добавить еще и перевод
                    if len(only_text(massiv[i + 2].strip())) > 0:  # если текст перевода есть
                        target = ElTree.SubElement(unit, 'target')
                        target.text = "old " + massiv[i + 2].strip()[4:]

    mydata = ElTree.tostring(XLIFF, encoding='unicode', method='xml')
    f2 = open(xlf_file, 'w', encoding='utf-8')
    f2.write("<?xml version=\"1.0\"?>\n")
    f2.write(mydata)
    f2.close()

    print('Создан файл {}'.format(xlf_file))


# размещает перевод из xliff-файла в дорожку перевода оригинального файла
def reverse_xliff(filename):
    try:
        os.makedirs(bak_dir)
    except FileExistsError:
        pass

    try:
        FILENAME = filename
        if copy_dir_structure:
            rel_path = os.path.split(filename)[0].replace(root + "\\game\\tl\\" + lang, orig_dir)
            xlf_file = rel_path + '\\' + os.path.splitext(os.path.split(filename)[1])[0] + ".xliff"

            rel_path = os.path.split(filename)[0].replace(root + "\\game\\tl\\" + lang, bak_dir)
            OLDFILENAME = rel_path + '\\' + os.path.split(filename)[1] + suffix_old
            try:
                os.makedirs(rel_path)
            except FileExistsError:
                pass
        else:
            rel_path = os.path.split(filename)[0].replace(root + "\\game\\tl\\" + lang, '').replace("\\", "-")[1:]
            if rel_path != '':
                xlf_file = orig_dir + '\\' + rel_path + "-" + os.path.splitext(os.path.split(filename)[1])[0] + ".xliff"
                OLDFILENAME = bak_dir + '\\' + rel_path + "-" + os.path.split(filename)[1] + suffix_old
            else:
                xlf_file = orig_dir + '\\' + os.path.splitext(os.path.split(filename)[1])[0] + ".xliff"
                OLDFILENAME = bak_dir + '\\' + os.path.split(filename)[1] + suffix_old

        str_f = str_tr = 0

        xlf_tree = ElTree.parse(xlf_file)

        xlf_root = xlf_tree.getroot()

        str_tr = len(xlf_root[0][0])

        current_block = 0

        with open(FILENAME, "r", encoding='utf-8') as f:
            massiv = f.readlines()
            for i, line in enumerate(massiv, start=0):
                if ".rpy:" in line:
                    if "translate" in massiv[i + 1]:
                        st = i + 3
                        while re.match(r'^\s+#', massiv[st]) is not None:
                            if include_voice:
                                str_f += 1
                            else:
                                if re.match(r'^\s+# voice', massiv[st]) is None:
                                    str_f += 1
                            st += 1
                    elif "old" in massiv[i + 1]:
                        str_f += 1

        # проверка на равенство строк
        if str_f == str_tr:
            # xlf_root[0][0][3][1].text
            for i, line in enumerate(massiv, start=0):
                if ".rpy:" in line:
                    if "translate" in massiv[i + 1]:
                        st = i + 3
                        len_block = 0
                        while re.match(r'^\s+#', massiv[st]) is not None:
                            if re.match(r'^\s+# voice', massiv[st]) and not include_voice:
                                len_block += 1
                            else:
                                str_zamena = xlf_root[0][0][current_block][1].text + "\n"
                                # удаление хеша из строки
                                str_zamena = "    " + str_zamena[2:]
                                massiv.pop(st + len_block + 1)
                                massiv.insert(st + len_block + 1, str_zamena)

                                current_block += 1

                            st += 1
                    elif "old" in massiv[i + 1]:
                        str_zamena = xlf_root[0][0][current_block][1].text + "\n"
                        # замена old на new в строке
                        str_zamena = '    new' + str_zamena[3:]
                        massiv.pop(i + 2)
                        massiv.insert(i + 2, str_zamena)

                        current_block += 1

            # возвращаем список в файл
            try:
                os.rename(FILENAME, OLDFILENAME)
                with open(FILENAME, 'w', encoding='utf-8') as frev:
                    frev.writelines(massiv)
            except FileExistsError:
                print('Ошибка записи в этот файл: {}'.format(FILENAME))

            print('\nОбработан файл {}\nOK'.format(FILENAME))
        elif str_f == 0 or str_tr == 0:
            print("Файлы пусты")
        else:
            print('{}\n{}:{}\n{}:{}\n'.format('File length mismatch!',
                                              FILENAME, str_f,
                                              xlf_file, str_tr))
            exit()

    except FileNotFoundError:
        print('Файл {} не найден'.format(xlf_file))


# размещает перевод из tl файлов предыдущей версии игры
# папку с нужным языком из старой игры копируем в папку tl_old
# для подстановки перевода должны быть выполнены слеющие условия:
# 1. перевод в старом файле должен быть непустым
# 2. строка оригинала должна быть размещены в том же файле (исключая конструкции "old", они могут быть в любом файле)
# 3. строка оригинала должна располагаться в блоке с тем же самым именем-меткой
# 4. строка оригинала должна полностью совпадать в старом и новом файлах
def insert_from_old():
    file_dict = {}
    dict_old = {}

    # считываем все файлы в папке tl_old\[lang]
    files = glob(root + '\\tl_old\\' + lang + '\\**\\*.rpy', recursive=True)
    for file in files:
        file_name = file.replace(root + "\\tl_old\\" + lang+"\\", '')

        with open(file, "r", encoding='utf-8') as f:
            massiv = f.readlines()

        for i, line in enumerate(massiv, start=0):
            if ".rpy:" in line:
                if "translate" in massiv[i + 1]:
                    ln = re.match(r'(.* )(\w+)(_\w+:)', massiv[i + 1]).group(2) # label name - имя метки
                    st = i + 3
                    len_block = 0
                    while re.search(r'^\s+#', massiv[st]) is not None:
                        if re.search(r'^\s+# voice', massiv[st]) and not include_voice:
                            len_block += 1
                        else:
                            source = massiv[st + len_block].strip()
                            target = massiv[st + 1 + len_block].strip()
                            if len(only_text(target)) > 0:
                                # если в блоке есть перевод:
                                #   размещаем имя файла с относительным путем в словаре file_dict в качестве ключа,
                                #      в качестве значения идет словарь с ключом ИМЯ_МЕТКИ,
                                #         в качестве значения которой идет список кортежей [(исх.текст : перевод), ...]
                                if not file_name in file_dict:
                                    file_dict[file_name] = {}
                                if not ln in file_dict[file_name]:
                                    file_dict[file_name][ln] = []
                                file_dict[file_name][ln].append((source, target))
                        st += 1
                elif "old" in massiv[i + 1]:
                    # размещаем в dict_old {исходный текст : перевод}
                    source = massiv[i + 1].strip()
                    target = massiv[i + 2].strip()
                    if len(only_text(target)) > 0:
                        dict_old[source] = target

    # перебираем файлы в папке 'game\tl\[lang]'
    files = glob(root + '\\game\\tl\\' + lang + '\\**\\*.rpy', recursive=True)
    for file in files:
        file_name = file.replace(root + "\\game\\tl\\" + lang+"\\", '')

        rel_path = os.path.split(file)[0].replace(root + "\\game\\tl\\" + lang, bak_dir)
        OLDFILENAME = rel_path + '\\' + os.path.split(file)[1] + suffix_old
        try:
            os.makedirs(rel_path)
        except FileExistsError:
            pass


        with open(file, "r", encoding='utf-8') as f:
            massiv = f.readlines()

        for i, line in enumerate(massiv, start=0):
            if ".rpy:" in line:
                old_char = new_char = ''
                # последовательно перебираем блоки и пытаемся найти исходную строку в словаре
                if "translate" in massiv[i + 1]:
                    ln = re.match(r'(.* )(\w+)(_\w+:)', massiv[i + 1]).group(2) # label name - имя метки
                    st = i + 3
                    len_block = 0
                    while re.search(r'^\s+#', massiv[st]) is not None:
                        if re.search(r'^\s+# voice', massiv[st]) and not include_voice:
                            len_block += 1
                        else:
                            source = massiv[st + len_block].strip()
                            if file_name in file_dict:
                                if ln in file_dict[file_name]:
                                    # если совпадают файлы и метки, начинаем перебирать список кортежей
                                    for k, kort in enumerate(file_dict[file_name][ln], start=0):
                                        target = ''
                                        if kort[0] == source:
                                            target = kort[1]
                                        elif compare_without_emotion:
                                            # получим имя персонажа без эмоций
                                            old_char = re.match(r'(# )(\w+)(.*)', kort[0]).group(2)
                                            new_char = re.match(r'(# )(\w+)(.*)', source).group(2)
                                            if old_char.find('_') > 0:
                                                # если эмоция отделена подчеркиванием, тоже ее уберем
                                                old_char = re.match(r'(\w+)(_\w+)', old_char).group(1)
                                            if new_char.find('_') > 0:
                                                new_char = re.match(r'(\w+)(_\w+)', new_char).group(1)
                                            if old_char == new_char and only_text(kort[0]) == only_text(source):
                                                # если совпадают имена без эмоций и текст фразы, это искомая строка
                                                target = (source[2:source.find('"')+1] + only_text(kort[1]) +
                                                          source[source.rfind('"'):])
                                        if target != '':
                                            target = '    ' + target + '\n'
                                            massiv.pop(st + len_block + 1)
                                            massiv.insert(st + len_block + 1, target)
                                            file_dict[file_name][ln].remove(kort)
                                            break
                        st += 1
                elif "old" in massiv[i + 1]:
                    source = massiv[i + 1].strip()
                    if source in dict_old:
                        target = '    '+ dict_old[source] + '\n'
                        massiv.pop(i + 2)
                        massiv.insert(i + 2, target)

        # возвращаем список в файл
        try:
            os.rename(file, OLDFILENAME)
            with open(file, 'w', encoding='utf-8') as frev:
                frev.writelines(massiv)
        except FileExistsError:
            print('Ошибка записи в этот файл: {}'.format(file))

        print('\nОбработан файл {}\nOK'.format(file))



# создает рабочую папку и запускает меню выбора
def folders():
    global orig_dir, bak_dir
    os.system('cls')
    orig_dir = os.path.join(root, "work")
    bak_dir = os.path.join(root, "backup " + timez)
    try:
        os.makedirs(orig_dir)
    except FileExistsError:
        pass

    choose()


# меню выбора действий
def choose():
    b = input('\nВыберите пункт меню:'
              '\n1. Выдернуть из всех файлов дорожку оригинала в текст'
              '\n2. Выдернуть из всех файлов дорожку перевода в текст'
              '\n3. Проверить файл на незакрытые кавычки'
              '\n4. Проверить файлы на русские буквы в переводе'
              '\n5. Вставить перевод из *.txt в файлы оригинала'
              '\n6. Выдернуть дорожку оригинала из всех файлов в xliff'
              '\n7. Выдернуть оригинал и перевод из всех файлов в xliff'
              '\n8. Вставить перевод из *.xliff в файлы оригинала'
              '\n9. Интегрировать перевод из файлов предыдущей версии игры'
              '\n0. Выход из программы\n')

    if b == '1':
        files = glob(root + '/**/tl/' + lang + '/**/*.rpy', recursive=True)
        for file in files:
            parser(file)
        choose()

    elif b == '2':
        files = glob(root + '/**/tl/' + lang + '/**/*.rpy', recursive=True)
        for file in files:
            parser_tran(file)
        choose()

    elif b == '3':
        files = glob(root + '/**/tl/' + lang + '/**/*.rpy', recursive=True)
        for file in files:
            check(file)
        choose()

    elif b == '4':
        files = glob(root + '/**/tl/' + lang + '/**/*.rpy', recursive=True)
        for file in files:
            miss_letter(file)
        choose()

    elif b == '5':
        files = glob(root + '/**/tl/' + lang + '/**/*.rpy', recursive=True)
        for file in files:
            try:
                reverse(file)
            except FileExistsError:
                print('Сорян')
        choose()

    elif b == '6':
        files = glob(root + '/**/tl/' + lang + '/**/*.rpy', recursive=True)
        for file in files:
            parser_xliff(file)
        choose()

    elif b == '7':
        files = glob(root + '/**/tl/' + lang + '/**/*.rpy', recursive=True)
        for file in files:
            parser_xliff(file, True)
        choose()

    elif b == '8':
        files = glob(root + '/**/tl/' + lang + '/**/*.rpy', recursive=True)
        for file in files:
            try:
                reverse_xliff(file)
            except FileExistsError:
                print('Сорян')
        choose()

    elif b == '9':
        insert_from_old()
        choose()

    elif b == '0':
        exit()

    else:
        print('Шта?')
        choose()


def screen():
    os.system('cls')

    while True:
        folders()


if __name__ == '__main__':
    screen()
