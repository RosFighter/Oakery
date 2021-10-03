################################################################################
## события Лизы

label lisa_sleep_night:
    if all([flags.film_punish, not lisa.dcv.special.done, tm < '00:30']):
        call lisa_select_movie from _call_lisa_select_movie

    scene BG char Lisa bed-n-01
    $ AvailableActions['touch'].active = True
    $ renpy.show('Lisa sleep-night '+pose3_1)
    $ renpy.show('FG Lisa sleep-night '+pose3_1+lisa.dress)
    return


label lisa_sleep_morning:
    scene BG char Lisa bed-morning
    $ renpy.show('Lisa sleep-morning '+pose3_1)
    $ renpy.show('FG Lisa sleep-morning '+pose3_1+lisa.dress)
    return


label lisa_shower:
    scene location house bathroom door-morning
    if lisa.daily.shower > 3:
        menu:
            Max_00 "Лиза сейчас принимает душ..."
            "{i}уйти{/i}":
                jump .end_peeping2
    elif lisa.daily.shower > 2:
        Max_14 "Лиза уже поймала меня на подглядывании. Грозилась рассказать маме. Не стоит злить её ещё больше."
        jump .end_peeping2
    elif lisa.daily.shower > 1:
        Max_09 "Сегодня я уже чуть не попался Лизе при подглядывании. Повезло, что успел вовремя сбежать. Не стоит рисковать ещё раз."
        jump .end_peeping2
    elif lisa.daily.shower > 0:
        Max_01 "Сегодня я уже подсматривал за Лизой. Повезло, что она меня не заметила. Не стоит рисковать ещё раз."
        jump .end_peeping2

    $ renpy.block_rollback()
    $ renpy.dynamic('r1')
    $ lisa.daily.shower = 4
    menu:
        Max_09 "Кажется, Лиза что-то делает в ванной..."
        "{i}постучаться{/i}":
            menu:
                Lisa "{b}Лиза:{/b} Кто там? Я ещё не закончила. Подождите немного..."
                "Это я, Макс!":
                    menu:
                        Lisa "{b}Лиза:{/b} Макс, чего хотел? Я же говорю, скоро выйду!"
                        "Можно я войду? Мне очень нужно...":
                            menu:
                                Lisa "{b}Лиза:{/b} Нет, Макс. Жди за дверью. Я скоро!"
                                "Ладно, ладно...":
                                    $ lisa.daily.shower = 4
                                    jump .end_peeping
                        "Хорошо, я подожду":
                            $ lisa.daily.shower = 4
                            jump .end_peeping
                "{i}уйти{/i}":
                    $ lisa.daily.shower = 4
                    jump .end_peeping
        "{i}заглянуть со двора{/i}":
            if lisa.sorry.owe:
                Max_10 "Хочется, конечно, ещё разок взглянуть на голую сестрёнку, но я ещё не отдал ей обещанное..."
                jump .end_peeping2
            jump .start_peeping
        "{i}воспользоваться стремянкой{/i}" if flags.ladder > 2:
            jump .ladder
        "{i}уйти{/i}":
            $ lisa.daily.shower = 4
            jump .end_peeping

    label .ladder:
        $ renpy.dynamic('lst')
        $ renpy.scene()
        $ renpy.show('Max bathroom-window-morning 01'+mgg.dress)
        Max_04 "Посмотрим, что у нас тут..."
        $ lisa.flags.ladder += 1
        # назначим или определим одёжку
        if lisa.dress_inf != '04a':
            $ r1 = {'04c':'a', '04d':'b', '02c':'c', '00':'d', '00a':'d'}[lisa.dress_inf]
        else:
            $ lst = ['a', 'b', 'c', 'd'] if 'bathrobe' in lisa.gifts else ['c', 'd']
            $ r1 = renpy.random.choice(lst)
            $ lisa.dress_inf = {'a':'04c', 'b':'04d', 'c':'02c', 'd':'00'}[r1]

        scene BG bathroom-morning-00
        $ renpy.show('Lisa bath-window-morning '+renpy.random.choice(['01', '02', '03'])+r1)
        show FG bathroom-morning-00
        $ Skill('hide', 0.05)
        if r1 in ['a', 'b']:
            Max_03 "Класс! Лиза смотрится в подаренном мною халатике очень соблазнительно... Особенно когда так хорошо видно её упругие сисечки!"
        elif r1 == 'c':
            Max_07 "О, да! Моя обворожительная сестрёнка в одних трусиках... Так и хочется зайти и стянуть их с её прекрасной попки!"
        else:
            Max_06 "Ого! Утро может быть действительно очень добрым, если удаётся полюбоваться совершенно голенькой Лизой! Да... её тело завораживает..."

        if looked_ladder():
            $ house[3].max_cam = 2
            $ items['hide_cam'].unblock()
            Max_07 "Мои зрители явно пропускают много всего интересного! Мне однозначно стоит установить сюда ещё одну камеру..."
        Max_00 "Хоть и не хочется, но пока меня не заметили, лучше уходить..."
        jump .end_peeping

    label .start_peeping:
        $ lisa.daily.shower = 1
        $ Skill('hide', 0.03, 60)
        $ r1 = renpy.random.randint(1, 4)

        $ renpy.scene()
        $ renpy.show('Lisa shower 0'+str(r1))
        $ renpy.show('FG shower 00'+mgg.dress)
        play music spying
        menu:
            Max_07 "Отлично! Моя младшая сестрёнка принимает душ... Даже видно кое-что... Много кое-чего! Только бы она меня не заметила..."
            "{i}продолжить смотреть{/i}" ('hide', mgg.stealth * 3, 90, 2) if lisa.dcv.shower.stage<2:
                jump .closer_peepeng
            "{i}взглянуть со стороны{/i}" ('hide', mgg.stealth * 2, 90, 2) if lisa.dcv.shower.stage<2:
                jump .alt_peepeng
            "{i}немного пошуметь{/i}" if lisa.dcv.shower.stage<2 and (0<len(lisa.sorry.give)<4 or (not poss['SoC'].used(0) and mgg.stealth * 3 > 60)):
                jump .pinded
            "{i}немного пошуметь{/i}" if len(lisa.sorry.give)>3 and lisa.dcv.shower.stage<2:
                jump .pinded
            "{i}уйти{/i}":
                jump .end_peeping

    label .alt_peepeng:
        if rand_result < 2:
            jump .not_luck
        $ spent_time += 10
        $ lisa.daily.shower = 1
        $ lisa.dress_inf = '00a'
        $ r1 = renpy.random.randint(1, 6)
        scene BG shower-alt
        $ renpy.show('Max shower-alt 01'+mgg.dress)
        $ renpy.show('Lisa shower-alt 0'+str(r1))
        show FG shower-water
        if 1 < r1 < 5:
            Max_02 "[undetect!t]Лиза вся такая мокренькая... класс! Фигурка и всё остальное у неё – что надо... Как же хочется потрогать!"
        else:
            Max_03 "[undetect!t]О, да! За тем, как вода стекает по её обворожительной попке, хочется смотреть не отрываясь..."
        jump .end_peeping

    label .closer_peepeng:
        $ spent_time += 10
        if rand_result > 1:
            $ lisa.daily.shower = 1
            $ lisa.dress_inf = '00a'
            $ r1 = renpy.random.randint(1, 6)
            scene BG shower-closer
            $ renpy.show('Lisa shower-closer 0'+str(r1))
            show FG shower-closer
            if 1 < r1 < 5:
                Max_02 "[undetect!t]Лиза вся такая мокренькая... класс! Фигурка и всё остальное у неё – что надо... Как же хочется потрогать!"
            else:
                Max_03 "[undetect!t]О, да! За тем, как вода стекает по её обворожительной попке, хочется смотреть не отрываясь..."
            jump .end_peeping
        else:
            jump .not_luck

    label .not_luck:
        if lisa_was_topless():
            jump .pinded
        if rand_result or len(lisa.sorry.give) > 3:
            $ lisa.daily.shower = 2
            $ lisa.dress_inf = '00a'
            $ r1 = renpy.random.choice(['07', '08'])
            scene BG shower-closer
            $ renpy.show('Lisa shower-closer '+r1)
            show FG shower-closer
            Max_12 "{color=[orange]}{i}Кажется, Лиза что-то заподозрила!{/i}{/color}\nО нет! Похоже, она что-то заметила... Надо бежать!"
        else:
            jump .pinded
        jump .end_peeping

    label .pinded:
        $ lisa.weekly.shower += 1
        if flags.film_punish:
            $ lisa.dcv.special.set_lost(1)
        else:
            $ lisa.daily.shower = 3
            $ punreason[0] = 1
        if lisa_was_topless():
            # после второго ТВ с Оливией
            $ r1 = renpy.random.choice(['07', '08'])
        else:
            $ r1 = renpy.random.choice(['09', '10'])
        scene BG shower-closer
        $ renpy.show('Lisa shower-closer '+r1)
        show FG shower-closer
        if lisa_was_topless() and lisa.dcv.other.stage:
            if lisa.weekly.shower>2:
                Lisa_11 "[spotted!t]Ой, Макс! Опять ты подглядываешь... Это уже маньячество какое-то!"
                Max_02 "Просто любуюсь формами! А так, я вообще мимо шёл, а здесь ты..."
                Lisa_10 "Вот и иди мимо! И без майки ты меня теперь две недели точно не увидишь. Помнишь, я предупреждала?"
                Max_08 "Блин! Точно, вспомнил... Но, может..."
                Lisa_13 "Нет. Это будет для тебя уроком!"
                Max_11 "Ладно..."
                $ lisa.dcv.shower.set_lost(14)
                jump .end_peeping
            else:
                menu:
                    Lisa_09 "[spotted!t]Ну, Макс! Опять ты подглядываешь... Если так неймётся ужастики смотреть со мной, то считай ты попал! А сейчас, кыш отсюда..."
                    "{i}уйти{/i}":
                        jump .end_peeping

        elif lisa.dcv.shower.stage:
            Lisa_13 "[spotted!t]Ай, Макс!!! Ты в конец бессовестный что ли?! Отвернись немедленно и иди куда шёл!"
            Max_13 "Лиза, я случайно! Ты же не расскажешь маме?"
            Lisa_14 "Ещё как расскажу! Сразу же, как только душ спокойно приму... А ты, вали с глаз моих!"
            Max_10 "Вот же попал!"
            $ lisa.dcv.shower.stage = 2
            $ lisa.dcv.shower.set_lost(4)
            jump .end_peeping

        else:
            menu:
                Lisa_12 "[spotted!t]Макс! Ты подглядываешь за мной? Как тебе не стыдно?! Я всё маме расскажу!"
                "{i}Бежать{/i}":
                    jump .end_peeping

    label .end_peeping2:
        $ current_room = house[6]
        jump AfterWaiting
    label .end_peeping:
        $ current_room = house[6]
        $ spent_time += 10
        jump Waiting
    return


label lisa_read:
    scene BG char Lisa bed-mde-01
    $ renpy.show('Lisa reading ' + pose3_1)
    $ renpy.show('FG Lisa reading ' + pose3_1 + lisa.dress)
    $ persone_button1 = ['Lisa reading ' + pose3_1, 'FG Lisa reading ' + pose3_1 + lisa.dress]

    return


label lisa_read_closer:
    scene BG char Lisa bed-mde-01
    show Lisa reading 00
    $ renpy.show('FG Lisa reading 00' + lisa.dress)
    return


