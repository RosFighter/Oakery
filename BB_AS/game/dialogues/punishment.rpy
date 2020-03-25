
label StartPunishment:
    $ pun_list.clear()
    $ first = True
    $ defend = False
    # Макс теоретически может получить наказание как утром, так и вечером
    if punreason[2] or punreason[3] and tm < "18:00":  # утром наказание за подглядывание за Анной или Анной с Эриком
        $ pun_list.append("mgg")
    elif max(punreason) and tm > "18:00":
        $ pun_list.append("mgg")

    if tm > "18:00" and 0 < GetWeekday(day) < 6:
        # Лиза получает наказание только вечером по будним дням
        $ chance = GetLisaPunChance()  # шанс получения Лизой двойки
        if RandomChance(chance):  # получит ли Лиза двойку
            $ punlisa[0][1] = 1
            $ pun_list.append("lisa")
    if tm > "18:00" and 'smoke' in dcv and dcv['smoke'].stage > 1:
        $ chance = GetAlicePunChance()  # шанс нахождения Анной сигарет Алисы
        if RandomChance(chance):  # найдет ли Анна сигареты Алисы
            $ punalice[0][1] = 1
            $ pun_list.append("alice")

    $ renpy.random.shuffle(pun_list) # перемешаем список последовательности наказания

    if len(pun_list):
        jump punishment
    elif tm > "14:00":
        jump dinner_after_punishment
    else:
        jump breakfast_after_punishment


label punishment:
    $ renpy.block_rollback()
    if tm < "14:00":
        scene BG punish-morning 00
        $ renpy.show("Ann punish-morning 00"+chars["ann"].dress)
    else:
        scene BG punish-evening 00
        $ renpy.show("Ann punish-evening 00"+chars["ann"].dress)

    Ann_16 "Прежде, чем мы начнём, кое-кто заслуживает наказания и сейчас все на это посмотрят..."
    $ _i = 0
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

    if tm > "14:00":
        jump dinner_after_punishment
    else:
        jump breakfast_after_punishment


