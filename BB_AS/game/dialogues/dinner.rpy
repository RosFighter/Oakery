
label after_dinner:
    $ dishes_washed = False  # посуда грязная, кто-то должен ее помыть
    $ spent_time = 60

    if len(punlisa)> 0 and punlisa[0][3] == 1:
        # Лизу наказали
        if all([
                    punlisa[0][0] == 1, len(punlisa) >= 7,
                    poss['sg'].stn == 2,
                    ColumnSum(punlisa, 1, 7) == 2,
                    talk_var['truehelp']>=6
                ]):
            # Макс подставил Лизу, за последние 7 дней это вторая двойка, Макс на "хорошей" ветке и успел 6 раз сделать задания за Лизу
            call conversation_after_dinner(5) from _call_conversation_after_dinner_4
        elif all([
                    punlisa[0][0] == 1,
                    ColumnSum(punlisa, 4) >= 1000,
                    poss['sg'].stn > 2
                ]):
            # если Макс подставил Лизу и её подозрение достигло 100% (1000)
            call conversation_after_dinner(4) from _call_conversation_after_dinner
        elif all([
                    len(punlisa) >= 7,
                    ColumnSum(punlisa, 0, 7) == 0,
                    ('lisa.ad' not in dcv or dcv['lisa.ad'].done)
                ]):
            # если Макс не помогал Лизе семь раз и разговора после ужина не было больше недели
            if talk_var['help.hw'] == 0 and poss['sg'].stn <= 2:
                # совсем не помогал
                call conversation_after_dinner(1) from _call_conversation_after_dinner_1
            elif poss['sg'].stn == 2:
                # безвозмездно помогал, но перестал
                call conversation_after_dinner(2) from _call_conversation_after_dinner_2
            elif poss['sg'].stn > 2:
                # обещал помогать за услуги, но не стал или перестал
                call conversation_after_dinner(3) from _call_conversation_after_dinner_3

    jump Waiting


label typical_dinner:
    menu:
        Ann_00 "Всем приятного аппетита. Сегодня что-то устала. Так что, давайте поужинаем в тишине..."
        "Как скажешь, мам...":
            Ann_05 "Спасибо за понимание, Макс! Ну, приступим..."
            Max_00 "Приятного аппетита!"
        "У тебя всё хорошо?":
            Ann_05 "Да, всё в порядке, Макс. Спасибо, что спросил. Просто за день столько всего, что пора бы уже и отдохнуть..."
            Max_00 "Понятно. Приятного аппетита!"
    jump after_dinner


label dinner_first:
    $ talk_var['dinner'] = 1
    Ann_07 "Рада, что все смогли сегодня собраться. Всем приятного аппетита! Ну, у кого как день прошёл?"
    Alice_00 "Мам, да у нас всё как обычно. Это ты рассказывай, как первый рабочий день?"
    menu:
        Ann_00 "Вы знаете, довольно неплохо. Такой офис! Такие все важные. Но я смогу там работать и даже планирую подняться по карьерной лестнице..."
        "Напомни, а кем ты работаешь?":
            menu:
                Ann_01 "Что, Макс, с памятью проблемы? Может быть, попросить врача выписать тебе витамины? Я работаю в отделе развития, занимаюсь маркетингом."
                "Точно. Ну, поздравляю!":
                    jump .great
                "А с начальником повезло?":
                    jump .boss
        "А где находится твой офис?":
            menu:
                Ann_14 "Вот с этим беда. На общественном транспорте добираться долго. Но думаю, что эта проблема решится..."
                "Поздравляю!":
                    jump .great
                "А с начальником повезло?":
                    jump .boss

    label .great:
        Ann_07 "Спасибо, Макс. Вы всё вопросы задаёте. Поели бы, хоть немного. Кстати, молодец Алиса, что приготовила ужин. Сама я бы ещё долго возилась."
        Alice_07 "Не за что. Ты же сама меня научила всему, вот и пожинай плоды! Слушай, ну а кто у тебя начальник на работе?"

    label .boss:
        menu:
            Ann_14 "Ну мой непосредственный начальник - лысый толстый мужик, которого все ненавидят. Думаю, его скоро сменят. А вот босс моего начальника..."
            "А что с ним?":
                pass
            "Ещё толще и лысее?":
                pass
        menu:
            Ann_01 "Вот он - мужчина что надо! Сразу меня заметил, помог разобраться в делах. И даже до дома подвёз! Может быть, он мне даже личного водителя выделит!"
            "Ого! Да он в тебя влюбился?":
                menu:
                    Ann_00 "Почему сразу влюбился? Может быть, он джентльмен, который помогает новенькой на новом месте работы..."
                    "Да, точно! А может быть, и он тебе нравится?":
                        jump .yeah
                    "И как его зовут?":
                        jump .boss_name
            "И как его зовут?":
                jump .boss_name
            "Мне кажется, это плохая идея":
                menu:
                    Lisa_02 "Макс! Мама давно ни с кем не общалась и если нашла себе босса начальника, то какой от этого может быть вред?"
                    "А вред такой, что если поссорится, её уволят!":
                        Lisa_01 "Мне кажется, что если ссориться со своим боссом, то так и так могут уволить..."
                        Max_00 "Тоже верно..."
                    "Может, ты и права...":
                        pass
        Lisa_03 "Мам, похоже и он тебе нравится, да?"
        jump .yeah

    label .boss_name:
        Ann_07 "Его зовут Эрик. Фамилия вам ничего не даст, так что, это не важно. Может быть, я вас однажды и познакомлю..."
        Max_05 "Значит, он тебе нравится..."

    label .yeah:
        Ann_12 "Я уже сказала, что он симпатичный молодой парень и это нормально... Или не сказала? Не важно. Хватит меня допрашивать, всё остывает!"
        Ann_07 "Сегодня не у меня одной первый день. Лиза тоже пошла в новую школу. Рассказывай, как у тебя всё прошло?"
        Lisa_01 "Ну, школа находится тут совсем рядом, почти за углом. Уроки короткие, занятий мало. Но преподают интересно, гораздо лучше, чем в старой школе. Думаю, здесь даже Максу понравилось бы учиться!"
        Ann_07 "Ну а ученики какие? Повезло с классом? Уже завела себе друзей и подруг?"
        menu:
            Lisa_02 "Да, познакомилась... с одной подружкой. Класс супер, всё хорошо, мам!"
            "Ага, а подружку зовут Алекс..." if talk_var['boy'] > 0:
                $ talk_var['boy'] = 3
                menu:
                    Lisa_12 "Макс! Я же тебе по секрету рассказала..."
                    "Ой, извини. Я думал, у нас нет секретов...":
                        pass
                    "А ты не сказала, что это секрет...":
                        pass
                Lisa_00 "Не удивляйся потом, если твои секреты тоже окажутся... не секретами."
                Ann_07 "Лиза, так что там за подружка по имени Алекс?"
                jump .secret
            "Что за подружка?" if talk_var['boy'] == 0:
                $ talk_var['boy'] = 4
            "Что за подружка? {i}(подмигнуть){/i}" if talk_var['boy'] > 0:
                $ talk_var['boy'] = 5
        Lisa_00 "Ой, да обычная подружка..."
        Alice_06 "Кажется, у кого-то секреты..."
        jump .secret

    label .secret:
        Lisa_09 "Ну что вы, в самом деле. Ну да, с парнем познакомилась. Зовут Алекс. Учимся вместе, сидим рядом!"
        Max_01 "Так бы сразу и сказала!"
        Lisa_09 "А я так и сказала! Всё. Больше ничего не спрашивайте!"
        Ann_00 "Извини, Лиза, я же не знала. Я вот тоже познакомилась с Эриком в первый же день. Не мне тебя судить!"
        Lisa_02 "Да всё в порядке, мам. Просто, мы только познакомились, поболтали и улыбнулись друг другу, а всё выглядит так, как будто у меня уже есть парень..."
        Ann_07 "Тоже верно... Так, ладно. Спасибо всем за ужин. Лиза, сейчас как раз твоя очередь мыть посуду?"
        Lisa_01 "Да, мам. Но если мне кто-то поможет... Например, Макс, то я не откажусь..."
        Max_00 "Может быть..."
        menu:
            Ann_04 "Ладно, разбирайтесь сами. А я собираюсь принять ванну. Так что, не беспокоить!"
            "Хорошо, мам!":
                pass

    jump after_dinner


