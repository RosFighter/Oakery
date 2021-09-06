## Данный файл содержит настройки, способные изменить вашу игру.
##
## Строки, начинающиеся  с двух '#' — комментарии, и вы не должны их
## раскомментировать. Строки, начинающиеся с одной '#' — комментированный код,
## который вы можете раскомментировать, если посчитаете это нужным.


## Основное ####################################################################

## Читаемое название игры. Используется при установке стандартного заголовка
## окна, показывается в интерфейсе и отчётах об ошибках.
##
## Символы "_()", окружающие название, отмечают его как пригодное для перевода.

define config.name = _("Большой брат: Другая история")


## Определяет, показывать ли заголовок, данный выше, на экране главного меню.
## Установите на False, чтобы спрятать заголовок.

define gui.show_name = True


## Версия игры.

define config.version = "0.06.8.07"


## Текст, помещённый в экран "Об игре". Поместите текст между тройными скобками.
## Для отделения абзацев оставляйте между ними пустую строку.

define gui.about = _p("""
""")


## Короткое название игры, используемое для исполняемых файлов и директорий при
## постройке дистрибутивов. Оно должно содержать текст формата ASCII и не должно
## содержать пробелы, двоеточия и точки с запятой.

define build.name = "BigBrother_AnotherStory"


## Звуки и музыка ##############################################################

## Эти три переменные контролируют соответствующие микшеры громкости в
## настройках, которые игрок может настраивать по умолчанию. Изменив один из
## параметров на False, скроется соответствующий микшер.

define config.has_sound = True
define config.has_music = True
define config.has_voice = False


## Чтобы разрешить игроку тестировать громкость на звуковом или голосовом
## каналах, раскомментируйте строчку и настройте пример звука для прослушивания.

# define config.sample_sound = "sample-sound.ogg"
# define config.sample_voice = "sample-voice.ogg"


## Раскомментируйте следующую строчку, чтобы настроить аудиофайл, который будет
## проигрываться в главном меню. Этот файл продолжит проигрываться во время
## игры, если не будет остановлен, или не начнёт проигрываться другой аудиофайл.

define config.main_menu_music = "audio/main.ogg"

define config.default_music_volume = 0.5
define config.default_sfx_volume = 0.5

## Переходы ####################################################################
##
## Эти переменные задают переходы, используемые в различных событиях. Каждая
## переменная должна задавать переход или None, чтобы указать на то, что переход
## не должен использоваться.

## Вход и выход в игровое меню.

define config.enter_transition = dissolve
define config.exit_transition = dissolve


## Переход между экранами игрового меню.

define config.intra_transition = dissolve


## Переход, используемый после загрузки слота сохранения.

define config.after_load_transition = None


## Используется при входе в главное меню после того, как игра закончится.

define config.end_game_transition = None


## Переменная, устанавливающая переход, когда старт игры не существует. Вместо
## неё используйте функцию with после показа начальной сценки.


## Управление окнами ###########################################################
##
## Эта строка контролирует, когда появляется диалоговое окно. Если "show" — оно
## всегда показано. Если "hide" — оно показывается, только когда представлен
## диалог. Если "auto" — окно скрыто до появления оператора scene и показывается
## при появлении диалога.
##
## После начала игры этот параметр можно изменить с помощью "window show",
## "window hide" и "window auto".

define config.window = "hide"


## Переходы, используемые при показе и скрытии диалогового окна

define config.window_show_transition = Dissolve(.2)
define config.window_hide_transition = Dissolve(.2)


## Стандартные настройки #######################################################

## Контролирует стандартную скорость текста. По умолчанию, это 0 — мгновенно,
## в то время как любая другая цифра — это количество символов, печатаемых в
## секунду.

default preferences.text_cps = 0


## Стандартная задержка авточтения. Большие значения означают долгие ожидания, а
## от 0 до 30 — вполне допустимый диапазон.

default preferences.afm_time = 15


## Директория сохранений #######################################################
##
## Контролирует зависимое от платформы место, куда Ren'Py будет складывать файлы
## сохранения этой игры. Файлы сохранений будут храниться в:
##
## Windows: %APPDATA\RenPy\<config.save_directory>
##
## Macintosh: $HOME/Library/RenPy/<config.save_directory>
##
## Linux: $HOME/.renpy/<config.save_directory>
##
## Этот параметр обычно не должен изменяться, а если и изменился, должен быть
## текстовой строчкой, а не выражением.

define config.save_directory = 'BB_AS'

## Настройка автосохранений ####################################################
##
init python:
    config.has_autosave = True
    config.autosave_frequency = None
    config.autosave_on_choice  = False



## Иконка ######################################################################
##
## Иконка, показываемая на панели задач или на dock.

define config.window_icon = 'gui/window_icon.png'


## Другие ######################################################################
##

