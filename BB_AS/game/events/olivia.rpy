
label olivia_lisa_sun:
    scene BG char Lisa Olivia 2sun-01
    $ renpy.show('Lisa 2sun '+pose3_1+lisa.dress)
    $ renpy.show('Olivia 2sun '+pose3_3+olivia.dress)
    return


label olivia_lisa_swim:
    $ renpy.scene()
    $ renpy.show('BG char Lisa Olivia 2swim-'+pose3_3)
    if olivia.dress=='a':
        $ renpy.show('FG Lisa Olivia 2swim-'+pose3_3)
    return


label olivia_lisa_tv:
    if not film:
        $ film = ol_tv_order.pop(0)
        if not ol_tv_order:
            $ ol_tv_order = ['0'+str(i) for i in range(1, 8)]
            $ renpy.random.shuffle(ol_tv_order)

    # tv-watch-01 + сериал(один из семи, с окончанием 02) + tv-watch-01-lisa&olivia-(01/01a)
    scene tv-watch-01
    $ renpy.show('tv serial '+film+'-02', at_list=[tv_screen,])
    $ renpy.show('Olivia night-tv 01-01'+lisa.dress)

    if olivia.daily.tv_sex:
        return

    $ olivia.daily.tv_sex = 1
    $ renpy.dynamic('ch1')
    $ ch1 = GetChance(mgg.stealth, 2, 900)
    menu:
        Max_07 "{i}( Девчонки смотрят какой-то сериал, а я бы лучше на них посмотрел... Вот только обещал не мешать... ){/i}"
        "{i}подсмотреть\n{color=[ch1.col]}(Скрытность. Шанс: [ch1.vis]){/color}{/i}":
            if not RandomChance(ch1.ch):
                menu:
                    Max_10 "[risky!t]{i}( Нет, слишком опасно подглядывать за ними! Они в любой момент могут меня заметить... И хуже от этого будет только мне! ){/i}"
                    "{i}уйти{/i}":
                        jump .leave
            else:
                # tv-mass-05 + tv-watch-02-max-(01a/01b) + (tv-watch-02-lisa&olivia-(01/01a) или tv-watch-02-lisa&olivia-(02/02a) или tv-watch-02-lisa&olivia-(03/03a))
                scene BG tv-mass-05
                $ renpy.show('Max tv 02'+mgg.dress)
                $ renpy.show('Olivia night-tv 02-0'+str(renpy.random.randint(1, 3))+lisa.dress)
                if lisa.dcv.special.stage < 4:
                    Max_04 "{i}( Красота! Сидеть вместе с ними на диване было бы куда интереснее... Можно было бы поглядывать одним глазком на них, а другим на экран. Эх, лучше здесь не задерживаться, они в любой момент могут меня заметить... ){/i}"
                else:
                    Max_04 "{i}( Красота! Сидеть вместе с ними на диване было бы куда интереснее... Можно было бы поглядывать одним глазком на них, а другим на экран. Эх, лучше здесь не задерживаться, они в любой момент могут меня заметить... ){/i}" nointeract

                if not poss['SoC'].used(0):
                    # возможность "Кнут или пряник?" не открыта
                    Max_09 "{i}( Как же мне попасть вместе с ними на диван? Нужно, чтобы Лиза адекватнее относилась к моему возбуждённому виду, но как... Может, если она заметит, что я подглядываю за ней в душе, мне удастся с ней договориться и она не сдаст меня маме, а взамен она захочет увидеть голым меня? ){/i}" nointeract
                elif lisa.dcv.special.stage < 4:
                    # открыта возможность "Кнут или пряник?", но ещё не было просмотра ужастиков
                    Max_09 "{i}( Как же мне попасть вместе с ними на диван? Нужно, чтобы Лиза адекватнее относилась к моему возбуждённому виду, но как... Может, стоит чаще попадаться, когда я подглядываю за ней в душе? ){/i}" nointeract
                $ rez = renpy.display_menu([("{i}уйти{/i}", 'exit')])
                $ Skill('hide', 0.1)
                jump .leave

        "{i}уйти{/i}":
            jump .leave
    label .leave:
        $ current_room = house[0]
        jump AfterWaiting


label olivia_lisa_sleep:
    scene BG char Lisa bed-night
    $ renpy.show('Olivia sleep '+pose2_4+lisa.dress)
    return