# label lisa_dressed_school:
#     scene location house myroom door-morning
#
#     $ renpy.dynamic('r1', 'mood', 'suf')
#     $ mood = 0
#     if lisa.hourly.dressed:
#         return
#
#     $ lisa.hourly.dressed = 1
#     menu:
#         Max_09 "{m}Сейчас Лиза должна собираться в школу...{/m}"        #Max_09 "{m}Похоже, Лиза собирается в школу...{/m}"
#         "{i}войти в комнату{/i}":
#             if random_outcome(40) and tm[-2:]=='00':
#                 call lisa_sudden_dressing(0, -10) from _call_lisa_sudden_dressing    # "нулевой"
#             elif random_outcome(45):
#                 call lisa_sudden_dressing(1, -20) from _call_lisa_sudden_dressing_1    # неповезло
#             else:
#                 call lisa_sudden_dressing(2, -30) from _call_lisa_sudden_dressing_2    # повезло
#             jump .end
#         "{i}постучаться{/i}":
#             menu:
#                 Lisa "{b}Лиза:{/b} Кто там? Я переодеваюсь!"
#                 "{i}войти в комнату{/i}":
#                     call lisa_sudden_dressing(1, -20) from _call_lisa_sudden_dressing_3
#                 "Можно войти на секунду? Я только ноутбук возьму..." if flags.warning:
#                     menu:
#                         Lisa "{b}Лиза:{/b} Макс, дай одеться спокойно! Потом свой ноутбук заберёшь..."
#                         "{i}забрать ноутбук{/i}":
#                             $ lvl = get_lisa_emancipation()
#                             $ mood = {
#                                 1 : -50,
#                                 2 : -30,
#                                 3 : 0,
#                                 }[lvl]
#                             scene BG char Lisa dressing-02
#                             call lisa_dress_first_second(renpy.random.choice(['h', 'h', 'p']),
#                                                          lvl,
#                                                          0,
#                                                          renpy.random.randint(0, 1),
#                                                          renpy.random.randint(0, 1),
#                                                          0 if lvl < 3 else renpy.random.randint(0, 1)) from _call_lisa_dress_first_second
#                             Lisa_11 "Макс! Я не одета!!! Быстро закрой дверь с той стороны и не входи, пока я не переоденусь!"
#                             Max_09 "Лиза, мне ноутбук нужен для дела!"
#                             Lisa_13 "Какого дела? Ты дома сидишь целыми днями и ничего не делаешь..."
#                             menu:
#                                 Lisa_12 "Ладно, неважно... Забирай свой ноутбук и уходи. Дай мне уже переодеться..."
#                                 "{i}уйти с ноутбуком на веранду{/i}":
#                                     $ spent_time += 10
#                                     $ at_comp = True
#                                     $ current_room = house[5]
#                                     $ cam_flag.append('notebook_on_terrace')
#                                     $ AddRelMood('lisa', 0, mood)
#                                     jump Laptop
#                         "Хорошо, я подожду...":
#                             pass
#                 "Хорошо, я подожду...":
#                     pass
#             $ spent_time = 10
#             jump .end
#         "{i}заглянуть в окно{/i}":
#             jump .look_window
#         "{i}уйти{/i}":
#             $ spent_time = 10
#             jump .end
#
#     label .look_window:
#         $ spent_time = 10
#         $ r1 = renpy.random.choice(['01', '02', '03', '04'])
#         $ lisa.dress_inf = {'01':'02h', '02':'02e', '03':'02b', '04':'02c'}[r1]
#
#         if mgg.stealth >= 11.0 and renpy.random.choice([False, False, True]):
#             scene BG char Lisa voyeur-01
#             $ renpy.show('Lisa voyeur alt-'+r1)
#             $ renpy.show('FG voyeur-lisa-01'+mgg.dress)
#         else:
#             scene BG char Lisa voyeur-00
#             $ renpy.show('Lisa voyeur '+r1)
#             $ renpy.show('FG voyeur-lisa-00'+mgg.dress)
#
#         $ Skill('hide', 0.03, 10)
#         menu:
#             Max_01 "Ого, какой вид! Вот это я удачно заглянул!"
#             "{i}уйти{/i}":
#                 $ renpy.block_rollback()
#                 $ alt_wait()
#                 scene location house myroom door-morning
#                 call screen room_navigation
#                 # jump .end
#
#     # label .come_in:
#     #     scene BG char Lisa morning
#     #
#     #     $ spent_time = 60 - int(tm.split(":")[1])
#     #     if not lisa_was_topless():
#     #         $ lisa.dress_inf = '01b'
#     #         $ suf = 'b' if GetRelMax('lisa')[0]>1 else 'a' if GetRelMax('lisa')[0]>=0 else ''
#     #         $ renpy.show('Lisa school-dressed 01'+suf)
#     #         menu:
#     #             Lisa_00 "Макс, ну чего ломишься? Ты же знаешь, что мне в школу пора...\n\n{color=[orange]}{i}{b}Подсказка:{/b} Клавиша [[ h ] или [[ ` ] - вкл/выкл интерфейс.{/i}{/color}"
#     #             "Это и моя комната!":
#     #                 if lisa.GetMood()[0] < 0: # настроение не очень и ниже
#     #                     show Lisa school-dressed 01
#     #                     Lisa_12 "Так и знала, что тебя надо было на диванчики в гостиную отправлять... Ладно, я уже оделась, входи уж... А я в школу побежала."
#     #                     Max_00 "Удачи"
#     #                     $ rel  -= 5 # при плохом настроении отношения и настроение снижаются
#     #                     $ mood -= 25
#     #                 else: # нейтральное настроение
#     #                     Lisa_02 "В любом случае, я уже оделась, так что, входи. А я побежала в школу."
#     #                     Max_00 "Удачи"
#     #             "Да чего я там не видел...":
#     #                 if GetRelMax('lisa')[0] < 1: # отношения прохладные и ниже
#     #                     Lisa_12 "Что бы ты там не видел, но подождать немного за дверью можно было? Так или иначе, я уже оделась и побежала в школу. Вернусь часа в четыре."
#     #                     Max_00 "Пока, Лиза!"
#     #                     $ rel  -= 5 # при низком отношении отношения и настроение снижаются
#     #                     $ mood -= 25
#     #                 elif GetRelMax('lisa')[0] < 2: # Неплохие отношения
#     #                     Lisa_01 "А за дверью постоять не мог? А ладно, входи... Я уже оделась и побежала в школу."
#     #                     Max_00 "Пока, Лиза!"
#     #                 else: # хорошие и выше отношения
#     #                     Lisa_02 "Но за дверью подождать немного ты всё равно мог! Хотя бы для приличия..."
#     #                     show Lisa school-dressed 01a
#     #                     Lisa_01 "Как бы там ни было, проходи... Я уже оделась и побежала в школу. Вернусь часа в четыре."
#     #                     Max_00 "Пока, Лиза!"
#     #                     $ mood += 25 # при хорошем отношении настроение повышается
#     #             "Извини":
#     #                 if GetRelMax('lisa')[0] < 2: # Неплохие отношения
#     #                     Lisa_03 "Да ты у нас джентльмен! В общем, я тут закончила и побежала в школу. Пока!"
#     #                 else:
#     #                     Lisa_03 "Да ты у нас, оказывается, джентльмен!"
#     #                     show Lisa school-dressed 01a
#     #                     Lisa_01 "В общем, я тут закончила и побежала в школу. Пока!"
#     #                 Max_00 "Пока, Лиза!"
#     #                 $ mood += 25 # при извинении настроение повышается
#     #     else:
#     #         $ r1 = '0'+str(renpy.random.randint(3, 4))
#     #         $ suf = 'b' if GetRelMax('lisa')[0]>1 else 'a' if GetRelMax('lisa')[0]>=0 else ''
#     #         $ renpy.show('Lisa school-dressed '+r1+suf)
#     #         menu:
#     #             Lisa_09 "Макс, я в школу одеваюсь! И ты прекрасно это знал..."
#     #             "Могла бы и не прикрываться...":
#     #                 #спрайт в блузке и трусиках
#     #                 show Lisa school-dressed 01b
#     #                 if GetRelMax('lisa')[0] < 0:
#     #                     # настроение не очень и ниже отношения и настроение снижаются
#     #                     $ rel  -= 5
#     #                     $ mood -= 25
#     #                     Lisa_12 "А ты бы мог и за дверью подождать немного! Хотя бы для приличия..."
#     #                     #одетая
#     #                     show Lisa school-dressed 01
#     #                     Lisa_00 "Ладно, я уже оделась, входи уж... А я в школу побежала."
#     #                     Max_01 "Удачи!"
#     #                 else:
#     #                     # настроение нейтральное и выше
#     #                     Lisa_02 "Могла бы... Но не буду, пока тут такие любознательные личности, как ты, лазят!"
#     #                     #одетая
#     #                     show Lisa school-dressed 01a
#     #                     Lisa_01 "Ладно, я уже оделась, входи уж... А я в школу побежала."
#     #                     Max_01 "Удачи!"
#     #             "У тебя классная грудь, не стесняйся..." if r1==3:   # Лиза без верха
#     #                 #спрайт в блузке и трусиках
#     #                 show Lisa school-dressed 01b
#     #                 if GetRelMax('lisa')[0] < 1:
#     #                     # отношения прохладные и ниже отношения и настроение снижаются
#     #                     $ rel  -= 5
#     #                     $ mood -= 25
#     #                     Lisa_12 "И что теперь, тебе можно на неё глазеть, когда захочешь?! Нет уж, не угадал!"
#     #                     #одетая
#     #                     show Lisa school-dressed 01
#     #                     Lisa_00 "Так или иначе, я уже оделась и побежала в школу."
#     #                     Max_01 "Удачи!"
#     #                 elif GetRelMax('lisa')[0] < 2:
#     #                     # неплохие отношения
#     #                     Lisa_00 "Ага, красивая... Но это не значит, что из-за этого я должна её тебе показывать!"
#     #                     #одетая
#     #                     show Lisa school-dressed 01
#     #                     Lisa_01 "Ладно, я уже оделась, входи уж... А я в школу побежала."
#     #                     Max_01 "Удачи!"
#     #                 else:
#     #                     # при хорошем (и выше) отношении настроение повышается
#     #                     $ mood += 25
#     #                     Lisa_02 "Спасибо! Но ты и так слишком часто её видишь... Хорошего должно быть понемножку!"
#     #                     Max_03 "Не так часто, как хотелось бы."
#     #                     #одетая
#     #                     show Lisa school-dressed 01a
#     #                     Lisa_01 "Ладно, я уже оделась, входи уж... А я в школу побежала."
#     #                     Max_01 "Удачи!"
#     #             "Подумаешь, твою очаровательную попку без трусиков увижу..." if r1==4:   # Лиза без низа
#     #                 #спрайт в маечке и трусиках
#     #                 $ renpy.show('Lisa school-dressed 02'+suf)
#     #                 if GetRelMax('lisa')[0] < 1:
#     #                     # отношения прохладные и ниже отношения и настроение снижаются
#     #                     $ rel  -= 5
#     #                     $ mood -= 25
#     #                     Lisa_12 "Мог бы и за дверью подождать немного! Хотя бы для приличия..."
#     #                     #спрайт в юбке
#     #                     show Lisa school-dressed 01c
#     #                     Lisa_09 "Прекращай пялиться! Припёрся ни раньше и ни позже..."
#     #                     #одетая
#     #                     show Lisa school-dressed 01
#     #                     Lisa_00 "Можешь входить... А я в школу побежала."
#     #                     Max_01 "Удачи!"
#     #                 elif GetRelMax('lisa')[0] < 2:
#     #                     # неплохие отношения
#     #                     Lisa_00 "Так, на мою попку сильно не глазеть! Я тут переодеваюсь не для того, чтобы тебя порадовать."
#     #                     #спрайт в юбке
#     #                     show Lisa school-dressed 01c
#     #                     Lisa_09 "Отвернись, Макс! Я чувствую, как ты пялишься на меня..."
#     #                     #одетая
#     #                     show Lisa school-dressed 01
#     #                     Lisa_01 "Можешь входить... А я в школу побежала."
#     #                     Max_01 "Удачи!"
#     #                 else:
#     #                     #при хорошем (и выше) отношении настроение повышается
#     #                     $ mood += 25
#     #                     Lisa_02 "А вот и не увидишь! Когда надо, я могу их так быстренько одеть, как тебе и не снилось!"
#     #                     Max_03 "Это правда! В моих снах ты делаешь это очень медленно..."
#     #                     #спрайт в юбке
#     #                     show Lisa school-dressed 01c
#     #                     Lisa_05 "Так же медленно, как и эту юбку?"
#     #                     Max_05 "О да! Примерно так же..."
#     #                     #одетая
#     #                     show Lisa school-dressed 01a
#     #                     Lisa_01 "Так, представим, что я ничего не слышала! Можешь входить... А я в школу побежала."
#     #                     Max_01 "Удачи!"
#     #
#     #     jump .rel_mood
#     #
#     # label .open_door2:
#     #     # Лиза уже снимала майку во время ТВ
#     #     $ spent_time = 20
#     #     $ r1 = renpy.random.randint(3, 5)
#     #     $ suf = 'b' if GetRelMax('lisa')[0]>1 else 'a' if GetRelMax('lisa')[0]>=0 else ''
#     #     $ lisa.dress_inf = {2:'02a', 3:'02c', 4:'02b', 5:'00'}[r1]
#     #     scene BG char Lisa morning
#     #     $ renpy.show('Lisa school-dressed 0'+str(r1)+suf)
#     #
#     #     if r1 < 5:
#     #         # Лиза без верха или без низа
#     #         menu:
#     #             Lisa_12 "Макс! Ты почему без стука входишь? Я не одета..."
#     #             "У тебя классная грудь, не стесняйся..." if r1==3:
#     #                 if GetRelMax('lisa')[0] < 1:
#     #                     # отношения прохладные и ниже отношения и настроение снижаются
#     #                     $ rel  -= 5
#     #                     $ mood -= 25
#     #                     Lisa_12 "И что теперь, тебе можно на неё глазеть, когда захочешь?! Нет уж, не угадал! Выйди быстро, пока маму не позвала!" nointeract
#     #                 elif GetRelMax('lisa')[0] < 2:
#     #                     # неплохие отношения
#     #                     Lisa_00 "Ага, красивая... Но это не значит, что из-за этого я должна её тебе показывать! Выйди, пожалуйста..." nointeract
#     #                 else:
#     #                     # при хорошем (и выше) отношении настроение повышается
#     #                     $ mood += 25
#     #                     Lisa_02 "Спасибо! Но ты и так слишком часто её видишь... Хорошего должно быть понемножку! А теперь выйди, дай переодеться..." nointeract
#     #             "Подумаешь, твою очаровательную попку без трусиков увижу..." if r1==4:
#     #                 if GetRelMax('lisa')[0] < 1:
#     #                     # отношения прохладные и ниже отношения и настроение снижаются
#     #                     $ rel  -= 5
#     #                     $ mood -= 25
#     #                     Lisa_12 "Так, быстро выйди и жди за дверью! Хотя бы для приличия... Или мне маму позвать?" nointeract
#     #                 elif GetRelMax('lisa')[0] < 2:
#     #                     # неплохие отношения
#     #                     Lisa_00 "Так, на мою попку сильно не глазеть! Будь добр, выйди и дверь закрой..." nointeract
#     #                 else:
#     #                     # при хорошем (и выше) отношении настроение повышается
#     #                     $ mood += 25
#     #                     Lisa_02 "А вот и не увидишь! Дай переодеться спокойно, нечего тут всяким любопытным личностям лазить..." nointeract
#     #     else:
#     #         # Лиза голая
#     #         menu:
#     #             Lisa_12 "Макс! Я не одета! Быстро закрой дверь с той стороны!"
#     #             "Извини, я думал, что ты уже оделась. Хотя бы немного...":
#     #                 pass
#     #         if GetRelMax('lisa')[0] < 1:
#     #             # отношения прохладные и ниже отношения и настроение снижаются
#     #             $ rel  -= 5
#     #             $ mood -= 25
#     #             Lisa_12 "И что теперь, можно заходить когда вздумается и без стука?! Нет уж, не угадал! Выйди быстро, пока маму не позвала!" nointeract
#     #         elif GetRelMax('lisa')[0] < 2:
#     #             # неплохие отношения
#     #             Lisa_00 "Не оделась... Но это не значит, что ты можешь вот просто так заходить без стука! Выйди, пожалуйста..." nointeract
#     #         else:
#     #             # при хорошем (и выше) отношении настроение повышается
#     #             $ mood += 25
#     #             Lisa_02 "Ещё нет! Считай, тебе повезло, но дай мне пожалуйста переодеться..." nointeract
#     #     menu:
#     #         "{i}уйти{/i}":
#     #             scene location house myroom door-morning
#     #             jump .rel_mood
#     #
#     # label .open_door:
#     #     # Лиза ещё не снимала майку во время ТВ
#     #     $ spent_time = 20
#     #     $ r1 = renpy.random.randint(2, 5)
#     #     $ suf = 'b' if GetRelMax('lisa')[0]>1 else 'a' if GetRelMax('lisa')[0]>=0 else ''
#     #     $ lisa.dress_inf = {2:'02a', 3:'02c', 4:'02b', 5:'00'}[r1]
#     #     scene BG char Lisa morning
#     #     $ renpy.show('Lisa school-dressed 0'+str(r1)+suf)
#     #
#     #     $ mood -= 50 # настроение портится в любом случае
#     #     if r1 < 3: # Лиза практически одета
#     #         menu:
#     #             Lisa_12 "Макс! Стучаться надо! А вдруг я была бы голая?! \n\n{color=[orange]}{i}{b}Подсказка:{/b} Клавиша [[ h ] или [[ ` ] - вкл/выкл интерфейс.{/i}{/color}"
#     #             "Ну, тогда мне бы повезло":
#     #                 $ rel -= 5
#     #                 Lisa_13 "Ну ты хам! Быстро закрой дверь с той стороны!"
#     #                 Max_00 "Хорошо..."
#     #             "Извини, я забыл...":
#     #                 Lisa_01 "Установил бы замки на двери, не было бы таких проблем. А теперь выйди и подожди за дверью. Пожалуйста."
#     #                 Max_00 "Хорошо..."
#     #                 $ mood += 50
#     #     elif r1 < 5: # Лиза частично одета
#     #         menu:
#     #             Lisa_12 "Макс! Не видишь, я собираюсь в школу! Быстро закрой дверь! \n\n{color=[orange]}{i}{b}Подсказка:{/b} Клавиша [[ h ] или [[ ` ] - вкл/выкл интерфейс.{/i}{/color}"
#     #             "Извини... Кстати, отличный зад!" if r1 < 3:
#     #                 if GetRelMax('lisa')[0] < 2:
#     #                     $ rel -= 5
#     #             "Извини..." if r1 > 2:
#     #                 $ mood += 50
#     #     else: # Лиза полностью голая
#     #         menu:
#     #             Lisa_12 "Макс! Я не одета! Быстро закрой дверь с той стороны! \n\n{color=[orange]}{i}{b}Подсказка:{/b} Клавиша [[ h ] или [[ ` ] - вкл/выкл интерфейс.{/i}{/color}"
#     #             "А у тебя сиськи подросли!":
#     #                 $ rel -= 5
#     #                 menu:
#     #                     Lisa_11 "Что?! Я всё маме расскажу!"
#     #                     "Всё, всё, ухожу!":
#     #                         pass
#     #                     "Уже ухожу, но сиськи - супер!":
#     #                         $ rel -= 5
#     #                         menu:
#     #                             Lisa_12 "..."
#     #                             "{i}Бежать{/i}":
#     #                                 pass
#     #             "Извини, я не хотел...":
#     #                 Lisa_12 "Установил бы замки на двери, не было бы таких проблем. А теперь выйди и подожди за дверью. Пожалуйста."
#     #                 Max_00 "Хорошо..."
#     #                 if GetRelMax('lisa')[0] > 1:
#     #                     $ mood += 50
#     #
#     #     scene location house myroom door-morning
#     #
#     # label .rel_mood:
#     #     $ AddRelMood('lisa', rel, mood)
#
#     label .end:
#         jump Waiting
#
#
# label lisa_dressed_shop:
#     scene location house myroom door-morning
#
#     if lisa.hourly.dressed:
#         return
#
#     $ renpy.dynamic('mood', 'rel', 'warned', 'r1')
#
#     $ mood = 0
#     $ rel = 0
#     $ warned = False
#     $ lisa.hourly.dressed = 1
#     $ spent_time = 10 # 60 - int(tm[-2:])
#     menu .lisa_dressed:
#         Max_09 "Кажется, все собираются на шоппинг и Лиза сейчас переодевается..."
#         "{i}постучаться{/i}":
#             jump .knock
#         "{i}открыть дверь{/i}":
#             jump .open_door
#         "{i}заглянуть в окно{/i}":
#             jump .look_window
#         "{i}уйти{/i}":
#             $ spent_time = 10
#             jump .rel_mood
#
#     menu .knock:
#         Lisa "{b}Лиза:{/b} Кто там? Я переодеваюсь!"
#         "Это я, Макс. Можно войти?":
#             menu:
#                 Lisa "{b}Лиза:{/b} Нет, Макс, нельзя! Я переодеваюсь. Жди там."
#                 "{i}открыть дверь{/i}":
#                     $ warned = True
#                     jump .open_door
#                 "Хорошо...":
#                     jump .rel_mood
#         "Можно войти на секунду? Я только ноутбук возьму..." if flags.warning:
#             jump get_laptop
#         "Хорошо, я подожду...":
#             jump .rel_mood
#
#     label .open_door:
#         $ spent_time = 20
#         $ r1 = renpy.random.randint(3, 5)
#         $ lisa.dress_inf = {3:'02c',4:'02b',5:'00'}[r1]
#         scene BG char Lisa morning
#         if GetRelMax('lisa')[0] < 0:
#             $ renpy.show('Lisa school-dressed 0'+str(r1))
#         elif GetRelMax('lisa')[0] < 2:
#             $ renpy.show('Lisa school-dressed 0'+str(r1)+'a')
#         else:
#             $ renpy.show('Lisa school-dressed 0'+str(r1)+'b')
#
#         if warned:
#             $ mood -= 150
#             $ rel -= 15
#             $ phrase = _("Я же сказала, что я не одета! ")
#         else:
#             $ mood -= 50 # настроение портится в любом случае
#             $ phrase = _("Я не одета! ")
#
#         menu:
#             Lisa_12 "Макс! [phrase!t]Быстро закрой дверь с той стороны!"
#             "Извини... Кстати, отличный зад!" if r1 == 2:
#                 if GetRelMax('lisa')[0] < 2:
#                     $ rel -= 5
#             "А у тебя сиськи подросли!":
#                 menu:
#                     Lisa_11 "Что?! Я всё маме расскажу!"
#                     "Всё, всё, ухожу!":
#                         jump .rel_mood
#                     "Уже ухожу, но сиськи - супер!":
#                         $ mood -= 50
#                         $ rel -= 5
#                         menu:
#                             Lisa_12 "..."
#                             "{i}Бежать{/i}":
#                                 jump .rel_mood
#             "Извини, я не хотел...":
#                 $ mood += 50
#                 $ rel += 5
#                 jump .rel_mood
#
#     label .look_window:
#         $ spent_time = 10
#         $ r1 = renpy.random.choice(['03', '04', '05', '06'])
#         $ lisa.dress_inf ={'03':'02b', '04':'02c', '05':'02i', '06':'02g'}[r1]
#         scene BG char Lisa voyeur-00
#         $ renpy.show('Lisa voyeur '+r1)
#         $ renpy.show('FG voyeur-lisa-00'+mgg.dress)
#         $ Skill('hide', 0.03, 10)
#         menu:
#             Max_01 "Ого, какой вид! Вот это я удачно заглянул!"
#             "{i}уйти{/i}":
#                 jump .rel_mood
#
#     scene location house myroom door-morning
#
#     label .rel_mood:
#         $ AddRelMood('lisa', rel, mood)
#
#     jump Waiting
#
#
# label get_laptop:
#     scene BG char Lisa morning
#     show Lisa school-dressed 02b
#     Lisa_00 "Мог бы и подождать немного. Ты что, без ноутбука и часа прожить не можешь?"
#     Max_00 "Лиза, мне ноутбук нужен для дела."
#     Lisa_00 "Какого дела? Ты дома сидишь целыми днями и ничего не делаешь..."
#     Lisa_00 "Ладно, неважно... Забирай свой ноутбук и уходи. Дай мне уже переодеться..."
#     $ spent_time += 10
#     $ at_comp = True
#     $ current_room = house[5]
#     $ cam_flag.append('notebook_on_terrace')
#     jump Laptop
#


