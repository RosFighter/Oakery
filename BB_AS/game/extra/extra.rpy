
init python:

    def MySet(i, x):
        global cur_starts
        cur_starts[i][0] = x

    class Memories:
        def __init__(self, module, pict, set='', capt="", cond=''):
            self.module = module  # метка воспоминания
            self.pict   = pict    # скрин для кнопки в галерее воспоминаний
            self.set    = set     # блок формирования настроек для текущего воспоминания
            self.capt   = capt    # подпись, наименование воспоминания

        def __repr__(self):
            return "label='{self.module}', подпись - \"{self.capt}\"".format(self=self)

        def open(self):
            if self.module in persistent.memories:
                return 'open' if persistent.memories[self.module] else 'block'
            else:
                return 'open' if renpy.seen_label(self.module) else 'close'                


define mems = [
        [
            Memories('gift_swimsuit.swimsuit_show', 'lisa-newsuit-01', 'set_gift_swimsuit', _("Новый купальник Лизы")),
            Memories('gift_pajamas', 'alice-pajamas-01', 'set_gift_pajamas', _("Извинительная пижамка для Алисы")),
        ],
        [
            Memories('Lisa_HomeWork.first_foot_mass', 'lisa-massage-01', 'set_foot_mass', _("Первый массаж ног")),
            Memories('liza_hand_mass', 'lisa-massage-02', 'set_hand_mass', _("Внимание к пальчикам")),
            Memories('Lisa_HomeWork.shoulders', 'lisa-massage-03', 'set_shoulders_mass', _("Разомнём и плечики")),
        ],
    ]

screen menu_gallery():
    tag menu
    style_prefix 'extra'
    $ cur_starts = [[0, len(mems[i])] for i in range(len(mems))]

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
                                    sensitive cur_starts[i][0] > 0
                                    action Function(MySet, i, cur_starts[i][0]-1)
                                imagebutton xpos 1505 yalign 0.4 auto 'interface next %s':
                                    focus_mask True
                                    sensitive cur_starts[i][0]+3 < cur_starts[i][1]
                                    action Function(MySet, i, cur_starts[i][0]+1)
                                frame area(105, 0, 1380, 330) padding(0, 0, 0, 0) background None:
                                    hbox spacing 15:
                                        for j in range(min(3, cur_starts[i][1])):
                                            button xysize (450, 330) padding(0, 0, 0, 0) background None:
                                                if mems[i][j].set !='':
                                                    action [eval(mems[i][j].set+'()'), Replay(mems[i][j].module, my_scope)]
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