label olivia_first_meeting:

    #кат-сцена во дворе (среда, 17:00)
    # lisa-incoming-00 + lisa&olivia-incoming-01
    scene BG incoming-00
    show Olivia incoming 00
    with Fade(0.4, 0, 0.3)
    play music olivia
    Lisa_01 "Вот и мой старший брат, знакомьтесь, это Оливия, моя одноклассница!"
    Max_04 "Привет, я Макс!"
    Olivia_01 "Приятно познакомиться, Макс!"
    Max_02 "Да, мне тоже... Рад, что у Лизы наконец-то появилась подруга."
    Olivia_04 "Я тоже рада. Вау... у вас такой большой, красивый и стильный дом... И такой классный бассейн!"
    Max_03 "Так отдыхайте, пока солнце ещё светит!"
    Lisa_02 "Ага, мы сейчас быстренько переоденемся и будем в бассейне плескаться, часок-другой. Может и позагорать успеем... если кое-кто нам мешать не будет..."
    Max_01 "Если только немного..."
    Olivia_03 "Давай уже разденемся, а потом будем разговаривать."
    menu:
        Lisa_01 "Да, мы скоро вернёмся..."
        "{i}дождаться девчонок{/i}":
            pass
    # lisa-incoming-00
    scene BG incoming-00
    Max_07 "{i}( А Оливия симпатичная девчонка! Надеюсь, она с этим Алексом только из-за его внешности и на деле, ничего особенного он из себя не представляет... Так или иначе, Лиза всё равно поделится со мной этой информацией, когда всё узнает... ){/i}"

    # punish-sun-01 + punish-sun-01-max-(01a/01b) + sun-incoming-01-lisa&olivia-01
    scene BG punish-sun 01
    $ renpy.show('Max punish-sun 01-01'+mgg.dress)
    show Olivia incoming 01
    Olivia_03 "Эй, Макс... О чём задумался?"
    Max_06 "Да так... Ого! Нет, не так... ого-го-го... Я заснул что ли?! Или ты просто что-то дома забыла?"
    Olivia_02 "Нет, не забыла. На самом деле, я взяла с собой больше, чем хотелось бы... У меня родители натуристы и мы дома все ходим голые, я к этому привыкла! Ну и я знаю, как это может шокировать, особенно мальчиков, поэтому и решила хотя бы низ купальника одеть..."
    Lisa_02 "Ага, он ведь так много всего скрывает..."
    Max_02 "Знаешь, Оливия, если тебе намного комфортнее вообще без купальника, то можешь снять! Никто против не будет..."
    Lisa_03 "Ну ещё бы... Макс уже кажется отреагировал на это в своём стиле..."

    # punish-sun-02 + sun-incoming-02-lisa&olivia-01
    scene BG punish-sun 02
    show Olivia incoming 02
    Olivia_05 "Да это нормально! У папы такая же реакция была, когда мы вместе с ним купались или загорали... Так что, я привыкла!"
    Max_07 "Слышала, Лиза? Это нормально! Оливия, а где твой папа сейчас?"
    Olivia_06 "Ну... Они с мамой поругались некоторое время назад и сейчас он с нами не живёт. А ещё у нас сломался бассейн и его некому чинить... Можно я к вам буду приходить купаться?"
    Max_05 "Я всеми руками и не руками за!"
    Olivia_04 "Здорово! Пойдём с нами купаться, Макс! Или загорать... Я вам так завидую... У вас есть чистый бассейн и пальмы почти ничего не закрывают... Тут как будто рай!"
    Max_07 "Я бы с радостью, да только вот кое-что будет вас смущать..."

    # hugging-sun-01 + sun-incoming-03-lisa&olivia-01 + sun-incoming-03-max-(01a/01b)
    scene BG char Alice hugging sun-01
    show Olivia incoming 03
    $ renpy.show('Max incoming 01'+mgg.dress)
    Olivia_03 "Да ладно тебе прикрываться... Меня это нисколько не смущает! Честно говоря, я не видела таких больших ещё ни разу... У моего папы меньше раза в два, если не в три, да и у моего парня... Ой. Это я вслух сказала сейчас?!"
    Max_09 "Я уже понял, что тебя это не смущает, а вот Лизу ещё как..."
    Olivia_05 "Правда?! Лиза, ты же говорила, вы с Максом в одной комнате живёте... Почему ты смущаешься?"
    Lisa_10 "Просто я долгое время думала, что у него стоит, потому что он что-то похабное со мной представляет."
    Max_07 "А я ей кучу раз говорил, что это естественная реакция" ###оно само так делается..."
    Olivia_02 "Эх, ребята... Ну теперь-то вы всё прекрасно знаете и понимаете, так? Пора уже привыкать к особенностям друг друга, а то как дети малые... Ладно, я хочу позагорать, а потом купаться! Если захочешь к нам присоединиться, Макс, мы здесь..."
    Max_01 "Ага, отдыхайте..."

    #после этого девчонки будут загорать и купаться с 17:00 до 19:00
    $ lisa.flags.crush = 12
    $ poss['Schoolmate'].open(5)
    call AddOlivia from _call_AddOlivia
    # если уже началась борьба с Эриком за Лизу, ночные встречи будут каждую неделю, иначе раз в две недели
    $ olivia.dcv.battle.stage = 1 if lisa.dcv.battle.stage else 2

    $ spent_time += 30
    jump Waiting


label olivia_night_visit:
    $ olivia.daily.tvwatch = 1      # сразу прописываем, что состоялся диалог о совместном просмотре ТВ
    $ olivia.dress = renpy.random.choice(['a', 'b'])
    if not olivia.dcv.special.stage:
        # первый ночной визит
        $ olivia.dcv.special.stage = 1
        jump olivia_first_night_visit

    elif olivia.dcv.special.stage < 2:
        # второй ночной визит Оливии (повторяемый, пока не дошло до просмотра ТВ второй раз)
        if GetRelMax('olivia')[0]<2:
            $ AttitudeChange('olivia', 1)   # Хорошие
        jump olivia_second_night_visit

    else:       # третий и последующие визиты
        jump olivia_night_visit_r


