
label StartPunishment:
    $ pun_list.clear()
    $ first = True
    $ defend = False
    if tm > '18:00':
        # на извинительные подарки у Макса времени до ужина
        if lisa.sorry.owe and lisa.sorry.left == 0: # если Макс обещал Лизе подарок, но не вручил его вовремя
            $ lisa.sorry.owe = False
            $ punreason[0] = 1
            $ poss['SoC'].open(1)
            $ lisa.dcv.shower.stage = 1
            $ lisa.dcv.shower.set_lost(3)
        elif all([flags.film_punish, lisa.dcv.special.enabled, lisa.dcv.special.done]):
            $ punreason[0] = 1

        if alice.sorry.owe and alice.sorry.left == 0: # если Макс обещал Алисе подарок, но не вручил его вовремя
            $ alice.sorry.owe = False
            $ punreason[1] = 1
            $ poss['risk'].open(1)
            $ alice.dcv.shower.stage = 1
            $ alice.dcv.shower.set_lost(3)
        elif all([flags.mistres_pun, alice.dcv.mistress.enabled, alice.dcv.mistress.done]):
            $ punreason[1] = 1

    # Макс теоретически может получить наказание как утром, так и вечером
    if punreason[2] or punreason[3] and tm < "18:00":
        # утром наказание за подглядывание за Анной или Анной с Эриком
        $ pun_list.append("mgg")
    elif punreason[1] and alice.dcv.shower.stage>1 and tm < "18:00":
        # наказание за подсматривание за Алисой в душе во время отката
        $ pun_list.append("mgg")
    elif punreason[0] and lisa.dcv.shower.stage>1 and tm < "18:00":
        # наказание за подсматривание за Лизой в душе во время отката
        $ pun_list.append("mgg")

    elif max(punreason) and tm > "18:00":
        $ pun_list.append("mgg")

    if tm > "18:00" and 0 < weekday < 6:
        # Лиза получает наказание только вечером по будним дням
        if random_outcome(GetLisaPunChance()):  # получит ли Лиза двойку
            $ punlisa[0][1] = 1
            $ pun_list.append("lisa")
        else:
            # если начато противостояние с Эриком за Лизу, то есть шанс
            # наказания Лизы за плохое поведение в школе.
            # шанс всегда 50%, если прошел откат
            if all([
                    any([newpunishment==2,
                         newpunishment==1 and (day >= 50 or (dcv.new_pun.stage==2 and dcv.new_pun.done))]),
                    flags.add_training,
                    lisa.dcv.punpause.done,
                    random_outcome(50)
                ]):
                    $ punlisa[0][1] = 2
                    $ pun_list.append("lisa")
            elif all([
                      newpunishment==2,
                      flags.add_training,
                      lisa.dcv.punpause.done,
                      weekday in [1,2],
                      random_outcome(80),
                      lisa.flags.topless,
                      not lisa.dcv.other.enabled
                    ]):
                    $ punlisa[0][1] = 2
                    $ pun_list.append("lisa")

    if all([
            tm > "18:00",
            alice.dcv.special.enabled,
            alice.dcv.special.stage > 1,
            (not alice.flags.privpunish or 0 < weekday < 6)
            ]):
        # Алиса получает наказание вечером (в будни, если были приватные наказания), если открыт ивент с сигаретами
        if random_outcome(GetAlicePunChance()):  # найдет ли Анна сигареты Алисы
            $ pun_list.append("alice")

    $ renpy.random.shuffle(pun_list) # перемешаем список последовательности наказания

    if len(pun_list):
        $ renpy.block_rollback()
        if tm < "14:00":
            scene BG punish-morning 00
            $ renpy.show("Ann punish-morning 00"+ann.dress)
            with fade4
        else:
            scene BG punish-evening 00
            $ renpy.show("Ann punish-evening 00"+ann.dress)
            with fade4

        if newpunishment == 0 and flags.dinner>=12:
            jump first_new_punishment

        if newpunishment == 1 and (day >= 50 or (dcv.new_pun.stage==2 and dcv.new_pun.done)):
            jump first_naked_punishment

        Ann_16 "Прежде, чем мы начнём, кое-кто заслуживает наказания и сейчас все на это посмотрят..."
        jump punishment
    elif tm > "14:00":
        stop music
        $ music_starter()
        jump dinner_after_punishment
    else:
        stop music
        $ music_starter()
        jump breakfast_after_punishment


label punishment:
    $ _i = 0
    play music punishment
    while len(pun_list) > _i:
        if pun_list[_i] == "mgg":
            if len(pun_list) > 1:  # за эвент будут наказаны больше одного персонажа
                if first: # Макс наказывается первым
                    $ first = False
                    Ann_18 "Итак, Макс, ты первый..."
                else: # Макса наказывают не первым
                    Ann_18 "Макс, теперь твоя очередь..."
            else:  # Макс единственный наказуемый
                Ann_18 "Макс, иди сюда..."
            call punishment_max from _call_punishment_max
        elif pun_list[_i] == "lisa":
            if len(pun_list) > 1:  # за эвент будут наказаны больше одного персонажа
                if first: # Лиза наказывается первой
                    $ first = False
                    Ann_18 "Так, Лиза, начнём с тебя..."
                else: # Лизу наказывают не первой
                    Ann_18 "Теперь Лиза..."
            else:  # наказывают только Лизу
                Ann_18 "Лиза, подойди-ка ко мне."
            call punishment_lisa from _call_punishment_lisa
        elif pun_list[_i] == "alice":
            if len(pun_list) > 1:  # за эвент будут наказаны больше одного персонажа
                if first: # Алиса наказывается первой
                    $ first = False
                    Ann_18 "Алиса, начнём с тебя..."
                else: # Алису наказывают не первой
                    Ann_18 "Теперь ты, Алиса..."
            else:  # наказывают только Алису
                Ann_18 "Алиса, подойди-ка сюда."
            call punishment_alice from _call_punishment_alice
        $ _i += 1

    stop music fadeout 1.0
    if tm > "14:00":
        stop music
        $ music_starter()
        jump dinner_after_punishment
    else:
        stop music
        $ music_starter()
        jump breakfast_after_punishment


