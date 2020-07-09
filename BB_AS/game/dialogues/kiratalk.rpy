
label KiraTalkStart:

    $ dial = TalkMenuItems()

    # $ __cur_plan = GetPlan(plan_ann, day, tm)
    $ __cur_plan = kira.get_plan()
    if __cur_plan.talklabel is not None:
        call expression __cur_plan.talklabel from _call_expression_10

    if len(dial) > 0:
        $ dial.append((_("{i}Ой, в другой раз...{/i}"), "exit"))
    else:
        jump Waiting

    $ renpy.block_rollback()
    Max_01 "Не против компании?"
    Kira_01 "Конечно, Макс. Ложись рядом. Погода сегодня отличная!" nointeract
    $ rez =  renpy.display_menu(dial)

    if rez != "exit":
        if renpy.has_label(talks[rez].label): # если такая метка сушествует, запускаем ее
            call expression talks[rez].label from _call_expression_11
        jump KiraTalkStart       # а затем возвращаемся в начало диалога, если в разговоре не указан переход на ожидание

    jump AfterWaiting            # если же выбрано "уйти", уходим в после ожидания


label kira_firsttalk:
    scene BG char Kira sun-talk-01
    show Kira sun-talk 01
    show Max sun-talk 01
    Kira_04 "Ну, рассказывай, Макс, как ты тут живёшь, как твои дела, что нового?"
    Max_04 "Ну, я... э..."
    menu:
        Kira_02 "Макс, тебя смущает мой купальник? Может быть, его снять?"
        "О... Да, было бы супер!":
            menu:
                Kira_07 "Ну да, не сомневаюсь. Только что же с тобой будет? Макс, ты можешь смотреть мне в глаза или мы тебя потеряли?"
                "Извини, тётя Кира...":
                    pass
                "Просто я отвлёкся...":
                    pass
        "Ну, я не знаю...":
            menu:
                Kira_07 "Зато знаю я. Макс, постарайся не пялиться на мою грудь. Глаза чуть выше. Ау. Ты здесь, Макс?"
                "Извини, тётя Кира...":
                    pass
                "Просто я отвлёкся...":
                    pass
    Kira_04 "Да, это моя ошибка, что выбрала такой купальник. Если честно, то я обычно загораю голая, но вы же дети и стоит хоть немного прикрываться. Вот я и прикрылась... Макс!"
    Max_07 "А? Что?"
    show Kira sun-talk 02
    show Max sun-talk 02
    menu:
        Kira_05 "Ого... Да я смотрю твой рост пошёл куда надо! И давно ты такое сокровище скрываешь?"
        "Ну, я не знаю...":
            pass
        "Да я и не скрываю...":
            pass
    ## открытие первого этапа возможности "Любимая тётя"
    menu:
        Kira_06 "Как я вижу, ты весь пошёл в отца... А кое в чём, так особенно..."
        "Что?!":
            Kira_03 "Ой, я конечно про твою... скромность. Да, речь о ней. И, вообще, давай сменим тему!"
        "Откуда ты знаешь, что...":
            Kira_03 "Что я знаю? Ничего. Я так, про твою скромность, конечно... И, вообще, давай сменим тему!"
    Max_08 "Тётя Кира!"
    Kira_04 "А что тётя Кира? Проехали. Кое-кому, так вообще нужно принять душ и расслабиться. Может быть, и мне тоже, но вдвоём не стоит это делать. Так что, иди ты в душ. И включи холодную воду. Очень холодную!"
    Max_00 "Хорошо..."
    scene BG shower-closer
    show Max shower 04
    show FG shower-closer
    menu:
        Max_03 "{i}( Расслабиться в душе? Легко. Особенно, когда рядом такая женщина. Ух! Я и не задумывался о своей тёте в этом плане никогда, но сейчас что-то изменилось... или во мне или в ней... ){/i}"
        "{i}снять напряжение{/i}":
            Max_20 "О, Кира... Ты когда-нибудь станешь моей..."
            show Max shower 05
            Max_07 "Я же не сказал это вслух?"
            $ mgg.cleanness = 100
    $ dcv['kiratalk'].stage += 1
    $ dcv['kiratalk'].set_lost(1)
    $ SetCamsGrow(house[6], 200)
    $ spent_time += 30
    jump Waiting