label lisa_dressed:
    scene location house myroom door-morning

    if lisa.hourly.dressed:
        return

    $ lisa.hourly.dressed = 1
    $ renpy.dynamic('mood', 'warned', 'r1', 'pose', 'var', 'np')
    $ warned = False
    $ r1 = random_outcome(50)   # начала ли Лиза переодеваться
    $ mood = 0
    $ lvl = get_lisa_emancipation()
    $ np = False
    $ var = {'bobs':False, 'ass':False, 'np':False, 'fin':False}

    if 6 > GetWeekday(day) > 0:
        # будний день, Лиза собирается в школу
        Max_09 "{m}Сейчас Лиза должна собираться в школу...{/m}" nointeract
    elif GetWeekday(day) == 6:
        # суббота, Лиза собирается на шопинг
        Max_09 "{m}Сейчас Лиза должна переодеваться, чтобы отправиться вместе со всеми по магазинам...{/m}" nointeract
    elif lisa.dcv.battle.stage in [2, 4, 5]:    # Эрик оплатил репетитора
        # воскресенье, репетитор
        Max_09 "{m}Сейчас Лиза обычно переодевается, чтобы отправиться на занятие к репетитору...{/m}" nointeract
    else:
        # воскресенье, прогулка
        Max_09 "{m}Сейчас Лиза обычно переодевается, чтобы пойти погулять. Ну, или что она там ещё делает...{/m}" nointeract

    menu:
        "{i}войти в комнату{/i}":
            if random_outcome(40) and tm[-2:]=='00':
                call .moment0 from _call_lisa_dressed_moment0    # "нулевой"
            elif random_outcome(45):
                call .moment1 from _call_lisa_dressed_moment1    # неповезло
            else:
                call .moment2 from _call_lisa_dressed_moment2    # повезло
            jump .end
        "{i}постучаться{/i}":
            $ warned = True
            menu:
                Lisa "{b}Лиза:{/b} Кто там? Я переодеваюсь!"
                "{i}войти в комнату{/i}":
                    call .moment1 from _call_lisa_dressed_moment1_1
                "Можно войти на секунду? Я только ноутбук возьму...":
                    if r1 or tm > '10:00':
                        menu:
                            Lisa "{b}Лиза:{/b} Макс, дай одеться спокойно! Потом свой ноутбук заберёшь..."
                            "{i}всё равно забрать ноутбук{/i}":
                                call .get_notebook0 from _call_lisa_dressed_get_notebook0
                            "Хорошо, я подожду...":
                                jump .end
                    else:
                        call .get_notebook1 from _call_lisa_dressed_get_notebook1
                "Хорошо, я подожду...":
                    jump .end
        "{i}заглянуть в окно{/i}" if GetWeekday(day):
            # в любой день, кроме воскресенья
            $ spent_time = 10
            if GetWeekday(day) == 6:
                $ r1 = renpy.random.choice(['03', '04', '05', '06'])
                $ lisa.dress_inf ={'03':'02b', '04':'02c', '05':'02i', '06':'02g'}[r1]
            else:
                $ r1 = renpy.random.choice(['01', '02', '03', '04'])
                $ lisa.dress_inf = {'01':'02h', '02':'02e', '03':'02b', '04':'02c'}[r1]

            if all([GetWeekday(day) != 6, mgg.stealth >= 11.0, renpy.random.choice([False, False, True])]):
                scene BG char Lisa voyeur-01
                $ renpy.show('Lisa voyeur alt-'+r1)
                $ renpy.show('FG voyeur-lisa-01'+mgg.dress)
            else:
                scene BG char Lisa voyeur-00
                $ renpy.show('Lisa voyeur '+r1)
                $ renpy.show('FG voyeur-lisa-00'+mgg.dress)

            $ Skill('hide', 0.03, 10)
            menu:
                Max_01 "Ого, какой вид! Вот это я удачно заглянул!"
                "{i}уйти{/i}":
                    $ renpy.block_rollback()
                    $ alt_wait()
                    scene location house myroom door-morning
                    call screen room_navigation
        "{i}уйти{/i}":
            jump .end

    label .get_notebook0:
        scene BG char Lisa dressing-02
        # только ("неповезло")
        $ pose, var = get_lisa_dress_pose(1)
        $ renpy.show('Lisa dressing '+pose)
        if lvl == 1:
            Lisa_11 "Макс! Я не одета!!! Быстро закрой дверь с той стороны и не входи, пока я не переоденусь!"
            Max_09 "Лиза, мне ноутбук нужен для дела!"
            Lisa_13 "Какого дела? Ты дома сидишь целыми днями и ничего не делаешь..."
            Lisa_12 "Ладно, неважно... Забирай свой ноутбук и уходи. Дай мне уже переодеться..." nointeract
        elif lvl == 2:
            Lisa_11 "Макс! Я не одета!!! Выйди и закрой за собой дверь! Мне нужно переодеться!"
            Max_09 "Лиза, мне ноутбук нужен для дела!"
            Lisa_09 "Деловой, куда деваться! Сказал бы хоть, что заходишь..."
            Lisa_10 "Ты не глазей, а ноутбук быстрее забирай и уходи. Дай мне уже переодеться..." nointeract
        else:   # lvl == 3
            Lisa_11 "Макс! Я не одета!!! Выйди, пожалуйста, чтобы я могла переодеться! И дверь за собой закрой!"
            Max_09 "Лиза, мне ноутбук нужен для дела!"
            if var['np']:
                #если на Лизе нет трусиков
                Lisa_09 "Деловой, куда деваться! Сказал бы хоть, что заходишь..."
                Lisa_10 "Ты не глазей, а ноутбук быстрее забирай и уходи. Дай мне уже переодеться..." nointeract
            else:
                #если на Лизе есть трусики
                Lisa_09 "Не раньше тебе и не позже! Бери и уходи. Я хочу спокойно переодеться..." nointeract
        menu:
            "{i}уйти с ноутбуком на веранду{/i}":
                jump .get_laptop

    label .get_notebook1:
        scene BG char Lisa dressing-01
        # только нулевой момент (рано)
        $ pose, var = get_lisa_dress_pose(0)
        $ renpy.show('Lisa dressing '+pose)
        menu:
            Lisa "{b}Лиза:{/b} Ладно, так уж и быть, забирай быстрее..."
            "{i}забрать ноутбук{/i}":
                if lvl == 1:
                    Lisa_01 "Ты что, без ноутбука и часа прожить не можешь? Подождать никак не мог?"
                    Max_07 "Нет, он мне очень срочно нужен для дела!"
                    Lisa_02 "Сомневаюсь, что у тебя там могут быть какие-то сверхважные дела..."
                    Lisa_00 "Ладно, неважно... Дай мне уже переодеться!" nointeract
                elif lvl == 2:
                    Lisa_01 "Вот именно сейчас он тебе обязательно понадобился, да? Подождать никак не мог?"
                    Max_07 "Нет, он мне очень срочно нужен для дела!"
                    Lisa_02 "Макс, если под \"делами\" ты подразумеваешь какие-нибудь детские передачи, то пора бы уже из этого вырасти..."
                    Lisa_00 "Ладно, неважно... Дай мне уже переодеться!" nointeract
                else:   # lvl == 3
                    Lisa_01 "Повезло тебе, что я ещё не начала раздеваться. Или ноутбук - это просто предлог и ты надеялся, что я тут полуголая буду?"
                    Max_02 "Не без этого, но он мне действительно очень нужен для дела!"
                    Lisa_02 "Ага, так я тебе и поверила. Забирай его уже быстрее, деловой..." nointeract
        menu:
            "{i}уйти с ноутбуком на веранду{/i}":
                $ cam_flag.append('lisa_dr0')
                jump .get_laptop

    label .moment0(vr = 0):     # рано (или уже поздно)
        $ lisa.hourly.dressed = 1
        if vr < 0:
            scene BG char Lisa dressing-02
        else:
            scene BG char Lisa dressing-01
        $ pose, var = get_lisa_dress_pose(0)
        $ renpy.show('Lisa dressing '+pose)
        menu:
            Lisa_00 "Ой, Макс! А ты можешь немного погулять? Я переодеться хотела..."
            "А я разве чем-то помешаю?" if lvl == 1:
                menu:
                    Lisa_10 "Ну да... Я стесняюсь это делать при тебе. Ты же наверняка подглядывать будешь!"
                    "Да чего я там не видел...":
                        Lisa_13 "В смысле?! Это когда ты успел меня голой увидеть?" nointeract
                        jump .wait_or_leave
                    "Не буду. Честное слово!":
                        Lisa_09 "Ага! Так я тебе и поверила. Пожалуйста, дай спокойно переодеться. Я же недолго, Макс!" nointeract
                        jump .wait_or_leave
            "Да чего я там не видел..." if lvl == 2:
                Lisa_09 "Откуда я знаю, что ты видел, а что ещё нет? Как бы там ни было, я стесняюсь и хочу переодеться без свидетелей." nointeract
                jump .wait_or_leave
            "А при мне ты этого сделать не можешь?" if lvl == 3:
                Lisa_02 "Вот представь, ну никак не могу! Стесняюсь. А переодеться надо. Так что, можно я спокойно это сделаю? И без свидетелей..." nointeract
                jump .wait_or_leave
            "Хорошо, только ноутбук заберу..." if all([lisa.plan_name == 'dressed', flags.warning]):   # Лиза одевается в школу или в город
                if lvl < 3:
                    Lisa_01 "И сдался он тебе прямо сейчас? Я же не буду одеваться целый час." nointeract
                else:
                    Lisa_01 "Ну забирай, если он тебе так нужен. А так, я недолго буду одеваться, можешь подождать..." nointeract
                $ cam_flag.append('lisa_dr0')
                jump .get_laptop
            "Да легко! Не буду мешать...":
                $ mood += 20
                Lisa_01 "Спасибо, Макс. Я быстренько!" nointeract
                jump .wait_or_leave

    label .moment2:     # повезло

        $ lisa.hourly.dressed = 1
        scene BG char Lisa dressing-01
        $ pose, var = get_lisa_dress_pose(2)
        $ np = var['np']
        $ renpy.show('Lisa dressing '+pose)

        Lisa_11 "Макс! Я не одета!!! {p=3}{nw}"

        $ pose, var = get_lisa_dress_pose(1, pose)
        $ renpy.show('Lisa dressing '+pose)

        if lvl == 1:
            Lisa_14 "Быстро закрой дверь с той стороны и не входи, пока я не переоденусь!" nointeract
            call .lvl_1 from _call_lisa_dressed_lvl_1
        elif lvl == 2:
            Lisa_13 "Выйди и закрой за собой дверь! Мне нужно переодеться!" nointeract
            call .lvl_2 from _call_lisa_dressed_lvl_2
        else:   # lvl == 3
            Lisa_10 "Выйди, пожалуйста, чтобы я могла переодеться! И дверь за собой закрой!" nointeract
            call .lvl_3 from _call_lisa_dressed_lvl_3

    label .moment1:     # неповезло
        $ lisa.hourly.dressed = 1
        scene BG char Lisa dressing-01
        $ pose, var = get_lisa_dress_pose(1)
        $ np = var['np']
        $ renpy.show('Lisa dressing '+pose)
        if lvl == 1:
            Lisa_11 "Макс! Я не одета!!! Быстро закрой дверь с той стороны и не входи, пока я не переоденусь!" nointeract
            call .lvl_1 from _call_lisa_dressed_lvl_1_1
        elif lvl == 2:
            Lisa_11 "Макс! Я не одета!!! Выйди и закрой за собой дверь! Мне нужно переодеться!" nointeract
            call .lvl_2 from _call_lisa_dressed_lvl_2_1
        else:   # lvl == 3
            Lisa_11 "Макс! Я не одета!!! Выйди, пожалуйста, чтобы я могла переодеться! И дверь за собой закрой!" nointeract
            call .lvl_3 from _call_lisa_dressed_lvl_3_1

    label .lvl_1:
        menu:
            "А у тебя сиськи подросли!" if var['boobs']:  # Лиза прикрывает грудь
                $ mood -= 20
                Lisa_12 "Что?! Если не уйдёшь, то я всё маме расскажу!" nointeract
                call .wait_or_leave from _call_lisa_dressed_wait_or_leave
            "Отличный зад, я тебе скажу!" if var['ass']:    # Лиза прикрывает попу
                $ mood -= 20
                Lisa_12 "Что?! Если не уйдёшь, то я всё маме расскажу!" nointeract
                call .wait_or_leave from _call_lisa_dressed_wait_or_leave_1
            "А если я хочу на это посмотреть?" if var['fin']:   # Лиза с верхом и в трусиках
                Lisa_12 "Макс! Я ведь маме на тебя нажалуюсь, если не уйдёшь!" nointeract
                call .wait_or_leave from _call_lisa_dressed_wait_or_leave_2
            "Извини, я не знал... Красиво смотришься!":
                Lisa_13 "Ну и долго ты ещё пялиться на меня будешь?! Выйди и подожди за дверью. Пожалуйста!"
                call .wait_or_leave from _call_lisa_dressed_wait_or_leave_3

    label .lvl_2:
        menu:
            "У тебя красивая грудь, Лиза. Не стесняйся..." if var['boobs']:  # Лиза прикрывает грудь
                Lisa_10 "Не надо меня тут комплиментами одаривать, чтобы подольше поглазеть! Или хочешь, чтобы я маме об этом рассказала?" nointeract
                call .wait_or_leave from _call_lisa_dressed_wait_or_leave_4
            "Какая соблазнительная попка у тебя..." if var['ass']:    # Лиза прикрывает попу
                Lisa_10 "А вот не надо на неё так глазеть! Я ведь и маме всё могу рассказать, если не уйдёшь." nointeract
                call .wait_or_leave from _call_lisa_dressed_wait_or_leave_5
            "А где же волшебное слово?" if var['fin']:   # Лиза с верхом и в трусиках
                Lisa_10 "Ну, Макс! Дай переодеться спокойно... Пожалуйста! Или мне маме пожаловаться?" nointeract
                call .wait_or_leave from _call_lisa_dressed_wait_or_leave_6
            "Извини, я не знал... Красиво смотришься!":
                if lisa.plan_name != 'dressed':
                    $ mood += 20
                Lisa_09 "Ну и долго ты ещё пялиться на меня будешь?! Выйди и подожди. Я недолго..." nointeract
                call .wait_or_leave from _call_lisa_dressed_wait_or_leave_7

    label .lvl_3:
        menu:
            "У тебя красивая грудь, Лиза. Не прячь её..." if var['boobs']:  # Лиза прикрывает грудь
                $ mood += 20
                Lisa_01 "Ты, видимо, только об этом и мечтаешь...  Но нечего глазеть, как я одеваюсь! Лучше займи себя чем-нибудь полезным..."
                Max_02 "Как раз это и делаю..."
                Lisa_09 "Ну, Макс!" nointeract
                call .wait_or_leave from _call_lisa_dressed_wait_or_leave_8
            "Какая соблазнительная попка у тебя..." if var['ass']:    # Лиза прикрывает попу
                $ mood += 20
                Lisa_01 "Думаешь, она у меня такая, чтобы тебя постоянно радовать? А вот и нет! Дай одеться спокойно..."
                Max_02 "Ага, сейчас. Только ещё немного полюбуюсь..."
                Lisa_09 "Ну, Макс!" nointeract
                call .wait_or_leave from _call_lisa_dressed_wait_or_leave_9
            "Эх, не повезло! Я надеялся, что ты будешь раздета..." if var['fin']:   # Лиза с верхом и в трусиках
                Lisa_01 "Ну ничего, Макс, ничего... Я скоро уйду и ты сможешь вдоволь поплакать. Сильно расстроился?"
                Max_02 "Нет. Как представляю, что я тут пропустил - сразу приятно становится."
                Lisa_09 "Ну, Макс!"
                call .wait_or_leave from _call_lisa_dressed_wait_or_leave_10
            "Кто-то у нас тут трусики не успел надеть..." if np:        # Лиза без трусиков
                Lisa_13 "Ты! Ничего! Не видел! Понял? И хватит на меня глазеть с таким довольным лицом... Выйди и подожди за дверью!" nointeract
                call .wait_or_leave from _call_lisa_dressed_wait_or_leave_11
            "Извини, я не знал... Ты такая очаровательная!":
                if lisa.plan_name != 'dressed':
                    $ mood += 30
                Lisa_01 "Спасибо. Но давай ты не будешь пялиться и подождёшь за дверью, я недолго... Хорошо?"
                Max_04 "А может повторим? Мне понравилось..."
                Lisa_02 "Макс, займись чем-нибудь путным." nointeract
                call .wait_or_leave from _call_lisa_dressed_wait_or_leave_12

    label .wait_or_leave:
        menu:
            "{i}подождать за дверью, пока Лиза переоденется{/i}":
                # показывваем дверь, "ожидание", затем входим в комнату
                $ renpy.scene()
                $ renpy.show('location house myroom door-'+get_time_of_day())
                pause(2)

                $ ClothingNps('lisa', lisa.plan_name)
                $ AddRelMood('lisa', 0, mood)

                $ renpy.block_rollback()
                scene BG black with dissolve
                if lisa.plan_name == 'dressed':
                    if weekday in [0, 6]:
                        $ spent_time = 40 - int(tm[-2:])
                    else:
                        $ spent_time = 20 - int(tm[-2:])
                    jump Waiting
                else:
                    jump AfterWaiting

            "{i}уйти{/i}":
                # показываем дверь, для продолжения нужно перейти в другую локацию
                $ renpy.scene()
                $ renpy.show('location house myroom door-'+get_time_of_day())
                $ AvailableActions['talk'].active = False

                $ ClothingNps('lisa', lisa.plan_name)
                $ AddRelMood('lisa', 0, mood)

                $ renpy.block_rollback()
                call screen room_navigation

    label .get_laptop:
        $ spent_time += 10
        $ at_comp = True
        $ current_room = house[5]
        $ cam_flag.append('notebook_on_terrace')
        jump Laptop

    label .end:
        $ AddRelMood('lisa', 0, mood)
        jump Waiting