label first_new_punishment:
    Ann_12 "Да, напоминаю всем. С сегодняшнего дня все наказания будут в обнажённом виде. Да, я понимаю, что это непедагогично, но очень эффективно."
    Max_10 "Но мам..."
    Ann_16 "Я знаю, Макс, но уговаривать и пытаться вас убедить другим способом у меня нет ни сил ни времени. Чем более унизительно наказание, тем у вас будет меньше желания нарушить правила."
    Lisa_09 "Мам, и что, нам с Алисой придётся раздеваться догола прямо перед Максом? А если он разденется, нам смотреть на этот... его... ну..."
    Max_07 "Что, страшно?"
    Ann_00 "Да, Лиза. Видишь, ты уже боишься. Значит, приложишь все усилия, чтобы тебя не наказали. Уже правила работают, а стоит один раз вам быть униженными перед всей семьёй..."
    Max_09 "А если ты накосячишь? Кто тебя будет наказывать?"
    Ann_02 "Макс, ну что за ерунда. Что я могу нарушить? Я же ваша мама и всегда даю вам пример для подражания..."
    Max_08 "Э... Ты уверена?"
    Ann_04 "Да, Макс, я уверена. Но даже если я и совершу ошибку, то меня сможет наказать, допустим, Эрик... Но этого не случится. Я соблюдаю свои же правила!"
    Max_09 "Ага, уж он то накажет..."
    Ann_12 "Макс, ты слишком много говоришь... Ладно, дам вам последнюю поблажку - в ближайший месяц можете оставаться в трусах во время наказания. Но если и это никак вас не образумит, то всё, будете раздеваться догола. И больше никаких предупреждений. Теперь всё будет строго."
    $ dcv.new_pun.stage = 2
    $ dcv.new_pun.set_lost(30)
    $ newpunishment = 1
    jump punishment


label first_naked_punishment:
    Ann_12 "А так как месяц прошёл, а вы всё так же не взялись за ум, то с этого момента наказывать я вас буду полностью голых! Как и обещала..."
    Lisa_11 "Ой, нет! Не надо, мам!"
    Alice_16 "Это беспредел какой-то!"
    Ann_19 "Тихо! У вас был шанс этого избежать. Если вам не стыдно за свою безалаберность, то, надеюсь, станет стыдно получать по голому заду на глазах у всех!"
    $ newpunishment = 2
    jump punishment