label kira_talk2:
    scene BG char Kira sun-talk-01
    show Kira sun-talk 01
    show Max sun-talk 01
    menu:
        Kira_02 "В прошлый раз наш разговор не очень удался. Ты был такой возбуждённый... Слушай, Макс, а у тебя есть девушка?"
        "Есть!":
            menu:
                Kira_04 "А она об этом знает?"
                "Конечно!":
                    Kira_08 "Ну ничего себе! А как её зовут?"
                    Max_00 "Это не важно..."
                    Kira_01 "Хорошо... Тогда последний вопрос. Ты её видишь прямо сейчас, она где-то здесь?"
                    Max_08 "Да я её не выдумал! Она не вымышленная девушка!"
                    Kira_07 "Ну тогда я рада за тебя, Макс. И давно вы встречаетесь?"
                    Max_10 "Ну... Э..."
                    Kira_02 "Я так и думала. Ладно, Макс, не стоит переживать по этому поводу. Ты же только приехал в новый город, из дома не выходишь. Ну скажи честно, нет же у тебя никакой девушки?"
                    Max_11 "Ну да, ты права, нет..."
                "Ты права, нет девушки...":
                    pass
        "Нет...":
            pass
    Kira_07 "Ну, это многое объясняет. Возраст такой, гормоны, кругом полуобнажённые девушки и женщины... Наверное, для тебя это каторга? Со мной можешь говорить откровенно. Я никому ни слова!"
    Max_00 "Да, бывает возбуждаюсь..."
    Kira_06 "Это потому-что пялишься не туда, куда надо. В глаза смотри..."
    Max_04 "Да, хорошо... Просто так само получается..."
    menu:
        Kira_05 "Понятно. Ну, старайся держать себя в руках. Хотя, я в прошлый раз видела как ты себя держал. Это не совсем то, что я имею в виду... Я слишком пошлая, да? Мне надо быть тактичнее?"
        "Что ты, всё хорошо!":
            pass
        "Меня всё устраивает...":
            pass
    Kira_04 "Я рада. Обычно я не слежу за языком и он меня в такие места заводит... Но с детьми надо быть... Хотя, ты уже совсем не ребёнок."
    Max_01 "Верно..."
    Kira_01 "Слушай, Макс, а как тебе удаётся с Лизой в одной комнате уживаться? Наверное, тяжело? Она же сверкает своим нижним бельём, да и спите вы рядом."
    Max_02 "Ну, был один инцидент..."
    Kira_02 "Утренний стояк, наверное? И как она отреагировала?"
    Max_03 "Панику подняла, маму позвала!"
    menu:
        Kira_08 "Представляю! Ну, я с Лизой тоже побеседую. Она уже не девочка... хотя, с вашей строгой мамой она о жизни толком ничего и не знает, похоже."
        "Верно...":
            pass
        "И что ты ей скажешь?":
            Kira_03 "Расскажу откуда дети берутся, конечно! Макс, ты такой смешной. У девочек свои секреты, тебе всё знать не обязательно..."
            Max_01 "Я понял..."
    ## У Макса опять стояк
    show Kira sun-talk 02
    show Max sun-talk 02
    menu:
        Kira_07 "Макс... Кажется, тебе снова пора в душ. Может быть, мне как-то прикрываться, когда ты рядом, раз у тебя все мысли где-то в другом месте?"
        "Не надо прикрываться!":
            Kira_04 "Ладно, не буду. Но в душ ты сходи. И обязательно холодный. А ещё лучше ледяной..."
            Max_00 "Хорошо..."
        "Пожалуй, я пойду...":
            pass
    scene BG shower-closer
    show Max shower 04
    show FG shower-closer
    menu:
        Max_20 "{i}( Вроде тётя Кира специально и не провоцирует, но меня к ней так тянет. Её горячее, почти обнажённое тело так и манит... ){/i}"
        "{i}кончить{/i}":
            show Max shower 05
            Max_07 "{i}( О да... Надеюсь, она не поняла, что я сейчас делал, глядя на неё. Хотя, всё она понимает. Да ещё и видела меня, мой... ){/i}"
            $ mgg.cleanness = 100
    $ dcv['kiratalk'].stage += 1
    $ dcv['kiratalk'].set_lost(1)
    $ SetCamsGrow(house[6], 200)
    $ spent_time += 30
    jump Waiting


