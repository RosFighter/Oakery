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
            shortfn = fn[:-5] if fn.lower().endswith('.webp') else fn[:-4]
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

################################################################################

layeredimage Lisa_read_phone:   # Лиза читает или лежит с телефоном
    always:
        'Lisa read myroom-bedlisa-mde-01'
    group naked:
        attribute talk_read:
            'Lisa read myroom-bedlisa-mde-01-lisa-read-00'
        attribute talk_phone:
            'Lisa read myroom-bedlisa-mde-01-lisa-phone-00'
        attribute read:
            'Lisa read myroom-bedlisa-mde-01-lisa-read-[pose3_1]'
        attribute phone:
            'Lisa read myroom-bedlisa-mde-01-lisa-phone-[pose3_1]'
    group lisa:
        attribute talk_read:
            'Lisa read myroom-bedlisa-mde-01-lisa-read-00[lisa.dress]'
        attribute talk_phone:
            'Lisa read myroom-bedlisa-mde-01-lisa-phone-00[lisa.dress]'
        attribute read:
            'Lisa read myroom-bedlisa-mde-01-lisa-read-[pose3_1][lisa.dress]'
        attribute phone:
            'Lisa read myroom-bedlisa-mde-01-lisa-phone-[pose3_1][lisa.dress]'

layeredimage Lisa_read_kiss:    # Урок поцелуев для Лизы (во время чтения)
    group BG:
        attribute kiss default:
            'Lisa read myroom-bedlisa-mde-02'
        attribute touch:
            'Lisa read myroom-bedlisa-mde-03'
        attribute neck:
            'Lisa read myroom-bedlisa-mde-04'
        attribute kiss_breast:
            'Lisa read myroom-bedlisa-mde-05'
    group naked:
        attribute neck:
            'Lisa read myroom-bedlisa-mde-04-max-01-lisa-01-kiss'
        attribute kiss_breast:
            'Lisa read myroom-bedlisa-mde-05-max-01-lisa-01-kiss'
    group lisa:
        attribute hug0 default:  # myroom-bedlisa-mde-02-lisa-(01b/01c/01d/01e)-hug
            'Lisa read myroom-bedlisa-mde-02-lisa-01[lisa.dress]-hug'
        attribute opened:       # myroom-bedlisa-mde-02-lisa-(02b/02c/02d/02e)-hug
            'Lisa read myroom-bedlisa-mde-02-lisa-02[lisa.dress]-hug'
        attribute start:        # myroom-bedlisa-mde-02-lisa-(01b/01c/01d/01e)-kiss или myroom-bedlisa-mde-02-lisa-(02b/02c/02d/02e)-kiss
            'Lisa read myroom-bedlisa-mde-02-lisa-[var_pose][lisa.dress]-kiss'
        attribute ass1:         # myroom-bedlisa-mde-03-lisa-(01b/01c/01d/01e)-kiss
            'Lisa read myroom-bedlisa-mde-03-lisa-01[lisa.dress]-kiss'
        attribute breast1:      # myroom-bedlisa-mde-03-lisa-(02b/02c/02d/02e)-kiss
            'Lisa read myroom-bedlisa-mde-03-lisa-02[lisa.dress]-kiss'
        attribute neck:
            'Lisa read myroom-bedlisa-mde-04-lisa-01[lisa.dress]-kiss'
        attribute kiss_breast:
            'Lisa read myroom-bedlisa-mde-05-lisa-01[lisa.dress]-kiss'
    group mgg:
        attribute hug default:  # myroom-bedlisa-mde-02-max-(01b/01c)-hug
            'Lisa read myroom-bedlisa-mde-02-max-01[mgg.dress]-hug'
        attribute start:        # myroom-bedlisa-mde-02-max-(01b/01c)-kiss или myroom-bedlisa-mde-02-max-(02b/02c)-kiss
            'Lisa read myroom-bedlisa-mde-02-max-[var_pose][mgg.dress]-kiss'
        attribute ass1:         # myroom-bedlisa-mde-03-max-(01b/01c)-kiss
            'Lisa read myroom-bedlisa-mde-03-max-01[mgg.dress]-kiss'
        attribute breast1:      # myroom-bedlisa-mde-03-max-(02b/02c)-kiss
            'Lisa read myroom-bedlisa-mde-03-max-02[mgg.dress]-kiss'
        attribute neck:
            'Lisa read myroom-bedlisa-mde-04-max-01[mgg.dress]-kiss'
        attribute kiss_breast:
            'Lisa read myroom-bedlisa-mde-05-max-01[mgg.dress]-kiss'

layeredimage Lisa_read_with_Max:
    group BG:
        attribute read:     # myroom-bedlisa-mde-01
            'Lisa read myroom-bedlisa-mde-01'
        attribute kiss:     # myroom-bedlisa-mde-06
            'Lisa read myroom-bedlisa-mde-06'

    if var_pose in ['01', '03']:
        'Lisa read myroom-bedlisa-mde-04'
    elif var_pose == '02':
        'Lisa read myroom-bedlisa-mde-05'

    group naked:
        attribute read:     # myroom-bedlisa-mde-01-max&lisa-read-(01/02/03)
            'Lisa read myroom-bedlisa-mde-01-max&lisa-read-[pose3_1]'
        attribute kiss:     # myroom-bedlisa-mde-06-max&lisa-tchkiss-(01/02/03)
            'Lisa read myroom-bedlisa-mde-06-max&lisa-tchkiss-[pose3_1]'

    if var_pose in ['01', '03']:
        'Lisa read myroom-bedlisa-mde-04-max&lisa-tch-[var_pose]'
    elif var_pose == '02':
        'Lisa read myroom-bedlisa-mde-05-max&lisa-tch-02'

    group lisa_dress:
        attribute read:
            'Lisa read myroom-bedlisa-mde-01-lisa&max-read-[pose3_1][lisa.dress]'

    if var_pose in ['01', '03']:
        'Lisa read myroom-bedlisa-mde-04-lisa-tch-[var_pose][lisa.dress]'
    elif var_pose == '02':
        'Lisa read myroom-bedlisa-mde-05-lisa-tch-02[lisa.dress]'

    group max_dress:
        attribute read:
            'Lisa read myroom-bedlisa-mde-01-max&lisa-read-[pose3_1][mgg.dress]'
        attribute kiss:
            'Lisa read myroom-bedlisa-mde-06-max-[pose3_1][mgg.dress]'

    if var_pose in ['01', '03']:
        'Lisa read myroom-bedlisa-mde-04-max-tch-[var_pose][mgg.dress]'
    elif var_pose == '02':
        'Lisa read myroom-bedlisa-mde-05-max-tch-02[mgg.dress]'

    group lisa_dress:
        attribute kiss:
            'Lisa read myroom-bedlisa-mde-06-lisa-[pose3_1][lisa.dress]'