label punishment_max:
    $ renpy.block_rollback()

    if tm < "14:00":
        scene BG punish-morning 01
        $ renpy.show("Ann punish-morning 01"+ann.dress)
        $ renpy.show("Max punish-morning 01"+mgg.dress)
    else:
        scene BG punish-evening 01
        $ renpy.show("Ann punish-evening 01"+ann.dress)
        $ renpy.show("Max punish-evening 01"+mgg.dress)

    if warning < 2 and newpunishment == 0:
        $ warning += 1
        Ann_19 "Макс! Я вынуждена отчитать тебя перед всеми, так как у нас в семье не должно быть никаких секретов."
        if warning > 0:
            Max_10 "Я снова не виноват!"
            Ann_17 "Не виноват, значит? Снова? Кажется, ты не осознаёшь, что это последнее предупреждение и в следующий раз я тебя выпорю на глазах у сестёр. Ты меня понял? А теперь рассказывай, что натворил, чтобы все были в курсе!" nointeract
        else:
            Max_10 "Я не виноват!"
            Ann_17 "Не виноват, значит? А я думаю, что ещё как виноват. В этот раз тебе повезло, это всего лишь первое предупреждение. Надеюсь, второго не потребуется... Кстати, можешь всем рассказать, что ты натворил..." nointeract
        menu .pun_reson:
            "Ну, я случайно оказался рядом с душем, когда там была Лиза..." if punreason[0]:
                Lisa_12 "Он видел меня голой, мам! Накажи его! Почему он отделывается только предупреждением? Пусть получит, что заслужил!"
                $ punreason[0] = 0
                Max_11 "Да ничего я не заслужил!"

            "Ну, я оказался случайно рядом с душем, где мылась Алиса..." if punreason[1]:
                Alice_16 "Случайно? Врёт он всё, мам! Он стоял и пялился на меня!"
                $ punreason[1] = 0
                Max_11 "Да, я мимо проходил!"

            "Ну, я подглядывал за тобой, мам..." if punreason[2]:
                Ann_14 "Очень хочу надеяться, что это было случайно. Тем не менее, ты пойман и как я уже сказала, получаешь предупреждение."
                $ punreason[2] = 0
                Max_10 "Больше это не повторится!"

            "Ну, я подглядывал за вами с Эриком..." if punreason[3]:
                Ann_14 "Очень хочу надеяться, что ты это сделал не специально и просто проходил мимо. Тем не менее, ты пойман и как я уже сказала, получаешь предупреждение."
                $ punreason[3] = 0
                Max_10 "Да, я мимо проходил!"

            "Ну, я плохо себя вёл..." if punreason[4]:
                Ann_14 "У тебя есть ещё время подумать над своим поведением. Надеюсь, следующего раза не будет!"
                $ punreason[4] = 0
                Max_10 "Да, мам..."

            "Ну, я оказался случайно рядом с душем, где мылась Алиса..." if punreason[5]:
                Alice_16 "Случайно? Мам! Он всё врёт! Он подглядывал и, может быть, даже паука подбросил! А ты знаешь, как я боюсь пауков..."
                $ punreason[5] = 0
                Max_09 "Трусиха!"

        if max(punreason):
            $ _r1 = renpy.random.randint(1, 3)
            if _r1 == 1:
                Ann_18 "Ты не закончил, Макс. Продолжай..." nointeract
            elif _r1 == 2:
                Ann_18 "Дальше, Макс, мы тебя внимательно слушаем..." nointeract
            else:
                Ann_18 "А ты про кое-что ещё не забыл?" nointeract
            jump .pun_reson
        Ann_16 "У тебя есть ещё время подумать над своим поведением. Надеюсь, следующего раза не будет!"
        Max_14 "Да, мам..."
        Ann_12 "В общем, на этот раз вопрос уладили. Все сделали выводы, а кое-кто и серьёзно задумается. Да, Макс? Можешь не отвечать."
    elif newpunishment == 0:  # стандартное наказание без штанов, но в трусах и майке
        menu:
            Ann_16 "Макс! Сейчас ты будешь наказан, сам знаешь за что!"
            "Я же не виноват!" ('soc', mgg.social * 2, 90):
                pass
        if rand_result:
            Ann_14 "[succes!t]Ты знаешь, Макс, всё говорит о том, что ты виноват и должен быть наказан. Но поверю тебе на слово, что это была какая-то ошибка. Надеюсь, я не пожалею о своём решении..."
            Max_08 "Спасибо, мам!"
            python:
                for d in range(len(punreason)):
                    punreason[d] = 0
            $ alice.daily.shower = 0
            $ lisa.daily.shower = 0
            return
        else:
            if mgg.dress == "a":
                $ _text = _("штаны")
            else:
                $ _text = _("шорты")
            menu:
                Ann_19 "[failed!t]Вот так просто? \"Я не виноват\" и всё забудем? Нет, Макс, со мной эти шуточки не прокатят. Давай, снимай [_text!t] и ложись на мои колени. Надеюсь, ты сегодня в трусах..."
                "{i}снять штаны{/i}":
                    pass
        if tm < "14:00":
            $ renpy.show("Max punish-morning 02"+mgg.dress)
        else:
            $ renpy.show("Max punish-evening 02"+mgg.dress)

        Ann_18 "Ну и долго я буду ждать?! Давай ложись..."

        if tm < "14:00":
            scene BG punish-morning 02
            $ renpy.show("Ann punish-morning max-01"+ann.dress+mgg.dress)
        else:
            scene BG punish-evening 02
            $ renpy.show("Ann punish-evening max-01"+ann.dress+mgg.dress)

        # Макс без штанов у Анны на коленях
        play sound [slap1, "<silence .5>", slap1, "<silence .5>", slap1, "<silence 1.5>"] loop

        if punreason.count(1) > 1:  # несколько причин для наказания, общая фраза
            Ann_16 "У Макса несколько провинностей... Он их прекрасно знает и перечислять я их не стану. Сейчас он получит за все сразу!"
        else:  # конкретная причина для наказания
            $ _text = {
                0 : _("Если вы не в курсе, Макс будет наказан за то, что подглядывал за Лизой. Я уже предупреждала, что не люблю, когда кто-то нарушает личное пространство..."),
                1 : _("Если вы не в курсе, Макс будет наказан за то, что подглядывал за Алисой. Я уже предупреждала, что не люблю, когда кто-то нарушает личное пространство..."),
                2 : _("Если вы не в курсе, Макс будет наказан за то, что подглядывал за мной. Я уже предупреждала, что не люблю, когда кто-то нарушает личное пространство..."),
                3 : _("Если вы не в курсе, Макс будет наказан за то, что подглядывал за мной... с Эриком. Я уже предупреждала, что такое недопустимо!"),
                4 : _("Если вы не в курсе, Макс будет наказан за своё отвратительное поведение. Надеюсь, теперь ты будешь хорошенько думать о том, что делаешь и что говоришь!"),
                5 : _("Если вы не в курсе, Макс будет наказан за то, что подглядывал за Алисой в душе и, возможно, даже подбросил туда паука. Ты знаешь, что такое я не потерплю!"),
                }[punreason.index(1)]
            Ann_16 "[_text!t]"
        ### сцена наказания
        if tm < "14:00":
            $ renpy.show("Ann punish-morning max-02"+ann.dress+mgg.dress)
        else:
            $ renpy.show("Ann punish-evening max-02"+ann.dress+mgg.dress)

        Max_14 "[impact_reduced!t]{m}Мама наказывает меня прямо перед сёстрами... Это так унизительно...{/m}"

        call max_consequences from _call_max_consequences

        if punreason[1] and alice.dcv.shower.stage>1:
            $ poss['risk'].open(5)
        if punreason[0] and lisa.dcv.shower.stage>1:
            $ poss['SoC'].open(5)

        stop sound

        if tm < "14:00":
            scene BG punish-morning 01
            $ renpy.show("Ann punish-morning 01"+ann.dress)
            $ renpy.show("Max punish-morning 03"+mgg.dress)
        else:
            scene BG punish-evening 01
            $ renpy.show("Ann punish-evening 01"+ann.dress)
            $ renpy.show("Max punish-evening 03"+mgg.dress)

        Ann_12 "Ну вот. Теперь все всё поняли? Ведите себя хорошо и вас не ждёт эта участь..."
    elif newpunishment in [1, 2]:  # второй и третий вариант наказания
        # убедить Аню в своей невиновности уже нельзя (теперь всё строго)
        if newpunishment == 1:
            if mgg.dress=='b':  # шорты и майка
                menu:
                    Ann_12 "Ну, Макс, раздевайся до трусов. Остальные просто посмотрят, что бывает, когда кто-то косячит..."
                    "{i}раздеться{/i}":
                        pass
            else: # только шорты
                menu:
                    Ann_12 "Ну, Макс, снимай шорты. Остальные просто посмотрят, что бывает, когда кто-то косячит..."
                    "{i}снять шорты{/i}":
                        pass
        else:
            menu:
                Ann_12 "Ну, Макс, раздевайся. Остальные просто посмотрят, что бывает, когда кто-то косячит..."
                "{i}раздеться{/i}":
                    pass
        if tm < "14:00":
            $ renpy.show("Max punish-morning 02"+('c' if newpunishment == 1 else 'ca'))
        else:
            $ renpy.show("Max punish-evening 02"+('c' if newpunishment == 1 else 'ca'))
        Ann_14 "Хорошо. А теперь, ложись на мои колени и приступим, а то все голодные сидят..."
        if tm < "14:00":
            scene BG punish-morning 02
            $ renpy.show("Ann punish-morning max-01"+ann.dress+('c' if newpunishment == 1 else 'ca'))
        else:
            scene BG punish-evening 02
            $ renpy.show("Ann punish-evening max-01"+ann.dress+('c' if newpunishment == 1 else 'ca'))
        # Макс без штанов у Анны на коленях
        play sound [slap1, "<silence .5>", slap1, "<silence .5>", slap1, "<silence 1.5>"] loop

        if punreason.count(1) > 1:  # несколько причин для наказания, общая фраза
            Ann_16 "У Макса несколько провинностей... Он их прекрасно знает и перечислять я их не стану. Сейчас он получит за все сразу!"
        else:  # конкретная причина для наказания
            $ _text = {
                0 : _("Если вы не в курсе, Макс будет наказан за то, что подглядывал за Лизой. Я уже предупреждала, что не люблю, когда кто-то нарушает личное пространство..."),
                1 : _("Если вы не в курсе, Макс будет наказан за то, что подглядывал за Алисой. Я уже предупреждала, что не люблю, когда кто-то нарушает личное пространство..."),
                2 : _("Если вы не в курсе, Макс будет наказан за то, что подглядывал за мной. Я уже предупреждала, что не люблю, когда кто-то нарушает личное пространство..."),
                3 : _("Если вы не в курсе, Макс будет наказан за то, что подглядывал за мной... с Эриком. Я уже предупреждала, что такое недопустимо!"),
                4 : _("Если вы не в курсе, Макс будет наказан за своё отвратительное поведение. Надеюсь, теперь ты будешь хорошенько думать о том, что делаешь и что говоришь!"),
                5 : _("Если вы не в курсе, Макс будет наказан за то, что подглядывал за Алисой в душе и, возможно, даже подбросил туда паука. Ты знаешь, что такое я не потерплю!"),
                }[punreason.index(1)]
            Ann_16 "[_text!t]"
        ### сцена наказания
        if tm < "14:00":
            $ renpy.show("Ann punish-morning max-02"+ann.dress+('c' if newpunishment == 1 else 'ca'))
        else:
            $ renpy.show("Ann punish-evening max-02"+ann.dress+('c' if newpunishment == 1 else 'ca'))
        Max_14 "[impact_reduced!t]{m}Блин... Все с таким интересом смотрят, как меня наказывают...  Это так унизительно...{/m}"

        call max_consequences from _call_max_consequences_1

        if punreason[1] and alice.dcv.shower.stage>1:
            $ poss['risk'].open(5)
        if punreason[0] and lisa.dcv.shower.stage>1:
            $ poss['SoC'].open(5)

        stop sound

        if tm < "14:00":
            scene BG punish-morning 01
            $ renpy.show("Ann punish-morning 01"+ann.dress)
            $ renpy.show("Max punish-morning 03"+('c' if newpunishment == 1 else 'ca'))
        else:
            scene BG punish-evening 01
            $ renpy.show("Ann punish-evening 01"+ann.dress)
            $ renpy.show("Max punish-evening 03"+('c' if newpunishment == 1 else 'ca'))

        $ SetCamsGrow(house[5], 150)

        Ann_12 "Ну всё, Макс, одевайся. Надеюсь, ты сделал выводы и постараешься больше не попадать в такую унизительную ситуацию..."

    if newpunishment==2:
        $ mgg.flags.nakedpunish = True

    $ alice.daily.shower = 0
    $ lisa.daily.shower = 0
    return