label olivia_first_night_visit:

    # villa-door-night-01 + villa-olivia-(01/01a)
    scene villa-door-night-01
    $ renpy.show('Olivia night-visit 01'+olivia.dress)
    with Fade(0.4, 0, 0.3)
    play music olivia
    Olivia_01 "Приветик! А вот и я... Спасибо, что встретил, Макс."
    Max_04 "Да без проблем. Проходи..."
    Olivia_02 "Значит, кроме нас и Лизы дома больше никого нет?"
    Max_03 "Да... Мама ушла к Эрику, а Алиса с тётей Кирой как всегда в это время тусят где-то. Вернутся поздно, так что у нас полно времени!"

    # after-club-alice&kira-00-f + villa-lisa-02 + villa-olivia-(02/02a)
    scene BG char Kira after-club-pull
    show Lisa night-visit 02
    $ renpy.show('Olivia night-visit 02'+olivia.dress)
    menu:
        Olivia_03 "Отлично! Конечно, ночью особо не позагораешь, но в этом есть своя прелесть... Ну всё, Лиза, пойдём что-нибудь посмотрим на вашем большом экране! Макс, ты как, с нами?"
        "Конечно с вами!":
            pass
    Olivia_05 "Только учтите, дресс-код на наше мероприятие - только нижнее бельё или пижамы! Кому в чём комфортнее..."
    Lisa_02 "А ты в чём будешь?"
    Olivia_03 "Конечно голышом! Думаю, вы уже достаточно ко мне привыкли, чтобы не смущаться меня и моего образа жизни."
    # after-club-alice&kira-00-f + villa-lisa-03 + villa-olivia-(03/03a)
    scene BG char Kira after-club-pull
    show Lisa night-visit 03b
    $ renpy.show('Olivia night-visit 03'+olivia.dress)
    Max_02 "Я особо и не смущался!"

    if lisa.dcv.special.stage < 4: # не было просмотров ужастиков с Лизой
        jump .failure
    else:   # был просмотр ужастиков с Лизой
        Lisa_01 "Ну да, оно и видно! У Макса уже в шортах кое-что шевелится... И нам с ним {b}ТАКИМ{/b} придётся сидеть..."
        Olivia_02 "Для меня это не проблема, Лиза... А вот что на счёт тебя?"
        Max_10 "Да ладно тебе, Лиза! Что тут такого?"
        Lisa_05 "Ничего... Я, в общем-то, привыкла уже. Почти..."

        if all([flags.film_punish, not lisa.dcv.special.done]):
            # попался на подглядывании за Лизой и должен был смотреть с ней ужастик
            jump olivia_about_film_punish   # в разговорах

    menu:
        Olivia_04 "Ну и отлично! Пойдёмте уже..."
        "{i}идти в гостиную{/i}":
            if not _in_replay:
                $ poss['Schoolmate'].open(10)
            jump night_tv_with_olivia

    label .failure:
        Lisa_10 "Ну нет, так не пойдёт! У Макса уже в шортах кое-что шевелится... Я не хочу, чтобы он с нами {b}ТАКОЙ{/b} сидел!"
        Max_10 "Да ладно тебе, Лиза! Что тут такого?"
        Olivia_06 "Похоже, Макс, у нас будет девичник... Уж извини! Лиза пока к такому не готова."
        Max_11 "Вот блин!"
        Lisa_13 "И подглядывать не вздумай!"

        if all([flags.film_punish, not lisa.dcv.special.done]):
            # попался на подглядывании за Лизой и должен был смотреть с ней ужастик
            jump olivia_about_film_punish   # в разговорах

        Max_14 "Ладно..."
        #перенос Макса в его комнату
        $ poss['Schoolmate'].open(9)
        $ spent_time = 20
        $ current_room = house[0]
        jump Waiting


label olivia_second_night_visit:
    # villa-door-night-01 + villa-olivia-(01/01a)
    scene villa-door-night-01
    $ renpy.show('Olivia night-visit 01'+olivia.dress)
    with Fade(0.4, 0, 0.3)
    play music olivia
    Olivia_01 "Привет, Макс. Вот я и снова к вам пришла... Как домашние? Никому не помешаю?"
    Max_04 "Нет, всё в порядке... Проходи, чувствуй себя как дома."

    # after-club-alice&kira-00-f + villa-lisa-02 + villa-olivia-(02/02a)
    scene BG char Kira after-club-pull
    show Lisa night-visit 02
    $ renpy.show('Olivia night-visit 02'+olivia.dress)
    menu:
        Olivia_02 "С радостью бы искупалась, но так устала, что хочу только валяться и смотреть сериалы. Пойдём, Лиза... Макс, ты как, с нами?"
        "Конечно с вами!":
            pass
    Olivia_03 "Лиза, а ты так и будешь в маечке и трусиках? Дома же никого нет."
    Lisa_09 "Никого, ага... Ладно ты, а Макс как же?"

    if lisa.dcv.special.stage < 4: # не было просмотров ужастиков с Лизой
        Max_07 "Ты настолько меня стесняешься?"
        Lisa_13 "Ну, да. Как любая девочка любого мальчика... Разве это неправильно?"
        # after-club-alice&kira-00-f + villa-lisa-03 + villa-olivia-(03/03a)
        show Lisa night-visit 03b
        $ renpy.show('Olivia night-visit 03'+olivia.dress)
        Olivia_05 "Стесняшка ты наша. Макс сказал, чтобы я чувствовала себя как дома... Так что я раздеваюсь."
        jump olivia_first_night_visit.failure

    else:       # был просмотр ужастиков с Лизой
        Olivia_05 "Макс вот своего тела не стесняется. И как я поняла, он уже видел всё, что скрывается под твоей одеждой..."
        Lisa_10 "Если я разденусь, он же всё время будет глазеть на меня, а не на экран. И как тут не стесняться?!"
        Max_07 "А как ты будешь со своим будущим парнем себя вести? Тоже будешь стесняться?"
        Lisa_13 "Не знаю... Может быть. Мне кажется, не очень правильно возбуждать тебя своим обнажённым видом."
        # after-club-alice&kira-00-f + villa-lisa-03 + villa-olivia-(03/03a)
        show Lisa night-visit 03b
        $ renpy.show('Olivia night-visit 03'+olivia.dress)
        Olivia_03 "Знаешь, Лиза, хоть вы брат и сестра, но вместе с тем - ты ещё и девочка. А природой заложено так, что девочки возбуждают мальчиков и наоборот. И это классно... чувствовать себя желанной!"
        Lisa_09 "Ну... не знаю... Я не могу так сразу на это решиться."
        Max_00 "Ты подумай над этим. Потому что парням быстро наскучивают зажатые девушки."
        if all([flags.film_punish, not lisa.dcv.special.done]):
            # попался на подглядывании за Лизой и должен был смотреть с ней ужастик
            jump olivia_about_film_punish   # в разговорах
    menu:
        Olivia_04 "Такими темпами мы ничего не посмотрим. Пойдёмте уже..."
        "{i}идти в гостиную{/i}":
            jump night_tv_with_olivia


