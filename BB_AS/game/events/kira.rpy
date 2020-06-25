

label kira_swim:
    scene image 'Kira swim '+pose3_4+kira.dress
    $ persone_button1 = 'Kira swim '+pose3_4+kira.dress+'b'
    return


label kira_sun:
    scene image 'BG char Alice sun'
    $ renpy.show('Kira sun '+pose3_4+kira.dress)
    $ persone_button1 = 'Kira sun '+pose3_4+kira.dress+'b'
    return


label kira_bath:
    return


label kira_night_swim:
    return


label kira_sleep_night:
    # не доступна пользователю
    return


label kira_sleep_morning:

    scene BG char Kira lounge-morning-01
    $ renpy.show('Kira sleep '+pose3_4+kira.dress)
    if peeping['kira_sleep'] != 0:
        return

    $ peeping['kira_sleep'] = 1
    menu:
        Max_04 "Ага! Тётя Кира ещё спит. Хорошо, что её ночнушка слегка просвечивает... Ухх, как она хороша..."
        "{i}подойти поближе{/i}":
            scene BG char Kira lounge-morning-02
            $ renpy.show('Kira sleep-closer '+pose3_4+kira.dress)
            if pose3_4=='01':
                Max_02 "Класс! Какая сладкая попка у моей тёти... Хочется любоваться бесконечно. И не только любоваться..."
            elif pose3_4=='02':
                Max_03 "О, да! К этой шикарной попке я бы с удовольствием прижался... Как и к этим соблазнительным сисечкам. Ммм, очаровательна, как ни крути..."
            else:
                Max_05 "Чёрт, от вида этих раздвинутых и стройных ножек в шортах становится слишком тесно... Ещё бы, такая горячая красотка!"
        "{i}уйти{/i}":
            pass

    return


label return_for_club:
    return


