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
## Лиза

layeredimage Lisa_read_phone:   # Лиза читает или лежит с телефоном
    image_format 'Lisa read {image}'
    always:
        'myroom-bedlisa-mde-01'
    group naked:
        attribute talk_read:
            'myroom-bedlisa-mde-01-lisa-read-00'
        attribute talk_phone:
            'myroom-bedlisa-mde-01-lisa-phone-00'
        attribute read:
            'myroom-bedlisa-mde-01-lisa-read-[pose3_1]'
        attribute phone:
            'myroom-bedlisa-mde-01-lisa-phone-[pose3_1]'
    group lisa:
        attribute talk_read:
            'myroom-bedlisa-mde-01-lisa-read-00[lisa.dress]'
        attribute talk_phone:
            'myroom-bedlisa-mde-01-lisa-phone-00[lisa.dress]'
        attribute read:
            'myroom-bedlisa-mde-01-lisa-read-[pose3_1][lisa.dress]'
        attribute phone:
            'myroom-bedlisa-mde-01-lisa-phone-[pose3_1][lisa.dress]'

layeredimage Lisa_read_kiss:    # Урок поцелуев для Лизы (во время чтения)
    image_format 'Lisa read {image}'
    group BG:
        attribute kiss default:
            'myroom-bedlisa-mde-02'
        attribute touch:
            'myroom-bedlisa-mde-03'
        attribute neck:
            'myroom-bedlisa-mde-04'
        attribute kiss_breast:
            'myroom-bedlisa-mde-05'
    group naked:
        attribute neck:
            'myroom-bedlisa-mde-04-max-01-lisa-01-kiss'
        attribute kiss_breast:
            'myroom-bedlisa-mde-05-max-01-lisa-01-kiss'
    group lisa:
        attribute hug0 default:  # myroom-bedlisa-mde-02-lisa-(01b/01c/01d/01e)-hug
            'myroom-bedlisa-mde-02-lisa-01[lisa.dress]-hug'
        attribute opened:       # myroom-bedlisa-mde-02-lisa-(02b/02c/02d/02e)-hug
            'myroom-bedlisa-mde-02-lisa-02[lisa.dress]-hug'
        attribute start:        # myroom-bedlisa-mde-02-lisa-(01b/01c/01d/01e)-kiss или myroom-bedlisa-mde-02-lisa-(02b/02c/02d/02e)-kiss
            'myroom-bedlisa-mde-02-lisa-[var_pose][lisa.dress]-kiss'
        attribute ass1:         # myroom-bedlisa-mde-03-lisa-(01b/01c/01d/01e)-kiss
            'myroom-bedlisa-mde-03-lisa-01[lisa.dress]-kiss'
        attribute breast1:      # myroom-bedlisa-mde-03-lisa-(02b/02c/02d/02e)-kiss
            'myroom-bedlisa-mde-03-lisa-02[lisa.dress]-kiss'
        attribute neck:
            'myroom-bedlisa-mde-04-lisa-01[lisa.dress]-kiss'
        attribute kiss_breast:
            'myroom-bedlisa-mde-05-lisa-01[lisa.dress]-kiss'
    group mgg:
        attribute hug default:  # myroom-bedlisa-mde-02-max-(01b/01c)-hug
            'myroom-bedlisa-mde-02-max-01[mgg.dress]-hug'
        attribute start:        # myroom-bedlisa-mde-02-max-(01b/01c)-kiss или myroom-bedlisa-mde-02-max-(02b/02c)-kiss
            'myroom-bedlisa-mde-02-max-[var_pose][mgg.dress]-kiss'
        attribute ass1:         # myroom-bedlisa-mde-03-max-(01b/01c)-kiss
            'myroom-bedlisa-mde-03-max-01[mgg.dress]-kiss'
        attribute breast1:      # myroom-bedlisa-mde-03-max-(02b/02c)-kiss
            'myroom-bedlisa-mde-03-max-02[mgg.dress]-kiss'
        attribute neck:
            'myroom-bedlisa-mde-04-max-01[mgg.dress]-kiss'
        attribute kiss_breast:
            'myroom-bedlisa-mde-05-max-01[mgg.dress]-kiss'