label lisa_dressed_repetitor:
    scene location house myroom door-morning

    if lisa.hourly.dressed:
        return

    # добавить возможность подглядываать после начала секс.обучения Лизы у АиЭ
    menu:
        Max_09 "Кажется, Лиза куда-то собирается, но дверь закрыта..."
        "{i}уйти{/i}":
            $ lisa.hourly.dressed = 1

    label .end:
        jump Waiting


label lisa_swim:
    scene image 'Lisa swim '+pose3_1+lisa.dress
    $ persone_button1 = 'Lisa swim '+pose3_1+lisa.dress+'b'
    return


label lisa_sun:
    scene image 'BG char Lisa sun-'+pose3_1
    $ renpy.show('Lisa sun '+pose3_1+lisa.dress)
    $ persone_button1 = 'Lisa sun '+pose3_1+lisa.dress+'b'
    return


label lisa_dishes:
    scene BG crockery-evening-00
    $ renpy.show('Lisa crockery-evening 01'+lisa.dress)
    $ persone_button1 = 'Lisa crockery-evening 01'+lisa.dress+'b'
    return


label lisa_dishes_closer:
    scene BG crockery-sink-01
    $ renpy.show('Lisa crockery-closer '+pose3_1+lisa.dress)
    return


label lisa_phone:
    scene BG char Lisa bed-mde-01
    $ renpy.show('Lisa phone-evening ' + pose3_1)
    $ renpy.show('FG Lisa phone-evening ' + pose3_1 + lisa.dress)
    $ persone_button1 = ['Lisa phone-evening ' + pose3_1, 'FG Lisa phone-evening ' + pose3_1 + lisa.dress]
    return


label lisa_phone_closer:
    scene BG char Lisa bed-mde-01
    show Lisa phone-evening 00
    $ renpy.show('FG Lisa phone-evening 00' + lisa.dress)
    return