label dinner_2:
    $ talk_var['dinner'] = 2
    Ann_04 "Всем приятного аппетита. У кого какие новости? Рассказывайте..."
    Max_04 "У меня всё как всегда"
    menu:
        Alice_04 "Ещё бы. Ты же дома всё время сидишь..."
        "А ты прямо уработалась, да?":
            pass
        "А ты чем занимаешься?":
            pass
    Alice_01 "А я своим блогом занимаюсь. Вечерами. Иногда. Когда есть возможность..."
    Max_01 "Всё с тобой ясно..."
    Lisa_01 "Возможность? А что такое?"
    Alice_13 "Лиза, я же тебе говорила, что в тех вещах, что пропали, были все мои кремы, лаки, про которые я и вела свой бьюти-блог..."
    Lisa_09 "Ой, точно. Извини, я совсем забыла про это. Да, сочувствую..."
    menu:
        Ann_01 "Бьюти-блог... Эх, Алиса, лучше бы делом занялась! Тебе поступать пора, а ты воздух пинаешь. Сидела бы и готовилась!"
        "А на что она будет поступать?":
            menu:
                Ann_14 "Ну, я не знаю. Денег лишних у нас нет, но одарённые дети точно могут учиться бесплатно. Им ещё и стипендию доплачивают..."
                "Это кто одарённый? Алиса?":
                    jump .who
                "Ну да, ей уже сейчас должны платить за то, что она такая звезда!":
                    jump .star
                "А при чём тут Алиса?":
                    jump .wtf
        "Да ей лень!":
            Alice_01 "И ничего мне не лень. Просто, у нас денег нет для того, чтобы поступать..."
            menu:
                Ann_00 "Ну ты знаешь, иногда можно поступить и без денег, было бы желание. Одарённым детям ещё и стипендию доплачивают..."
                "Это кто одарённый? Алиса?":
                    jump .who
                "Ну да, ей уже сейчас должны платить за то, что она такая звезда!":
                    jump .star
                "А при чём тут Алиса?":
                    jump .wtf

    menu .who:
        Alice_01 "Да уж одарённее некоторых... У меня хотя бы блог есть. Кстати, на блогах можно заработать больше, чем на работе после нескольких лет учёбы!"
        "Так чего жы ты такая бедная?":
            jump .poor
        "И какой план?":
            jump .plan
    menu .star:
        Alice_04 "Да, звезда. И я бы не отказалась от лишних денег. А если серьёзно, то на блогах можно заработать больше, чем на работе после нескольких лет учёбы!"
        "Так чего жы ты такая бедная?":
            jump .poor
        "И какой план?":
            jump .plan
    menu .wtf:
        Alice_01 "Очень смешно, Макс. А если серьёзно, то на блогах можно заработать больше, чем на работе после нескольких лет учёбы!"
        "Так чего жы ты такая бедная?":
            jump .poor
        "И какой план?":
            jump .plan

    menu .poor:
        Alice_13 "Для тупых повторяю - у меня всё украли! Так что меня не трогать, я думаю и строю план!"
        "Ну как построишь, позови!":
            pass
        "Помощь нужна?":
            pass
    if talk_var['blog'] < 2:
        jump .help
    else:
        jump .blog2

    menu .plan:
        Alice_13 "Когда придумаю, тогда и поделюсь. Пока я только строю план."
        "Ну как построишь, позови!":
            pass
        "Помощь нужна?":
            if talk_var['blog'] < 2:
                $ poss['blog'].OpenStage(0)
                jump .help

    label .blog2:
        if talk_var['blog'] == 2:
            Alice_00 "Кстати, ты уже предлагал свою помощь, если я не ошибаюсь... Или это было так, не серьёзно всё?"
            Max_09 "А ты и правда прислушаешься к моим советам?"
            Alice_13 "Макс, я готова на любую помощь. У самой уже нет идей, если честно. Так что, да. Прислушаюсь..."
            $ poss['blog'].OpenStage(0)
            Max_03 "Отлично. Тогда и правда помогу!"
            jump .next
        else:
            $ poss['blog'].OpenStage(0)
            menu:
                Alice_07 "Зачем? Чтобы ты в очередной раз посмеялся? И, вообще, если ты такой умный, то вот ты и придумай что-нибудь. Я даже спасибо скажу. Честно говоря, я в депрессии..."
                "Даже спасибо? Ну, хорошо...":
                    jump .next
                "Ладно...":
                    jump .next

    menu .help:
        Alice_07 "Ну если честно, то да. Я думаю, что у меня даже депрессия развивается. Если появятся какие-то мысли, буду рада их услышать. Даже от тебя. А если что-то дельное предложишь, то и спасибо скажу..."
        "Спасибо? Мне? От тебя?!":
            pass
        "Ладно...":
            pass

    label .next:
        Ann_01 "Ох, детишки. Не понимаю я ничего в этих ваших блогах и не уверена, что на это надо тратить своё время, но разберётесь. Я хотела спросить, ни к кому в комнату никакие насекомые не заползали?"
        Max_09 "Нет вроде, а что?"
        Ann_00 "Да я сегодня огромного паука видела... Даже не знала, что такие бывают..."
        menu:
            Alice_14 "Что?! Здесь есть пауки?! Мама... я поехала обратно..."
            "Ты что, пауков боишься?":
                pass
            "Да они же безобидные, наверное...":
                pass
        Lisa_02 "Макс, ты что, забыл? В прошлом году маленький паучок летом на Алису заполз, так она орала два часа! Бегала и кричала..."
        Max_02 "Что-то такое было, вроде бы..."
        Alice_02 "Ага, маленький... Да он был с тебя размером! Ненавижу пауков. Кто их, вообще, выдумал. Хоть на северный полюс уезжай. Надеюсь, хоть там их нет..."
        $ poss['spider'].OpenStage(0)
        Max_03 "Нам тебя будет нехватать..."
        Alice_01 "А вот знаешь что, Макс, не дождёшься! Я не видела ещё ни одного паука и, может быть, это маме только показалось. Буду думать так. Так спокойнее..."
        Max_01 "Ну, думай..."
        Ann_07 "Так, ладно. Думайте что хотите, а вам всем спасибо за ужин. я пойду немного поваляюсь в ванне..."
        Max_04 "Ага, спасибо."

    jump after_dinner