label punishment_max:
    $ renpy.block_rollback()

    if tm < "14:00":
        scene BG punish-morning 01
        $ renpy.show("Ann punish-morning 01"+chars["ann"].dress)
        $ renpy.show("Max punish-morning 01"+mgg.dress)
    else:
        scene BG punish-evening 01
        $ renpy.show("Ann punish-evening 01"+chars["ann"].dress)
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
        $ __list = []
        label .pun_reson:
            $ __list.clear()
            if punreason[0]:
                $ __list.append((_("Ну, я случайно оказался рядом с душем, когда там была Лиза..."), 0))
            if punreason[1]:
                $ __list.append((_("Ну, я оказался случайно рядом с душем, где мылась Алиса..."), 1))
            if punreason[2]:
                $ __list.append((_("Ну, я подглядывал за тобой, мам..."), 2))
            if punreason[3]:
                $ __list.append((_("Ну, я подглядывал за вами с Эриком..."), 3))
            if punreason[4]:
                $ __list.append((_("Ну, я оказался случайно рядом с душем, где мылась Алиса..."), 4))
            $ rez = renpy.display_menu(__list)
            if rez == 0:
                Lisa_12 "Он видел меня голой, мам! Накажи его! Почему он отделывается только предупреждением? Пусть получит, что заслужил!"
                $ punreason[0] = 0
                $ peeping['lisa_shower'] = 0
                Max_11 "Да ничего я не заслужил!"
            if rez == 1:
                Alice_16 "Случайно? Врёт он всё, мам! Он стоял и пялился на меня!"
                $ punreason[1] = 0
                $ peeping['alice_shower'] = 0
                Max_11 "Да, я мимо проходил!"
            if rez == 2:
                Ann_14 "Очень хочу надеяться, что это было случайно. Тем не менее, ты пойман и как я уже сказала, получаешь предупреждение."
                $ peeping['ann_shower'] = 0
                $ punreason[2] = 0
                Max_10 "Больше это не повторится!"
            if rez == 3:
                Ann_14 "Очень хочу надеяться, что ты это сделал не специально и просто проходил мимо. Тем не менее, ты пойман и как я уже сказала, получаешь предупреждение."
                $ punreason[3] = 0
                Max_10 "Да, я мимо проходил!"
            if rez == 4:
                Alice_16 "Случайно? Мам! Он всё врёт! Он подглядывал и, может быть, даже паука подбросил! А ты знаешь, как я боюсь пауков..."
                $ peeping['alice_shower'] = 0
                $ punreason[4] = 0
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
        $ _chance = GetChance(mgg.social, 2, 900)
        $ _chance_color = GetChanceColor(_chance)
        $ ch_vis = str(int(_chance/10)) + "%"
        menu:
            Ann_16 "Макс! Сейчас ты будешь наказан, сам знаешь за что!"
            "Я же не виноват! {color=[_chance_color]}(Убеждение. Шанс: [ch_vis]){/color}":
                pass
        if RandomChance(_chance):
            $ mgg.social += 0.2
            Ann_14 "{color=[lime]}{i}Убеждение удалось!{/i}{/color}\nТы знаешь, Макс, всё говорит о том, что ты виноват и должен быть наказан. Но поверю тебе на слово, что это была какая-то ошибка. Надеюсь, я не пожалею о своём решении..."
            Max_08 "Спасибо, мам!"
            python:
                for d in range(len(punreason)):
                    punreason[d] = 0
            return
        else:
            $ mgg.social += 0.1
            if mgg.dress == "a":
                $ _text = _("штаны")
            else:
                $ _text = _("шорты")
            menu:
                Ann_19 "{color=[orange]}{i}Убеждение не удалось!{/i}{/color}\nВот так просто? \"Я не виноват\" и всё забудем? Нет, Макс, со мной эти шуточки не прокатят. Давай, снимай [_text!tq] и ложись на мои колени. Надеюсь, ты сегодня в трусах..."
                "{i}снять штаны{/i}":
                    pass
        $ renpy.show("Max punish-evening 02"+mgg.dress)

        Ann_18 "Ну и долго я буду ждать?! Давай ложись..."

        if tm < "14:00":
            scene BG punish-morning 02
            if mgg.dress == "a":
                $ renpy.show("Ann punish-morning max-01"+chars["ann"].dress)
            else:
                $ renpy.show("Ann punish-morning max-03"+chars["ann"].dress)
        else:
            scene BG punish-evening 02
            if mgg.dress == "a":
                $ renpy.show("Ann punish-evening max-01"+chars["ann"].dress)
            else:
                $ renpy.show("Ann punish-evening max-03"+chars["ann"].dress)

        # Макс без штанов у Анны на коленях
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
            Ann_16 "[_text!tq]"
        ### сцена наказания
        if tm < "14:00":
            if mgg.dress == "a":
                $ renpy.show("Ann punish-morning max-02"+chars["ann"].dress)
            else:
                $ renpy.show("Ann punish-morning max-04"+chars["ann"].dress)
        else:
            if mgg.dress == "a":
                $ renpy.show("Ann punish-evening max-02"+chars["ann"].dress)
            else:
                $ renpy.show("Ann punish-evening max-04"+chars["ann"].dress)
        Max_14 "{i}Мама наказывает меня прямо перед сёстрами... Это так унизительно...{/i}\n\n{color=[orange]}{b}Внимание:{/b} Ваше влияние на присутствующих понизилось!{/color}"
        ## здесь снижение влияния Макса для присутствующих персонажей
        python:
            for cr in current_room.cur_char:
                if chars[cr].infmax is not None:
                    chars[cr].infmax = clip(chars[cr].infmax - 5.0, 0.0, 100.0)
            # обнуление провинностей
            for d in range(len(punreason)):
                punreason[d] = 0

        if tm < "14:00":
            scene BG punish-morning 01
            $ renpy.show("Ann punish-morning 01"+chars["ann"].dress)
            $ renpy.show("Max punish-morning 03"+mgg.dress)
        else:
            scene BG punish-evening 01
            $ renpy.show("Ann punish-evening 01"+chars["ann"].dress)
            $ renpy.show("Max punish-evening 03"+mgg.dress)

        Ann_12 "Ну вот. Теперь все всё поняли? Ведите себя хорошо и вас не ждёт эта участь..."
    # elif newpunishment == 1:  # второй вариант наказания
    #
    return