label lisa_bath:
    scene location house bathroom door-evening
    if lisa.daily.bath:
        return

    $ renpy.dynamic('mood', 'rel', 'r1')
    $ lisa.daily.bath = 1
    $ mood = 0
    $ rel = 0
    menu:
        Max_00 "В это время Лиза обычно плескается в ванне..."
        "{i}постучаться{/i}":
            jump .knock
        "{i}открыть дверь{/i}":
            jump .open
        "{i}заглянуть со двора{/i}" if flags.ladder < 2:
            scene Lisa bath 01
            $ renpy.show('FG voyeur-bath-00'+mgg.dress)
            Max_00 "Кажется, Лиза и правда принимает ванну. Жаль, что из-за матового стекла почти ничего не видно. Но ближе подойти опасно - может заметить..."
            Max_09 "Нужно что-нибудь придумать..."
            $ flags.ladder = 1
            jump .end
        "{i}установить стремянку{/i}" if items['ladder'].have:
            scene BG char Max bathroom-window-evening-00
            $ renpy.show('Max bathroom-window-evening 01'+mgg.dress)
            Max_01 "Надеюсь, что ни у кого не возникнет вопроса, а что же здесь делает стремянка... Как, что? Конечно стоит, мало ли что! А теперь начинается самое интересное..."
            $ flags.ladder = 3
            $ items['ladder'].give()
            jump .ladder
        "{i}воспользоваться стремянкой{/i}" if flags.ladder > 2:
            jump .ladder
        "{i}уйти{/i}":
            jump .end

    label .ladder:
        $ renpy.scene()
        $ renpy.show('Max bathroom-window-evening 02'+mgg.dress)
        Max_04 "Посмотрим, что у нас тут..."
        $ spent_time += 10

        $ r1 = renpy.random.randint(1, 4)

        scene BG bath-00
        $ renpy.show('Lisa bath-window 0'+str(r1))
        show FG bath-00
        $ Skill('hide', 0.03, 10)
        if r1 == 1:
            menu:
                Max_03 "Кажется, Лиза как раз собирается принять ванну... О да, моя младшая сестрёнка хороша... а голенькая, так особенно!"
                "{i}смотреть ещё{/i}":
                    $ spent_time += 10
                    $ renpy.show('Lisa bath-window '+renpy.random.choice(['02', '03', '04']))
                    $ Skill('hide', 0.03, 10)
                    menu:
                        Max_05 "Ох, вот это повезло! Лиза демонстрирует свои прелестные сисечки словно специально! Разумеется, она не знает, что я смотрю, а то крику бы было..."
                        "{i}уйти{/i}":
                            $ spent_time += 10
                            $ lisa.dress_inf = '00a'
                            jump .end
                "{i}уйти{/i}":
                    jump .end
        else:
            menu:
                Max_05 "Ох, вот это повезло! Лиза демонстрирует свои прелестные сисечки словно специально! Разумеется, она не знает, что я смотрю, а то крику бы было..."
                "{i}смотреть ещё{/i}":
                    $ spent_time += 10
                    show Lisa bath-window 05
                    $ Skill('hide', 0.03, 10)
                    menu:
                        Max_07 "Эх! Вот и закончились водные процедуры... Ухх... И с этой обворожительной киской я живу в одной комнате! Красота..."
                        "{i}уйти{/i}":
                            $ spent_time += 10
                            $ lisa.dress_inf = '04a'
                            jump .end
                "{i}уйти{/i}":
                    jump .end

    menu .knock:
        Lisa "{b}Лиза:{/b} Кто там? Я принимаю ванну..."
        "Это я, Макс! Можно войти?":
            menu:
                Lisa "{b}Лиза:{/b} Я же сказала, что в ванне. Закончу, тогда и войдёшь! А пока жди..."
                "Хорошо, я подожду...":
                    jump .end
                "{i}открыть дверь{/i}":
                    jump .open_knock
                "{i}уйти{/i}":
                    jump .end
        "{i}открыть дверь{/i}":
            jump .open_knock
        "{i}уйти{/i}":
            jump .end

    label .open_knock:
        if poss['seduction'].st() < 31:
            $ mood -= 50
            scene BG bath-open-00
            if GetRelMax('lisa')[0] < 0:
                show Lisa bath-open 01
                Lisa_11 "Макс! Я же предупредила, что моюсь! Всё маме расскажу!"
            elif GetRelMax('lisa')[0] < 2:
                $ lisa.dress_inf = '00a'
                show Lisa bath-open 02
                Lisa_11 "Макс! Я же предупредила, что моюсь! Всё маме расскажу!"
            else:
                $ lisa.dress_inf = '00a'
                show Lisa bath-open 03
                Lisa_11 "Макс! Я же предупредила, что моюсь! Хочешь со мной поссориться?"
            Max_00 "Упс! Уже ушёл..."

            jump .end
        else:
            Max_00 "В следующих версиях..."
            jump .end

    label .open:
        if poss['seduction'].st() < 31:
            scene BG bath-open-00
            if GetRelMax('lisa')[0] < 0:
                show Lisa bath-open 01
            elif GetRelMax('lisa')[0] < 2:
                $ lisa.dress_inf = '00a'
                show Lisa bath-open 02
            else:
                $ lisa.dress_inf = '00a'
                show Lisa bath-open 03
            menu:
                Lisa_11 "Макс! А постучаться? Я же голая!"
                "Извини, дверь была открыта и я подумал...":
                    pass
                "А ты симпатичная...":
                    pass
                "И что такого? Сестра стесняется брата?":
                    pass
            Lisa_12 "Макс, выйди немедленно!"
            Max_00 "Хорошо, уже ухожу..."
        else:
            Max_00 "В следующих версиях..."

    label .end:
        $ AddRelMood('lisa', rel, mood)
        $ spent_time = 10
        jump Waiting


label lisa_homework:
    scene BG char Lisa lessons
    $ renpy.show('Lisa lessons '+pose3_1+lisa.dress)
    $ persone_button1 = 'Lisa lessons '+pose3_1+lisa.dress
    return


label lisa_homework_closer:
    scene BG char Lisa lessons
    $ renpy.show('Lisa lessons 00'+lisa.dress)
    return


label lisa_select_movie:
    if lisa.dcv.special.stage < 1:
        # первый просмотр романтического фильма
        jump lisa_romantic_movie_0

    elif lisa.dcv.special.stage < 4:
        # периодический просмотр романтического фильма
        jump lisa_romantic_movie_r

    elif lisa.dcv.special.stage < 5:
        # первый просмотр ужастика
        jump lisa_horor_movie_0

    elif lisa.dcv.special.stage < 8:
        # периодический просмотр ужастика
        jump lisa_horor_movie_r


label lisa_romantic_movie_0:

    scene BG myroom-night-talk-01
    $ renpy.show("Lisa myroom-night-talk 01"+lisa.dress)
    with Fade(0.4, 0, 0.3)
    Lisa_01 "Ну что, Макс, смотрим кино или как?"
    Max_01 "Да, смотрим. Сейчас всё подготовлю..."
    Lisa_02 "А я пока свет выключу."

    scene BG char Lisa horror-myroom 00
    show Max horror-myroom 01a
    $ renpy.show("Lisa horror-myroom 00-01"+lisa.dress)
    Max_04 "Давай, запрыгивай! Ты уже знаешь, что будем смотреть?"
    Lisa_09 "В смысле, \"запрыгивай\"? К тебе на кровать, что ли?"
    Max_07 "Да, ко мне. Или к тебе, если хочешь."
    Lisa_10 "Я думала каждый со своей кровати будет смотреть!"
    Max_09 "Здесь же у нас не такой экран, как в гостиной. Смотреть надо близко."
    Lisa_00 "Ну... ладно. Подвинься тогда."

    scene BG char Lisa horror-myroom 01
    $ renpy.show("Lisa horror-myroom 01-01"+lisa.dress)
    Max_00 "Ну так... каким фильмом ты собиралась меня мучить?"
    Lisa_01 "Точно не знаю. Напиши в поиске \"лучшие романтические фильмы\" и я что-нибудь выберу."
    Max_03 "Вот, смотри... Выбирай... Может вот этот? Постер уж очень интересный!"
    Lisa_02 "Нет, мы будем смотреть то, что интересно мне! Хочу вон тот фильм! Давай, включай..."
    play music romantic
    Max_07 "{m}Да уж, это конечно намного лучше, чем получать при всех от мамы по заднице, но так скучно! Хотя бы с сестрёнкой рядом на одной кровати полежу. А смотреть можно и вполглаза...{/m}"
    Lisa_13"Макс, не спи! Ты должен смотреть - это твоё наказание! Если будешь спать, то я буду тебя пихать..."

    scene BG char Lisa horror-myroom 01a
    $ renpy.show("Lisa horror-myroom 01a-01"+lisa.dress)
    Max_02 "{m}Я бы тоже с огромным удовольствием попихал в тебя чем-нибудь! А если бы она ещё и уснула со мной в обнимку это было бы...{/m}"
    Lisa_10 "Ой-ёй-ёй! У фильма же вроде семейный рейтинг?! Почему они раздеваются?"
    Max_03 "А вот это уже будет поинтереснее смотреть! Хороший момент, мне нравится..."
    Lisa_11 "Давай промотаем! Мне как-то неудобно... Ого! А что это он там делает ей?!"
    Max_05 "Я не против, что персонажей в этой сцене решили... хорошенько раскрыть..."
    Lisa_12 "Чем это ты ноутбук шевелишь? У тебя рука что ли трясётся или..."
    Max_07 "Ну... почти."

    scene BG char Lisa horror-myroom 04
    $ renpy.show("Lisa horror-myroom 04-02"+lisa.dress)
    Lisa_11 "Макс! У тебя встал что ли?"
    Max_08 "Да, немного. Такой уж фильм ты выбрала!"
    Lisa_13 "Немного?! Это не немного! Какой же ты озабоченный!"
    Max_09 "Вообще-то, так все мужчины реагируют на такое!"
    Lisa_12 "Молодец, Макс! Испортил весь просмотр."
    Max_07 "А ты на экран смотри, а не на член."
    Lisa_10 "Да не могу я смотреть на экран, когда и там и у тебя такое... Всё, я спать!"
    stop music fadeout 1.0
    Max_08 "Погоди, но это ведь считается, что я отбыл наказание?"
    Lisa_09 "Да ну тебя!"
    Max_01 "Ладно. Доброй ночи тогда."

    $ lisa.dcv.special.stage = 1
    $ lisa.dcv.special.disable()
    $ poss['SoC'].open(12)
    $ infl[lisa].add_m(12)
    $ spent_time += 60
    $ flags.cur_series = 1
    jump Waiting


label lisa_romantic_movie_r:

    scene BG myroom-night-talk-01
    $ renpy.show("Lisa myroom-night-talk 01"+lisa.dress)
    with Fade(0.4, 0, 0.3)
    Lisa_01 "Ну что, Макс, смотрим кино или как?"
    Max_01 "Да, смотрим. Сейчас всё подготовлю..."
    Lisa_02 "А я пока свет выключу."

    scene BG char Lisa horror-myroom 00
    show Max horror-myroom 01a
    $ renpy.show("Lisa horror-myroom 00-01"+lisa.dress)
    if flags.cur_series < 2:
        Max_04 "Давай, запрыгивай! Будем досматривать тот фильм?"   #если не досмотрели фильм
        Lisa_09 "Да, но промотай тот момент, ну ты понял..."
        play music romantic
        Max_03 "Считай, что уже сделано. Я к отбытию наказания готов!"
        Lisa_02 "И смотри чтобы ничего у тебя там не шевелилось больше!"
    else:
        Max_04 "Давай, запрыгивай! Ты уже знаешь, что будем смотреть?"   #если досмотрели фильм
        Lisa_01 "Нет. Выводи список романтический фильмов и я выберу. Только давай нормальные фильмы, а не как в прошлый раз!"
        play music romantic
        Max_03 "Ты сама выбирала, моё дело маленькое. Вот этот вроде ничего должен быть..."
        Lisa_02 "Ага, давай его. И твоё маленькое дело - это смотреть фильм, мучиться и чтобы у тебя ничего не шевелилось!"

    if renpy.random.randint(1, 2) < 2:
        scene BG char Lisa horror-myroom 01
        $ renpy.show("Lisa horror-myroom 01-01"+lisa.dress)
    else:
        scene BG char Lisa horror-myroom 01a
        $ renpy.show("Lisa horror-myroom 01a-01"+lisa.dress)

    Max_07 "{m}Легко говорить, чтобы ничего не шевелилось! Достаточно просто представить, как Лиза лежит рядом со мной, совсем обнажённая... Ой, лучше не думать!{/m}"
    Lisa_03 "Что, Макс, заскучал? Будешь знать, как за мной подглядывать! И не вздумай спать, а то я начну тебя щипать..."
    Max_02 "Так я и ответить могу тем же, если ты не в курсе!"
    Lisa_13 "Эй! Нет, меня нельзя щипать! Ой, ну вот опять откровенные сцены начались..."
    Max_04 "{m}Вовремя! А то у меня уже слегка привстал, ведь в голову пришло уже столько пошлых мыслей от того, что Лиза лежит так близко ко мне.{/m}"

    scene BG char Lisa horror-myroom 04
    $ renpy.show("Lisa horror-myroom 04-02"+lisa.dress)

    if lisa.flags.kiss_lesson and lisa.dcv.special.stage == 3:
        #как только открываются уроки поцелуев с Лизой и посмотрели 3 раза романтику
        Lisa_10 "Макс, у тебя опять стоит! Ну сколько можно?"
        Max_01 "Фильмы такие! Что тут поделать..."
        Lisa_01 "А я знаю что! Мы будем смотреть что-нибудь такое, на что ты не будешь реагировать так, как сейчас."
        Max_05 "Например? О, давай боевики?! Или комедии? А ещё лучше - комедийные боевики!"
        Lisa_02 "Нет, мы будем смотреть ужастики!"
        Max_09 "Ужастики?! Ты уверена, что смотреть ужастики в тёмное время суток - это то, что нужно?"
        Lisa_03 "Что, Макс, струсил?! Это то, что мне и нужно. Наверняка, ты будешь визжать от страха, как маленькая девочка!"
        Max_16 "Не дождёшься! Считай, что вызов я принял! Ещё увидим, кто будет визжать..."
        Lisa_02 "Да, да... Не удивлюсь, если подглядывания за мной... прекратятся."
        Max_09 "У тебя, кстати, есть своя кровать, помнишь?"
        Lisa_01 "Тогда я пойду спать, а то ты сегодня что-то не в духе."
        stop music fadeout 1.0
        Max_15 "Да, будь так добра..."
        $ poss['SoC'].open(13)
        $ lisa.dcv.special.stage = 4

    elif flags.cur_series > 1:
        # чередующийся вариант окончания просмотра
        Lisa_12 "Ну и ты следом сразу возбудился! Это вообще нормально?"
        Max_07 "Спроси хоть у кого и ответ будет всегда один - да, это нормальная реакция."
        Lisa_10 "Ну и как теперь дальше фильм смотреть, а Макс?"
        Max_02 "Как и до этого смотрела, просто с небольшим бонусом."
        Lisa_09 "Ага! Очень такой \"небольшой\" бонус, аж в трусах не умещается... Всё, я спать!"
        Max_07 "Ничего, если я тут досмотрю этот момент, интересно, как закончится?"
        Lisa_12 "Нет! Выключай всё! А то это уже не наказание получается."
        stop music fadeout 1.0
        Max_01 "Ладно. Тогда спим..."
    else:
        # чередующийся вариант окончания просмотра
        Lisa_10 "Макс, может уже хватит меня смущать?! Почему ты такой озабоченный?"
        Max_02 "Не понимаю о чём ты говоришь, у меня всё нормально."
        Lisa_13 "Ага, развалился тут со своим членом на всю кровать и довольный! А это вообще-то наказание!"
        Max_07 "Ну а что я сделаю, если они там решили поразвлечься?!"
        Lisa_09 "Опять ты весь просмотр испортил! Я пошла спать..."
        Max_04 "Ну давай, а я ещё немного посмотрю..."
        Lisa_10 "Нет уж! Давай выключай! А то лицо у тебя слишком довольное стало."
        Max_03 "И не только лицо..."
        Lisa_09 "Да ну тебя!"
        stop music fadeout 1.0
        Max_01 "Ладно. Доброй ночи тогда."

    if lisa.dcv.special.stage < 3:
        $ lisa.dcv.special.stage += 1

    $ lisa.dcv.special.disable()
    $ infl[lisa].add_m(12)
    $ spent_time += 60
    $ flags.cur_series = {1:2, 2:1}[flags.cur_series]
    jump Waiting