label dinner_3:
    $ talk_var['dinner'] = 3
    $ __mmood = 0
    $ __lmood = 0
    Ann_00 "Всем приятного аппетита. Предлагаю поужинать. Есть у кого-то какие-то новости?"
    Max_04 "У нас всё как всегда. У тебя какие новости?"
    menu:
        Ann_05 "Ой, у меня всё замечательно. Сегодня Эрик намекнул, что хочет меня перевести из моего отдела в свои личные ассистенты, представляете?"
        "А это точно хорошо?":
            Alice_13 "Макс, ну вот опять ты в своём репертуаре! Порадуйся за маму. Кроме того, наверняка, это ещё и прибавка к зарплате! Да, мам?"
        "Поздравляю, мам!":
            $ __mmood += 50
            Alice_07 "Ух-ты! Это же здорово! Наверняка, тебе и зарплату повысят и теперь не придётся беспокоиться о доме. Да, мам?"
    Ann_05 "Всё правильно, Алиса! У меня зарплата теперь будет даже больше, чем у текущего начальника. Того, лысого, о котором говорила..."
    Max_00 "И что будет входить в твои обязанности?"
    menu:
        Ann_14 "Ну, я пока точно не знаю. Видимо, помогать с бумагами, может быть что-то ещё. Как дело дойдёт до повышения, я ознакомлюсь с должностными обязанностями, конечно..."
        "И теперь ты будешь ещё больше от него зависеть...":
            pass
        "А если поссоришься с этим Эриком, то всё...":
            pass
    Ann_01 "Макс. Все подчинённые зависят от своего руководства, так или иначе. Это вполне нормально. Но на этой должности я буду ближе к самой верхушке и смогу многому научиться..."
    Max_09 "Ну да, в этом что-то есть..."
    Ann_00 "Спасибо, Макс, что ты меня понимаешь. Давайте сменим тему. Лиза, как у тебя в школе дела, как там твой Алекс поживает?"
    menu:
        Lisa_00 "Он не мой. А вообще, всё хорошо. Спасибо, что спросили, но рассказывать нечего..."
        "Давай, рассказывай подробности!":
            $ __lmood -= 50
            Lisa_12 "Макс! Завязывай. Давайте сменим тему. Значит, завтра шоппинг... Мам! Я вспомнила. Мне нужен купальник. В этом просто невозможно загорать, а других у меня нет!"
        "Ладно, не будем мучать Лизу вопросами...":
            $ __lmood += 50
            Lisa_02 "Спасибо, Макс. Давайте сменим тему. Значит, завтра шоппинг... Мам! Я вспомнила. Мне нужен купальник. В этом просто невозможно загорать, а других у меня нет!"
    Ann_01 "Ну вот, и тебе что-то нужно. Да, это повышение точно будет полезно для всех нас. Ну раз нужен купальник, то посмотрим. Обещать ничего не буду, но..."
    Alice_13 "Ага, Лизе купальник посмотрим, а мне платье для клуба, значит, нет? Я бы сегодня уже пошла, а так придётся ждать следующей пятницы... И то если купим..."
    Ann_00 "Алиса, я тебе уже говорила, что идея с коротким платьем для клубов мне не нравится. Но если будут деньги и попадётся приличное, то, возможно, купим..."
    menu:
        Alice_00 "Хорошо, мам. Но я на тебя надеюсь. Я просто сойду с ума, если никуда не буду выбираться, даже из такого... дома. Мне нужны друзья и подруги, а они любят клубы..."
        "Бери меня с собой!":
            pass
        "Я тоже люблю клубы!":
            pass
    Alice_02 "Очень смешно, Макс! Во-первых, тебя не пустят. Ростом не вышел. А во-вторых, с тобой я не пойду. Просто потому, что в клубы с братьями не ходят!"
    Max_11 "Ну и ладно!"
    Ann_01 "Вижу, вы уже нашли общий язык? Ладно. Думаю, ужин закончен. Всем спасибо. Лиза, как всегда, моет посуду, а я пойду поваляюсь в ванне."
    Max_01 "Ага, спасибо за ужин."
    $ AddRelMood('ann', 0, __mmood)
    $ AddRelMood('lisa', 0, __lmood)
    jump after_dinner