label olivia_night_visit_r:
    # villa-door-night-01 + villa-olivia-(01/01a)
    scene villa-door-night-01
    $ renpy.show('Olivia night-visit 01'+olivia.dress)
    with Fade(0.4, 0, 0.3)
    play music olivia
    Olivia_01 "Привет, Макс. А вот и я! Дома никого?"
    Max_04 "Привет! Рад тебя видеть. Дома только я и Лиза. Проходи..."
    # after-club-alice&kira-00-f + villa-lisa-02 + villa-olivia-(02/02a)
    scene BG char Kira after-club-pull
    show Lisa night-visit 02
    $ renpy.show('Olivia night-visit 02'+olivia.dress)
    Olivia_02 "Лиза, я полдня тебя сегодня не видела, а уже соскучилась... Жду не дождусь уже раздеться и заниматься ничегонеделанием. Только сериалы с любимыми друзьями!"
    menu:
        Lisa_02 "Я тоже рада поваляться вместе с вами хоть один поздний вечерок."
        "Я с вами!":
            pass
    $ lisa.get_plan()
    if lisa_will_be_topless()>0:
        #Лиза без майки
        $ lisa.flags.topless += 1
        $ lisa.dress = 'c'
        # after-club-alice&kira-00-f + villa-lisa-03a + villa-olivia-(03/03a)
        show Lisa night-visit 03c
        $ renpy.show('Olivia night-visit 03'+olivia.dress)
        Max_05 "Ого! Лиза у нас сегодня тоже почти голенькая будет! Рад, что не стесняешься..."
        Lisa_02 "Ну... Почему бы немного не порадовать тебя, раз уж ты достойно помогал мне со всем, чем только можно на неделе."
        Max_03 "Хороший стимул... Мне нравится!"
        Lisa_01 "Только не засматривайся на меня так сильно! Я ведь и одеться могу."
    else:
        #Лиза в майке
        # after-club-alice&kira-00-f + villa-lisa-03 + villa-olivia-(03/03a)
        show Lisa night-visit 03b
        $ renpy.show('Olivia night-visit 03'+olivia.dress)
        if lisa_will_be_topless()==-4:
            Olivia_03 "Лиза, а ты почему маечку не снимаешь? Опять стесняешься..."
            Lisa_00 "Нет. У нас с Максом было... одно соглашение и он его нарушил. Поэтому радости у него сегодня будет поменьше."
        else:
            Max_07 "Лиза, а ты почему маечку не снимаешь? Я думал, ты уже не особо нас стесняешься..."
            Lisa_09 "Я бы сняла, да вот только не очень хочется тебя так радовать."
            Max_10 "Да ладно тебе, Лиза! Почему?"
            if lisa_will_be_topless()==-1:
                Lisa_10 "Вот помогал бы мне на этой неделе хоть немного с домашним заданием, ручки бы мои пожалел, с посудой помог... Или ты думаешь, защитил меня от маминого наказания разок и всё? Голую грудь в студию?!"
            elif lisa_will_be_topless()==-2:
                Lisa_10 "Вот помогал бы мне на этой неделе хоть немного с домашним заданием, ручки бы мои пожалел, с посудой помог... С таким Максом я бы ещё рядом посидела без маечки, а так..."
            else:
                Lisa_10 "Вот помогал бы мне на этой неделе хоть немного с домашним заданием, ручки бы мои пожалел, с посудой помог... А ты даже от маминого наказания меня не защитил..."
            Max_11 "Ну... Я мог бы..."
            Lisa_13 "Вот как сможешь, так и посмотрим. А пока что я ничего снимать с себя не хочу."

    if all([flags.film_punish, not lisa.dcv.special.done]):
        # попался на подглядывании за Лизой и должен был смотреть с ней ужастик
        jump olivia_about_film_punish   # в разговорах

    if lisa_will_be_topless()==-4:
        Olivia_04 "Эх, Макс! Прошляпил всё веселье. Ладно, пойдёмте уже..." nointeract
    else:
        Olivia_04 "Такими темпами мы ничего не посмотрим. Пойдёмте уже..." nointeract

    menu:
        "{i}идти в гостиную{/i}":
            jump night_tv_with_olivia
    label .end:
        $ olivia.daily.tvwatch = 2
        $ spent_time = 20
        jump Waiting


label night_tv_with_olivia:
    if not film:
        $ film = ol_tv_order.pop(0)
        if not ol_tv_order:
            $ ol_tv_order = ['0'+str(i) for i in range(1, 8)]
            $ renpy.random.shuffle(ol_tv_order)

    if not olivia.dcv.other.stage:
        # дошло до гостиной (1-ый раз)
        $ olivia.dcv.other.stage = 1
        jump olivia_first_night_out_with

    elif olivia.dcv.other.stage < 2:
        # дошло до гостиной (2-ой раз)
        $ olivia.dcv.other.stage = 2
        $ olivia.dcv.special.stage = 2
        jump olivia_second_night_out_with
    else:
        # следующие просмотры ТВ
        jump olivia_repeatable_night_out_with