label lisa_horor_movie_0:

    scene BG myroom-night-talk-01
    $ renpy.show("Lisa myroom-night-talk 01"+lisa.dress)
    with Fade(0.4, 0, 0.3)
    Lisa_01 "Ну что, Макс, смотрим кино или как?"
    Max_01 "Да, смотрим. Сейчас всё подготовлю..."
    Lisa_02 "А я пока свет выключу. Тебе уже страшно?"

    scene BG char Lisa horror-myroom 00
    show Max horror-myroom 01a
    show Lisa horror-myroom 00-01b
    Max_07 "Как бы не так! Ты уже знаешь, что будем смотреть?"
    menu:
        Lisa_03 "Я думала посмотреть все части \"Кошмара на улице Вязов\" или \"Пятницы 13-е\". Мне в школе посоветовали. Но выбирать тебе, ты же будешь бояться."
        "{i}смотреть \"Кошмар на улице Вязов\"{/i}":   #после выбора начинает играть соответствующая фильму музыка
            $ flags.cur_movies = ['hes', 1, 0, 0]
            play music hes
        "{i}смотреть \"Пятница 13-е\"{/i}":   #после выбора начинает играть соответствующая фильму музыка
            $ flags.cur_movies = ['f13', 0, 1, 0]
            play music f13
        "{i}смотреть \"Крик\"{/i}":
            $ flags.cur_movies = ['scr', 0, 0, 1]
            play music scream

    scene BG char Lisa horror-myroom 01
    show Lisa horror-myroom 01-01b
    Lisa_02 "Макс, если тебе будет сильно страшно, то так и скажи! В этом нет ничего такого, мы сразу всё выключим."
    Max_03 "Мне нечего бояться, с моей стороны стена, так что никто из под кровати на меня не нападёт. Чего не могу сказать о твоём положении, ты сильно рискуешь!"

    scene BG char Lisa horror-myroom 01a
    show Lisa horror-myroom 01a-01b
    Lisa_00 "Хорошая попытка, но меня этим не напугаешь, наверно... Вот молчал бы и я об этом сейчас не думала бы!"
    Max_02 "Но если тебе всё же начнёт казаться, как что-то тянется из темноты к твоей ноге, то сразу скажи. И мы сразу всё выключим!"

    scene BG char Lisa horror-myroom 03
    show Lisa horror-myroom 03-01b
    Lisa_09 "Не пугай меня, Макс! И так фильм страшный, так ты тут ещё жути нагоняешь!"
    Max_00 "Не бойся, мне тоже страшно!"
    Lisa_10 "Правда? По тебе не скажешь..."
    Max_04 "Есть немного, но трусишка у нас ты... Но мне это нравится, очень мило."

    scene BG char Lisa horror-myroom 02
    show Lisa horror-myroom 02-01b
    $ renpy.show("FG horror-myroom "+flags.cur_movies[0]+" 01-01")
    Lisa_11 "Ой-ёй-ёй... Зря мы это смотрим! Кажется, я теперь от таких ужасов не смогу заснуть..."
    Max_09 "Ну, ты не одна в комнате, так что бояться нечего. Всех монстров я возьму на себя!"
    Lisa_13 "Макс, это что мне в ногу такое твёрдое упёрлось?!"
    Max_07 "Ноутбук, должно быть."

    scene BG char Lisa horror-myroom 04
    $ renpy.show("Lisa horror-myroom 04-02"+lisa.dress)
    Lisa_12 "Ага, ноутбук, как же! Сейчас-то у тебя от чего встал?!"
    Max_08 "Ты ко мне прижалась, вот я и возбудился. Пора бы тебе уже спокойно на это реагировать и не обращать внимание."
    Lisa_09 "Да как тут внимание не обращать, ты же меня своим членом сейчас трогал?!"
    Max_09 "Во-первых, не трогал, а ты просто положила на него свою ногу, а во-вторых, ты же к моей ноге своей киской тоже прижалась... Так что всё честно!"

    scene BG char Lisa horror-myroom 00
    show Max horror-myroom 01a
    show Lisa horror-myroom 00-02b
    Lisa_10 "Ничем таким я к тебе не прижималась! И вообще, я спать пошла... только страшно..."
    stop music fadeout 1.0
    Max_01 "Ладно. И попку давай береги по пути, а то монстры любят хватать за что-нибудь такое!"
    Lisa_11 "Ой ой ой!"

    $ spent_time += 60
    $ lisa.dcv.special.stage = 5
    $ lisa.dcv.special.disable()
    $ poss['SoC'].open(14)
    $ infl[lisa].add_m(12)
    $ flags.cur_series = 1
    jump Waiting


label lisa_horor_movie_r:

    if all([lisa.dcv.other.stage>1, lisa.dcv.other.done, lisa.dcv.shower.done]):
        # Лиза уже снимала майку во время ужастика
        # закончился откат по наказаниям и по подсматриванию в душе
        $ lisa.dress = 'c'

    scene BG myroom-night-talk-01
    $ renpy.show("Lisa myroom-night-talk 01"+lisa.dress)
    with Fade(0.4, 0, 0.3)
    Lisa_01 "Ну что, Макс, смотрим кино или как?"
    if all([lisa.dcv.other.stage==1, lisa.dcv.other.done, lisa.dcv.shower.done]):
        Max_01 "Да, смотрим. Сейчас всё подготовлю... Не стесняйся, снимай маечку."
        Lisa_02 "Сейчас сниму, только свет сначала выключу. Тебе уже страшно?"
        $ lisa.dcv.other.stage = 2
        $ lisa.dress = 'c'

    else:
        Max_01 "Да, смотрим. Сейчас всё подготовлю..."
        Lisa_02 "А я пока свет выключу. Тебе уже страшно?"

    scene BG char Lisa horror-myroom 00
    show Max horror-myroom 01a
    $ renpy.show('Lisa horror-myroom 00-01'+lisa.dress)

    if flags.cur_series < 2:
        #если не досмотрели фильм
        Max_07 "Как бы не так! Будем досматривать тот фильм, который тогда смотрели?"
        menu:
            Lisa_00 "Ой, я даже не знаю... Главное, чтобы и тебе было страшно! И желательно, чтобы больше, чем мне."
            "Тогда досматриваем... (продолжаем смотреть \"Кошмар на улице Вязов\")" if flags.cur_movies[0] == 'hes':   #после выбора начинает играть соответствующая фильму музыка
                $ flags.cur_series = 2
                play music hes
            "Тогда досматриваем... (продолжаем смотреть \"Пятница 13-е\")" if flags.cur_movies[0] == 'f13':   #после выбора начинает играть соответствующая фильму музыка
                $ flags.cur_series = 2
                play music f13
            "Тогда досматриваем... (продолжаем смотреть \"Крик\")" if flags.cur_movies[0] == 'scr':   #после выбора начинает играть соответствующая фильму музыка
                $ flags.cur_series = 2
                play music scream
            "{i}смотреть \"Кошмар на улице Вязов\"{/i}" if flags.cur_movies[0]!='hes':   #после выбора начинает играть соответствующая фильму музыка
                $ flags.cur_movies[0] = 'hes'
                if flags.cur_movies[1] < 5:
                    $ flags.cur_movies[1] += 1
                else:
                    $ flags.cur_movies[1] = 1
                play music hes
            "{i}смотреть \"Пятница 13-е\"{/i}" if flags.cur_movies[0]!='f13':   #после выбора начинает играть соответствующая фильму музыка
                $ flags.cur_movies[0] = 'f13'
                if flags.cur_movies[2] < 5:
                    $ flags.cur_movies[2] += 1
                else:
                    $ flags.cur_movies[2] = 1
                play music f13
            "{i}смотреть \"Крик\"{/i}" if flags.cur_movies[0]!='scr':   #после выбора начинает играть соответствующая фильму музыка
                $ flags.cur_movies[0] = 'scr'
                if flags.cur_movies[3] < 4:
                    $ flags.cur_movies[3] += 1
                else:
                    $ flags.cur_movies[3] = 1
                play music scream
    else:
        #если досмотрели фильм
        Max_07 "Как бы не так! Будем смотреть следующий фильм в той серии, которую начали?"
        $ flags.cur_series = 1
        menu:
            Lisa_00 "Ой, я даже не знаю... Главное, чтобы и тебе было страшно! И желательно, чтобы больше, чем мне."
            "Тогда смотрим дальше... (продолжаем смотреть серию фильмов \"Кошмар на улице Вязов\")"  if flags.cur_movies[0] == 'hes':
                if flags.cur_movies[1] < 5:
                    $ flags.cur_movies[1] += 1
                else:
                    $ flags.cur_movies[1] = 1
                play music hes
            "Тогда смотрим дальше...  (продолжаем смотреть серию фильмов \"Пятница 13-е\")" if flags.cur_movies[0] == 'f13':
                if flags.cur_movies[2] < 5:
                    $ flags.cur_movies[2] += 1
                else:
                    $ flags.cur_movies[2] = 1
                play music f13
            "Тогда смотрим дальше...  (продолжаем смотреть серию фильмов \"Крик\")" if flags.cur_movies[0] == 'scr':
                if flags.cur_movies[3] < 4:
                    $ flags.cur_movies[3] += 1
                else:
                    $ flags.cur_movies[3] = 1
                play music scream
            "{i}смотреть \"Кошмар на улице Вязов\"{/i}" if flags.cur_movies[0]!='hes':   #после выбора начинает играть соответствующая фильму музыка
                $ flags.cur_movies[0] = 'hes'
                if flags.cur_movies[1] < 5:
                    $ flags.cur_movies[1] += 1
                else:
                    $ flags.cur_movies[1] = 1
                play music hes
            "{i}смотреть \"Пятница 13-е\"{/i}" if flags.cur_movies[0]!='f13':   #после выбора начинает играть соответствующая фильму музыка
                $ flags.cur_movies[0] = 'f13'
                if flags.cur_movies[2] < 5:
                    $ flags.cur_movies[2] += 1
                else:
                    $ flags.cur_movies[2] = 1
                play music f13
            "{i}смотреть \"Крик\"{/i}" if flags.cur_movies[0]!='scr':   #после выбора начинает играть соответствующая фильму музыка
                $ flags.cur_movies[0] = 'scr'
                if flags.cur_movies[3] < 4:
                    $ flags.cur_movies[3] += 1
                else:
                    $ flags.cur_movies[3] = 1
                play music f13


    if renpy.random.randint(1, 2) < 2:
        scene BG char Lisa horror-myroom 01
        $ renpy.show("Lisa horror-myroom 01-01"+lisa.dress)
    else:
        scene BG char Lisa horror-myroom 01a
        $ renpy.show("Lisa horror-myroom 01a-01"+lisa.dress)

    Lisa_09 "Может хоть для приличия испугаешься? А то иначе я уже не знаю, как тебя наказать, разве что маме тебя сдать..."
    Max_14 "Я боюсь! Теперь стало намного страшнее после твоих слов."

    scene BG char Lisa horror-myroom 03
    $ renpy.show('Lisa horror-myroom 03-01'+lisa.dress)
    Lisa_10 "Вот и хорошо, а то я не хочу одна бояться. Ну вот что они делают?! Это же точно ничем хорошим не закончится!"
    Max_02 "{m}Хорошо, что в ужастиках куча тупых персонажей, потому что это гарантирует мне крепкие объятия от Лизы! Главное стараться не думать, какими прелестями она ко мне прижимается.{/m}"

    scene BG char Lisa horror-myroom 02
    $ renpy.show('Lisa horror-myroom 02-01'+lisa.dress)
    $ renpy.dynamic('h_film', 'r1')
    $ h_film = {'hes':1, 'f13':2, 'scr':3}[flags.cur_movies[0]]
    $ renpy.show('FG horror-myroom '+flags.cur_movies[0]+' 0'+str(flags.cur_movies[h_film])+"-0"+str(flags.cur_series))
    Lisa_11 "Ой-ёй-ёй... Зря мы это смотрим! Кажется, я теперь от таких ужасов не смогу заснуть..."

    if lisa.dress>'b':
        Max_10 "{m}Только бы у меня не встал! У меня тут полный эффект погружения... Ладно в ужастике сиськи голые периодически мелькают, а вот голая грудь моей сестрёнки, которой она слегка трётся о меня, вот это проблема... Как тут сдерживаться?{/m}" nointeract
    else:
        Max_10 "{m}Только бы у меня не встал! Ещё периодически сиськи голые в ужастике мелькают... Как тут сдерживаться?{/m}" nointeract
    menu:
        "{i}сдерживаться{/i}" ('sex', (mgg.sex + 6) * 3, 90):
            if not rand_result or (_in_replay and lisa.flags.kiss_lesson<12):
                # (не получилось сдержаться)
                Lisa_13 "[norestrain!t]Макс, мне кажется или у меня под ногой сейчас что-то увеличивается?"
                jump .not_restrain

            # (получилось сдержаться)
            if flags.cur_series < 2:
                # начали новый фильм
                Lisa_09 "[restrain!t]Макс, я уже спать хочу. Давай закругляться. Да и набоялась я уже слишком..."
            else:
                # продолжили смотреть
                Lisa_09 "[restrain!t]Наконец-то фильм заканчивается, а то я набоялась уже сполна..."
            #  выключается музыка
            stop music fadeout 1.0
            Max_04 "Ага, я тоже. Было страшно, но я рад, что ты была рядом. Это приятно."

            # horror-myroom-01a + horror-myroom-01a-max&lisa-02
            scene BG char Lisa horror-myroom 01a
            $ renpy.show('Lisa horror-myroom 01a-02'+lisa.dress)
            Lisa_10 "Мне только страшно до своей кровати идти теперь..."
            Max_03 "Так не иди. Спи со мной. Я очень даже не против!"
            menu:
                Lisa_05 "Чтобы со мной рядом кое-что шевелилось? Так я точно не усну. Мне нужно как-то храбрости набраться..."
                "{i}поцеловать Лизу{/i}" if lisa.flags.kiss_lesson > 6:   #если открыты поцелуи с прикосновениями
                    $ added_mem_var('horror_kiss')
                    # horror-myroom-02 + horror-myroom-02-max&lisa-02 или horror-myroom-02a + horror-myroom-02-max&lisa-03
                    $ r1 = '0'+str(renpy.random.randint(2, 3))
                    if r1=='02':
                        scene BG char Lisa horror-myroom 02
                    else:
                        scene BG char Lisa horror-myroom 02a
                    $ renpy.show('Lisa horror-myroom 02-'+r1+lisa.dress)
                    if lisa.dress>'b':
                        Max_05 "{m}Нежный поцелуй с сестрёнкой перед сном точно отвлечёт её от всяких страхов. Целуя её, вообще забываешь о том, что там было перед этим... Лишь её сочные губки и нежная грудь, которой она касается меня...{/m}"
                        $ added_mem_var('horror_topples_kiss')
                        if lisa.dcv.special.stage < 7:
                            $ lisa.dcv.special.stage = 7
                    else:
                        Max_05 "{m}Нежный поцелуй с сестрёнкой перед сном точно отвлечёт её от всяких страхов. Целуя её, вообще забываешь о том, что там было перед этим... Лишь её сочные губки...{/m}"
                        if lisa.dcv.special.stage < 6:
                            $ lisa.dcv.special.stage = 6

                    scene BG char Lisa horror-myroom 01a
                    $ renpy.show("Lisa horror-myroom 01a-01"+lisa.dress)
                    Lisa_02 "Да, так уже совсем не страшно. Я пойду... Спокойной ночи, Макс."
                    Max_01 "Ага. Приятных снов."
                    if not _in_replay:
                        if lisa.dress=='c':
                            $ poss['SoC'].open(17)
                        else:
                            $ poss['SoC'].open(15)

                    jump .end

                "Просто иди и всё..." if not _in_replay:
                    Lisa_13 "Ну ага, просто иди! А вдруг меня что-то схватит?!"
                    Max_07 "У нас в комнате нет никаких монстров! Если конечно не считать того, что у меня в трусах."

                    scene BG char Lisa horror-myroom 04
                    $ renpy.show("Lisa horror-myroom 04-02"+lisa.dress)
                    Lisa_01 "Ой, с тобой и правда страшно спать будет! Я пошла к себе..."
                    Max_01 "Ага. Спокойной ночи."
                    jump .end

        "{i}да пофиг!{/i}" if not (_in_replay and lisa.dcv.other.stage):
            Lisa_13 "Макс, мне кажется или у меня под ногой сейчас что-то увеличивается?"
            jump .not_restrain

    label .not_restrain:
        Max_07 "Однозначно кажется..."

        scene BG char Lisa horror-myroom 04
        $ renpy.show("Lisa horror-myroom 04-02"+lisa.dress)
        stop music fadeout 1.0
        if lisa.dress>'b':
            Lisa_12 "Ага, кажется, как же! Опять ты возбудился... Хотя, ничего удивительного, я была почти уверена, что так и будет."
            Max_09 "Ну встал и встал, подумаешь. Спрячу под ноутбуком."
        else:
            Lisa_12 "Ага, кажется, как же! Опять ты возбудился... Я же твоя сестра, тебе стыдно должно быть!"
            Max_09 "Стыдно?! Ну встал и встал, подумаешь."

        scene BG char Lisa horror-myroom 00
        show Max horror-myroom 01a
        $ renpy.show('Lisa horror-myroom 00-02'+lisa.dress)
        Lisa_10 "Хватит уже похабно думать обо мне! Я ушла спать... Ой! Как страшно..."
        Max_04 "Проводить тебя до кровати?"
        Lisa_13 "Сама справлюсь! Ой ой ой!"
        jump .end

    label .end:
        $ renpy.end_replay()
        $ spent_time += 60
        $ infl[lisa].add_m(12)
        $ lisa.dcv.special.disable()
        if lisa.dress>'b':
            $ lisa.dress = 'b'
        jump Waiting