label dinner_4:
    $ talk_var['dinner'] = 4
    $ __alice = 0
    $ __ann = 0
    Ann_05 "Я рада, что все мы вместе сегодня смогли собраться. Наконец-то, все познакомились с Эриком!"
    Lisa_03 "Да, Эрик классный! Кстати, это он мне и посоветовал тот купальник... Вот только мама не дала его купить..."
    Max_07 "Какой купальник?"
    Lisa_02 "Ну тот, дизайнерский какой-то. Он так хорошо на мне сидел. Эрик сказал, что идеально!"
    Eric_01 "Да, купальник был отличный, но я уважаю решение Ани и понимаю, почему не стали покупать. Ну, нет, так нет..."
    menu:
        Ann_05 "Спасибо, Эрик. Ты такой заботливый и внимательный..."
        "{i}промолчать{/i}":
            pass
        "А меня сейчас стошнит...":
            Ann_13 "Что такое, Макс? Что-то не свежее попалось?"
            Max_14 "Да нет, всё в порядке..."
    menu:
        Lisa_09 "Тем не менее, купальник мне всё ещё нужен. В закрытом я не могу загорать, а очень хочется..."
        "{i}промолчать{/i}":
            pass
        "Да загорай голая!":
            Lisa_13 "Очень смешно, Макс. Загорай сам как хочешь, а мне нужен купальник!"
            Max_09 "Ну, как хочешь. Моё дело предложить решение..."
    menu:
        Eric_05 "Лиза, я тебе обещаю, что если вместе поедем на шоппинг через неделю, я тебе куплю отличный купальник. Конечно, не дизайнерский, но красивый и такой, в котором сможешь загорать! Это будет мой подарок тебе."
        "{i}промолчать{/i}":
            $ poss['Swimsuit'].OpenStage(2)
            $ items['bikini'].InShop = True
    Ann_14 "Эрик, ну не стоит же её так баловать..."
    menu:
        Alice_02 "Если что, то мне тоже ничего не купили..."
        "Попрошайка!":
            $ __alice -= 50
        "{i}промолчать{/i}":
            pass
    Eric_00 "Точно, Алиса. Ты хотела какое-то платье, вроде бы... Верно?"
    menu:
        Ann_01 "По заднице она хотела! Платье ей нужно, чтобы по ночным клубам шастать, задом вилять. Я её хорошо знаю. Поэтому, я и была против..."
        "И правильно!":
            $ __alice -= 50
            $ __ann += 50
        "{i}промолчать{/i}":
            pass
    Eric_05 "Ань, а ты бываешь строгая, как я погляжу... Мне кажется, тебе стоит Алисе разрешить ходить в клубы. К тому же, она почти взрослая..."
    menu:
        Ann_12 "Ну, Эрик, раз ты так считаешь, то конечно. Я и сама в её возрасте немного шалила..."
        "Подробнее, пожалуйста...":
            pass
        "{i}промолчать{/i}":
            pass
    Alice_07 "Эрик! Я тебя обожаю! Тебе удалось переубедить маму! Это невероятно. Спасибо, тебе!!!"
    menu:
        Eric_05 "Да не стоит, пустяки. А чтобы ваш семейный бюджет не просел, я сам подарю тебе платье для клуба, какое скажешь. Через неделю."
        "{i}О нет...{/i}":
            pass
    menu:
        Ann_05 "Эрик, ну не стоит, я и сама могу купить ей платье. Просто, переживаю..."
        "И правильно делаешь!":
            $ __alice -= 50
            $ __ann += 50
        "{i}промолчать{/i}":
            pass
    $ poss['nightclub'].SetStage(0)
    $ items['dress'].InShop = True
    Alice_02 "Спасибо, Эрик! Ты и правда лучший! Буду ждать следующей субботы!"
    menu:
        Ann_00 "Так, ладно. Спасибо всем за ужин. Мы сейчас с Эриком уедем и вернусь завтра утром. Надеюсь, вопросов не возникнет, да? Алиса за старшую, а остальным - не шалите, хорошо?"
        "Повеселитесь там, как следует!":
            Ann_02 "Спасибо, Макс за пожелание, конечно. В общем, ведите себя хорошо тут."
            Max_01 "Конечно!"
        "Хорошо, мам!":
            Ann_05 "Вот и молодцы. Давайте не ругайтесь, не ссорьтесь. Если что - звоните, я сразу приеду..."
            Max_04 "Конечно!"
        "А что вы будете делать?":
            Ann_14 "Макс, твои глупые вопросы меня смущают. В общем, не теряйте, утром вернусь..."
            Max_00 "Ладно, мам..."
    $ AddRelMood('alice', 0, __alice)
    $ AddRelMood('ann', 0, __ann)

    jump after_dinner


