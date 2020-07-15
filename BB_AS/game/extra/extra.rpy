
init python:

    def MySet(i, x):
        global cur_starts
        cur_starts[i] = x

    class Memories:
        def __init__(self, module, pict, set='', capt="", cond='', var='True'):
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
        my_scope = eval(set_lbl+'()')
        renpy.call_replay(replay_lbl, my_scope)


define mems = [
        [
            Memories('gift_swimsuit.swimsuit_show', 'lisa-newsuit-01', 'set_gift_swimsuit', _("Новый купальник Лизы")),
            Memories('gift_pajamas', 'alice-pajamas-01', 'set_gift_pajamas', _("Извинительная пижамка для Алисы")),
        ],
        [
            Memories('massage_sunscreen', 'alice-massagesun-01', 'set_sunscreen', _("Давай я нанесу крем")),
            Memories('alice_talk_tv', 'alice-massagetv-01', 'set_talk_tv', _("Ножкам приятно")),
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
        ],
        [
            Memories('kira_night_tv.porn_view', 'kira-pornotv-01', 'set_porn_tv', _("Смотрим порно вместе с тётей")),
            Memories('kira_night_tv.first_lesson', 'kira-kisslesson-01', 'set_kira_kiss_01', _("Первый урок поцелуев")),
            Memories('kira_bath.mass_bath', 'kira-bathbj-01', 'set_kira_bathbj', _("А это уже совсем не массаж!"), var="'bath_cuni_bj' in persistent.mems_var"),
            Memories('kira_night_tv.second_lesson', 'kira-kisslesson-02', 'set_kira_kiss_02', _("Второй урок поцелуев")),
            Memories('kira_night_tv.repeat_lesson', 'kira-kisslesson-03', 'set_kira_kiss_03', _("Третий урок поцелуев"), var="'kira_tv_bj' in persistent.memories and persistent.memories['kira_tv_bj']>0"),
            Memories('kira_night_tv.tv_cuni', 'kira-pornotv-02', 'set_porn_tv2', _("Горячее, чем порно"), var="'kira_night_tv.porn_view' in persistent.memories and persistent.memories['kira_night_tv.porn_view']>2"),
        ],
    ]

define cur_starts = [0, 0, 0, 0]

screen menu_gallery():
    tag menu
    style_prefix 'extra'

    add 'interface phon'
    default st = 'mem'
    frame area(150, 95, 350, 50) background None:
        hbox spacing 15:
            textbutton _("ВОСПОМИНАНИЯ"):
                action SetScreenVariable('st', 'mem')
                selected st=='mem'
            textbutton _("ФОТОСНИМКИ"):
                action SetScreenVariable('st', 'art')
                selected st=='art'
                sensitive False
    imagebutton pos (1740, 100) auto 'interface close %s' action Jump('AfterWaiting') focus_mask True at close_zoom

    if st == 'mem':
        frame area(140, 160, 1640, 850) xalign 0.0 yalign 0.5 background None:
            hbox spacing 5:
                viewport mousewheel 'change' draggable True id 'vp' area(0, 0, 1630, 840):# scrollbars "vertical":
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

style extra_button_text is default:
    size 28
    font 'hermes.ttf'
    idle_color gui.accent_color
    hover_color gui.text_color
    selected_color gui.text_color
    insensitive_color gui.insensitive_color

style extra_vscroll is vscrollbar:
    unscrollable 'hide'
