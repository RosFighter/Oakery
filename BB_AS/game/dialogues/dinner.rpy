
label after_dinner:
    $ dishes_washed = False  # посуда грязная, кто-то должен ее помыть
    $ spent_time = 60
    $ current_room = house[5]
    # $ current_room.cur_bg = "location house terrace dinner-b"

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
            "Ага, а подружку зовут Алекс..." if talk_var["boy"] > 0:
                $ talk_var["boy"] = 3
                menu:
                    Lisa_12 "Макс! Я же тебе по секрету рассказала..."
                    "Ой, извини. Я думал, у нас нет секретов...":
                        pass
                    "А ты не сказала, что это секрет...":
                        pass
                Lisa_00 "Не удивляйся потом, если твои секреты тоже окажутся... не секретами."
                Ann_07 "Лиза, так что там за подружка по имени Алекс?"
                jump .secret
            "Что за подружка?" if talk_var["boy"] == 0:
                $ talk_var["boy"] = 4
            "Что за подружка? {i}(подмигнуть){/i}" if talk_var["boy"] > 0:
                $ talk_var["boy"] = 5
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
            if talk_var["blog"] < 2:
                jump .help
    menu .plan:
        Alice_13 "Когда придумаю, тогда и поделюсь. Пока я только строю план."
        "Ну как построишь, позови!":
            pass
        "Помощь нужна?":
            if talk_var["blog"] < 2:
                jump .help
    if talk_var["blog"] == 2:
        Alice_00 "Кстати, ты уже предлагал свою помощь, если я не ошибаюсь... Или это было так, не серьёзно всё?"
        Max_09 "А ты и правда прислушаешься к моим советам?"
        Alice_13 "Макс, я готова на любую помощь. У самой уже нет идей, если честно. Так что, да. Прислушаюсь..."# \n\n{color=[lime]}{i}{b}Внимание:{/b} Получена новая \"возможность\"!{/i}{/color}"
        Max_03 "Отлично. Тогда и правда помогу!"
        jump .next
    else:
        menu:
            Alice_07 "Зачем? Чтобы ты в очередной раз посмеялся? И, вообще, если ты такой умный, то вот ты и придумай что-нибудь. Я даже спасибо скажу. Честно говоря, я в депрессии..."# \n\n{color=[lime]}{i}{b}Внимание:{/b} Получена новая \"возможность\"!{/i}{/color}"
            "Даже спасибо? Ну, хорошо...":
                jump .next
            "Ладно...":
                jump .next

    menu .help:
        Alice_07 "Ну если честно, то да. Я думаю, что у меня даже депрессия развивается. Если появятся какие-то мысли, буду рада их услышать. Даже от тебя. А если что-то дельное предложишь, то и спасибо скажу..."# \n\n{color=[lime]}{i}{b}Внимание:{/b} Получена новая \"возможность\"!{/i}{/color}"
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
    Alice_02 "Ага, маленький... Да он был с тебя размером! Ненавижу пауков. Кто их, вообще, выдумал. Хоть на северный полюс уезжай. Надеюсь, хоть там их нет..."# \n\n{color=[lime]}{i}{b}Внимание:{/b} Получена новая \"возможность\"!{/i}{/color}"
    Max_03 "Нам тебя будет нехватать..."
    Alice_01 "А вот знаешь что, Макс, не дождёшься! Я не видела ещё ни одного паука и, может быть, это маме только показалось. Буду думать так. Так спокойнее..."
    Max_01 "Ну, думай..."
    Ann_07 "Так, ладно. Думайте что хотите, а вам всем спасибо за ужин. я пойду немного поваляюсь в ванне..."
    Max_04 "Ага, спасибо."

    jump after_dinner


label dinner_3:
    $ __mood = 0
    Ann_00 "Всем приятного аппетита. Предлагаю поужинать. Есть у кого-то какие-то новости?"
    Max_04 "У нас всё как всегда. У тебя какие новости?"
    menu:
        Ann_05 "Ой, у меня всё замечательно. Сегодня Эрик намекнул, что хочет меня перевести из моего отдела в свои личные ассистенты, представляете?"
        "А это точно хорошо?":
            Alice_13 "Макс, ну вот опять ты в своём репертуаре! Порадуйся за маму. Кроме того, наверняка, это ещё и прибавка к зарплате! Да, мам?"
        "Поздравляю, мам!":
            $ __mood += 50
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
    $ AddRelMood("ann", 0, __mood)
    $ __mood = 0
    menu:
        Lisa_00 "Он не мой. А вообще, всё хорошо. Спасибо, что спросили, но рассказывать нечего..."
        "Давай, рассказывай подробности!":
            $ __mood -= 50
            Lisa_12 "Макс! Завязывай. Давайте сменим тему. Значит, завтра шоппинг... Мам! Я вспомнила. Мне нужен купальник. В этом просто невозможно загорать, а других у меня нет!"
        "Ладно, не будем мучать Лизу вопросами...":
            $ __mood += 50
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
    $ AddRelMood("lisa", 0, __mood)
    jump after_dinner


label dinner_4:
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
            $ possibility["Swimsuit"].stage_number = 2
            $ possibility["Swimsuit"].stages[2].used = True
            $ items["bikini"].InShop = True
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
        Eric_05 "Да не стоит, пустяки. А чтобы ваш семейный бюджет не просел, я сам подарю тебе платье для клуба, какое скажешь. Через неделю."#\n\n<color=lime><i><b>Внимание:</b> Получена новая «возможность»!</i></color>"
        "{i}О нет...{/i}":
            pass
    menu:
        Ann_05 "Эрик, ну не стоит, я и сама могу купить ей платье. Просто, переживаю..."
        "И правильно делаешь!":
            $ __alice -= 50
            $ __ann += 50
        "{i}промолчать{/i}":
            pass
    $ possibility["nightclub"].stage_number = 0
    $ possibility["nightclub"].stages[0].used = True
    $ items["dress"].InShop = True
    $ AddRelMood("alice", 0, __alice)
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
    $ AddRelMood("ann", 0, __ann)

    jump after_dinner


label dinner:
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
    else:
        jump typical_dinner

    jump after_dinner