label dinner_5:
    Ann_04 "Молодцы, что все собрались. Всем приятного аппетита!"
    Max_01 "Приятного..."
    Lisa_01 "А что, Эрик сегодня не у нас ночует? Ты вроде говорила, что вы часто будете видеться?"
    Max_00 "Куда уж чаще..."
    menu:
        Ann_00 "Нет, Лиза, хорошего помаленьку... Эрик приедет завтра вечером на ужин и останется у нас с ночевой..."
        "И чем будете заниматься?":
            Ann_14 "Макс, ну что за вопросы. Ты же не маленький, вроде бы. Должен всё понимать..."
            Max_00 "Да я шучу..."
            Alice_02 "Да уж, Макс. Шуточки у тебя просто \"отличные\"! А мне вот Эрик понравился. Солидный, умный, ответственный мужчина. Маме именно такой и нужен, мне кажется..."
        "Отлично!":
            menu:
                Ann_06 "Ого. Значит, тебе понравился Эрик? Я рада..."
                "Почему понравился? Нормальный мужик...":
                    $ talk_var['empathic'] += 1
                    Alice_07 "Ну вот, мы же тебе говорили, что он нормальный, а ты всё ворчал. Вот увидишь, маме именно он и нужен был всё это время!"
                "Эрик? Понравился?! Нет, просто рад, что ты дома будешь...":
                    Alice_05 "Макс, а ты всё ещё придурок... Эрик отлично подходит маме! Он сильный, умный, ответственный, солидный такой и при деньгах. Маме именно такой и нужен!"
        "Зачем он тут нужен?":
            menu:
                Ann_01 "Ясно. Ты его всё ещё недолюбливаешь, да?"
                "А за что его любить?":
                    Alice_06 "А тебя за что любить? За то что ты такой... Макс? Я даже не знаю... Этой семье нужен мужчина. А Эрик - он сильный, красивый, умный... Как раз то, что нужно маме!"
                "Да козёл он!":
                    Alice_05 "Ого! Макс выразил своё авторитетное мнение? Абалдеть! Как был придурком, так и остался. Этой семье нужен сильный мужчина. Эрик именно такой. А ещё он умный и симпатичный. Думаю, маме давно именно его и не хватало..."

    Ann_07 "Спасибо, Алиса, что ты так обо мне заботишься. Да, я тоже думаю, что именно Эрика я и ждала всё это время. Честно говоря, не ожидала даже, что такие мужчины бывают... Но давайте сменим тему. Лизе завтра в школу. Ты готова?"
    Lisa_01 "Ну, ещё нужно сделать кое-что и да, буду готова. Не переживай, мам..."
    Ann_01 "Ну не знаю, Лиза. Я всегда преживаю. К тому же, требования в этой школе намного выше, чем в прошлой. Но это не даёт тебе права учиться плохо. Ты меня поняла?"
    Lisa_00 "Да, мам... Я постараюсь. Сделаю всё, что смогу..."
    Max_04 "А я, если что, помогу..."
    Ann_05 "Вот и молодцы вы у меня! Ладно, всем большое спасибо за ужин. Было приятно с вами поболтать. А сейчас меня ждёт, как всегда, ванна..."
    Max_01 "Ага, всем спасибо..."

    $ talk_var['dinner'] = 5
    jump after_dinner


