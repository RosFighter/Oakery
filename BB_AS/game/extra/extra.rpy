
init 100 python:
    extra_content = True


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
            Memories('alice_talk_tv_massage_next', 'alice-massagetv-02', 'set_advanced_massage1', _("Помассирую не только ножки"), var="'advanced_massage1' in persistent.mems_var"),
            Memories('advanced_massage1', 'alice-massagetv-03', 'set_advanced_massage2', _("Могу не только руками"), var="renpy.seen_label('advanced_massage1_no_rush')"),
            Memories('advanced_massage1_reciprocity', 'alice-massagetv-04', 'set_advanced_massage3', _("Ответная благодарность")),
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
            Memories('massage_sunscreen.spider', 'alice-spidermassage-02', 'set_spider_massage2', _("Держи и не отпускай"), var="'hide_behind' in persistent.mems_var"),
            Memories('alice_after_club.knock', 'alice-afterclub-01', 'set_after_club', _("После клуба")),
            Memories('alice_after_club.next1', 'alice-afterclub-02', 'set_after_club_next1', _("Я была плохой девочкой")),
            Memories('alice_after_club.next2', 'alice-afterclub-03', 'set_after_club_next2', _("Как тебе такое?"), var="renpy.seen_label('alice_after_club.cunnilingus')"),
            Memories('alice_towel_after_club', 'alice-afterclubbath-01', 'set_alice_towel_after_club', _("Я принес тебе полотенце!"), var="'bath_fan' in persistent.mems_var"),
            Memories('alice_blog_lingerie', 'alice-dress&photoset-01', 'set_alice_body_photoset1', _("Первые снимки для блога Алисы"), var="'alice_photoset1' in persistent.mems_var"),  # добавить условие на состоявшуюся фотосессию
            Memories('alice_blog_lingerie', 'alice-dress&max-01', 'set_gift_lace_lingerie', _("Я обошёл Эрика с подарком для Алисы"), var="'lace_ling_max1' in persistent.mems_var"),  # gift_lace_lingerie
            Memories('alice_private_punish_r.smoke_pun', 'alice-privatepun-01', 'set_private_punish1', _("Попка, которую я теперь могу отшлёпать")),
            Memories('alice_mistress_3', 'alice-dominance-01', 'set_alice_domine_drink', _("Меня нужно наказать именно так!"), var = "renpy.seen_label('alice_domine_drink.kiss')"),
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
            Memories('return_from_club', 'kira-strip-01', 'set_kira_strip_01', _("Стриптиз после клуба"), var="'kira_tv_bj' in persistent.memories and persistent.memories['kira_tv_bj']>0"),
            Memories('kira_talk6', 'kira-photoset-01', 'set_kira_photoset_01', _("Порно-портфолио для Киры"), var="'kira_photoset1' in persistent.mems_var"),
            Memories('kira_about_photo2', 'kira-photoset-02', '', _("Немного БДСМ от Киры")),
            Memories('kira_night_tv.teach_cuni', 'kira-tvsex-04', 'set_porn_tv3', _("Хватит мять сиськи"), var="renpy.seen_label('kira_night_tv.tv_sex1') or renpy.seen_label('kira_night_tv.tv_sex2')"),
            Memories('kira_bath.cuni_bj', 'kira-bathsex-04', 'set_kira_batxsex1', _("И помылись, и порезвились"), var="renpy.seen_label('kira_bath.horsewoman') or renpy.seen_label('kira_bath.dogstyle')"),
            Memories('kira_photoset3', 'kira-photoset-03', 'set_kira_photoset3', _("Кто нас фотографирует?")),
            Memories('kira_shower.sex', 'kira-shower-03', '', _("Вместо ночного плаванья")),
        ],
        [
            Memories('lisa_advanced_kiss_lesson', 'lisa-kisslesson-01', 'set_lisa_advanced_kiss_lesson', _("Вкусные уроки с сестрёнкой")),
            Memories('liza_hand_mass', 'lisa-kissmassage-02', 'set_kiss_massage1', _("Кажется, мы что-то забыли"), var="'kissing_massage' in persistent.mems_var"),
            Memories('Lisa_HomeWork.new_self', 'lisa-massage-04', 'set_homework_mass_01', _("Больше, чем помощь с домашним заданием")),
            Memories('lisa_horor_movie_r', 'lisa-horror-01', 'set_horor_01', _("Ужастики в обнимку с Лизой")),
            Memories('lisa_horor_movie_r', 'lisa-horror-02', 'set_horor_02', _("Без майки куда интереснее"), var="'horror_topples_kiss' in persistent.mems_var"),
            Memories('olivia_second_night_visit', 'lisa-tv-01', 'set_olivia_second_night_visit', _("Долой смущение"), var="renpy.seen_label('olivia_second_night_out_with')"),
        ],
        [
            Memories('ann_talk_tv.first_movie', 'ann-erotv-01', 'set_ann_ero1', _("Я уже взрослый!")),
            Memories('erofilm2_1', 'ann-erotv-02', 'set_ann_ero2', _("Это точно триллер-детектив?")),
            Memories('erofilm2_2', 'ann-erotv-03', 'set_ann_ero2', _("Полотенце снова сползает...")),
        ],
        [
            Memories('lessons_from_Eric.first_bj', 'ann&eric-bj01', 'set_lessons_Eric_01', _("Урок по минету от мамы и Эрика")),
            Memories('lessons_from_Eric.second_bj', 'ann&eric-bj02', 'set_lessons_Eric_01', _("Так близко к маминой попке")),
            Memories('lessons_from_Eric.third_bj', 'ann&eric-bj03', 'set_lessons_Eric_01', _("Глубокий минет в мамином исполнении")),
        ],
        [
            Memories('sexed_lisa.lesson_0', 'lisa-sexed-01', 'set_sexed_01', _("Её первые познания...")),
            Memories('sexed_lisa.lesson_1', 'lisa-sexed-02', 'set_sexed_01', _("Как возбудить ещё больше?")),
            Memories('sexed_lisa.lesson_2', 'lisa-sexed-03', 'set_sexed_01', _("Нежно и аккуратно!")),
            Memories('sexed_lisa.lesson_3', 'lisa-sexed-04', 'set_sexed_01', _("Как долго это нужно делать?")),
            Memories('blog_with_Eric', 'alice-dress&eric-01', 'set_blog_with_Eric_01', _("Кружевное боди для Алисы от Эрика"), var="'lace_ling_eric1' in persistent.mems_var"),
        ],
    ]