label punishment_lisa:
    $ renpy.block_rollback()

    scene BG punish-evening 01
    $ renpy.show("Lisa punish-evening 01"+chars["lisa"].dress)
    $ renpy.show("Ann punish-evening 01"+chars["ann"].dress)

    $ __mood = 0

    # Лиза стоит в одежде, Макс может вмешаться и прервать наказание (если получится)
    if chars["lisa"].dress == "a":  # Лиза в обычной одежде
        $ _text = _("Ближе подходи, Лиза. И да, снимай штаны, ты заслужила!")
    else: # Лиза в халате
        $ _text = _("Ближе подходи, Лиза. И да, снимай свой халат, ты заслужила!")
    if defend:  # Макс уже не может заступиться
        Ann_16 "[_text!tq]"
    else:
        $ _chance = GetChance(mgg.social, 2, 900)
        $ _chance_color = GetChanceColor(_chance)
        $ ch_vis = str(int(_chance/10)) + "%"
        menu:
            Ann_16 "[_text!tq]"
            "{i}Заступиться за Лизу {color=[_chance_color]}(Убеждение. Шанс: [ch_vis]){/color}{/i}":
                $ defend = True
                Max_08 "Мам, не нужно наказывать Лизу. Она правда старалась, я сам видел. Ну и я помогу ей подтянуть оценки."
                if "mgg" in pun_list:
                    Ann_12 "Нет, Макс, и даже не пытайся меня уговорить. Ты и сам накосячил... А ты, Лиза, не стой столбом, шевелись давай..."
                elif RandomChance(_chance):  # Удалось уговорить Анну
                    $ mgg.social += 0.2
                    Ann_00 "{color=[lime]}{i}Убеждение удалось!{/i}{/color}\nХорошо, Макс, в этот раз я не стану её наказывать. Надеюсь, я не пожалею о своём решении... А ты, Лиза, благодари брата, да учись давай, а то в следующий раз не помилую..."
                    Lisa_02 "Спасибо тебе, Макс!"
                    $ punlisa[0][2] = 2
                    return
                else:
                    $ mgg.social += 0.1
                    Ann_12 "{color=[orange]}{i}Убеждение не удалось!{/i}{/color}\nНет, Макс, твои уговоры ей не помогут. Получит то, что заслужила. А ты, Лиза, не стой столбом, шевелись давай..."
                    $ punlisa[0][2] = 1
            "{i}далее{/i}":
                pass

    Lisa_10 "Мам... Я не специально... Просто, задание было сложное..."
    if chars["lisa"].dress == "a":  # Лиза в обычной одежде
        $ _text = _("Быстро снимай штаны!")
    else: # Лиза в халате
        $ _text = _("Быстро снимай халат!")
    Ann_14 "Сложное? У тебя была куча времени, чтобы подготовиться! Сидишь в своём телефоне вечно вместо того, чтобы учиться. [_text!tq]"

    # Лиза стоит частично/полностью раздетая, если Макс не вмешивался, то может попробовать прервать наказание
    $ renpy.show("Lisa punish-evening 02"+chars["lisa"].dress)
    $ _text = _("Теперь ложись, и побыстрее, все есть хотят...")

    if defend:  # Макс уже заступался
        Ann_18 "[_text!tq]"
    else:
        menu:  # У Макса есть шанс заступиться за Лизу
            Ann_18 "[_text!tq]"
            "{i}Заступиться за Лизу {color=[_chance_color]}(Убеждение. Шанс: [ch_vis]){/color}{/i}":
                $ defend = True
                Max_08 "Мам, не нужно наказывать Лизу. Она правда старалась, я сам видел. Ну и я помогу ей подтянуть оценки."
                if "mgg" in pun_list:
                    Ann_12 "Нет, Макс, и даже не пытайся меня уговорить. Ты и сам накосячил... А ты, Лиза, не стой столбом, шевелись давай..."
                elif RandomChance(_chance):  # Удалось уговорить Анну
                    $ mgg.social += 0.2
                    Ann_00 "{color=[lime]}{i}Убеждение удалось!{/i}{/color}\nХорошо, Макс, в этот раз я не стану её наказывать. Надеюсь, я не пожалею о своём решении... А ты, Лиза, можешь одеваться. Скажи спасибо Максу, что сегодня осталась безнаказанной. Но не думай, что я всегда буду такой доброй..."
                    Lisa_02 "Спасибо тебе, Макс!"
                    $ punlisa[0][2] = 2
                    return
                else:
                    $ mgg.social += 0.1
                    Ann_12 "{color=[orange]}{i}Убеждение не удалось!{/i}{/color}\nНет, Макс, твои уговоры ей не помогут. Получит то, что заслужила. А ты, Лиза, не стой столбом, шевелись давай..."
                    $ punlisa[0][2] = 1
            "{i}далее{/i}":
                pass

    # сцена наказания Лизы
    scene BG punish-evening 02
    if chars["lisa"].dress == "a":
        $ renpy.show("Ann punish-evening lisa-01"+chars["ann"].dress)
    else:
        $ renpy.show("Ann punish-evening lisa-03"+chars["ann"].dress)

    $ __mood -= 100 # если Лизу наказывают, ее настроение портится
    $ talk_var['lisa.pun'] += 1

    Lisa_09 "Ма-ам, я больше не буду... Ай... В смысле, буду лучше учиться. Извини..."
    if chars["lisa"].dress == "a":
        $ renpy.show("Ann punish-evening lisa-02"+chars["ann"].dress)
    else:
        $ renpy.show("Ann punish-evening lisa-04"+chars["ann"].dress)

    $ _text = _("Говоришь тебе, говоришь, все как об стенку горох...") # вставка, если Макс не помогал за последнюю неделю

    # посмотрим, помогал ли Макс за последние 5 дней
    python:
        for i in range(min(5, len(punlisa))):
            if punlisa[i][0] == 1 or punlisa[i][0] > 2:
                _text = _("Поразительно! Тебе даже Макс помогает, а ты двойки хватаешь!") # вставка, если Макс помогал
                break

    Ann_00 "Конечно, будешь. [_text!tq] Совсем расслабилась."

    $ punlisa[0][3] = 1  # Лиза понесла наказание
    if punlisa[0][0] == 1:  # Макс умышленно сделал ошибку и Лизу наказали
        $ punlisa[0][4] = renpy.random.randint(50, 300)  # подозрительность Лизы растет случайно от 5 до 30%

    # сцена с наказанной Лизой
    scene BG punish-evening 01
    $ renpy.show("Lisa punish-evening 03"+chars["lisa"].dress)
    $ renpy.show("Ann punish-evening 01"+chars["ann"].dress)
    Ann_12 "Лиза, надеюсь, ты извлекла урок из этого наказания и больше это не повторится. А теперь одевайся!"

    $ AddRelMood('lisa', 0, __mood)
    return