label dinner_6:
    menu:
        Ann_04 "Всем добрый вечер и приятного аппетита! Эрик, мы очень рады, что ты смог сегодня к нам присоединиться!"
        "Ну, кто рад, а кто...":
            $ talk_var['empathic'] -= 2
            menu:
                Eric_02 "Макс, у нас с тобой какие-то проблемы? Может быть, расскажешь, чем я тебе не нравлюсь?"
                "Да всё нормально...":
                    Ann_01 "Макс, я тебя не так воспитывала. Будь чуточку дружелюбнее, пожалуйста..."
                    Max_00 "Ладно, мам..."
                "Вы слишком торопитесь.":
                    Ann_05 "Вот в чём дело! Да, я тебя понимаю, Макс. Но ты не переживай и лучше порадуйся за меня. Я очень рада, что встретила Эрика, настоящего мужчину и очень хотела бы, чтобы вы его приняли в семью..."
                    Max_00 "Хорошо, мам..."
                "Просто не нравишься!":
                    Ann_00 "Макс! Ты стал вести себя слишком агрессивно. Возможно, это гормоны, а может быть, ты почувствовал какую-то для себя угрозу со стороны Эрика. Но уверяю тебя, не стоит. Эрик очень хороший, ты сам это поймёшь!"
                    Max_00 "Как скажешь, мам..."
        "{i}промолчать{/i}":
            menu:
                Eric_02 "Макс, мне показалось, или я тебе не очень нравлюсь?"
                "Тебе показалось...":
                    Ann_01 "Вот видишь, Эрик, а ты переживал. Макс просто не сразу принимает новых людей, но как видишь, это не проблема. Да, Макс?"
                    Max_00 "Да, мам..."
                "Вы слишком торопитесь.":
                    Ann_05 "Вот в чём дело! Да, я тебя понимаю, Макс. Но ты не переживай и лучше порадуйся за меня. Я очень рада, что встретила Эрика, настоящего мужчину и очень хотела бы, чтобы вы его приняли в семью..."
                    Max_00 "Хорошо, мам..."
                "Просто не нравишься!":
                    Ann_00 "Макс! Ты стал вести себя слишком агрессивно. Возможно, это гормоны, а может быть, ты почувствовал какую-то для себя угрозу со стороны Эрика. Но уверяю тебя, не стоит. Эрик очень хороший, ты сам это поймёшь!"
                    Max_00 "Как скажешь, мам..."
    Ann_07 "Вот и замечательно. Теперь я хотела бы рассказать об одной идее Эрика. Я и сама о подобном задумывалась, но он озвучил мои мысли. Эрик, может быть ты и расскажешь?"
    Max_00 "Какая ещё идея?"
    Eric_05 "Конечно, Макс ещё не совсем мужчина, но он уже в подходящем возрасте для специального подросткового лагеря..."
    Max_09 "Чего чего? Какого ещё лагеря?!"
    Eric_01 "Военного. В этом лагере подготавливают детей твоего возраста к службе в армии. Это не значит, что ты обязан будешь идти служить, но тебя к этом подготовят и ты сам решишь, нравится тебе этот путь или нет..."
    Max_08 "Стоп. А если я уже знаю, что не хочу?"
    Eric_05 "Как ты можешь это знать заранее? Ты же не пробовал! Там готовят настоящих будущих мужчин. Дисциплина, физическая подготовка, субординация. Знакомые слова?"
    Max_09 "Нет, но они мне не нравятся!"
    Eric_02 "А зря. Хотя ваша мама и воспитала вас очень хорошо, ну некоторых точно. Но она воспитывала одна, а для того, чтобы мальчик стал настоящим мужчиной, нужно строгое, мужское воспитание. Вот в этом лагере его можно получить."
    Max_15 "Что-то хрень какая-то, эта ваша идея..."
    Ann_01 "Макс, что за слова! Ты всем своим видом доказываешь, что Эрик был прав. Тебе и правда не помешает набраться немного дисциплины. Конечно, я бы не хотела, чтобы ты пошёл в армию, но как минимум пусть тебе дадут все необходимые навыки и знания..."
    Max_08 "Я против."
    Eric_01 "Ну, как я и ожидал... И как же ты станешь настоящим мужчиной? Драться ты не умеешь, наверняка. Физическая подготовка? Ты зарядку хотя бы делаешь? Про дисциплину, вообще, молчу..."
    Max_16 "Я уже мужик!"
    Eric_05 "О да. Ну, посмотрим. Я ещё всё выясню про этот лагерь, когда у них ближайший набор, а в твоих силах пока есть время, доказать поступками, что ты уже мужик и не нуждаешься в этом лагере. Всё в твоих руках..."
    Max_09 "И кто будет решать - в лагерь меня или пока не надо?"
    Ann_01 "Решать буду я. Не могу сказать, что у меня есть серьёзные претензии к твоему поведению в данный момент, но иногда ты перегибаешь палку. Так что, я дам тебе время себя проявить. Если не будешь испытывать моего терпения, то повременим с этим лагерем. Ну а если я пойму, что пора, то уж извини..."
    Max_14 "Я понял. Буду вести тебя хорошо..."
    menu:
        Ann_04 "Вот и молодец, Макс. А тебе, Эрик, спасибо за этот совет. Теперь хотя бы будет какой-то способ воздействовать. А то порка не даёт того эффекта, на который я привыкла рассчитывать..."
        "{i}промолчать{/i}":
            pass
    Eric_09 "Да? Странно. Обычно она всегда помогает. Хотя, мне кажется, что ты делаешь это не так. Вот скажи, ты же стараешься просто шлёпать как можно сильнее, думая, что это всё что требуется, верно?"
    Max_07 "Может, сменим тему? Мне эта что-то не нравится..."
    Ann_14 "Ну, да... Потом вся ладошка болит... А разве я делаю это не так? Или в чём хитрость?"
    Max_09 "Определённо, мне это всё не нравится..."
    Eric_02 "Гораздо больший эффект оказывает окружение и условия, при которых происходит наказание. Я тебе потом обо всём подробно расскажу. Думаю, пока дети не готовы об этом услышать, тем более вот так за ужином..."
    Max_08 "Точно, это всё дурно пахнет..."
    Ann_05 "Хорошо, Эрик. Будет очень интересно узнать о правильной методике наказания. Ты такой умный, всё по полочкам раскладываешь... И где ты был всю мою жизнь..."
    Max_00 "Да завязывайте, уже!"
    Ann_01 "Вот Макс в очередной раз доказал, что моё воспитание недостаточно строгое... Ладно. Вижу, все уже закончили ужин. Всем больше спасибо, я пойду приму душ или, может быть, ванну..."
    Max_00 "Спасибо за ужин..."
    $ talk_var['dinner'] = 6
    jump after_dinner