define photo_album = [
        ("01-Kira", _("Порно-портфолио для Киры")),
        ("02-Kira", _("Немного БДСМ от Киры")),
        # ("03-Kira", _("Тройничок")),
        ("01-Alice", _("Первые снимки для блога Алисы")),
    ]

define cur_starts = [0, 0, 0, 0, 0, 0, 0, 0]
define displayed_group = [1, 1, 1, 1, 1, 1, 0, 0]
default st_gallery =  'mem'

define next_sh = False
define prev_sh = False

screen menu_gallery():
    tag menu
    style_prefix 'extra'

    $ renpy.start_predict('extra/**.webp')

    add 'interface phon'
    frame area(150, 95, 350, 50) background None:
        hbox spacing 15:
            textbutton _("ВОСПОМИНАНИЯ"):
                action SetVariable('st_gallery', 'mem')
                selected st_gallery == 'mem'
            textbutton _("ФОТОСНИМКИ"):
                action SetVariable('st_gallery', 'art')
                selected st_gallery == 'art'

    imagebutton pos (1740, 100) auto 'interface close %s' action Jump('AfterWaiting') at close_zoom:
        focus_mask (None if renpy.variant('small') else True)

    if st_gallery == 'mem':
        frame area(140, 160, 1640, 850) xalign 0.0 yalign 0.5 background None:
            hbox spacing 5:
                viewport mousewheel 'change' draggable True id 'vp' area(0, 0, 1630, 840):
                    vbox spacing 10:
                        for i, st_i in enumerate(cur_starts):
                            # выводим группу
                            $ __displayed = displayed_group[i]>0

                            if not __displayed:
                                for j, mem in enumerate(mems[i]):
                                    if mem.open()=='open':
                                        $ __displayed = True

                            if __displayed:
                                # если в группе нет отображаемых воспоминаний - не показываем её
                                frame ysize 330 padding(0, 0, 0, 0) background None:
                                    imagebutton xpos 5 yalign 0.4 auto 'interface prev %s':
                                        focus_mask (None if renpy.variant("small") else True)
                                        sensitive cur_starts[i] > 0
                                        action Function(MySet, i, cur_starts[i]-1)
                                    imagebutton xpos 1505 yalign 0.4 auto 'interface next %s':
                                        focus_mask (None if renpy.variant("small") else True)
                                        sensitive cur_starts[i] < len(mems[i])-3
                                        action Function(MySet, i, cur_starts[i]+1)
                                    frame area(105, 0, 1380, 330) padding(0, 0, 0, 0) background None:
                                        hbox spacing 15:
                                            for j in range(cur_starts[i], cur_starts[i]+ 3 if len(mems[i])>=3 else len(mems[i])):
                                                # видимые воспоминания группы
                                                button xysize (450, 330) padding(0, 0, 0, 0) background None:
                                                    if mems[i][j].set !='':
                                                        action Function(start_replay, mems[i][j].set, mems[i][j].module)
                                                    else:
                                                        action Replay(mems[i][j].module)
                                                    sensitive mems[i][j].open()=='open'
                                                    if mems[i][j].open()=='open':
                                                        add 'extra/mems/'+mems[i][j].pict+'.webp'
                                                        text renpy.config.say_menu_text_filter(renpy.translate_string(mems[i][j].capt)) align(0.5, 0.9) color gui.accent_color size 20
                                                    else:
                                                        if mems[i][j].open()=='block':
                                                            if config.gl2:
                                                                add 'extra/mems/'+mems[i][j].pict+'.webp' at desaturate
                                                            else:
                                                                add im.MatrixColor('extra/mems/'+mems[i][j].pict+'.webp', im.matrix.desaturate())
                                                            text _("Воспоминание недоступно") align(0.5, 0.9) color gui.accent_color size 20
                                                        else:
                                                            if config.gl2:
                                                                add 'extra/mems/'+mems[i][j].pict+'.webp' at desaturate, blurred
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
                                for id_alb, desc in photo_album:
                                    if id_alb in persistent.photos:
                                        if 'cur_album' not in globals() or cur_album is None or cur_album not in persistent.photos:
                                            $ cur_album = id_alb
                                        button background None action SetVariable('cur_album', id_alb) xsize 290 style 'alb_button':
                                            textbutton desc action SetVariable('cur_album', id_alb) selected cur_album == id_alb style 'album_button'

                        vbar value YScrollValue('vp1') style 'extra_vscroll'

                # таблица текущего альбома
                frame xsize 1500 ysize 850 background None:
                    hbox spacing 15:
                        vpgrid cols 3 spacing 40 mousewheel 'change' draggable True id 'vp':
                            for photo in persistent.photos[cur_album]:
                                frame xysize(450, 254) background None:
                                    if photo:
                                        imagebutton pos(0.5, 0.5) anchor (0.5, 0.5) idle 'extra photoshot '+cur_album+' '+photo action Show('photo_art', cur_alb=cur_album, photo=photo)
                                    else:
                                        imagebutton pos(0.5, 0.5) anchor (0.5, 0.5) idle 'extra photoshot closed' action NullAction()

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