label max_consequences:
    ## здесь снижение влияния Макса для присутствующих персонажей
    python:
        if all([flags.voy_stage==0, punreason[3], GetRelMax('eric')[0]>0]):
            flags.voy_stage=1 # если Макс попался на подглядывании за трахом Ани и Эрика, на пути дружбы с ним
            poss['control'].open(0)

        for cr in current_room.cur_char:
            if chars[cr] not in infl:
                continue
            # if chars[cr].infmax is not None:
            #     chars[cr].infmax = clip(chars[cr].infmax - 5.0, 0.0, 100.0)
            if infl[chars[cr]].m[0]:
                infl[chars[cr]].sub_m(5)

        # обнуление провинностей
        for d in range(len(punreason)):
            punreason[d] = 0

        if flags.film_punish:
            # Макса наказали, поэтому фильм с Лизой смотреть уже не нужно
            lisa.dcv.special.enabled = False

        alice.dcv.mistress.disable()

        mgg.flags.pun +=1

    return


label punishment_lisa:
    $ renpy.block_rollback()
    $ renpy.dynamic('mood')

    scene BG punish-evening 01
    $ renpy.show("Lisa punish-evening 01"+lisa.dress)
    $ renpy.show("Ann punish-evening 01"+ann.dress)

    $ mood = 0

    $ lisa.dcv.punpause.set_lost(renpy.random.randint(3, 8))
    $ lisa.weekly.punished += 1
    if newpunishment==0:
        # Лиза стоит в одежде, Макс может вмешаться и прервать наказание (если получится)
        if lisa.dress == "a":  # Лиза в обычной одежде
            $ _text = _("Ближе подходи, Лиза. И да, снимай штаны, ты заслужила!")
        else: # Лиза в халате
            $ _text = _("Ближе подходи, Лиза. И да, снимай свой халат, ты заслужила!")
        if defend or poss['sg'].st() == 4:  # Макс уже не может заступиться или нужно наказание для продвижения на "хорошем" пути Школьницы
            Ann_16 "[_text!t]"
        else:
            menu:
                Ann_16 "[_text!t]"
                "{i}Заступиться за Лизу{/i}" ('soc', mgg.social * 2, 90):
                    $ defend = True
                    Max_08 "Мам, не нужно наказывать Лизу. Она правда старалась, я сам видел. Ну и я помогу ей подтянуть оценки."
                    if "mgg" in pun_list:
                        Ann_12 "Нет, Макс, и даже не пытайся меня уговорить. Ты и сам накосячил... А ты, Лиза, не стой столбом, шевелись давай..."
                    elif rand_result:  # Удалось уговорить Анну
                        Ann_00 "[succes!t]Хорошо, Макс, в этот раз я не стану её наказывать. Надеюсь, я не пожалею о своём решении... А ты, Лиза, благодари брата, да учись давай, а то в следующий раз не помилую..."
                        Lisa_02 "Спасибо тебе, Макс!"
                        $ lisa.flags.defend += 1
                        $ lisa.weekly.protected += 1
                        $ punlisa[0][2] = 2
                        return
                    else:
                        Ann_12 "[failed!t]Нет, Макс, твои уговоры ей не помогут. Получит то, что заслужила. А ты, Лиза, не стой столбом, шевелись давай..."
                        $ punlisa[0][2] = 1
                "{i}далее{/i}":
                    pass
        Lisa_10 "Мам... Я не специально... Просто, задание было сложное..."
        if lisa.dress == "a":  # Лиза в обычной одежде
            $ _text = _("Быстро снимай штаны!")
        else: # Лиза в халате
            $ _text = _("Быстро снимай халат!")
        Ann_14 "Сложное? У тебя была куча времени, чтобы подготовиться! Сидишь в своём телефоне вечно вместо того, чтобы учиться. [_text!t]"

    elif newpunishment==1:
        Ann_12 "Лиза. Мне нужно всем объяснять за что ты сейчас будешь наказана? Молчишь? Значит, знаешь... Всё, давай раздевайся до трусов и быстро, без разговоров!"
    elif newpunishment==2:
        if punlisa[0][1] == 2:
            Ann_12 "Лиза. Твой классный руководитель говорит, ты плохо себя ведёшь в школе! Молчишь? Значит, это правда... Всё, давай раздевайся догола и быстро, без разговоров!"
        else:
            Ann_12 "Лиза. Мне нужно всем объяснять за что ты сейчас будешь наказана? Молчишь? Значит, знаешь... Всё, давай раздевайся и быстро, без разговоров!"

    # Лиза стоит частично/полностью раздетая, если Макс не вмешивался, то может попробовать прервать наказание
    $ _lisa_dress = 'b' if newpunishment==1 else 'ca' if newpunishment==2 else lisa.dress
    $ renpy.show("Lisa punish-evening 02"+_lisa_dress)
    if newpunishment==0:
        $ _text = _("Теперь ложись, и побыстрее, все есть хотят...")
        $ SetCamsGrow(house[5], 130)
    else:
        $_text = _("Что прикрываешься, Лиза? Стесняешься? Стыдно? Вот и хорошо... А теперь ложись на мои колени. Быстро!")
        $ SetCamsGrow(house[5], 150)

    if defend or poss['sg'].st() == 4:  # Макс уже не может заступиться или нужно наказание для продвижения на "хорошем" пути Школьницы
        Ann_18 "[_text!t]"
    else:
        menu:  # У Макса есть шанс заступиться за Лизу
            Ann_18 "[_text!t]"
            "{i}Заступиться за Лизу{/i}" ('soc', mgg.social * 2, 90):
                $ defend = True
                if punlisa[0][1] == 2:
                    Max_08 "Мам, не нужно наказывать Лизу. Обещаю, что бы там ни было, я поработаю с ней над поведением, честно. Вот увидишь, проблем больше не будет!"
                else:
                    Max_08 "Мам, не нужно наказывать Лизу. Она правда старалась, я сам видел. Ну и я помогу ей подтянуть оценки."
                if "mgg" in pun_list:
                    Ann_12 "Нет, Макс, и даже не пытайся меня уговорить. Ты и сам накосячил... А ты, Лиза, не стой столбом, шевелись давай..."
                elif flags.eric_wallet == 2:
                    Ann_12 "Нет, Макс! И скажи спасибо, что я не наказываю и тебя вместе с ней... А ты, Лиза, не стой столбом, шевелись давай..."
                elif rand_result:  # Удалось уговорить Анну
                    Ann_00 "[succes!t]Хорошо, Макс, в этот раз я не стану её наказывать. Надеюсь, я не пожалею о своём решении... А ты, Лиза, можешь одеваться. Скажи спасибо Максу, что сегодня осталась безнаказанной. Но не думай, что я всегда буду такой доброй..."
                    Lisa_02 "Спасибо тебе, Макс!"
                    if newpunishment==2:
                        $ lisa.flags.defend += 1

                        if lisa.flags.defend >= 5:
                            if all([poss['SoC'].used(15), lisa.flags.topless, not lisa.dcv.other.enabled, not lisa.dcv.other.stage]):
                                Max_07 "{m}На одних \"спасибо\" далеко не уедешь... Нужно придумать и для себя что-то хорошее. Думаю, Лизу удастся уговорить смотреть ужастики без маечки. Это точно лучше, чем получать по голой заднице от мамы у всех на глазах! И поговорить с ней лучше, пока моя доброта свежа в её памяти...{/m}"
                                $ poss['SoC'].open(16)
                                $ lisa.dcv.other.set_lost(1)
                            elif lisa.dcv.other.enabled:
                                $ lisa.dcv.other.set_lost(1)

                    $ lisa.weekly.protected += 1
                    $ punlisa[0][2] = 2
                    return
                else:
                    Ann_12 "[failed!t]Нет, Макс, твои уговоры ей не помогут. Получит то, что заслужила. А ты, Лиза, не стой столбом, шевелись давай..."
                    $ punlisa[0][2] = 1
            "{i}далее{/i}":
                pass

    # сцена наказания Лизы
    scene BG punish-evening 02
    $ renpy.show("Ann punish-evening lisa-01"+ann.dress+_lisa_dress)

    play sound [slap1, "<silence .5>", slap1, "<silence .5>", slap1, "<silence 1.5>"] loop

    $ mood -= 100 # если Лизу наказывают, её настроение портится
    $ lisa.flags.pun += 1

    if newpunishment==1:
        $ SetCamsGrow(house[5], 200)
        Max_04 "{m}А вот это мне уже нравится... Сестрёнка сверкает своими классными сиськами... Можно смотреть и ничего за это не будет! Красота!{/m}"
    elif newpunishment==2:
        $ SetCamsGrow(house[5], 250)
        Max_04 "{m}Хоть Лиза и получает сейчас по своей миленькой попке, но зато можно полюбоваться и всем остальным... А видно много чего интересного!{/m}"
    else:
        $ SetCamsGrow(house[5], 150)
        Lisa_09 "Ма-ам, я больше не буду... Ай... В смысле, буду лучше учиться. Извини..."
    $ renpy.show("Ann punish-evening lisa-02"+ann.dress+_lisa_dress)

    if newpunishment==0:
        $ _text = _("Говоришь тебе, говоришь, все как об стенку горох...") # вставка, если Макс не помогал за последнюю неделю

        # посмотрим, помогал ли Макс за последние 5 дней
        python:
            for i in range(min(5, len(punlisa))):
                if punlisa[i][0] == 1 or punlisa[i][0] > 2:
                    _text = _("Поразительно! Тебе даже Макс помогает, а ты двойки хватаешь!") # вставка, если Макс помогал
                    break

        Ann_00 "Конечно, будешь. [_text!t] Совсем расслабилась."
    else:
        Lisa_10 "Ой... Мам! Больно!"
        if punlisa[0][1] == 2:
            Ann_16 "Давай терпи! Плохо вела себя в школе - получила по голой заднице у всех на глазах."
        else:
            Ann_16 "Давай терпи! Получила двойку - получила по голой заднице у всех на глазах."

    $ punlisa[0][3] = 1  # Лиза понесла наказание
    if punlisa[0][0] == 1:  # Макс умышленно сделал ошибку и Лизу наказали
        $ punlisa[0][4] = renpy.random.randint(50, 300)  # подозрительность Лизы растет случайно от 5 до 30%

    stop sound
    # сцена с наказанной Лизой
    scene BG punish-evening 01
    $ renpy.show("Lisa punish-evening 03"+_lisa_dress)
    $ renpy.show("Ann punish-evening 01"+ann.dress)
    if newpunishment==0:
        Ann_12 "Лиза, надеюсь, ты извлекла урок из этого наказания и больше это не повторится. А теперь одевайся!"
    else:
        Ann_12 "Лиза, надеюсь, ты извлекла урок из этого наказания. Да, тебе было стыдно и неприятно, что все пялились на тебя, но надеюсь, ты всё поняла и больше это не повторится. А теперь одевайся!"

    if newpunishment==2:
        $ lisa.flags.nakedpunish = True

    $ AddRelMood('lisa', 0, mood)
    return