label dinner_11:
    Ann_04 "Всем добрый вечер и приятного аппетита! Сегодня мы с Эриком снова уедем, вернусь завтра. Но вы уже привыкли к этому, правда?"
    Alice_03 "Конечно, езжайте, развеятесь хоть..."
    Max_01 "Это ты так рада из-за платья?"
    Alice_02 "Макс! Из-за платья я в восторге! Да и за маму рада, что отдохнут от работы..."
    Lisa_02 "А ты сразу в клуб, да?"
    Max_04 "Вот-вот..."
    Ann_01 "Алиса, это правда? Ты сегодня в клуб собралась?"
    Alice_02 "Мам, нет конечно. Я в пятницу вечером с подругой пойду. Могла бы и сегодня, раз есть теперь в чём идти, но..."
    Ann_04 "Лучше бы делом занялась. На курсы подготовительные пошла бы, может быть, и поступить смогла бы куда-то..."
    Eric_02 "А что, Алиса, отличная идея. Если проблема с деньгами какая-то, то это не проблема, я помогу и даже организую всё..."
    Ann_05 "Эрик, ну что ты! Мы сами справимся. Особенно, когда ты меня так... повысил. К тому же, пусть своим умом поступает, а не нашими кошельками..."
    Lisa_01 "А у тебя, Эрик, есть высшее образование?"
    menu:
        Eric_05 "Лиза, что за глупый вопрос. Конечно! В нашем мире без этого ни за что не удалось бы занять такую высокую должность в компании. Да и в жизни без образования пробиваются только единицы..."
        "{i}промолчать{/i}":
            pass
        "Может быть, я такой...":
            pass
    menu:
        Ann_01 "Да, Эрик полностью прав. А ты, Макс, даже школу бросил. Прежде, чем думать о высшем образовании, неплохо было бы закончить среднее. Как считаешь?"
        "Сдалось оно мне...":
            Eric_01 "Ну, тогда у тебя одна дорога. В тот самый военный лагерь. Ну или какой-то другой. И это хорошо. Тебя подготовят, натренируют, научат дисциплине и субординации. Станешь настоящим мужиком!"
        "Я подумаю...":
            Eric_03 "Ты знаешь, думать нужно быстрее. Потому-что выбор у тебя либо школа, либо военный лагерь, а потом и армия... Я бы выбрал армию на твоём месте, но с твоими физическими данными..."
            Max_09 "А что с моими данными?"
            Eric_01 "Ну, они не очень. Хотя, тебя подготовят, натренеруют. А главное - научат дисциплине и субординации. Мама за тебя порадуется, когда увидит, что мужиком стал!"
    Max_15 "Да я уже мужик!"
    Eric_09 "Ну ладно, думай так... Заблуждаться никто не мешает..."
    Max_16 "Знаешь, что?"
    Ann_19 "Макс! Что за тон? Уважительно разговаривай с Эриком! А не то накажу. В общем, мы сейчас поехали, а вы приберитесь тут. Завтра я вернусь. Всем спасибо за ужин!"
    Max_00 "Да, спасибо..."
    ## теперь Алиса посещает ночной клуб по пятницам
    call alice_init_nightclub from _call_alice_init_nightclub

    ## после ужина должен состоятся разговор Макса с Эриком на счет решения Макса
    $ EventsByTime['Eric_afterdinner'].variable = "talk_var['dinner']==11"
    $ talk_var['dinner'] = 11
    jump after_dinner


