
init python:

    def MySet(i, x):
        global cur_starts
        cur_starts[i] = x

    class Memories:
        def __init__(self, module, pict, set='', capt="", var='True'):
            self.module = module  # метка воспоминания
            self.pict   = pict    # скрин для кнопки в галерее воспоминаний
            self.set    = set     # блок формирования настроек для текущего воспоминания
            self.capt   = capt    # подпись, наименование воспоминания
            self.var    = var     # дополнительное условие доступности

        def __repr__(self):
            return "label='{self.module}', подпись - \"{self.capt}\"".format(self=self)

        def open(self):
            if self.module in persistent.memories:
                if persistent.memories[self.module] > 0:
                    return 'open' if renpy.seen_label(self.module) and eval(self.var) else 'close'
                elif persistent.memories[self.module] < 0:
                    return 'block'
                else:
                    return 'close'
            else:
                return 'open' if renpy.seen_label(self.module) and eval(self.var) else 'close'

    def start_replay(set_lbl, replay_lbl):
        global my_scope
        my_scope = eval(set_lbl+'()') if set_lbl else None
        renpy.call_replay(replay_lbl, my_scope)

    def count_album():
        rez = 0
        for album in photo_album:
            if album[0] in persistent.photos:
                rez += 1
        return rez

    def prev_shot(id_key, shot):
        rez = False
        while not rez and shot>0:
            shot -= 1
            rez = persistent.photos[id_key][shot]
        return rez

    def next_shot(id_key, shot):
        rez = False
        while not rez and shot+1<len(persistent.photos[id_key]):
            shot += 1
            rez = persistent.photos[id_key][shot]
        return rez

define mems = [
        [
            Memories('gift_swimsuit.swimsuit_show', 'lisa-newsuit-01', 'set_gift_swimsuit', _("Новый купальник Лизы")),
            Memories('gift_pajamas', 'alice-pajamas-01', 'set_gift_pajamas', _("Извинительная пижамка для Алисы")),
            Memories('gift_black_lingerie', 'alice-newlingerie-01', 'set_gift_black_lingerie', _("Тёмное кружево")),
        ],
        [
            Memories('massage_sunscreen', 'alice-massagesun-01', 'set_sunscreen', _("Давай я нанесу крем")),
            Memories('alice_talk_tv', 'alice-massagetv-01', 'set_talk_tv', _("Ножкам приятно")),
            Memories('alice_talk_tv.massage_next', 'alice-massagetv-02', 'set_advanced_massage1', _("Помассирую не только ножки"), var="'advanced_massage1' in persistent.mems_var"),
            Memories('Lisa_HomeWork.first_foot_mass', 'lisa-massage-01', 'set_foot_mass', _("Первый массаж ног")),
            Memories('liza_hand_mass', 'lisa-massage-02', 'set_hand_mass', _("Внимание к пальчикам")),
            Memories('Lisa_HomeWork.shoulders', 'lisa-massage-03', 'set_shoulders_mass', _("Разомнём и плечики")),
            Memories('kira_bath.ladder', 'kira-bathmassage-01', 'set_kira_bathmass', _("Массаж для любимой тёти"), var="'kira_mass_bath_first' in persistent.mems_var"),
            Memories('kira_bath.mass_bath', 'kira-bathfj-01', 'set_kira_bathfj', _("Совсем другой массаж")),
        ],
        [
            Memories('spider_in_bed', 'alice-spidernight-01', 'set_spider_in_bed', _("Ночные страхи")),
            Memories('massage_sunscreen.spider', 'alice-spidermassage-01', 'set_spider_massage', _("Кто это там ползёт")),
            Memories('alice_shower.spider', 'alice-spidershower-01', 'set_spider_shower', _("Монстр в ванной комнате")),
            Memories('alice_after_club.knock', 'alice-afterclub-01', 'set_after_club', _("После клуба")),
            Memories('alice_after_club.next1', 'alice-afterclub-02', 'set_after_club_next1', _("Я была плохой девочкой")),
        ],
        [
            Memories('kira_night_tv.porn_view', 'kira-pornotv-01', 'set_porn_tv', _("Смотрим порно вместе с тётей")),
            Memories('kira_night_tv.first_lesson', 'kira-kisslesson-01', 'set_kira_kiss_01', _("Первый урок поцелуев")),
            Memories('kira_bath.mass_bath', 'kira-bathbj-01', 'set_kira_bathbj', _("А это уже совсем не массаж!"), var="'bath_cuni_bj' in persistent.mems_var"),
            Memories('kira_night_tv.second_lesson', 'kira-kisslesson-02', 'set_kira_kiss_02', _("Второй урок поцелуев")),
            Memories('kira_night_tv.repeat_lesson', 'kira-kisslesson-03', 'set_kira_kiss_03', _("Третий урок поцелуев"), var="'kira_tv_bj' in persistent.memories and persistent.memories['kira_tv_bj']>0"),
            Memories('kira_night_tv.tv_cuni', 'kira-pornotv-02', 'set_porn_tv2', _("Горячее, чем порно"), var="'kira_night_tv.porn_view' in persistent.memories and persistent.memories['kira_night_tv.porn_view']>2"),
            Memories('kira_night_swim', 'kira-night-pool-01', 'set_night_swim', _("Небольшое приключение перед сном"), "'hj_in_pool' in persistent.mems_var"),
            Memories('kira_about_photo1', 'kira-max-shower-bj-01', '', _("Не зря купил сорочку")),
            Memories('kira_shower.promise_cuni', 'kira-max-shower-cuni-01', '', _("С меня приятный должок")),
        ],
        [
            Memories('lisa_advanced_kiss_lesson', 'lisa-kisslesson-01', 'set_lisa_advanced_kiss_lesson', _("Вкусные уроки с сестрёнкой")),
            Memories('liza_hand_mass', 'lisa-kissmassage-02', 'set_kiss_massage1', _("Кажется, мы что-то забыли"), var="'kissing_massage' in persistent.mems_var"),
        ],
        [
            Memories('lessons_from_Eric.first_bj', 'ann&eric-bj01', 'set_lessons_Eric_01', _("Урок по минету от мамы и Эрика")),
            Memories('lessons_from_Eric.second_bj', 'ann&eric-bj02', 'set_lessons_Eric_01', _("Так близко к маминой попке")),
            Memories('lessons_from_Eric.third_bj', 'ann&eric-bj03', 'set_lessons_Eric_01', _("Глубокий минет в мамином исполнении")),
        ],
    ]

