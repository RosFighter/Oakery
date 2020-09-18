# стандартное автообъявление картинок, но с webp
# выполняется после всего остального
init 1900 python hide:
    def create_automatic_images():
        seps = config.automatic_images
        if seps is True:
            seps = [ ' ', '/', '_' ]
        for dir, fn in renpy.loader.listdirfiles():
            if fn.startswith('_'):
                continue
            if not fn.lower().endswith('.png') and not fn.lower().endswith('.jpg') and not fn.lower().endswith('.webp'):
                continue
            shortfn = fn[:-4]
            if fn.lower().endswith('.webp'):
                shortfn = fn[:-5]
            shortfn = shortfn.replace('\\', '/')
            name = ( shortfn, )
            for sep in seps:
                name = tuple(j for i in name for j in i.split(sep))
            while name:
                for i in config.automatic_images_strip:
                    if name[0] == i:
                        name = name[1:]
                        break
                else:
                    break
            if len(name) < config.automatic_images_minimum_components:
                continue
            if name in renpy.display.image.images:
                continue
            renpy.image(name, fn)
    if config.automatic_images:
        create_automatic_images()

init python:
    config.automatic_images_minimum_components = 1 # минимальное количество тегов
    config.automatic_images = [' ', '_', '/'] # список разделителей для создания тегов
    config.automatic_images_strip = ['images', 'gui'] # здесь через запятую можно указать и другие папки из директории game

image video1_movie = Movie(play='video/Impulse.webm', image='images/interface/laptop/start_page.webp', size=(1475, 829))

image AnimAnnEric1:  # Анимация в спальне
    'Eric fuck 06 00'
    0.033
    'Eric fuck 06 01'
    0.033
    'Eric fuck 06 02'
    0.033
    'Eric fuck 06 03'
    0.033
    'Eric fuck 06 04'
    0.033
    'Eric fuck 06 05'
    0.033
    'Eric fuck 06 06'
    0.033
    'Eric fuck 06 07'
    0.033
    'Eric fuck 06 08'
    0.033
    'Eric fuck 06 09'
    0.033
    'Eric fuck 06 10'
    0.033
    'Eric fuck 06 11'
    0.033
    'Eric fuck 06 12'
    0.033
    'Eric fuck 06 13'
    0.033
    'Eric fuck 06 14'
    0.033
    'Eric fuck 06 15'
    0.033
    'Eric fuck 06 16'
    0.033
    'Eric fuck 06 17'
    0.033
    repeat

image CamAnnEric1:
    'Eric cams fuck 06 00'
    0.033
    'Eric cams fuck 06 01'
    0.033
    'Eric cams fuck 06 02'
    0.033
    'Eric cams fuck 06 03'
    0.033
    'Eric cams fuck 06 04'
    0.033
    'Eric cams fuck 06 05'
    0.033
    'Eric cams fuck 06 06'
    0.033
    'Eric cams fuck 06 07'
    0.033
    'Eric cams fuck 06 08'
    0.033
    'Eric cams fuck 06 09'
    0.033
    'Eric cams fuck 06 10'
    0.033
    'Eric cams fuck 06 11'
    0.033
    'Eric cams fuck 06 12'
    0.033
    'Eric cams fuck 06 13'
    0.033
    'Eric cams fuck 06 14'
    0.033
    'Eric cams fuck 06 15'
    0.033
    'Eric cams fuck 06 16'
    0.033
    'Eric cams fuck 06 17'
    0.033
    repeat

image AnimAnnEric2:  # Анимация в душе (утром со стремянки)
    'Eric bath-window-morning 06b 00'
    0.033
    'Eric bath-window-morning 06b 01'
    0.033
    'Eric bath-window-morning 06b 02'
    0.033
    'Eric bath-window-morning 06b 03'
    0.033
    'Eric bath-window-morning 06b 04'
    0.033
    'Eric bath-window-morning 06b 05'
    0.033
    'Eric bath-window-morning 06b 06'
    0.033
    'Eric bath-window-morning 06b 07'
    0.033
    'Eric bath-window-morning 06b 08'
    0.033
    'Eric bath-window-morning 06b 09'
    0.033
    'Eric bath-window-morning 06b 10'
    0.033
    'Eric bath-window-morning 06b 11'
    0.033
    'Eric bath-window-morning 06b 12'
    0.033
    'Eric bath-window-morning 06b 13'
    0.033
    'Eric bath-window-morning 06b 14'
    0.033
    'Eric bath-window-morning 06b 15'
    0.033
    'Eric bath-window-morning 06b 16'
    0.033
    'Eric bath-window-morning 06b 17'
    0.033
    repeat