label punishment_alice:
    $ renpy.block_rollback()
    $ renpy.dynamic('mood', 'suf')

    scene BG punish-evening 01
    $ renpy.show("Alice punish-evening 01"+alice.dress)
    $ renpy.show("Ann punish-evening 01"+ann.dress)

    $ mood = 0
    $ alice.dcv.special.set_lost(3) # Анна забрала сигареты, поэтому Алиса пока не сможет курить
    $ alice.dcv.punpause.set_lost(renpy.random.randint(5, 14))

    $ alice.nopants = (alice.dress=="a" and alice.req.result=='nopants') or alice.dress=='b'
    $ alice.weekly.punished += 1
    if newpunishment==0:
        # Алиса стоит в одежде, Макс может вмешаться и прервать наказание (если получится)
        if alice.dress == "a":  # Алиса в обычной одежде
            Ann_16 "Подходи, подходи, Алиса, чего ты там мнешься. Штаны снимай, есть разговор!"
        else: # Алиса в пижамке
            Ann_16 "Подходи, подходи, Алиса, чего ты там мнешься. Снимай шорты, есть разговор!"
        Alice_12 "Мам, за что? Что я такого сделала?"
        if alice.dress == "a":  # Алиса в обычной одежде
            $ _text = _("Алиса, ты издеваешься? Я нашла сигареты у тебя в комнате! Ты опять куришь! Быстро сняла штаны и легла на мои колени, кому сказала!")
        else:
            $ _text = _("Алиса, ты издеваешься? Я нашла сигареты у тебя в комнате! Ты опять куришь! Быстро сняла шорты и легла на мои колени, кому сказала!")
        if defend:  # Макс уже не может заступиться
            Ann_18 "[_text!t]"
        else:
            menu:
                Ann_18 "[_text!t]"
                "{i}Заступиться за Алису{/i}" ('soc', mgg.social * 2, 90):
                    $ defend = True
                    $ alice.flags.defend += 1
                    Max_08 "Мам, не нужно наказывать Алису. Это не её сигареты, к ней сегодня подружка приходила, наверное, она забыла."
                    if "mgg" in pun_list:
                        Ann_12 "Нет, Макс, даже не пытайся её оправдывать. Ты и сам накосячил... Алиса, пошевеливайся..."
                    elif rand_result:  # Удалось уговорить Анну
                        Ann_14 "[succes!t]Хорошо, Макс, сегодня я не стану её наказывать. Надеюсь, я не пожалею об этом... Скажи брату спасибо, Алиса, что заступился, и не приглашай больше сюда таких подружек, хорошему они не научат..."
                        Alice_13 "Хорошо, мам. Спасибо, Макс, я этого не забуду."
                        $ punalice[0][2] = 2
                        $ alice.weekly.protected += 1
                        return
                    else:
                        Ann_16 "[failed!t]Нет, Макс, твои уговоры ей не помогут. Получит в любом случае, не за себя, так за подружку. Не будет водится с такими, до добра они не доведут..."
                        $ punalice[0][2] = 1
                "{i}далее{/i}":
                    pass

        Alice_13 "Мам... Это не мои сигареты... Я не курю, честно..."
        if alice.dress == "a":  # Алиса в обычной одежде
            Ann_14 "Не твои? А чьи они тогда? Быстро снимай штаны!"
            if alice.nopants:
                Alice_06 "Мам, но я сегодня без трусиков... Пусть Макс уйдёт или отвернётся, хотя бы..."
                Ann_20 "Ты ещё и без трусов?! Сейчас ещё и за это получишь! Макс пусть смотрит, а тебе будет стыдно. Может тогда за ум возьмёшься!"
                show Alice punish-evening 02aa
            else:
                show Alice punish-evening 02a
                if alice.req.result == 'not_nopants':
                    $ alice.req.noted = True
                    $ added_mem_var('alice_not_nopants')
                    Max_09 "{m}Ничего себе! А что это на Алисе делают трусики?! Мы же с ней договорились... Ну всё, сестрёнка, считай ты попала... и куда больше, чем есть сейчас!{/m}"
        else: # Алиса в пижамке
            Ann_14 "Не твои? А чьи они тогда? Быстро шорты снимай!"
            Alice_06 "Мам, но под ними нет трусиков... Пусть Макс уйдёт или отвернётся, хотя бы..."
            Ann_00 "А вот нечего целый день в пижаме по дому шарахаться... Совсем разленилась! Макс пусть смотрит, а тебе будет стыдно. Может тогда за ум возьмёшься!"
            show Alice punish-evening 02ba
    elif newpunishment==1:
        Ann_12 "Так, Алиса, раздевайся до трусов. Надеюсь, не надо объяснять, за что я тебя сейчас буду наказывать и сама всё понимаешь..."
        if alice.dress == "a" and alice.nopants:  # Алиса в джинсах и без трусиков
            Alice_06 "Мам, но я сегодня без трусиков... Пусть Макс уйдёт или отвернётся, хотя бы..."
        elif alice.dress == "b":  # Алиса в пижамке
            Alice_06 "Мам, но под шортами нет трусиков... Пусть Макс уйдёт или отвернётся, хотя бы..."
        if (alice.dress == "a" and alice.nopants) or alice.dress == "b":  # если Алиса в пижамке или без трусиков
            Ann_16 "Тогда раздевайся догола, так наказание даже эффективней будет. А Макс пусть смотрит, как и все остальные..."
            show Alice punish-evening 02ca
            $ SetCamsGrow(house[5], 200)
        elif alice.dress == "a":
            show Alice punish-evening 02c
        else:
            show Alice punish-evening 02d
    elif newpunishment==2:
        Ann_12 "Так, Алиса, раздевайся. Надеюсь, не надо объяснять, за что я тебя сейчас буду наказывать и сама всё понимаешь..."
        show Alice punish-evening 02ca

    if newpunishment==0:
        $ SetCamsGrow(house[5], 130)
        $ _text = _("Теперь ложись побыстрее, ужин стынет...")
    else:
        $ SetCamsGrow(house[5], 150 if newpunishment==1 else 250)
        $ _text = _("Ну как, Алиса, стыдно тебе? Молчишь? Вот подумай о своём поступке, пока я буду наказывать тебя на глазах у всех... Ложись на мои колени!")

    if defend or 0 < alice.dcv.private.stage < 4:  # Макс уже заступался
        if alice.dcv.private.stage==1:
            # первый раз поговорили с Алисой о приватном наказании
            Max_07 "{m}Посмотрим, станет ли Алиса посговорчивей, если я перестану вмешиваться... Главное, успеть поговорить с ней, пока ей будет ещё больно сидеть!{/m}"
            $ alice.dcv.private.stage = 2
            $ alice.dcv.private.set_lost((2 if weekday!=5 else 3))
        elif 1 < alice.dcv.private.stage < 4:
            $ alice.dcv.private.set_lost(2)
        Ann_18 "[_text!t]"
    else:
        menu:  # У Макса есть шанс заступиться за Алису
            Ann_18 "[_text!t]"
            "{i}Заступиться за Алису{/i}" ('soc', mgg.social * 2, 90):
                    $ defend = True
                    $ alice.flags.defend += 1
                    Max_08 "Мам, не нужно наказывать Алису. Это не её сигареты, к ней сегодня подружка приходила, наверное, она забыла."
                    if "mgg" in pun_list:
                        Ann_12 "Нет, Макс, даже не пытайся её оправдывать. Ты и сам накосячил... Алиса, пошевеливайся..."
                    elif flags.eric_wallet == 2:
                        Ann_12 "Нет, Макс! И скажи спасибо, что я не наказываю и тебя вместе с ней... Алиса, пошевеливайся..."
                    elif rand_result:  # Удалось уговорить Анну
                        Ann_14 "[succes!t]Хорошо, Макс, сегодня я не стану её наказывать. Надеюсь, я не пожалею об этом... Можешь одеваться, Алиса, да скажи брату спасибо, что заступился. И не приглашай сюда больше таких подружек, хорошему они не научат..."
                        Alice_13 "Хорошо, мам. Спасибо, Макс, я этого не забуду."

                        if all([alice.flags.nakedpunish, alice.flags.defend >= 5, alice.dcv.intrusion.stage in [5, 7]]):
                            # Алису наказывали голой + Макс подарил кружевное боди + получилось защитить Алису от наказания (минимум 5 раз, включая этот)
                            if not alice.dcv.private.enabled:
                                Max_09 "{m}Ага, как же, не забудет она... Хм... Может, стоит попросить у неё что-нибудь, чтобы она не думала, что моя доброта безвозмездна?! И сделать это нужно сегодня, пока она ещё под впечатлением...{/m}"
                                $ poss['ass'].open(0)
                            $ alice.dcv.private.set_lost((2 if weekday!=5 else 4))

                        $ punalice[0][2] = 2
                        $ alice.weekly.protected += 1
                        return
                    else:
                        Ann_16 "[failed!t]Нет, Макс, твои уговоры ей не помогут. Получит в любом случае, не за себя, так за подружку. Не будет водится с такими, до добра они не доведут..."
                        $ punalice[0][2] = 1
            "{i}далее{/i}":
                pass

    $ poss['smoke'].open(3)

    # сцена наказания Алисы
    scene BG punish-evening 02
    if newpunishment==0:
        $ SetCamsGrow(house[5], 150)
        $ suf = alice.dress + ('a' if alice.req.result == "nopants" or alice.dress=='b' else '')
        $ renpy.show("Ann punish-evening alice-01"+ann.dress+suf)
    else:
        if alice.req.result == "nopants" or alice.dress=='b' or newpunishment==2:  # править условие
            $ SetCamsGrow(house[5], 250)
            $ suf = 'ba'
        else:
            $ SetCamsGrow(house[5], 220)
            $ suf = alice.dress
        $ renpy.show('Ann punish-evening alice-03'+ann.dress+suf)
    play sound [slap1, "<silence .5>", slap1, "<silence .5>", slap1, "<silence 1.5>"] loop

    $ mood -= 50 # если Алису наказывают, её настроение портится
    $ alice.flags.pun += 1

    if newpunishment==0:
        Alice_15 "Ай, больно же! Мам, я больше не буду!!!"
        $ renpy.show("Ann punish-evening alice-02"+ann.dress+suf)
    else:
        if newpunishment==1:
            Max_04 "{m}Вот в такие моменты я не жалею, что нас наказывают практически голыми на глазах друг у друга! Даже порно не надо, когда такое шоу в паре метров от меня!{/m}"
        else:
            Max_04 "{m}Люблю, когда Алису наказывают... Стервозинка она та ещё, но без последствий полюбоваться её голыми прелестями в других ситуациях опасно для жизни!{/m}"
        $ renpy.show('Ann punish-evening alice-04'+ann.dress+suf)

    if newpunishment==0:
        Ann_17 "Я знаю, что не будешь. Заслужила наказание, терпи!"
    else:
        Alice_15 "Ай! Ма-ам! Больно же! Мам, я больше не буду!!!"
        Ann_16 "Давай не мамкай тут! Я знаю, что не будешь. Заслужила наказание, терпи!"

    $ punalice[0][3] = 1  # Алиса понесла наказание
    if  punalice[0][0] > 0 and punalice[0][1] == 1:  # Макс шантажировал Алису и подставил её в этот же день
        $ punalice[0][4] = renpy.random.randint(50, 300)  # подозрительность Алисы растет случайно от 5 до 30%

    stop sound
    # сцена с наказанной Алисой
    scene BG punish-evening 01
    $ renpy.show("Ann punish-evening 01"+ann.dress)
    if newpunishment==0:
        $ suf = alice.dress+('a' if alice.req.result == 'nopants' or alice.dress=='b' else '')
    else:
        $ suf = 'ca' if alice.req.result == 'nopants' or alice.dress=='b' or newpunishment == 2 else 'c' if alice.dress<'d' else 'd'

    $ renpy.show('Alice punish-evening 03'+suf)
    if newpunishment==0:
        if alice.dress == "a":
            Ann_12 "Так, всё, надевай свои джинсы. Надеюсь, ты осознала свои поступки и следующего раза не будет..."
        else:
            Ann_12 "Так, всё, надевай свои шорты. Надеюсь, ты осознала свои поступки и следующего раза не будет..."
    else:
        Ann_12 "Ну что, получила урок? Стыдно? Правильно. Должно быть стыдно. Надеюсь, это больше не повторится. А теперь, одевайся..."

    if newpunishment==2:
        $ alice.flags.nakedpunish = True

    $ AddRelMood('alice', 0, mood)
    return