define photo_album = [
        ("01-Kira", _("Порно-портфолио для Киры")),
        ("02-Kira", _("Немного БДСМ от Киры")),
        ("01-Alice", _("Первые снимки для блога Алисы")),
    ]

define cur_starts = [0, 0, 0, 0, 0, 0]
define cur_album = None
default st_gallery =  'mem'

define next_sh = False
define prev_sh = False

screen menu_gallery():
    tag menu
    style_prefix 'extra'

    add 'interface phon'
    frame area(150, 95, 350, 50) background None:
        hbox spacing 15:
            textbutton _("ВОСПОМИНАНИЯ"):
                action SetVariable('st_gallery', 'mem')
                selected st_gallery == 'mem'
            textbutton _("ФОТОСНИМКИ"):
                action SetVariable('st_gallery', 'art')
                selected st_gallery == 'art'

    imagebutton pos (1740, 100) auto 'interface close %s' action Jump('AfterWaiting'):
        if not renpy.variant('small'):
            focus_mask True
            at close_zoom
        else:
            at close_zoom_var_small

    if st_gallery == 'mem':
        frame area(140, 160, 1640, 850) xalign 0.0 yalign 0.5 background None:
            hbox spacing 5:
                viewport mousewheel 'change' draggable True id 'vp' area(0, 0, 1630, 840):
                    vbox spacing 10:
                        for i in range(len(cur_starts)):
                            frame ysize 330 padding(0, 0, 0, 0) background None:
                                imagebutton xpos 5 yalign 0.4 auto 'interface prev %s':
                                    focus_mask True
                                    sensitive cur_starts[i] > 0
                                    action Function(MySet, i, cur_starts[i]-1)
                                imagebutton xpos 1505 yalign 0.4 auto 'interface next %s':
                                    focus_mask True
                                    sensitive cur_starts[i] < len(mems[i])-3
                                    action Function(MySet, i, cur_starts[i]+1)
                                frame area(105, 0, 1380, 330) padding(0, 0, 0, 0) background None:
                                    hbox spacing 15:
                                        for j in range(cur_starts[i], cur_starts[i]+ 3 if len(mems[i])>=3 else len(mems[i])):
                                            button xysize (450, 330) padding(0, 0, 0, 0) background None:
                                                if mems[i][j].set !='':
                                                    action Function(start_replay, mems[i][j].set, mems[i][j].module)
                                                else:
                                                    action Replay(mems[i][j].module)
                                                sensitive mems[i][j].open()=='open'
                                                if mems[i][j].open()=='open':
                                                    add 'extra/mems/'+mems[i][j].pict+'.webp'
                                                    text mems[i][j].capt align(0.5, 0.9) color gui.accent_color size 20
                                                else:
                                                    if mems[i][j].open()=='block':
                                                        add im.MatrixColor('extra/mems/'+mems[i][j].pict+'.webp', im.matrix.desaturate())
                                                        text _("Воспоминание недоступно") align(0.5, 0.9) color gui.accent_color size 20
                                                    else:
                                                        add im.Scale(im.Scale(im.MatrixColor('extra/mems/'+mems[i][j].pict+'.webp', im.matrix.desaturate()), 50, 28), 450, 254)
                                                        text _("Воспоминание ещё не открыто") align(0.5, 0.9) color gui.accent_color size 20

                vbar value YScrollValue('vp') style 'extra_vscroll'
    elif st_gallery == 'art':
        if count_album()==0:
            frame area(100, 160, 1720, 850) xalign 0.0 yalign 0.5 background None:
                text _("В вашей коллекции ещё нет фотоснимков.") size 36 font 'hermes.ttf' color gui.accent_color align(0.5, 0.5)
        else:
            hbox spacing 15 pos (50, 160):
                # список альбомов
                frame ypos 20 xsize 320 ysize 830 background None:
                    hbox:
                        viewport mousewheel 'change' draggable True id 'vp1':
                            vbox spacing 5:
                                for id, desc in photo_album:
                                    if id in persistent.photos:
                                        if cur_album is None:
                                            $ cur_album = id
                                        button background None action SetVariable('cur_album', id) xsize 290 style 'alb_button':
                                            textbutton desc action SetVariable('cur_album', id) selected cur_album == id style 'album_button'

                        vbar value YScrollValue('vp1') style 'extra_vscroll'

                # таблица текущего альбома
                frame xsize 1500 ysize 850 background None:
                    hbox spacing 15:
                        vpgrid cols 3 spacing 40 mousewheel 'change' draggable True id 'vp':
                            for photo in persistent.photos[cur_album]:
                                frame xysize(450, 254) background None:
                                    if photo:
                                        imagebutton pos(0.5, 0.5) anchor (0.5, 0.5) idle 'photoshot '+cur_album+' '+photo action Show('photo_art', cur_alb=cur_album, photo=photo) at zoom_out(450, 254)
                                    else:
                                        imagebutton pos(0.5, 0.5) anchor (0.5, 0.5) idle 'photoshot closed' action NullAction() at zoom_out(450, 254)

                        vbar value YScrollValue('vp') style 'extra_vscroll'