label punishment_alice:
    $ renpy.block_rollback()

    scene BG punish-evening 01
    $ renpy.show("Alice punish-evening 01"+chars["alice"].dress)
    $ renpy.show("Ann punish-evening 01"+chars["ann"].dress)

    $ __mood = 0

    # Алиса стоит в одежде, Макс может вмешаться и прервать наказание (если получится)
    if chars["alice"].dress == "a":  # Алиса в обычной одежде
        Ann_16 "Подходи, подходи, Алиса, чего ты там мнешься. Штаны снимай, есть разговор!"
    else: # Алиса в пижамке
        Ann_16 "Подходи, подходи, Алиса, чего ты там мнешься. Снимай шорты, есть разговор!"
    Alice_12 "Мам, за что? Что я такого сделала?"
    if chars["alice"].dress == "a":  # Алиса в обычной одежде
        $ _text = _("Алиса, ты издеваешься? Я нашла сигареты у тебя в комнате! Ты опять куришь! Быстро сняла штаны и легла на мои колени, кому сказала!")
    else:
        $ _text = _("Алиса, ты издеваешься? Я нашла сигареты у тебя в комнате! Ты опять куришь! Быстро сняла шорты и легла на мои колени, кому сказала!")
    if defend:  # Макс уже не может заступиться
        Ann_18 "[_text!tq]"
    else:
        $ _chance = GetChance(mgg.social, 2, 900)
        $ _chance_color = GetChanceColor(_chance)
        $ ch_vis = str(int(_chance/10)) + "%"
        menu:
            Ann_18 "[_text!tq]"
            "{i}Заступиться за Алису {color=[_chance_color]}(Убеждение. Шанс: [ch_vis]){/color}{/i}":
                $ defend = True
                Max_08 "Мам, не нужно наказывать Алису. Это не её сигареты, к ней сегодня подружка приходила, наверное, она забыла."
                if "mgg" in pun_list:
                    Ann_12 "Нет, Макс, даже не пытайся её оправдывать. Ты и сам накосячил... Алиса, пошевеливайся..."
                elif RandomChance(_chance):  # Удалось уговорить Анну
                    $ mgg.social += 0.2
                    Ann_14 "{color=[lime]}{i}Убеждение удалось!{/i}{/color}\nХорошо, Макс, сегодня я не стану её наказывать. Надеюсь, я не пожалею об этом... Скажи брату спасибо, Алиса, что заступился, и не приглашай больше сюда таких подружек, хорошему они не научат..."
                    Alice_13 "Хорошо, мам. Спасибо, Макс, я этого не забуду."
                    $ punalice[0][2] = 2
                    return
                else:
                    $ mgg.social += 0.1
                    Ann_16 "{color=[orange]}{i}Убеждение не удалось!{/i}{/color}\nНет, Макс, твои уговоры ей не помогут. Получит в любом случае, не за себя, так за подружку. Не будет водится с такими, до добра они не доведут..."
                    $ punalice[0][2] = 1
            "{i}далее{/i}":
                pass

    Alice_13 "Мам... Это не мои сигареты... Я не курю, честно..."
    if chars["alice"].dress == "a":  # Алиса в обычной одежде
        Ann_14 "Не твои? А чьи они тогда? Быстро снимай штаны!"
        if chars['alice'].nopants:
            Alice_06 "Мам, но я сегодня без трусиков... Пусть Макс уйдёт или отвернётся, хотя бы..."
            Ann_20 "Ты ещё и без трусов?! Сейчас ещё и за это получишь! Макс пусть смотрит, а тебе будет стыдно. Может тогда за ум возьмёшься!"
            show Alice punish-evening 02aa
        else:
            show Alice punish-evening 02a
            if flags['smoke'] == 'not_nopants':
                $ flags['noted'] = True
                Max_09 "{i}Ничего себе! А что это на Алисе делают трусики?! Мы же с ней договорились... Ну всё, сестрёнка, считай ты попала... и куда больше, чем есть сейчас!{/i}"
    else: # Алиса в пижамке
        Ann_14 "Не твои? А чьи они тогда? Быстро шорты снимай!"
        Alice_06 "Мам, но под ними нет трусиков... Пусть Макс уйдёт или отвернётся, хотя бы..."
        Ann_00 "А вот нечего целый день в пижаме по дому шарахаться... Совсем разленилась! Макс пусть смотрит, а тебе будет стыдно. Может тогда за ум возьмёшься!"
        show Alice punish-evening 02ba

    $ _text = _("Теперь ложись побыстрее, ужин стынет...")

    if defend:  # Макс уже заступался
        Ann_18 "[_text!tq]"
    else:
        menu:  # У Макса есть шанс заступиться за Алису
            Ann_18 "[_text!tq]"
            "{i}Заступиться за Алису {color=[_chance_color]}(Убеждение. Шанс: [ch_vis]){/color}{/i}":
                $ defend = True
                Max_08 "Мам, не нужно наказывать Алису. Это не её сигареты, к ней сегодня подружка приходила, наверное, она забыла."
                if "mgg" in pun_list:
                    Ann_12 "Нет, Макс, даже не пытайся её оправдывать. Ты и сам накосячил... Алиса, пошевеливайся..."
                elif RandomChance(_chance):  # Удалось уговорить Анну
                    $ mgg.social += 0.2
                    Ann_14 "{color=[lime]}{i}Убеждение удалось!{/i}{/color}\nХорошо, Макс, сегодня я не стану её наказывать. Надеюсь, я не пожалею об этом... Можешь одеваться, Алиса, да скажи брату спасибо, что заступился. И не приглашай сюда больше таких подружек, хорошему они не научат..."
                    Alice_13 "Хорошо, мам. Спасибо, Макс, я этого не забуду."
                    $ punalice[0][2] = 2
                    return
                else:
                    $ mgg.social += 0.1
                    Ann_16 "{color=[orange]}{i}Убеждение не удалось!{/i}{/color}\nНет, Макс, твои уговоры ей не помогут. Получит в любом случае, не за себя, так за подружку. Не будет водится с такими, до добра они не доведут..."
                    $ punalice[0][2] = 1
            "{i}далее{/i}":
                pass

    # сцена наказания Алисы
    scene BG punish-evening 02
    if chars["alice"].dress == "a":
        if flags['smoke'] == "nopants":
            $ renpy.show("Ann punish-evening alice-03"+chars["ann"].dress)
        else:
            $ renpy.show("Ann punish-evening alice-01"+chars["ann"].dress)
    else:
        $ renpy.show("Ann punish-evening alice-05"+chars["ann"].dress)

    $ __mood -= 100 # если Алису наказывают, ее настроение портится
    $ talk_var['alice.pun'] += 1

    Alice_15 "Ай, больно же! Мам, я больше не буду!!!"
    if chars["alice"].dress == "a":
        if flags['smoke'] == "nopants":
            $ renpy.show("Ann punish-evening alice-04"+chars["ann"].dress)
        else:
            $ renpy.show("Ann punish-evening alice-02"+chars["ann"].dress)
    else:
        $ renpy.show("Ann punish-evening alice-06"+chars["ann"].dress)

    Ann_17 "Я знаю, что не будешь. Заслужила наказание, терпи!"

    $ punalice[0][3] = 1  # Алиса понесла наказание
    if  punalice[0][0] > 0 and punalice[0][1] == 1:  # Макс шантажировал Алису и подставил ее в этот же день
        $ punalice[0][4] = renpy.random.randint(50, 300)  # подозрительность Алисы растет случайно от 5 до 30%

    # сцена с наказанной Алисой
    scene BG punish-evening 01
    $ renpy.show("Ann punish-evening 01"+chars["ann"].dress)
    if chars["alice"].dress == "a":
        if flags['smoke'] == "nopants":
            show Alice punish-evening 03aa
        else:
            show Alice punish-evening 03a
        Ann_12 "Так, всё, надевай свои джинсы. Надеюсь, ты осознала свои поступки и следующего раза не будет..."
    else:
        show Alice punish-evening 03ba
        Ann_12 "Так, всё, надевай свои шорты. Надеюсь, ты осознала свои поступки и следующего раза не будет..."

    $ AddRelMood('alice', 0, __mood)
    return