label dinner_12:
    Ann_04 "Всем приятного аппетита!"
    Max_01 "Приятного аппетита..."
    menu:
        Ann_07 "У меня для вас отличная новость! Это связано с кем-то, кого вы очень любите..."
        "Ты беременна?":
            Ann_01 "Макс! Не неси ерунду. Как тебе такое в голову могло прийти только..."
            Max_00 "Ну, значит, точно про Эрика..."
        "Опять про Эрика?":
            Ann_05 "Нет, в этот раз речь не о нём. Ну, ещё варианты есть? Лиза? Алиса?"
            Max_00 "Ну, у меня есть один вариант..."
        "Не знаю даже...":
            Ann_01 "Макс, ну ты даёшь. Лиза, Алиса, может быть вы догадались о ком речь?"
            Max_00 "Ну, у меня есть один вариант..."
    menu:
        Ann_04 "Ну что же вы. К нам едет ваша тётя в гости!"
        "Я так и знал!":
            pass
        "Тётя Кира?":
            pass
    Lisa_03 "Да ладно?! А на долго? Просто в гости или по делам? Мам, ну расскажи!"
    Max_01 "Ого, сколько вопросов..."
    menu:
        Ann_05 "Лиза, я знаю, что ты очень её любишь, как и все мы, но успокойся. Она не завтра приедет, но скоро. На сколько - тоже не знаю, но думаю, что погостит какое-то время... А по делам или нет - сама спросишь."
        "Первая хорошая новость...":
            pass
        "{i}промолчать{/i}":
            pass
    Alice_07 "Да, это здорово. Я так соскучилась по тёте Кире... Кстати, она говорила, что сменила работу, но мне не сказала на какую. Ты не в курсе, мам?"
    menu:
        Ann_12 "Нет, мне она тоже ничего не сказала. Но ты же знаешь, что у неё шило в заднице. Кажется, она ни на одной работе не продержалась дольше полугода. Наверняка, опять связалась с чем-то незаконным..."
        "Почему ты так говоришь?":
            menu:
                Ann_01 "Ты что, забыл ту историю, когда мы её забирали из полиции? Или когда она в новости попала в... хм... таком виде. Хотя, вам это знать не обязательно..."
                "В каком виде?!":
                    Alice_07 "В каком, в каком... В голом, конечно! Если бы наш провайдер не блокировал всё подряд, я бы показала то видео..."
                    Max_05 "Есть видео?!"
                    Ann_01 "Макс! Ну что за вопросы. Всё, проехали. В общем, скоро тётя Кира нас навестит. Хотя проблемы неизбежны, но точно не соскучитесь!"
                    Max_04 "Отлично!"
                "Её арестовывали?":
                    Lisa_01 "Тётя Кира же рассказывала, Макс! Она любит эту историю, правда, каждый раз рассказывает её по-новому. Вот спросишь у неё и узнаешь новую версию!"
                    Max_02 "Ага, спрошу..."
        "А на кого она училась?":
            menu:
                Ann_01 "На искательницу приключений на свою задницу. Она училась на юриста, но бросила первый курс и решила, что хочет стать журналистом. Поступила снова, но и там ей быстро всё наскучило..."
                "Я не в курсе этой истории":
                    Ann_04 "Ну и очень хорошо. Это плохой пример для подражания. За что Кира не берётся, всё у неё получается... особым образом. И когда за ум только возьмётся..."
                    Max_03 "Понятно..."
                "Понятно...":
                    pass
            Ann_05 "В общем, к нам едет генератор проблем, зато точно не соскучитесь!"
            Max_05 "Супер!"
    Ann_02 "Да, она сказала, что приедет в ближайшие выходные, если решит какие-то очередные свои проблемы. Так что, ничего не планируйте. Да, спасибо всем за ужин. Хорошо поболтали."
    Max_01 "Да, всем спасибо!"
    $ talk_var['dinner'] = 12
    jump after_dinner


label dinner_17:
    Ann_04 "Всем приятного аппетита!"
    Max_01 "Приятного!"
    menu:
        Ann_07 "Ну что, все помнят какой завтра день?"
        "День шоппинга?":
            Ann_05 "Верно, Макс, но это не самое главное. Напоминаю, что завтра утром приедет ваша тётя Кира!"
            Max_04 "А как же шоппинг?"
            jump .shop
        "Тётя Кира приезжает?":
            menu:
                Ann_05 "Именно! Она звонила и сказала, что приедет рано утром. Так что, ложитесь пораньше сегодня. Я сейчас к Эрику, но до приезда Киры вернусь."
                "А без Эрика сегодня никак?":
                    Ann_01 "Макс. Я же сказала, что успею до приезда Киры. Вы тут и без меня справитесь, верно?"
                    Max_00 "Верно, верно. А где тётя Кира будет спать?"
                    jump .sleep
                "А как же шоппинг?":
                    jump .shop
    label .shop:
        Alice_01 "Макс! Да сдался тебе этот шоппинг. Это же наша тётя Кира!"
        Max_01 "Да я просто спросил..."
        Ann_07 "А шоппинг и не отменяется. Эрик заедет за нами как обычно, часов в 10. Может быть, и Киру с собой возьмём, если она согласится."
        Max_00 "А где она будет спать?"
        jump .sleep

    menu .sleep:
        Ann_00 "Ой. Хороший вопрос, Макс. Я как-то об этом не подумала. Может быть, она поспит на твоей кровати с Лизой в комнате, а ты в гостиной как-нибудь?"
        "Ну, я не против":
            Ann_07 "Вот и хорошо. А вообще, спросим у неё, как ей комфортнее. Ладно, это всё мелочи. Всем спасибо за ужин. Я побежала, Эрик прислал за мной машину. Вернусь утром."
        "Может быть, наоборот?":
            Ann_07 "Может быть и наоборот. Спросим у неё, как ей комфортнее. Ладно, это всё мелочи. Всем спасибо за ужин. Я побежала, Эрик прислал за мной машину. Вернусь утром."
    Max_01 "Хорошо..."
    $ talk_var['dinner'] = 17
    jump after_dinner


label dinner:
    $ current_room = house[5]
    $ Distribution()
    if poss['smoke'].stn == 0:
        jump talk_about_smoking

    jump StartPunishment


label dinner_after_punishment:
    $ renpy.block_rollback()

    $ seat_Dinner()

    if day == 1:
        jump dinner_first
    elif day == 2:
        jump dinner_2
    elif day == 3:
        jump dinner_3
    elif day == 4: # первый ужин с Эриком
        jump dinner_4
    elif all([day>=5, GetWeekday(day)==0, talk_var['dinner']==4]):
        jump dinner_5
    elif all([day>=6, GetWeekday(day)==1, talk_var['breakfast']==5, talk_var['dinner']==5]):
        jump dinner_6
    elif all([day>=11, GetWeekday(day)==6, talk_var['breakfast']==7, talk_var['dinner']==6]):
        jump dinner_11
    elif all([day>=12, GetWeekday(day)==0, talk_var['dinner']==11, talk_var['breakfast']==12]):
        jump dinner_12
    elif all([day>=17, GetWeekday(day)==5, talk_var['breakfast']==12, talk_var['dinner']==12]):
        jump dinner_17
    else:
        jump typical_dinner

    jump after_dinner