style extra_button_text is default:
    size 28
    font 'hermes.ttf'
    idle_color gui.accent_color
    hover_color gui.text_color
    selected_color gui.text_color
    insensitive_color gui.insensitive_color

style alb_button:
    padding(30, 0, 5, 0) xmargin 0 ymargin 5
    foreground 'interface marker'

style album_button_text:
    font 'trebucbd.ttf'
    yalign .5
    size 26
    idle_color gui.accent_color
    hover_color gui.text_color
    selected_color gui.text_color

style extra_vscroll is vscrollbar:
    unscrollable 'hide' #'insensitive'


screen photo_art(cur_alb, photo):
    $ photo_list = []
    for i in persistent.photos[cur_alb]:
        if i:
            $ photo_list.append(i)
    default cur_photo = photo
    frame xfill True yfill True background 'photoshot '+cur_alb+' '+cur_photo
    # text str(prev_shot(cur_alb, int(cur_photo)-1))+' / '+cur_photo+' / '+str(next_shot(cur_alb, int(cur_photo)-1))
    hbox:
        ypos 970
        xalign 0.5
        spacing 30
        button action NullAction() background Frame('interface items-shop bg', 10, 10):
            xpadding 5 xmargin 0 ymargin 0
            button action NullAction() style "alb_button":
                textbutton _("Предыдущий снимок") style 'album_button':
                    sensitive cur_photo > min(photo_list)
                    action SetScreenVariable('cur_photo', prev_shot(cur_alb, int(cur_photo)-1))
        button action Hide('photo_art') background Frame('interface items-shop bg', 10, 10):
            xpadding 5 xmargin 0 ymargin 0
            button action Hide('photo_art') style "alb_button":
                textbutton _("Вернуться в коллекцию") action Hide('photo_art') style 'album_button'

        button action NullAction() background Frame('interface items-shop bg', 10, 10):
            xpadding 5 xmargin 0 ymargin 0
            button action NullAction() style "alb_button":
                textbutton _("Следующий снимок") style 'album_button':
                    sensitive cur_photo < max(photo_list)
                    action SetScreenVariable('cur_photo', next_shot(cur_alb, int(cur_photo)-1))

    key 'K_ESCAPE' action Hide('photo_art')
    key 'mouseup_3' action Hide('photo_art')