label olivia_first_night_out_with:

    # lounge-tv-01 + tv-watch-03-lisa&olivia-01 + tv-max-(00a/00b)
    scene BG lounge-tv-01
    show Olivia night-tv 03-01b
    $ renpy.show('Max tv 00'+mgg.dress)
    with Fade(0.4, 0, 0.3)
    Max_05 "Ух ты! Ничего себе! Я даже забыл, что хотел спросить..."
    Olivia_03 "Так садись, Макс... Потом вспомнишь!"
    Max_02 "Ах, вот... Я тоже буду сидеть голышом! Вы же не против?"
    Olivia_05 "Нисколечко!"
    menu:
        Lisa_10 "Так, стоять! Это уже слишком! Я не уверена, что хочу сидеть рядом со своим голым братом. Хоть трусы оставь..."
        "{i}раздеться и сесть рядом{/i}":
            pass
    # lounge-tv-01 + tv-watch-03-lisa&olivia-02 + tv-watch-03-max-01
    show Olivia night-tv 03-02b
    show Max night-tv 03-01
    Olivia_04 "Ого, Макс! Это смело! И внушительно..."
    Lisa_11 "Ну ты даёшь! Тебе как вообще, не стыдно перед нами в таком виде рассиживаться?"
    Max_07 "Ты как с мальчиками-то собираешь встречаться, если даже со мной голым не можешь себя комфортно чувствовать? Привыкай..."
    Olivia_03 "Макс, кстати, прав... Тебе пора бы уже привыкать. Держаться с мальчиками за ручку и гулять - это здорово, но вы же не только этим будете заниматься."
    Lisa_10 "Поскромнее хоть сядьте оба, а то устроили тут нудистский диван."
    Max_04 "Давайте смотреть, что где показывают интересного..."
    # tv-watch-01 + сериал(один из семи, с окончанием 01) + tv-watch-01-lisa,olivia,max-01
    scene tv-watch-01
    $ renpy.show('tv serial '+film+'-01', at_list=[tv_screen,])
    show Olivia night-tv 01-02b
    Olivia_01 "Вот, можем этот сериал посмотреть... Вроде, что-то интересное происходит у них там. Надо вникать..."
    Max_02 "{i}( Мне куда интереснее то, что происходит на диване... А здесь рядом со мной сидят две обалденные девчонки и одна из них - совершенно голая, как и я! ){/i}"
    # tv-mass-01 + tv-watch-04-lisa,olivia,max-01
    scene BG tv-mass-01
    show Olivia night-tv 04-01b
    Max_03 "{i}( Лиза пока ещё стесняется моего вида... Слегка отвернулась, но поглядывает в мою сторону иногда. А вот Оливия очень комфортно себя чувствует. Такая расслабленная и красивая... ){/i}"
    Olivia_02 "Ты как там, Макс? Всё ещё возбуждён моим видом? Ага, вижу, что да..."
    Lisa_09 "И долго он таким может быть?"
    Olivia_03 "Похоже, что долго... Но вы к этому привыкните, если будете со мной больше времени проводить."
    # tv-mass-03 + tv-watch-05-lisa,olivia,max-01
    scene BG tv-mass-03
    show Olivia night-tv 05-01b
    Max_05 "По мне, так отличная причина тебе приходить к нам чаще!"
    Olivia_04 "Я бы с радостью, Макс. Было бы у меня больше свободного времени... Здесь и компания приятная, и вода в бассейне такая тёплая... Обожаю воду! Ну, вы уже в курсе."
    Lisa_01 "А Макс успокаивается наконец..."
    # tv-kiss-03 + tv-watch-06-lisa&olivia-(01/02) + tv-watch-06-max-01
    scene BG tv-kiss-03
    $ renpy.show('Olivia night-tv 06-0'+str(renpy.random.randint(1, 2))+'b')
    show Max night-tv 06-01
    Max_04 "Самую малость."
    Olivia_03 "Это я просто немного поскромнее уселась, чтобы у Макса косоглазие не развилось. Мальчики - они такие, он даже если будет стараться смотреть на экран, глаза всё равно потянутся в сторону голых девичьих прелестей."
    Lisa_02 "А у меня вот запросто получается смотреть сериал и никуда не отвлекаться."
    # tv-watch-01 + сериал(котороый выпал до этого, с окончанием 03) + tv-watch-01-lisa,olivia,max-01
    scene tv-watch-01
    $ renpy.show('tv serial '+film+'-03', at_list=[tv_screen,])
    show Olivia night-tv 01-02b
    Max_02 "{i}( Вижу я, как у тебя глазки бегают, то на меня, то на Оливию. Наверняка, Лизе даже нравится то, что здесь происходит сегодня... ){/i}"
    Olivia_06 "Ребята, у меня уже глаза слипаются. Давайте заканчивать, да я домой пойду..."
    Lisa_00 "Может не стоит ночью по улице бродить. Оставайся у нас, а утром вернёшься домой."
    Max_03 "Да, оставайся на ночь здесь!"
    Olivia_01 "Ой, я вообще-то не планировала, но вы правы, лучше остаться у вас до утра."
    Lisa_01 "Пойдёмте тогда в комнату..."
    # myroom-night-talk-01 + myroom-night-talk-01-lisa-02a + myroom-night-talk-01-olivia-01
    scene BG myroom-night-talk-01
    show Lisa myroom-night-talk 02b
    show Olivia myroom-night-talk 01
    with Fade(0.4, 0, 0.3)
    Max_04 "Кто куда ляжет?"
    Lisa_02 "Естественно, Оливия ляжет со мной, а ты как всегда... сам по себе."
    Max_02 "Оливия же в гостях... Может определим её на твою кровать, а ты со мной?"
    Lisa_01 "Чтобы ты всю ночь тыкался в меня своей штуковиной здоровенной?! Размечтался!"
    Olivia_02 "Хорошая попытка, Макс! Утром меня не теряйте, я уйду рано. Всем спокойной ночи..."
    Max_01 "Сладких снов."
    #переход на фон спящих Лизы и Оливии (Макс может делать, что хочет)
    #теперь Оливия будет загорать и плавать голышом

    $ spent_time = TimeDifference(tm, '02:00')
    stop music
    jump Waiting