image porn_01 01_02:
    'tv porn-01 01'
    6.0
    'tv porn-01 02'

image porn_01 03_04:
    'tv porn-01 03'
    6.0
    'tv porn-01 04'

image porn_01 05_06:
    'tv porn-01 05'
    6.0
    'tv porn-01 06'

image porn_01 07_08:
    'tv porn-01 07'
    6.0
    'tv porn-01 08'

image porn_01 09_10:
    'tv porn-01 09'
    6.0
    'tv porn-01 10'

image porn_02 01_02:
    'tv porn-02 01'
    6.0
    'tv porn-02 02'

image porn_02 03_04:
    'tv porn-02 03'
    6.0
    'tv porn-02 04'

image porn_02 05_06:
    'tv porn-02 05'
    6.0
    'tv porn-02 06'

image porn_02 07_08:
    'tv porn-02 07'
    6.0
    'tv porn-02 08'

image porn_02 09_10:
    'tv porn-02 09'
    6.0
    'tv porn-02 10'

image porn_03 01_02:
    'tv porn-03 01'
    6.0
    'tv porn-03 02'

image porn_03 03_04:
    'tv porn-03 03'
    6.0
    'tv porn-03 04'

image porn_03 05_06:
    'tv porn-03 05'
    6.0
    'tv porn-03 06'

image porn_03 07_08:
    'tv porn-03 07'
    6.0
    'tv porn-03 08'

image porn_03 09_10:
    'tv porn-03 09'
    6.0
    'tv porn-03 10'

image porn_04 01_02:
    'tv porn-04 01'
    6.0
    'tv porn-04 02'

image porn_04 03_04:
    'tv porn-04 03'
    6.0
    'tv porn-04 04'

image porn_04 05_06:
    'tv porn-04 05'
    6.0
    'tv porn-04 06'

image porn_04 07_08:
    'tv porn-04 07'
    6.0
    'tv porn-04 08'

image porn_04 09_10:
    'tv porn-04 09'
    6.0
    'tv porn-04 10'

image porn_05 01_02:
    'tv porn-05 01'
    6.0
    'tv porn-05 02'

image porn_05 03_04:
    'tv porn-05 03'
    6.0
    'tv porn-05 04'

image porn_05 05_06:
    'tv porn-05 05'
    6.0
    'tv porn-05 06'

image porn_05 07_08:
    'tv porn-05 07'
    6.0
    'tv porn-05 08'

image porn_05 09_10:
    'tv porn-05 09'
    6.0
    'tv porn-05 10'

image porn_06 01_02:
    'tv porn-06 01'
    6.0
    'tv porn-06 02'

image porn_06 03_04:
    'tv porn-06 03'
    6.0
    'tv porn-06 04'

image porn_06 05_06:
    'tv porn-06 05'
    6.0
    'tv porn-06 06'

image porn_06 07_08:
    'tv porn-06 07'
    6.0
    'tv porn-06 08'

image porn_06 09_10:
    'tv porn-06 09'
    6.0
    'tv porn-06 10'

image AnimMaxKira1:
    'Kira shower-Max 05 00'
    0.036
    'Kira shower-Max 05 01'
    0.036
    'Kira shower-Max 05 02'
    0.036
    'Kira shower-Max 05 03'
    0.036
    'Kira shower-Max 05 04'
    0.036
    'Kira shower-Max 05 05'
    0.036
    'Kira shower-Max 05 06'
    0.036
    'Kira shower-Max 05 07'
    0.036
    'Kira shower-Max 05 08'
    0.036
    'Kira shower-Max 05 09'
    0.036
    'Kira shower-Max 05 10'
    0.036
    'Kira shower-Max 05 11'
    0.036
    'Kira shower-Max 05 12'
    0.036
    'Kira shower-Max 05 13'
    0.036
    'Kira shower-Max 05 14'
    0.036
    'Kira shower-Max 05 15'
    0.036
    'Kira shower-Max 05 16'
    0.036
    'Kira shower-Max 05 17'
    0.036
    repeat