layeredimage Lisa_read_with_Max:
    image_format 'Lisa read {image}'
    group BG:
        attribute read:     # myroom-bedlisa-mde-01
            'myroom-bedlisa-mde-01'
        attribute kiss:     # myroom-bedlisa-mde-06
            'myroom-bedlisa-mde-06'

    if var_pose in ['01', '03']:
        'myroom-bedlisa-mde-04'
    elif var_pose == '02':
        'myroom-bedlisa-mde-05'

    group body:
        attribute read:     # myroom-bedlisa-mde-01-max&lisa-read-(01/02/03)
            'myroom-bedlisa-mde-01-max&lisa-read-[pose3_1]'
        attribute kiss:     # myroom-bedlisa-mde-06-max&lisa-tchkiss-(01/02/03)
            'myroom-bedlisa-mde-06-max&lisa-tchkiss-[pose3_1]'

    if var_pose in ['01', '03']:
        'myroom-bedlisa-mde-04-max&lisa-tch-[var_pose]'
    elif var_pose == '02':
        'myroom-bedlisa-mde-05-max&lisa-tch-02'

    group lisa_dress:
        attribute read:
            'myroom-bedlisa-mde-01-lisa&max-read-[pose3_1][lisa.dress]'

    if var_pose in ['01', '03']:
        'myroom-bedlisa-mde-04-lisa-tch-[var_pose][lisa.dress]'
    elif var_pose == '02':
        'myroom-bedlisa-mde-05-lisa-tch-02[lisa.dress]'

    group max_dress:
        attribute read:
            'myroom-bedlisa-mde-01-max&lisa-read-[pose3_1][mgg.dress]'
        attribute kiss:
            'myroom-bedlisa-mde-06-max-[pose3_1][mgg.dress]'

    if var_pose in ['01', '03']:
        'myroom-bedlisa-mde-04-max-tch-[var_pose][mgg.dress]'
    elif var_pose == '02':
        'myroom-bedlisa-mde-05-max-tch-02[mgg.dress]'

    group lisa_dress:
        attribute kiss:
            'myroom-bedlisa-mde-06-lisa-[pose3_1][lisa.dress]'

layeredimage Lisa_sleep:
    image_format 'Lisa sleep {image}'
    group BG:
        attribute mde:
            'myroom-bedlisa-m-01'
        attribute night default:
            'myroom-bedlisa-n-01'

    group body:
        attribute mde:
            'myroom-bedlisa-m-01-lisa-sleep-[pose3_1]'
        attribute one default:
            'myroom-bedlisa-n-01-lisa-sleep-[pose3_1]'
        attribute olivia:
            'myroom-bedlisa-n-01-lisa&olivia-sleep-[pose3_1]'

    group lisa_clothes:
        attribute mde:
            if_not 'naked'
            'myroom-bedlisa-m-01-lisa-sleep-[pose3_1][lisa.dress]'
        attribute one default:
            if_not 'naked'
            'myroom-bedlisa-n-01-lisa-sleep-[pose3_1][lisa.dress]'
        attribute olivia:
            if_not 'naked'
            'myroom-bedlisa-n-01-lisa&olivia-sleep-[pose3_1][lisa.dress]'

    attribute naked null

################################################################################
## Анна

layeredimage Ann_sleep:
    image_format 'Ann sleep {image}'
    group bg:
        attribute far default:
            'annroom-bedann-night-01'
        attribute closer:
            'annroom-bedann-n-01'

    attribute naked:
        if_not ['eric', 'closer']
        'ann-sleep-night-[pose3_3]'

    group body:
        attribute closer:
            if_not 'eric'
            'annroom-bedann-n-01-ann-sleep-[pose3_3]'

    attribute eric:
        if_not 'closer'
        'ann&eric-sleep-night-[pose3_3]'
    attribute eric:
        if_all 'closer'
        'annroom-bedann-n-01-ann&eric-sleep-[pose3_3]'

    group nightie:
        attribute far default:
            if_not ['eric', 'naked']
            'ann-sleep-night-[pose3_3][ann.dress]'
        attribute closer:
            if_not ['eric', 'naked']
            'annroom-bedann-n-01-ann-sleep-[pose3_3][ann.dress]'

    attribute max default:
        if_not 'closer'
        'max-voyeur-ann-night-00[mgg.dress]'