label olivia_second_night_out_with:

    # lounge-tv-01 + tv-watch-03-lisa&olivia-02 + tv-watch-03-max-01
    scene BG lounge-tv-01
    show Olivia night-tv 03-02b
    show Max night-tv 03-01
    with Fade(0.4, 0, 0.3)
    Lisa_11 "А вы ещё мне предлагаете раздеться! Это Макс только на тебя одну, Оливия, так реагирует... А представь, что будет, если разденусь и я? Его штука вообще, наверно, взорвётся!"
    Max_03 "Ничего не взорвётся, не переживай."
    Olivia_03 "Лучше радуйся за брата, Лиза. Далеко не каждому мальчику настолько везёт с размерами... Не каждый день такое можно увидеть в живую. Вернее... ты-то как раз и можешь видеть!"
    Lisa_03 "Вот только ради этого и живу... Чтобы хоть разок за день увидеть стояк Макса!"
    # tv-watch-01 + сериал(один из семи, с окончанием 01) + tv-watch-01-lisa,olivia,max-01
    scene tv-watch-01
    $ renpy.show('tv serial '+film+'-01', at_list=[tv_screen,])
    show Olivia night-tv 01-02b
    Olivia_05 "Хочешь сказать, ты никогда не думала о Максе, как о мальчике, с которым можно что-то попробовать... Ну... что-то такое..."
    Lisa_13 "Нет, конечно! Скажешь тоже..."
    Max_02 "{i}( Интересно, как бы Оливия отреагировала, если бы Лиза рассказала, как я учу её целоваться и где мои руки при этом оказываются?! Святую тут из себя строит. Ну да ладно... ){/i}"
    Olivia_03 "Так я тебе и поверила, проказница... Ну а ты, Макс?"
    # tv-mass-01 + tv-watch-04-lisa,olivia,max-01
    scene BG tv-mass-01
    show Olivia night-tv 04-01b
    Max_04 "Конечно, да! Но я тут бессилен, это же непроизвольно."
    Olivia_04 "Видишь, Лиза, какой у тебя брат честный! Не то, что Алекс."
    Max_07 "А что с ним?"
    Olivia_00 "Ах, да... Ты же, наверно, не в курсе. Алекс в наглую, не порвав со мной, пытался клеить Лизу! Скотина такая!"
    Max_09 "Вот как! Погодите... Но раз вы обе здесь, значит у вас всё хорошо?"
    # tv-mass-03 + tv-watch-05-lisa,olivia,max-01
    scene BG tv-mass-03
    show Olivia night-tv 05-01b
    Lisa_02 "У нас - да! У Алекса не очень. Он двух потрясающих девчонок упустил! Хотя, теперь зная, какой он козёл, не исключаю, что он уже кого-то ещё клеит..."
    Olivia_06 "Если уже не склеил! Нет, даже думать об этом не хочу... Фу!"
    Max_00 "Получается, Оливия с парнем рассталась?"
    Lisa_01 "Именно так."
    # tv-watch-01 + сериал(котороый выпал до этого, с окончанием 02) + tv-watch-01-lisa,olivia,max-01
    scene tv-watch-01
    $ renpy.show('tv serial '+film+'-02', at_list=[tv_screen,])
    show Olivia night-tv 01-02b
    Olivia_00 "А главное, Алекс не расстроился ни от того, что я его бросила, ни от того, что Лиза не стала с ним встречаться. Уверена, это потому что у него был запасной вариант."
    Max_07 "Вот почему я предпочитаю секс без отношений! Трахаешься, когда хочешь и с кем хочешь... И никакой \"Санта-Барбары\"!"
    Lisa_11 "Что-о-о-о!"
    Max_02 "Это я вас таким образом от темы с Алексом решил отвлечь."
    # tv-kiss-03 + tv-watch-06-lisa&olivia-(01/02) + tv-watch-06-max-01
    scene BG tv-kiss-03
    $ renpy.show('Olivia night-tv 06-0'+str(renpy.random.randint(1, 2))+'b')
    show Max night-tv 06-01
    Lisa_03 "Фух... А то мне сразу в голову всякое невероятное полезло!"
    Olivia_05 "Ха! Это было смешно, Макс! Я рада, что оказалась в такой тёплой компании. Надеюсь, так будет и дальше..."
    Max_04 "Ага, хорошо сидим!"
    Lisa_02 "Знаете, я в таком хорошем настроении сейчас, от того, что для нас с Оливией всё так хорошо закончилось, что готова даже снять майку..."
    Max_06 "Вот это ничего себе!"
    # tv-mass-01 + tv-watch-04-lisa,olivia,max-01a
    scene BG tv-mass-01
    show Olivia night-tv 04-01c
    Olivia_03 "Да ладно! Макс же тут... Ты вроде не хотела при нём..."
    Lisa_05 "Да пусть смотрит, если хочет. Будем считать, что ему сегодня очень повезло, потому что я хочу делиться своей радостью!"
    Max_05 "{i}( Во сестрёнка даёт! Естественно, я хочу на это смотреть... Не то, чтобы в наглую, но всё-таки такого количества голых сисек на этом диване ещё не было! ){/i}"
    Olivia_02 "А Макс притих. Наверно, весь в раздумьях, куда лучше смотреть! Хоть бы на экран поглядел для приличия."
    Max_03 "Голова никак не поворачивается."
    # tv-watch-01 + сериал(котороый выпал до этого, с окончанием 03) + tv-watch-01-lisa,olivia,max-01a
    scene tv-watch-01
    $ renpy.show('tv serial '+film+'-03', at_list=[tv_screen,])
    show Olivia night-tv 01-02c
    Lisa_01 "Ничего, ты сама говорила - привыкнет... Я же немного привыкла, что вы тут голые сидите."
    Olivia_01 "А я бы уже спать пошла. Уже поздно... Я вся иззевалась. Вы ещё не хотите?"
    Lisa_02 "Можно. Пойдёмте, пока все тут не заснули. Вот бы тётя Кира удивилась..."
    # myroom-night-talk-01 + myroom-night-talk-01-lisa-02b + myroom-night-talk-01-olivia-01
    scene BG myroom-night-talk-01
    show Lisa myroom-night-talk 02c
    show Olivia myroom-night-talk 01
    with Fade(0.4, 0, 0.3)
    Max_04 "Спокойной ночи, девчонки. Я в восторге от наших с вами ночных посиделок!"
    Lisa_03 "По тебе и так прекрасно видно, как сильно ты доволен. Уверена, надеешься, что я забуду маечку надеть и прямо так и лягу..."
    Max_02 "Ага. Зря, да?"
    Lisa_02 "Конечно, зря! Может сериалы среди ночи я и буду смотреть в одних трусиках, и то, это не факт... Но это не значит, что я теперь всё буду делать в таком виде!"
    Max_03 "Ладно. Уже и помечтать нельзя."
    Olivia_06 "В прошлый раз я же тихо и незаметно ушла? Никого не побеспокоила?"
    Lisa_01 "Нет, я даже не заметила, как ты встала..."
    Max_01 "Да, я тоже. Сладких снов, девчонки."

    $ renpy.end_replay()
    $ poss['Schoolmate'].open(12)
    $ lisa.dcv.other.enabled = False
    $ spent_time = TimeDifference(tm, '02:00')
    stop music
    jump Waiting


