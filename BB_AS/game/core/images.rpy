# стандартное автообъявление картинок, но с webp
# выполняется после всего остального
init 1900 python hide:
    def create_automatic_images():
        seps = config.automatic_images
        if seps is True:
            seps = [ ' ', '/', '_' ]
        for dir, fn in renpy.loader.listdirfiles():
            if fn.startswith("_"):
                continue
            if not fn.lower().endswith(".png") and not fn.lower().endswith(".jpg") and not fn.lower().endswith(".webp"):
                continue
            shortfn = fn[:-4]
            if fn.lower().endswith(".webp"):
                shortfn = fn[:-5]
            shortfn = shortfn.replace("\\", "/")
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
    config.automatic_images_strip = ["images", "gui"] # здесь через запятую можно указать и другие папки из директории game


image video1_movie = Movie(play="video/Impulse.webm", image="images/interface/laptop/start_page.webp", size=(1475, 829))

# image AnimAnnEric1:
#     "Animation AnnEric1 01"
#     0.033
#     "Animation AnnEric1 02"
#     0.033
#     "Animation AnnEric1 03"
#     0.033
#     "Animation AnnEric1 04"
#     0.033
#     "Animation AnnEric1 05"
#     0.033
#     "Animation AnnEric1 06"
#     0.033
#     "Animation AnnEric1 07"
#     0.033
#     "Animation AnnEric1 08"
#     0.033
#     "Animation AnnEric1 09"
#     0.033
#     "Animation AnnEric1 10"
#     0.033
#     "Animation AnnEric1 11"
#     0.033
#     "Animation AnnEric1 12"
#     0.033
#     "Animation AnnEric1 13"
#     0.033
#     "Animation AnnEric1 14"
#     0.033
#     "Animation AnnEric1 15"
#     0.033
#     "Animation AnnEric1 16"
#     0.033
#     "Animation AnnEric1 17"
#     0.033
#     "Animation AnnEric1 18"
#     0.033
#     "Animation AnnEric1 19"
#     0.033
#     "Animation AnnEric1 20"
#     0.033
#     repeat