define config.minimum_presplash_time = 1.0
define config.mouse_hide_time = 10
default preferences.desktop_rollback_side = "disable"   # сторона отката

init python:
    def json_callback(d):
        d["day"]    = day
        d["tm"]     = tm
        d["wd"]     = weekdays[GetWeekday(day)][0]
        d["desc"]   = save_name
        d["auto"]   = str(number_autosave)
        d["quick"]  = str(number_quicksave)

    config.default_fullscreen = False
    config.save_json_callbacks.append(json_callback)

## Настройка Дистрибутива ######################################################
##
## Эта секция контролирует, как Ren'Py строит дистрибутивные файлы из вашего
## проекта.

init python:

    ## Следующие функции берут образцы файлов. Образцы файлов не учитывают
    ## регистр и соответствующе зависят от директории проекта (base), с или без
    ## учёта /, задающей директорию. Если обнаруживается множество одноимённых
    ## файлов, то используется только первый.
    ##
    ## Инструкция:
    ##
    ## / — разделитель директорий.
    ##
    ## * включает в себя все символы, исключая разделитель директорий.
    ##
    ## ** включает в себя все символы, включая разделитель директорий.
    ##
    ## Например, "*.txt" берёт все файлы формата txt из директории base, "game/
    ## **.ogg" берёт все файлы ogg из директории game и всех поддиректорий, а
    ## "**.psd" берёт все файлы psd из любого места проекта.

    ## Классифицируйте файлы как None, чтобы исключить их из дистрибутивов.

    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**.rpym', None)
    build.classify('**/.**', None)
    build.classify('game/tl/**.rpy', None)
    build.classify('game/**.rpy', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)
    build.classify('**/*save*/*.*', None)
    build.classify('lovetime.*', None)

    ## Чтобы архивировать файлы, классифицируйте их, например, как 'archive'.

    build.archive("extra", "all")
    build.classify('game/extra/**.png', 'extra')
    build.classify('game/extra/**.jpg', 'extra')
    build.classify('game/extra/**.webp', 'extra')
    build.classify('game/extra/**.rpyc', 'extra')
    # build.classify('game/tl/**/extra/**.rpyc', 'extra')

    build.archive("img_fix", "all")
    build.classify('game/images/interface/poss/partygirl/ep08.webp', 'img_fix')
    build.classify('game/images/interface/poss/naughty/ep07.webp', 'img_fix')
    build.classify('game/images/Olivia/cams/night-tv/*.webp', 'img_fix')
    build.classify('game/images/Eric/jerk_off/fg-*.webp', 'img_fix')
    build.classify('game/images/interface/patreon_logo_2.webp', 'img_fix')
    build.classify('game/images/interface/patreon_music.webp', 'img_fix')

    build.archive("images", "all")

    build.classify('game/**.png', 'images')
    build.classify('game/**.jpg', 'images')
    build.classify('game/**.webp', 'images')

    build.archive('video', 'all')
    build.classify('game/**.webm', 'video')

    build.archive('audio', 'all')
    build.classify('game/audio/**.ogg', 'audio')
    build.classify('game/audio/**.mp3', 'audio')
    build.classify('game/audio/**.wav', 'audio')

    build.archive('translate', 'all')
    build.classify('game/tl/**.**', 'translate')

    build.archive('scripts', 'all')
    build.classify('game/*.rpyc', 'scripts')
    build.classify('game/core/**.rpyc', 'scripts')
    build.classify('game/dialogues/**.rpyc', 'scripts')
    build.classify('game/events/**.rpyc', 'scripts')

    build.archive('font', 'all')
    build.classify('game/**.ttf', 'font')
    build.classify('game/**.otf', 'font')

    ## Файлы, соответствующие образцам документации, дублируются в приложениях
    ## Mac, чтобы они появлялись и в приложении, и в zip архиве.

    build.documentation('*.html')
    build.documentation('*.txt')

## Эта строка отвечает за подписывание игры на Mac с помощью вашего Apple ID.
## Подписывайте только со своего Apple Developer ID.

# define build.mac_identity = "Developer ID Application: Guy Shy (XHTE5H7Z42)"


## Лицензионный ключ Google Play требуется для загрузки файлов расширений и
## поддержки внутриигровых покупок. Он может быть найден на странице "Services &
## APIs" консоли разработчика Google Play.

# define build.google_play_key = "..."


## Имя пользователя и название проекта, ассоциированные с проектом на itch.io,
## разделённые дробью.

# define build.itch_project = "renpytom/test-project"


## Включение поддержки 32-битных приложений ####################################
##
## Если True, то файлы, необходимые для работы на 32-разрядных процессорах x86,
## будут включены в сборки Linux и Mac. Если значение False, эти файлы не будут
## включены.

    build.include_i686 = True