label kira_talk3:
    scene BG char Kira sun-talk-01
    show Kira sun-talk 01
    show Max sun-talk 01
    menu:
        Kira_05 "Сегодня уже привык к моему купальнику? Или опять только одно на уме?"
        "Сегодня точно всё в порядке!":
            pass
        "Да я не могу ни о чём думать, когда тут такое...":
            Kira_07 "Понимаю, Макс. Ну, тут надо либо смириться, либо избегать. Как я вижу, избегать меня ты не планируешь и я очень рада этому. Но давай сменим тему, вдруг поможет..."
            Max_01 "Давай!"
    Kira_02 "Расскажи тогда, Макс, чем ты занимаешься, пока сидишь дома? Не может быть, чтобы только на порносайтах зависал?"
    Max_08 "У нас не работают порносайты..."
    Kira_14 "Ах вот в чём дело! А я никак не могла понять, что такое с моим телефоном. И почему? Мама установила такие порядки?"
    Max_09 "Ага, на стороне провайдера защита от детей..."
    Kira_04 "Тогда, Макс, я тебе ещё больше сочувствую и теперь лучше тебя понимаю... Может быть, сменим тему?"
    Max_01 "Хорошо..."
    menu:
        Kira_13 "Слушай, Макс, а тебе не показалось, что твоя мама какая-то... странная. Я имею в виду её одержимость Эриком..."
        "Вот именно!":
            menu:
                Kira_14 "Значит, не мне одной это показалось? Ну, в чём дело, рассказывай..."
                "{i}рассказать всю правду про Эрика{/i}":
                    pass
        "Нет, тебе показалось...":
            menu:
                Kira_02 "Макс, если что, я на твоей стороне. Мне можно доверять!"
                "Ну ладно... {i}Рассказать всю правду про Эрика{/i}":
                    pass
    menu:
        Kira_13 "Макс, ты наверное шутишь, да? Не может быть, чтобы всё было вот так. Твоя мама не слепая. Конечно, ею всегда было легко манипулировать, чем я и пользовалась, но такое..."
        "Чем ты пользовалась?":
            Kira_14 "Мне кажется, сейчас речь не об этом. Расскажу как-нибудь в другой раз... Значит, всё что ты рассказал про Эрика... это правда? Прямо не верится..."
            Max_07 "У меня нет причин врать!"
        "Я говорю правду!":
            pass
    Kira_03 "Думаю, мне нужно услышать другую сторону. Пообщаться или с Эриком или с твоей мамой, чтобы выяснить всё ли так. Может быть, ты немного... приукрасил..."
    Max_09 "И ничего я не приукрасил..."
    Kira_04 "Ладно, не дуйся. Давай сменим тему, а ещё лучше полежим на солнышке в тишине, если ты не возражаешь..."
    Max_01 "Ладно, не буду тебе мешать..."

    ## второй этап "Любимой тёти"

    $ dcv['kiratalk'].stage += 1
    $ dcv['kiratalk'].set_lost(1)
    $ SetCamsGrow(house[6], 200)
    $ spent_time += 30
    jump Waiting


label kira_about_kiss:
    $ renpy.block_rollback()
    menu:
        Kira_07 "Вот это подход, я понимаю! Может быть, тебе ещё что-то нужно?"
        "А можно что-то ещё?":
            Kira_08 "Шутник ты, Макс... Постой, ты нашёл себе девушку? Кто она? Откуда? Как познакомились? Как зовут? Хочу всё знать!"
        "Для начала только целоваться!":
            Kira_08 "Для начала? Забавно... Постой, ты нашёл себе девушку? Кто она? Откуда? Как познакомились? Как зовут? Хочу всё знать!"
    Max_01 "Как ты догадалась?"
    menu:
        Kira_05 "Ну зачем ещё парню может это понадобиться, сам подумай... И что, больше не у кого просить помощи, решил ко мне обратиться?"
        "Мама не помогла..." if 'ann' in talk_var['ask.teachkiss']:
            Kira_01 "Даже мама не помогла? Ого! Наверняка, сказала, чтобы ты учился целоваться со своей девушкой?"
            Max_07 "Точно!"
        "Да, Алиса меня отшила..." if 'alice' in talk_var['ask.teachkiss']:
            Kira_01 "Неудивительно. Наверняка, полез целоваться и получил... по... Хотя, нет. Видимо, тебе повезло. Ну я бы не стала к Алисе с такими вопросами обращаться на твоём месте..."
            Max_07 "Да, уже жалею..."
        "Ага...":
            pass
    menu:
        Kira_07 "Ну что же... Думаю, я смогу тебе помочь. Правда, не здесь и не сейчас. Нужна более интимная обстановка. О, я иногда вечерами смотрю телевизор. Если ещё не будешь спать, напомни о своей просьбе..."
        "Договорились!":
            pass
        "Хорошо! А ты только этому учишь?":
            Kira_04 "Макс, тебе стоит быть чуть более... тактичным. В общем, помочь я тебе помогу, только выбери подходящий момент. Договорились?"
            Max_01 "Конечно!"

    $ poss['seduction'].OpenStage(6)
    $ talk_var['ask.teachkiss'].append('kira')
    $ spent_time += 10
    return