# label lisa_sudden_dressing(var=0, mood=0):
#     # Макс случайно попадает в момент, когда Лиза переодевается
#     # Лизу можно поймать за переодеванием только в самом начале часа. Только 1 раз в сутки.
#
#     $ renpy.dynamic('lvl', 'lst','dr', 'fb', 'bt', 'np')
#     $ lisa.hourly.dressed = 1
#
#     $ lvl = get_lisa_emancipation()
#
#     if var < 0:
#         scene BG char Lisa dressing-02
#     else:
#         scene BG char Lisa dressing-01
#
#     if var > 0:
#         $ lst = []
#         if lisa.plan_name in ['sun', 'swim']:
#             $ lst.append('s')   # купальник
#         elif lisa.plan_name == 'read' and '19:00' > tm >= '13:00':
#             $ lst.append('s')   # купальник
#         else:
#             if lisa.plan_name == 'dressed':
#                 if 6 > GetWeekday(day) > 0:
#                     $ lst.append('h')   # школьная
#                     $ lst.append('h')
#                 else:
#                     $ lst.append('o')   # для выхода (магазин, репетитор)
#                     $ lst.append('o')
#             elif lisa.plan_name == 'homework':
#                 $ lst.append(lisa.clothes.learn.GetCur().suf)   # для домашки
#                 $ lst.append(lisa.clothes.learn.GetCur().suf)
#             else:
#                 $ lst.append(lisa.clothes.casual.GetCur().suf)  # повседневка
#                 $ lst.append(lisa.clothes.casual.GetCur().suf)
#
#             if lisa.prev_plan in ['shower', 'bath']:
#                 $ lst.append('g')   # трусики с полотенцем на голове
#             else:
#                 $ lst.append('p')   # трусики
#
#         $ dr = renpy.random.choice(lst)                         # трусики или вариант одежды
#         $ bt = renpy.random.randint(0, 1)                       # низ или верх
#         $ fb = 0 if dr == 'b' or (dr == 'h' and not bt) else renpy.random.randint(0, 1)   # передом или задом
#         $ np = 0 if lvl < 3 else renpy.random.randint(0, 1)     # в трусиках или без
#         # $ print(dr, bt, fb, np)
#     else:
#         call lisa_dress_zero_moment from _call_lisa_dress_zero_moment
#
#     if var > 1:
#         # "повезло"
#         # первый момент
#         call lisa_dress_first_second(dr, lvl, 1, fb, bt, np) from _call_lisa_dress_first_second_1
#         Lisa_11 "Макс! Я не одета!!! {p=3}{nw}"
#         # пауза 3-5 секунд
#         # второй момент
#         call lisa_dress_first_second(dr, lvl, 0, fb, bt, np) from _call_lisa_dress_first_second_2
#         if lvl == 1:
#             Lisa_14 "Быстро закрой дверь с той стороны и не входи, пока я не переоденусь!" nointeract
#             jump .lvl_1
#
#         elif lvl == 2:
#             Lisa_13 "Выйди и закрой за собой дверь! Мне нужно переодеться!" nointeract
#             jump .lvl_2
#
#         elif lvl == 3:
#             $ mood = 0
#             Lisa_10 "Выйди, пожалуйста, чтобы я могла переодеться! И дверь за собой закрой!" nointeract
#             jump .lvl_3
#
#     elif var > 0:
#         # "не повезло" (var==2)
#         # второй момент
#         call lisa_dress_first_second(dr, lvl, 0, fb, bt, np) from _call_lisa_dress_first_second_3
#         if lvl == 1:
#             Lisa_11 "Макс! Я не одета!!! Быстро закрой дверь с той стороны и не входи, пока я не переоденусь!" nointeract
#             jump .lvl_1
#         elif lvl == 2:
#             Lisa_11 "Макс! Я не одета!!! Выйди и закрой за собой дверь! Мне нужно переодеться!" nointeract
#             jump .lvl_2
#         elif lvl == 3:
#             Lisa_11 "Макс! Я не одета!!! Выйди, пожалуйста, чтобы я могла переодеться! И дверь за собой закрой!" nointeract
#             jump .lvl_3
#
#     else:
#         # "нулевой" момент
#         Lisa_00 "Ой, Макс! А ты можешь немного погулять? Я переодеться хотела..." nointeract
#         if lvl == 1:
#             menu:
#                 "А я разве чем-то помешаю?":
#                     menu:
#                         Lisa_10 "Ну да... Я стесняюсь это делать при тебе. Ты же наверняка подглядывать будешь!"
#                         "Да чего я там не видел...":
#                             Lisa_13 "В смысле?! Это когда ты успел меня голой увидеть?" nointeract
#                             jump .wait_or_leave
#                         "Не буду. Честное слово!":
#                             Lisa_09 "Ага! Так я тебе и поверила. Пожалуйста, дай спокойно переодеться. Я же недолго, Макс!" nointeract
#                             jump .wait_or_leave
#                 "Хорошо, только ноутбук заберу..." if all([lisa.plan_name == 'dressed', flags.warning]):   # Лиза одевается в школу или в город
#                     Lisa_01 "И сдался он тебе прямо сейчас? Я же не буду одеваться целый час." nointeract
#                     jump .get_laptop
#                 "Да легко! Не буду мешать...":
#                     $ mood += 20
#                     Lisa_01 "Спасибо, Макс. Я быстренько!" nointeract
#                     jump .wait_or_leave
#
#         elif lvl == 2:
#             menu:
#                 "Да чего я там не видел...":
#                     Lisa_09 "Откуда я знаю, что ты видел, а что ещё нет? Как бы там ни было, я стесняюсь и хочу переодеться без свидетелей." nointeract
#                     jump .wait_or_leave
#                 "Хорошо, только ноутбук заберу..." if all([lisa.plan_name == 'dressed', flags.warning]):   # Лиза одевается в школу или в город
#                     Lisa_01 "И сдался он тебе прямо сейчас? Я же не буду одеваться целый час." nointeract
#                     jump .get_laptop
#                 "Да легко! Не буду мешать...":
#                     $ mood += 20
#                     Lisa_01 "Спасибо, Макс. Я быстренько!" nointeract
#                     jump .wait_or_leave
#
#         elif lvl == 3:
#             menu:
#                 "А при мне ты этого сделать не можешь?":
#                     Lisa_02 "Вот представь, ну никак не могу! Стесняюсь. А переодеться надо. Так что, можно я спокойно это сделаю? И без свидетелей..." nointeract
#                     jump .wait_or_leave
#                 "Хорошо, только ноутбук заберу..." if all([lisa.plan_name == 'dressed', flags.warning]):   # Лиза одевается в школу или в город
#                     Lisa_01 "Ну забирай, если он тебе так нужен. А так, я недолго буду одеваться, можешь подождать..." nointeract
#                     jump .get_laptop
#                 "Да легко! Не буду мешать...":
#                     $ mood += 20
#                     Lisa_01 "Спасибо, Макс. Я быстренько!" nointeract
#                     jump .wait_or_leave
#
#     menu .lvl_1:
#         "А у тебя сиськи подросли!" if not fb:  # Лиза стоит передом к Максу
#             $ mood -= 20
#             Lisa_12 "Что?! Если не уйдёшь, то я всё маме расскажу!" nointeract
#             jump .wait_or_leave
#         "Отличный зад, я тебе скажу!" if fb:    # Лиза стоит задом к Максу
#             $ mood -= 20
#             Lisa_12 "Что?! Если не уйдёшь, то я всё маме расскажу!" nointeract
#             jump .wait_or_leave
#         "Извини, я не знал... Красиво смотришься!":
#             Lisa_13 "Ну и долго ты ещё пялиться на меня будешь?! Выйди и подожди за дверью. Пожалуйста!"
#             jump .wait_or_leave
#
#     menu .lvl_2:
#         "У тебя красивая грудь, Лиза. Не стесняйся..." if not fb:   # Лиза стоит передом к Максу
#             Lisa_10 "Не надо меня тут комплиментами одаривать, чтобы подольше поглазеть! Или хочешь, чтобы я маме об этом рассказала?" nointeract
#             jump .wait_or_leave
#         "Какая соблазнительная попка у тебя..." if fb:               # Лиза стоит задом к Максу
#             Lisa_10 "А вот не надо на неё так глазеть! Я ведь и маме всё могу рассказать, если не уйдёшь." nointeract
#             jump .wait_or_leave
#         "Извини, я не знал... Красиво смотришься!":
#             if lisa.plan_name != 'dressed':
#                 $ mood += 20
#             Lisa_09 "Ну и долго ты ещё пялиться на меня будешь?! Выйди и подожди. Я недолго..." nointeract
#             jump .wait_or_leave
#
#     menu .lvl_3:
#         "У тебя красивая грудь, Лиза. Не прячь её..." if not fb:    # Лиза стоит передом к Максу
#             $ mood += 20
#             Lisa_01 "Ты, видимо, только об этом и мечтаешь...  Но нечего глазеть, как я одеваюсь! Лучше займи себя чем-нибудь полезным..."
#             Max_02 "Как раз это и делаю..."
#             Lisa_09 "Ну, Макс!" nointeract
#             jump .wait_or_leave
#         "Какая соблазнительная попка у тебя..." if fb:              # Лиза стоит задом к Максу
#             $ mood += 20
#             Lisa_01 "Думаешь, она у меня такая, чтобы тебя постоянно радовать? А вот и нет! Дай одеться спокойно..."
#             Max_02 "Ага, сейчас. Только ещё немного полюбуюсь..."
#             Lisa_09 "Ну, Макс!" nointeract
#             jump .wait_or_leave
#         "Кто-то у нас тут трусики не успел надеть..." if all([np, var > 1, dr not in ['p', 'g']]):        # Лиза без трусиков
#             Lisa_13 "Ты! Ничего! Не видел! Понял? И хватит на меня глазеть с таким довольным лицом... Выйди и подожди за дверью!" nointeract
#             jump .wait_or_leave
#         "Извини, я не знал... Ты такая очаровательная!":
#             if lisa.plan_name != 'dressed':
#                 $ mood += 30
#             Lisa_01 "Спасибо. Но давай ты не будешь пялиться и подождёшь за дверью, я недолго... Хорошо?"
#             Max_04 "А может повторим? Мне понравилось..."
#             Lisa_02 "Макс, займись чем-нибудь путным." nointeract
#             jump .wait_or_leave
#
#     menu .get_laptop:
#         "{i}уйти с ноутбуком на веранду{/i}":
#             $ AddRelMood('lisa', 0, mood)
#             $ spent_time += 10
#             $ at_comp = True
#             $ current_room = house[5]
#             $ cam_flag.append('notebook_on_terrace')
#             jump Laptop
#
#     label .wait_or_leave:
#         menu:
#             "{i}подождать за дверью, пока Лиза переоденется{/i}":
#                 # показывваем дверь, "ожидание", затем входим в комнату
#                 $ renpy.scene()
#                 $ renpy.show('location house myroom door-'+get_time_of_day())
#                 pause(2)
#
#                 $ ClothingNps('lisa', lisa.plan_name)
#                 $ AddRelMood('lisa', 0, mood)
#
#                 $ renpy.block_rollback()
#                 scene BG black with dissolve
#                 if lisa.plan_name == 'dressed':
#                     $ spent_time = 20 - int(tm[-2:])
#                     jump Waiting
#                 else:
#                     jump AfterWaiting
#
#             "{i}уйти{/i}":
#                 # показываем дверь, для продолжения нужно перейти в другую локацию
#                 $ renpy.scene()
#                 $ renpy.show('location house myroom door-'+get_time_of_day())
#                 $ AvailableActions['talk'].active = False
#
#                 $ ClothingNps('lisa', lisa.plan_name)
#                 $ AddRelMood('lisa', 0, mood)
#
#                 $ renpy.block_rollback()
#                 call screen room_navigation
#
#
# # "нулевой" момент переодеваний Лизы (рано)
# label lisa_dress_zero_moment:
#
#     if lisa.prev_plan in ['shower', 'bath']:                # после душа или после ванной
#         # myroom-wardrobe-mde-01-lisa-dresses-07g
#         show Lisa dressing 00g
#
#     elif lisa.prev_plan == 'in_shop':
#         show Lisa dressing 00o
#
#     elif lisa.prev_plan == 'at_tutor':
#         $ renpy.show('Lisa dressing 00' +lisa.clothes.weekend.GetCur().suf)
#
#     elif lisa.prev_plan in ['in_shcool', 'on_courses']:     # после школы
#         # myroom-wardrobe-mde-01-lisa-dresses-07e
#         show Lisa dressing 00h
#
#     elif lisa.prev_plan in ['sun', 'swim']:                 # после отдыха во дворе
#         if lisa.clothes.swimsuit.GetCur().suf == 'a':
#             show Lisa dressing 00s0
#         else: #if lisa.clothes.swimsuit.GetCur().suf == 'b':
#             show Lisa dressing 00s1
#
#     elif lisa.plan_name in ['dressed', 'read', 'dishes']:   # после чтения, мытья посуды или одевается "на выход" (в школу, магазин или к репетитору)
#         # myroom-wardrobe-mde-01-lisa-dresses-07a
#         # myroom-wardrobe-mde-01-lisa-dresses-07b
#         # myroom-wardrobe-mde-01-lisa-dresses-07d
#         $ renpy.show('Lisa dressing 00'+lisa.clothes.casual.GetCur().suf)
#
#     return
#
# ### показывает этап одевания Лизы
# # dr    - одежда назначения:
# #           's' - купальник
# #           'p' - трусики
# #           'g' - с полотенцем на голове
# #           'h' - школьная
# #           'o' - одежда для выхода
# #           'a' - базовая
# #           'b' - халат
# #           'd' - розовый
# # stage - первый или второй момент
# # fb    - передом (0) или задом (1) стоит Лиза
# # bt    - низ (0) или верх (1)
# # np    - без трусиков
# label lisa_dress_first_second(dr, lvl, stage, fb, bt, np):
#
#     if dr == 's':       # купальник
#         if lvl > 1 and not bt:  # только трусики от бикини
#             if fb:  # Лиза стоит задом
#                 if stage:   # первый момент
#                     show Lisa dressing 04c
#                 else:       # второй момент
#                     show Lisa dressing 06c
#             else:   # Лиза стоит передом
#                 if stage:   # первый момент
#                     show Lisa dressing 01c
#                 else:       # второй момент
#                     show Lisa dressing 03c
#         else:                   # бикини
#             if fb:  # Лиза стоит задом
#                 if stage:   # первый момент
#                     show Lisa dressing 04c1
#                 else:       # второй момент
#                     show Lisa dressing 05c1
#             else:   # Лиза стоит передом
#                 if stage:   # первый момент
#                     show Lisa dressing 01c1
#                 else:       # второй момент
#                     show Lisa dressing 02c1
#     elif dr == 'p':     # трусики
#         if np:  # голая
#             if fb:  # Лиза стоит задом
#                 if stage:   # первый момент
#                     show Lisa dressing 04
#                 else:       # второй момент
#                     show Lisa dressing 06
#             else:   # Лиза стоит передом
#                 if stage:   # первый момент
#                     show Lisa dressing 01
#                 else:       # второй момент
#                     show Lisa dressing 03
#         else:   # в трусиках
#             if fb:  # Лиза стоит задом
#                 if stage:   # первый момент
#                     show Lisa dressing 04h
#                 else:       # второй момент
#                     if lvl < 2: # прикрывает низ
#                         show Lisa dressing 06h
#                     else:       # не прикрывает низ
#                         show Lisa dressing 05h
#             else:   # Лиза стоит передом
#                 if stage:   # первый момент
#                     show Lisa dressing 01h
#                 else:       # второй момент
#                     if lvl < 2: # прикрывает низ
#                         show Lisa dressing 03h
#                     else:       # не прикрывает низ
#                         show Lisa dressing 02h
#     elif dr == 'g':     # трусики с полотенцем на голове
#         if np:  # голая с полотенцем на голове
#             if fb:  # Лиза стоит задом
#                 if stage:   # первый момент
#                     show Lisa dressing 04g
#                 else:       # второй момент
#                     show Lisa dressing 06g
#             else:   # Лиза стоит передом
#                 if stage:   # первый момент
#                     show Lisa dressing 01g
#                 else:       # второй момент
#                     show Lisa dressing 03g
#         else:   # в трусиках с полотенцем на голове
#             if fb:  # Лиза стоит задом
#                 if stage:   # первый момент
#                     show Lisa dressing 04g1
#                 else:       # второй момент
#                     if lvl < 2: # прикрывает низ
#                         show Lisa dressing 06g1
#                     else:       # не прикрывает низ
#                         show Lisa dressing 05g1
#             else:   # Лиза стоит передом
#                 if stage:   # первый момент
#                     show Lisa dressing 01g1
#                 else:       # второй момент
#                     if lvl < 2: # прикрывает низ
#                         show Lisa dressing 03g1
#                     else:       # не прикрывает низ
#                         show Lisa dressing 02g1
#     elif dr == 'h':     # школьная форма
#         if np:  # без трусиков
#             if fb:  # Лиза стоит задом
#                 if bt:  # школьная юбка
#                     if stage:   # первый момент
#                         show Lisa dressing 04e
#                     else:       # второй момент
#                         show Lisa dressing 06e
#                 else:   # школьная рубашка
#                     if stage:   # первый момент
#                         show Lisa dressing 04e2
#                     else:       # второй момент
#                         show Lisa dressing 08e2
#             else:   # Лиза стоит передом
#                 if bt:  # школьная юбка
#                     if stage:   # первый момент
#                         show Lisa dressing 01e
#                     else:       # второй момент
#                         show Lisa dressing 03e
#                 else:   # школьная рубашка
#                     if stage:   # первый момент
#                         show Lisa dressing 01e2
#                     else:       # второй момент
#                         show Lisa dressing 08e2
#         else:   # в трусиках
#             if fb:  # Лиза стоит задом
#                 if bt:  # школьная юбка
#                     if stage:   # первый момент
#                         show Lisa dressing 04e1
#                     else:       # второй момент
#                         if lvl < 2:     # прикрывая низ
#                             show Lisa dressing 06e
#                         else:           # не прикрывая низ
#                             show Lisa dressing 05e1
#                 else:   # школьная рубашка
#                     if stage:   # первый момент
#                         show Lisa dressing 04e3
#                     else:       # второй момент
#                         if lvl < 2:     # прикрывая низ
#                             show Lisa dressing 08e3
#                         else:           # не прикрывая низ
#                             show Lisa dressing 07e3
#             else:   # Лиза стоит передом
#                 if bt:  # школьная юбка и трусики
#                     if stage:   # первый момент
#                         show Lisa dressing 01e1
#                     else:       # второй момент
#                         if lvl < 2:     # прикрывая низ
#                             show Lisa dressing 03e
#                         else:           # не прикрывая низ
#                             show Lisa dressing 02e1
#                 else:   # школьная рубашка и трусики
#                     if stage:   # первый момент
#                         show Lisa dressing 01e3
#                     else:       # второй момент
#                         if lvl < 2:     # прикрывая низ
#                             show Lisa dressing 08e3
#                         else:           # не прикрывая низ
#                             show Lisa dressing 07e3
#     elif dr == 'o':     # одежда "для выхода"
#         if fb:  # Лиза стоит задом
#             if bt:  # одеты штаны
#                 if stage:   # первый момент
#                     show Lisa dressing 04a
#                 else:       # второй момент
#                     show Lisa dressing 05a
#             else:   # топ и трусики
#                 if stage:   # первый момент
#                     show Lisa dressing 04f1
#                 else:       # второй момент
#                     show Lisa dressing 08f1
#         else:   # Лиза стоит передом
#             if bt:  # одеты штаны
#                 if stage:   # первый момент
#                     show Lisa dressing 01a
#                 else:       # второй момент
#                     show Lisa dressing 02a
#             else:   # топ и трусики
#                 if stage:   # первый момент
#                     show Lisa dressing 01f1
#                 else:       # второй момент
#                     show Lisa dressing 08f1
#     elif dr == 'a':     # базовая
#         if fb:  # Лиза стоит задом
#             if stage:   # первый момент
#                 show Lisa dressing 04a
#             else:       # второй момент
#                 show Lisa dressing 05a
#         else:   # Лиза стоит передом
#             if stage:   # первый момент
#                 show Lisa dressing 01a
#             else:       # второй момент
#                 show Lisa dressing 02a
#     elif dr == 'b':     # халат
#         if np:  # халат без трусиков
#             if stage:   # первый момент
#                 show Lisa dressing 01b
#             else:       # второй момент
#                 show Lisa dressing 03b
#         else:   # халат и трусики
#             if stage:   # первый момент
#                 show Lisa dressing 01b1
#             else:       # второй момент
#                 if lvl < 2:     # прикрывая низ
#                     show Lisa dressing 03b1
#                 else:           # не прикрывая низ
#                     show Lisa dressing 02b1
#     elif dr == 'd':     # розовые топ и юбка
#         if np:  # без трусиков
#             if fb:  # Лиза стоит задом
#                 if stage:   # первый момент
#                     show Lisa dressing 01d
#                 else:       # второй момент
#                     show Lisa dressing 03d
#             else:   # Лиза стоит передом
#                 if stage:   # первый момент
#                     show Lisa dressing 04d
#                 else:       # второй момент
#                     show Lisa dressing 06d
#         else:   # с трусиками
#             if fb:  # Лиза стоит задом
#                 if bt:  # юбка без топа
#                     if stage:   # первый момент
#                         show Lisa dressing 04d1
#                     else:       # второй момент
#                         if lvl < 2:     # прикрывая низ
#                             show Lisa dressing 06d
#                         else:           # не прикрывая низ
#                             show Lisa dressing 05d1
#                 else:   # юбка и топ
#                     if stage:   # первый момент
#                         show Lisa dressing 04d2
#                     else:       # второй момент
#                         show Lisa dressing 05d2
#             else:   # Лиза стоит передом
#                 if bt:  # юбка без топа
#                     if stage:   # первый момент
#                         show Lisa dressing 01d1
#                     else:       # второй момент
#                         if lvl < 2:     # прикрывая низ
#                             show Lisa dressing 03d
#                         else:           # не прикрывая низ
#                             show Lisa dressing 02d1
#                 else:   # юбка и топ
#                     if stage:   # первый момент
#                         show Lisa dressing 01d2
#                     else:       # второй момент
#                         show Lisa dressing 02d2
#     return
#

label lisa_repeats_homework:
    scene BG char Lisa lessons
    $ renpy.show('Lisa lessons '+pose3_1+lisa.dress)
    $ persone_button1 = 'Lisa lessons '+pose3_1+lisa.dress
    return


label lisa_repeats_homework_closer:
    scene BG char Lisa lessons
    $ renpy.show('Lisa lessons 00'+lisa.dress)
    return