layeredimage Ann_dressing:
    image_format 'Ann dressing {image}'
    group BG:
        attribute door default:
            'annroom-wardrobe-mde-01'
        attribute balcony:
            'annroom-balcony-md-01'
        attribute talk:
            'annroom-balcony-md-02'

    attribute eric:
        'annroom-wardrobe-mde-01-eric-dresses-07c'

    group body:
        attribute dress default:
            if_not 'empty'
            'annroom-wardrobe-mde-01-ann-dresses-[var_pose][var_dress]'
        attribute zero:
            'annroom-balcony-md-01-ann-dresses-01[var_dress]'
        attribute talk:
            'annroom-balcony-md-02-max&ann-[var_pose]'

    if var_pose < '05':
        if_all 'talk'
        'annroom-balcony-md-02-max-[var_pose][mgg.dress]'
    else:
        if_all 'talk'
        'annroom-balcony-md-02-ann-[var_pose][var_dress]'

    if var_pose < '05':
        if_all 'talk'
        'annroom-balcony-md-02-ann-[var_pose][var_dress]'
    else:
        if_all 'talk'
        'annroom-balcony-md-02-max-[var_pose][mgg.dress]'

    attribute talk:
        'annroom-balcony-md-02a'

    attribute empty null

layeredimage Ann_gift:
    attribute door default:
        'Ann dressing annroom-wardrobe-mde-01'

    attribute hug1:
        'Ann hugging morning-annroom [var_pose]-1[var_dress][mgg.dress]'
    attribute hug2:
        'Ann hugging morning-annroom [var_pose]-2[var_dress][mgg.dress]'
    attribute hug3:
        'Ann hugging morning-annroom [var_pose]-3[var_dress][mgg.dress]'

layeredimage Ann_yoga:
    image_format 'Ann yoga {image}'
    group BG:
        attribute basic:
            'ann-yoga-01'
        attribute stage default:
            if_not 'seven'
            'yoga-[var_stage]'

    attribute basic:
        'ann-yoga-[var_pose][ann.dress]'

    if var_stage == '07' and var_pose != '03':
        if_all 'seven'
        'yoga-06'
    if var_stage == '04' and var_pose == '03':
        'yoga-06-max&ann-03'

    if var_stage == '01':
        if_not 'basic'  # ann
        'yoga-[var_stage]-ann-[var_pose][ann.dress]'
    elif var_stage == '02':
        if_not 'basic'  # max
        'yoga-[var_stage]-max-01[mgg.dress]'
    elif var_stage == '04' and var_pose == '03':
        if_not 'basic'  # max
        'yoga-06-max-[var_pose][mgg.dress]'
    elif var_stage == '05' and var_pose != '03':
        if_not 'basic'  # ann
        'yoga-05-ann-[var_pose][ann.dress]'
    elif var_stage == '06':
        if_not ['basic', 'seven'] # body
        'yoga-06-max&ann-[var_pose]'
    elif var_stage in ['06', '07']:
        if_all 'seven'  # body / bg_body
        'yoga-07-max&ann-[var_pose]'
    else:
        if_not 'basic'  # ann+max
        'yoga-[var_stage]-max-[var_pose][mgg.dress]-ann-[var_pose][ann.dress]'

    if var_stage == '01':
        if_not 'basic'  # max
        'yoga-[var_stage]-max-01[mgg.dress]'
    elif var_stage == '02':
        if_not 'basic'  # ann
        'yoga-[var_stage]-ann-[var_pose][ann.dress]'
    elif var_stage == '04' and var_pose == '03':
        if_not 'basic'  # ann
        'yoga-06-ann-[var_pose][ann.dress]'
    elif var_stage == '05' and var_pose != '03':
        if_not 'basic'  # max
        'yoga-05-max-[var_pose][mgg.dress]'

    if var_stage == '06':
        if_not ['basic', 'seven'] # max_dress
        'yoga-06-max-[var_pose][mgg.dress]'
    elif var_stage in ['06', '07']:
        if_all 'seven'          # ann_dress
        'yoga-07-ann-[var_pose][ann.dress]'

    if var_stage == '06':
        if_not ['basic', 'seven'] # ann_dress
        'yoga-06-ann-[var_pose][ann.dress]'
    elif var_stage in ['06', '07']:
        if_all 'seven'          # max_dress
        'yoga-07-max-[var_pose][mgg.dress]'

    attribute seven null

################################################################################
## Макс

layeredimage Max_sleep:
    image_format 'Max sleep {image}'
    group BG:
        attribute mde:
            'myroom-bedmax-mde-01'
        attribute night default:
            'myroom-bedmax-n-01'
    group body:
        attribute mde:
            'myroom-bedmax-mde-01-max-sleep-[pose3_3]'
        attribute night default:
            'myroom-bedmax-n-01-max-sleep-[pose3_3]'
    group clothes:
        attribute mde:
            'myroom-bedmax-mde-01-max-sleep-[pose3_3][mgg.dress]'
        attribute night default:
            'myroom-bedmax-n-01-max-sleep-[pose3_3]a'