label olivia_repeatable_night_out_with:
    scene BG lounge-tv-01
    $ renpy.show('Olivia night-tv 03-01'+lisa.dress)
    $ renpy.show('Max tv 00'+mgg.dress)
    with Fade(0.4, 0, 0.3)
    if lisa_will_be_topless()>0:
        #Лиза без майки
        # lounge-tv-01 + tv-watch-03-lisa&olivia-01a + tv-max-(00a/00b)
        Lisa_02 "Ты чего завис, Макс? Давай садись быстрее..."
        Max_02 "Знаешь, бывают моменты, когда засмотришься на что-то и потом никак оторваться не можешь..."
        Lisa_01 "Может, мне тогда стоит одеться, чтобы ты над душой не стоял?"
        Max_04 "Нет, нет, нет... Я уже раздеваюсь!"
    else:
        #Лиза в майке
        # lounge-tv-01 + tv-watch-03-lisa&olivia-01 + tv-max-(00a/00b)
        Lisa_02 "Ты чего завис, Макс? Давай садись быстрее..."
        Max_02 "Да я вот задумался, как мне тебя уговорить маечку снять... Только, по-моему, без шансов, да?"
        Lisa_01 "Именно! Ты или тогда не стой над душой, или раздевайся и присоединяйся... пока я добрая."
        Max_04 "От такой симпатичной компании, как вы, я не откажусь!"

    # lounge-tv-01 + tv-watch-03-lisa&olivia-(02/02a) + tv-watch-03-max-01
    $ renpy.show('Olivia night-tv 03-02'+lisa.dress)
    show Max night-tv 03-01

    if renpy.random.randint(0, 1):
        #вариант 1
        Olivia_05 "Ты бы поосторожнее запрыгивал на диван, Макс! А то своей огромной штуковиной по Лизе ещё попадёшь! Тебе же потом придётся объяснять всем своим, откуда у неё фингал."
        Max_03 "Уж извините... Со мной лучше ртом не зевать!"
        Lisa_02 "Что правда, то правда! Я видела Макса голым уже столько раз, а всё ещё удивляюсь."
        Max_05 "И кто на кого, в итоге, больше всех засматривается?"
    else:
        #вариант 2
        Lisa_02 "Ты поосторожнее, Макс, запрыгивай на диван, а то этой своей штукой ещё по мне попадёшь! Я не хочу потом с фингалом ходить и придумывать историю, в которой не фигурирует твой член."
        Max_03 "Со мной лучше быть начеку! Тогда и фингалов никаких не будет."
        Olivia_05 "Я таких беззастенчивых парней, как Макс, ещё не встречала. Хотя, оно и понятно, почему... Есть чем гордиться!"
        Max_05 "Спасибо! Я, конечно, не против этого внимания, прикованного к моему члену, но вы и на экран поглядывайте тоже."

    # tv-watch-01 + сериал(один из семи, с окончанием 01) + tv-watch-01-lisa,olivia,max-(01/01a)
    scene tv-watch-01
    $ renpy.show('tv serial '+film+'-01', at_list=[tv_screen,])
    $ renpy.show('Olivia night-tv 01-02'+lisa.dress)

    if renpy.random.randint(0, 1):
        #вариант 1
        Olivia_04 "О! Давайте это посмотрим... Жалко, что не на самое начало серии попали, а то как-то совсем уж непонятно, что там происходит."
        Lisa_01 "Непонятно, но лично меня заинтриговало... Мне интересно, что дальше будет."
        Max_04 "{i}( А вот мне нет разницы, что происходит в сериале... Ведь на этом диване есть то, что в сериалах не каждый день увидишь! ){/i}"
    else:
        #вариант 2
        Olivia_04 "Вот, можем этот сериал посмотреть... Вроде, что-то интересное происходит у них там. Надо вникать..."
        Lisa_01 "Тогда смотрим... Может, по ходу просмотра во всём разберёмся."
        Max_04 "{i}( А вот мне куда интереснее то, что происходит на диване... Здесь, рядом со мной, сидят две обалденные девчонки, которые не против моей компании! ){/i}"

    # tv-mass-01 + tv-watch-04-lisa,olivia,max-(01/01a)
    scene BG tv-mass-01
    $ renpy.show('Olivia night-tv 04-01'+lisa.dress)

    if renpy.random.randint(0, 1):
        #вариант 1
        Olivia_02 "Здорово, что можно просто вот так, побездельничать в пустом и шикарном доме... Да ещё и с такими классными ребятами, как вы!"
        Lisa_03 "Ага. Особенно здорово Максу. Мальчики, наверно, только о таком и мечтают?!"
    else:
        #вариант 2
        Olivia_02 "А хорошо закрутили, совсем у них дела плохи... Я аж на месте не могу усидеть. Хочется раскинуться на диване, но для вас это будет слишком откровенно."
        Lisa_03 "Мне и самой хочется... Особенно здорово будет Максу, он ведь наверняка о таком и мечтает сейчас!"
    Max_02 "Не только о таком. Но и то, что сейчас - тоже круто!"

    # tv-mass-03 + tv-watch-05-lisa,olivia,max-(01/01a)
    scene BG tv-mass-03
    $ renpy.show('Olivia night-tv 05-01'+lisa.dress)

    Olivia_01 "Тебе повезло с братом, Лиза. Мальчишки думают только об одном, но такими уж их сделала природа. И Макс не исключение, но он хотя бы внимателен к нам."
    Lisa_02 "Макс очень внимательный, когда хочет за кем-нибудь подсмотреть!"
    Max_01 "Я внимательный всегда."

    # tv-watch-01 + сериал(котороый выпал до этого, с окончанием 02) + tv-watch-01-lisa,olivia,max-(01/01a)
    scene tv-watch-01
    $ renpy.show('tv serial '+film+'-02', at_list=[tv_screen,])
    $ renpy.show('Olivia night-tv 01-02'+lisa.dress)
    Olivia_03 "Ну и как думаешь, Макс... Правильно герои сериала делают или нет?"
    Max_03 "Так или иначе - да. Ведь впереди ещё много сезонов..."
    Lisa_09 "Эй, ты испортил всю интригу! Как мы теперь дальше будем смотреть, зная, что у них всё получится?"

    # tv-kiss-03 + tv-watch-06-lisa&olivia-(01(a)/02(a)) + tv-watch-06-max-01
    scene BG tv-kiss-03
    $ renpy.show('Olivia night-tv 06-0'+str(renpy.random.randint(1, 2))+lisa.dress)
    show Max night-tv 06-01
    Max_07 "Так не всем же может повезти! Кто-нибудь да огребёт... возможно..."
    Olivia_04 "Твоя правда. Ладно, тихо... Мы смотреть будем или обсуждать?"
    Lisa_01 "Конечно, смотреть! Обсудить и потом можно... Если Макс опять о чём-нибудь не проболтается."

    # tv-watch-01 + сериал(котороый выпал до этого, с окончанием 03) + tv-watch-01-lisa,olivia,max-(01/01a)
    scene tv-watch-01
    $ renpy.show('tv serial '+film+'-03', at_list=[tv_screen,])
    $ renpy.show('Olivia night-tv 01-02'+lisa.dress)
    Olivia_06 "Вот и серия заканчивается. Вы как, спать хотите? Я вот уже зеваю, но оно и понятно, ночь на дворе..."
    menu:
        Lisa_05 "Ага, давайте пойдём по кроваткам, пока здесь не заснули."
        "{i}идти в свою комнату{/i}":
            pass
    # myroom-night-talk-01 + myroom-night-talk-01-lisa-(02a/02b) + myroom-night-talk-01-olivia-01
    scene BG myroom-night-talk-01
    $ renpy.show('Lisa myroom-night-talk 02'+lisa.dress)
    show Olivia myroom-night-talk 01
    with Fade(0.4, 0, 0.3)
    Max_04 "Если вдруг вам надоест спать вместе, я всегда рад приютить любую из вас на своей кровати."
    Olivia_03 "Спасибо, Макс! Трусы хоть одень, чтобы было не так заметно, насколько ты рад этим фантазиям."
    Lisa_02 "И с чего ты взял, что нам надоест?"
    Max_02 "Ну мало ли."
    Olivia_01 "Всем спокойной ночи..."
    Max_01 "Приятных снов."

    if lisa.dress > 'b':    # возвращаем маечку
        $ lisa.dress = 'b'

    $ renpy.end_replay()
    $ poss['Schoolmate'].open(13)
    $ spent_time = TimeDifference(tm, '02:00')
    stop music
    jump Waiting