label kira_night_tv:
    $ renpy.block_rollback()
    scene BG tv-watch-01
    $ renpy.show('tv serial '+renpy.random.choice(['01','02','03','04','05','06','07']), at_list=[tv_screen,])
    $ renpy.show('Kira tv-watch 01'+eric.dress)

    menu:
        Max_01 "Тётя Кира ещё не легла спать... смотрит сериалы. Может, стоит задержаться?"
        "{i}Непременно{/i}":
            pass
        "{i}уже поздно...{/i}":
            jump .end

    scene BG lounge-tv-00
    $ renpy.show('Kira tv '+pose3_4+kira.dress)
    menu:
        Max_00 "Да-а-а, кто-то залипает на сериалы, а я вот залипаю на свою тётю..."
        "Тётя Кира?":
            scene BG lounge-tv-01
            $ renpy.show('Kira tv-closer '+pose3_4+kira.dress)
            $ renpy.show('Max tv 00'+mgg.dress)

            menu:
                Kira_00 "А? Макс? Как ты подкрался незаметно... Я думала, уже все спят давно... А меня тут один сериальчик зацепил, решила досмотреть..."
                "Мне что-то не спится. Можно тоже телек с тобой посмотреть?":
                    menu:
                        Kira_00 "Да без проблем, садись рядом. Будем досматривать сериал или найдём какой-нибудь боевик, фантастику?"
                        "Может быть, эротику?":
                            Kira_00 "Макс, а ты не слишком юн для этого? Я не думаю, что это хорошая идея."
                            Max_00 "Ты прямо как моя мама! Я уже взрослый, а в этом доме не то что посмотреть эротику не выйдет, так даже просто произнести это нельзя."
                            Kira_00 "Вообще, я думаю, что тебе уже пора спать. Три часа ночи... Давай в другой раз поговорим об этом..."
                            Max_00 "Вот так всегда..."
                            jump .end
                        "Давай смотреть порно?!" if talk_var['kira.porn']:
                            jump .porn
                        "Я насчёт уроков поцелуев, если момент подходящий..." if 'kira' in talk_var['ask.teachkiss']:
                            jump .teachkiss
                "Я просто хотел пожелать спокойной ночи!":
                    Kira_00 "Хорошо, Макс. Спокойной ночи! Я тоже уже скоро ложусь спать, только серию досмотрю..."
                    Max_00 "Ага, приятных снов..."
                    jump .end
        "{i}продолжать смотреть{/i}":
            pass
        "{i}уже поздно...{/i}":
            jump .end

    scene BG lounge-tv-00
    $ renpy.show('Kira tv m-'+pose3_4+kira.dress)
    # "здесь нужен какой-то переход..."
    "Серия закончилась и Кира включила эротику или даже порно, пока непонятно..."
    menu:
        "Вот это уже горячо! От такой компании я не откажусь..."
        "Тётя Кира?":
            scene BG lounge-tv-01
            $ renpy.show('Kira tv-closer m-'+pose3_4+kira.dress)
            $ renpy.show('Max tv 00'+mgg.dress)

            if talk_var['kira.porn']:
                menu:
                    Kira_00 "А? Макс? Как ты подкрался незаметно... Я думала, уже все спят давно... А я тут... отдыхаю, как видишь. Присоединишься?"
                    "Конечно, да!":
                        jump .porn
                    "Я насчёт уроков поцелуев, если момент подходящий..." if 'kira' in talk_var['ask.teachkiss']:
                        jump .teachkiss
                    "Я просто хотел пожелать спокойной ночи!":
                        jump .good_night
            else:
                menu:
                    Kira_00 "А? Макс? Как ты подкрался незаметно... Я думала, уже все спят давно... А я тут... отдыхаю, как видишь. Я тебя не смущаю таким своим видом?"
                    "Ни капли!":
                        Kira_00 "Если твоя мама узнает, то нам обоим влетит. Так что... Пусть этот инцидент останется тайной..."
                        Max "Конечно, тётя Кира. А мне можно тоже... посмотреть этот фильм?"
                        jump .porn
                    "Да ты продолжай, я посижу, посмотрю...":
                        Kira_00 "Ну что ты, Макс. Я просто не ожидала, что кто-то увидит. Так неловко... Мы ведь сохраним этот инцидент в тайне?"
                        Max "Конечно, тётя Кира. А мне можно тоже... посмотреть этот фильм?"
                        jump .porn
                    "Я насчёт уроков поцелуев, если момент подходящий..." if 'kira' in talk_var['ask.teachkiss']:
                        jump .teachkiss
                    "Я просто хотел пожелать спокойной ночи!":
                        jump .good_night
        "{i}уже поздно...{/i}":
            jump .end

    label .porn:
        Kira_00 "Макс, а не рано тебе такое смотреть? Если эротику, то ещё куда ни шло... но это самое настоящее порно! Хотя, и эротику тебе не стоит смотреть. Во всяком случае, со мной..."
        Max_00 "Как будто я порно не видел... Мама с Эриком всё время тут порно смотрят, прежде чем уходят к себе наверх."
        if online_cources[0].current > 2:
            $ _ch1 = GetChance(mgg.social, 5, 900)
        menu:
            Kira_00 "Ага. И ты не придумал ничего лучше, чем попробовать посмотреть со своей тётей порно среди ночи?"
            "Вообще-то, с лучшей тётей на свете! {color=[_ch1.col]}(Убеждение. Шанс: [_ch1.vis]){/color}" if online_cources[0].current > 2: # второй курс убеждения пройден
                if RandomChance(_ch1.ch):
                    Kira_00 "[succes!t] Очень приятно это слышать, Макс. Порно, значит... Ну давай, присаживайся. Только руки не распускать. И не смущайся - я иногда... к себе прикасаюсь, так ощущения от фильма более... интересные, если ты меня понимаешь..."
                    Max_00 "Да без проблем! Давай уже смотреть..."
                    $ talk_var['kira.porn']=True
                else:
                    jump .failed
            "Вообще-то, с лучшей тётей на свете!": # курс не пройден, убедить нельзя
                jump .failed

    # совместный просмотр порно
    $ renpy.show('Kira tv-closer 01'+kira.dress)
    $ renpy.show("Max tv-closer "+pose3_1+mgg.dress)
    "..."
    jump .end

    label .teachkiss:
        "..."
        jump .end

    label .good_night:
        Kira_00 "Хорошо, Макс. Спокойной ночи! Я тоже уже ложусь спать... скоро."
        Max_00 "Ага, приятных снов..."
        jump .end

    label .failed:
        Kira_00 "[failed!t] Приятно слышать, Макс, но тебе пора спать! Три часа ночи... Мне уже и самой пора ложиться спать."
        Max_00 "Вот так всегда..."

    label .end:
        $ spent_time += 30
        jump Waiting


label kira_shower:
    return


label kira_lisa_shower:
    return


label kira_alice_shower:
    return
