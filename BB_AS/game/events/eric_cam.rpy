
label cam0_eric_ann_sleep:
    if flags.eric_jerk and '02:00'<=tm<'02:30':
        $ renpy.show('Ann cams sleep '+cam_poses_manager(ann, ['01', '02', '03'])+ann.dress, at_list=[laptop_screen])
    else:
        $ renpy.show('Eric cams sleep2 '+cam_poses_manager(eric, ['01', '02', '03']), at_list=[laptop_screen])
    show FG cam-shum-act at laptop_screen

    if all([flags.eric_jerk, '02:00'<=tm<'02:30', not prenoted, not flags.eric_noticed]):
        $ prenoted = 1
        if not eric.stat.mast:
            # 1-ое спаливание Эрика у окна Алисы
            Max_07 "{m}Как же повезло, что у меня такая горячая мама... Стойте-ка, а Эрик где?! Может, пошёл в ванную комнату? Или ещё куда...{/m}"
        else:
            if all([flags.eric_wallet == 2, flags.eric_photo2]):
                Max_07 "{m}Ага! Мама одна... Значит, Эрик почти наверняка сейчас дрочит на Алису. Нужно проверить...{/m}"

                scene BG char Max laptop-night-01t
                $ renpy.show('BG-cam house aliceroom-0 night', at_list=[laptop_screen,])
                $ renpy.show('Alice cams sleep night '+cam_poses_manager(alice, ['01', '02', '03']), at_list=[laptop_screen])
                show Eric cams Alice-room 02 at laptop_screen
                show FG cam-shum-act at laptop_screen
                with dissolve
                pause 1

                jump cam_before_frame_eric

            Max_07 "{m}Как же повезло, что у меня такая горячая мама... А Эрик опять где-то полуночничает...{/m}"

    elif all([flags.eric_jerk, '02:00'<=tm<'02:30', flags.eric_noticed, 'ann_sleep_alone' not in cam_flag]) or not check_is_room('eric', house[2]):
        # Эрик уже замечен или с Кирой в ванной
        $ cam_flag.append('ann_sleep_alone')
        Max_01 "{m}Как же повезло, что у меня такая горячая мама... Выглядит потрясающе, аж глаза отрывать не хочется!{/m}"

    if 'ann_sleep' not in cam_flag and not (flags.eric_jerk and '02:00'<=tm<'02:30'):
        $ cam_flag.append('ann_sleep')
        Max_01 "{m}Мама и Эрик спят совсем голые. Ни стыда, ни совести...{/m}"
    return

label cam0_eric_ann_shower:
    default ann_eric_scene = ''
    if tm[-2:] < '30':
        show FG cam-shum-noact at laptop_screen
        if 'ann_not_shower' not in cam_flag:
            $ cam_flag.append('ann_not_shower')
            if len(house[3].cams)>1:
                Max_09 "{m}Мамы и Эрика не видно через эту камеру... Может посмотреть через другую?{/m}"
            else:
                Max_09 "{m}Мамы и Эрика не видно через эту камеру...{/m}"
    else:
        $ ann.dress_inf = '00a'
        if not ann_eric_scene:
            $ ann_eric_scene = cam_poses_manager(eric, ['01', '02', '03'])
        elif ann_eric_scene in ['01', '02', '03']:
            $ ann_eric_scene = {
                    '01' : cam_poses_manager(eric, ['04', '05', '06']),
                    '02' : cam_poses_manager(eric, ['08', '10']),
                    '03' : cam_poses_manager(eric, ['07', '09', '11']),
                }[ann_eric_scene]

        if tm[-2:] < '50':
            $ renpy.show('Eric cams shower '+ann_eric_scene, at_list=[laptop_screen])
        else:
            if ann_eric_scene in ['01', '02', '03']:
                $ ann_eric_scene = {
                        '01' : cam_poses_manager(eric, ['04', '05', '06'], forced=True),
                        '02' : cam_poses_manager(eric, ['08', '10'], forced=True),
                        '03' : cam_poses_manager(eric, ['07', '09', '11'], forced=True),
                    }[ann_eric_scene]
            $ renpy.show('Eric cams shower '+ann_eric_scene+'a', at_list=[laptop_screen])
        show other cam-shower-water at laptop_screen
        show FG cam-shum-act at laptop_screen
        if tm[-2:] < '40' and 'ann_shower1' not in cam_flag:
            $ cam_flag.append('ann_shower1')
            Max_07 "{m}Вот это да... Похоже намечается что-то большее, чем просто принять душ!{/m}"
        elif tm[-2:]<'50' and 'ann_shower2' not in cam_flag:
            $ cam_flag.append('ann_shower2')
            if ann_eric_scene in ['04', '05']:
                # минет
                Max_08 "{m}Да уж, устроился Эрик хорошо... Мама отсасывает ему с таким наслаждением, аж оторваться не может!{/m}"
            elif ann_eric_scene in ['06', '07']:
                # дрочка
                Max_04 "{m}Охх... Вот же Эрику повезло... Ведь у мамы такие нежные и ласковые руки!{/m}"
            elif ann_eric_scene in ['08', '09']:
                # секс спереди
                Max_06 "{m}Охренеть! Вот это страсть! Они так увлечены друг другом... И похоже, маме это очень нравится!{/m}"
            else:
                # секс ссзади
                Max_05 "{m}Ого! Эрик трахает маму сзади, да так активно... И... кажется, ей это очень нравится, она даже двигается ему навстречу... и изнывает от страсти!{/m}"
        elif tm[-2:]=='50' and 'ann_shower3' not in cam_flag:
            $ cam_flag.append('ann_shower3')
            if ann_eric_scene in ['04', '05']:
                # минет
                Max_09 "{m}Вот чёрт! Эрик кончает маме прямо на лицо, как в каком-то порно! Причём, ей это настолько нравится, что она улыбается и ловит его сперму своим ртом!{/m}"
            elif ann_eric_scene in ['06', '07', '08']:
                # дрочка
                Max_01 "{m}Ну да! Кто бы сомневался, что Эрик не продержится слишком долго. Мама своё дело знает!{/m}"
            elif ann_eric_scene in ['08', '09']:
                # секс спереди
                Max_07 "{m}Ох, чёрт... Эрик уже кончил... Хорошо, что не в маму... Счастливый сукин сын... И она ещё улыбается?!{/m}"
            else:
                # секс ссзади
                Max_08 "{m}Чёрт возьми... он уже кончил... Счастливый ублюдок... забрызгал маме всю спину с попкой своей спермой!{/m}"
    return

label cam1_eric_ann_shower:
    if tm[-2:] < '30':
        default __r1 = ''

        if tm[-2:] < '10':
            $ __r1 = '01'
        elif tm[-2:] < '20':
            $ __r1 = cam_poses_manager(eric, ['02', '05', '06'], 1)
        else:
            $ __r1 = '04' if __r1=='06' else '03'
        $ renpy.show('Eric cams bath-mirror '+__r1, at_list=[laptop_screen])
        show FG cam-shum-act at laptop_screen
        if __r1=='01' and 'ann_bath_mirror1' not in cam_flag:
            $ cam_flag.append('ann_bath_mirror1')
            Max_07 "{m}Охх... Боже мой, какие нежности. Похоже, сейчас что-то начнётся...{/m}"
        elif __r1=='02' and 'ann_bath_mirror2' not in cam_flag:
            $ cam_flag.append('ann_bath_mirror2')
            Max_10 "{m}Моя мама снова отсасывает этому... Эрику! Да с такой страстью! Ей что, действительно так нравится это делать или она его настолько любит?{/m}"
        elif __r1=='05' and 'ann_bath_mirror2' not in cam_flag:
            $ cam_flag.append('ann_bath_mirror2')
            Max_08 "{m}О Боже! Как бы я мечтал оказаться на месте это счастливого ублюдка! Когда её мокрая попка так красиво скачет на члене, голова начинает идти кругом!{/m}"
        elif __r1=='06' and 'ann_bath_mirror2' not in cam_flag:
            $ cam_flag.append('ann_bath_mirror2')
            Max_10 "{m}Ничего себе! Вот это они вытворяют! Эрик трахает маму, разложив её у зеркала как какую-то шлюшку...{/m}"
        elif __r1 == '03' and 'ann_bath_mirror3' not in cam_flag:
            $ cam_flag.append('ann_bath_mirror3')
            Max_08 "{m}Чёрт возьми! Она приняла всю его сперму себе в рот и на лицо, и теперь с такой жадностью и удовольствием слизывает её с его члена...{/m}"
        elif __r1 == '04' and 'ann_bath_mirror3' not in cam_flag:
            $ cam_flag.append('ann_bath_mirror3')
            Max_10 "{m}А вот и финал не заставил себя ждать! И похоже всем всё понравилось, как и всегда...{/m}"
    else:
        show FG cam-shum-noact at laptop_screen
        if 'ann_shower0' not in cam_flag:
            $ cam_flag.append('ann_shower0')
            Max_09 "{m}Мамы и Эрика не видно через эту камеру... Может посмотреть через другую?{/m}"
    return

label cam0_eric_resting:
    $ renpy.show('Eric cams relax '+cam_poses_manager(eric, ['01', '02', '03'])+eric.dress, at_list=[laptop_screen])
    show FG cam-shum-act at laptop_screen
    if 'eric_resting' not in cam_flag:
        $ cam_flag.append('eric_resting')
        if eric.daily.sweets and weekday in [1, 3]:
            Max_01 "{m}Кажется, подмешанное Эрику в еду средство испортило ему всё настроение и он не рискует идти к моей сестрёнке... Именно на это я и рассчитывал!{/m}"
        else:
            Max_01 "{m}О, \"В мире животных\" показывают! То ли шимпанзе на стероидах, то ли горилла...{/m}"
    return

label cam0_eric_ann_tv:
    if tm[-2:] < '10' or tm[-2:] >= '50':
        $ tv_scene = ''
        $ pose2_3 = cam_poses_manager(eric, ['01', '02', '03'])
    elif tm[-2:] < '30' and eric.stat.handjob and not tv_scene:
        $ tv_scene = renpy.random.choice(['bj', 'hj']) if eric.stat.handjob else 'hj'
        $ pose2_3 = '01'
    elif tm[-2:]>='30' and tv_scene:
        $ pose2_3 = '02'

    $ renpy.show('Eric cams tv '+tv_scene+pose2_3+eric.dress, at_list=[laptop_screen])
    show FG cam-shum-act at laptop_screen

    if tv_scene == '':
        if 'eric_tv' not in cam_flag:
            $ cam_flag.append('eric_tv')
            if eric.stat.handjob:
                Max_01 "{m}Мама с Эриком смотрят какой-то фильм. Наверняка, опять порнушку...{/m}"
            else:
                Max_01 "{m}Мама с Эриком смотрят какой-то фильм. Интересно, какой?{/m}"
    elif eric.daily.tv_sex == 1:
        # начали смотреть еще в гостиной
        if 'eric_tv1' not in cam_flag:
            $ cam_flag.append('eric_tv1')
            if tv_scene == 'hj':
                Max_08 "{m}Как же повезло Эрику! Я бы тоже с огромной радостью так посмотрел что угодно... если бы мамины нежные и умелые ручки ласкали мой член...{/m}"
            elif tv_scene == 'bj':
                Max_08 "{m}Блин, мама, тебе что, настолько неинтересно то, что происходит на экране или ты просто любишь отсасывать Эрику?!{/m}"
    else:
        $ eric.daily.tv_sex = 3
        if tv_scene and pose2_3 == '01':
            if 'eric_tv2' not in cam_flag:
                $ cam_flag.append('eric_tv2')
                Max_09 "{m}Ну конечно, ведь просто так смотреть, что происходит на экране они не будут, обязательно надо вот это вот делать...{/m}"
        elif tv_scene:
            if 'eric_tv3' not in cam_flag:
                $ cam_flag.append('eric_tv3')
                Max_10 "{m}А, ну да, без полотенца однозначно лучше... Но вы же в гостиной! А если зайдёт кто-то, а вы тут развлекаетесь...{/m}"
    return

label cam0_eric_ann_fucking:
    if eric.daily.sex > 2:
        # уже все посмотрели через окно или камеру
        $ renpy.show('Eric cams fuck relax '+cam_poses_manager(eric, ['01', '02', '03'], 1), at_list=[laptop_screen])
        show FG cam-shum-act at laptop_screen
        if 'eric_fuck_end' not in cam_flag:
            $ cam_flag.append('eric_fuck_end')
            Max_09 "{m}Утомлённые мама с Эриком лежат на кровати. Благо, они не только трахаются всё время, но ещё и разговаривают...{/m}"
    else:
        if 'eric_fuck0' not in cam_flag:
            $ cam_flag.append('eric_fuck0')
            $ fuck_scene = cam_poses_manager(eric, [6,1,2,3,4,5,6,7,1,2,3,4,5,6,7,1,2,3,4,5,6,7])
            if fuck_scene == 6:
                show CamAnnEric1 at laptop_screen
            else:
                $ renpy.show('Eric cams fuck 0'+str(fuck_scene), at_list=[laptop_screen])
            show FG cam-shum-act at laptop_screen
            if eric.daily.sex == 2:
                # Макса поймали на подглядывании
                Max_07 "{m}Через окно подсмотреть мне не дали, значит заценим через камеру... А они тут развлекаются, только в путь!{/m}"
            elif eric.daily.sex == 1:
                # ушли от закрытой двери
                Max_07 "{m}Подсмотреть через окно я не рискнул, могут заметить, а вот через камеру могу наслаждаться безнаказанно, сколько захочу... И посмотреть есть на что!{/m}"
            else:
                # вообще не подходили к двери
                Max_07 "{m}Ого! Вот это я удачно заглянул! Всё равно, что порно посмотреть...{/m}"
        elif tm[-2:] == '50' and 'eric_fuck_fin' not in cam_flag:
            # конец часа, финал траха
            if fuck_scene not in globals():
                $ fuck_scene = cam_poses_manager(eric, [6,1,2,3,4,5,6,7,1,2,3,4,5,6,7,1,2,3,4,5,6,7])
            $ eric.daily.sex = 4
            $ cam_flag.append('eric_fuck_fin')
            $ renpy.show('Eric cams fuck 0'+str(fuck_scene)+'a', at_list=[laptop_screen])
            show FG cam-shum-act at laptop_screen
            Max_08 "{m}Ну вот они и кончили. По крайней мере, Эрик так точно, а вот мама...{/m}"
        else:
            $ fuck_scene = cam_poses_manager(eric, [6,1,2,3,4,5,6,7,1,2,3,4,5,6,7,1,2,3,4,5,6,7])
            if fuck_scene == 6:
                show CamAnnEric1 at laptop_screen
            else:
                $ renpy.show('Eric cams fuck 0'+str(fuck_scene), at_list=[laptop_screen])
            show FG cam-shum-act at laptop_screen

    return

label cam0_sexed_lisa:
    if flags.lisa_sexed < 0:
        # вводный урок
        $ renpy.show('Eric cams sexed 01-01'+eric.dress, at_list=[laptop_screen])
        $ renpy.show('Lisa cams sexed 01'+lisa.dress, at_list=[laptop_screen])

        show FG cam-shum-act at laptop_screen

        if 'ae_lisa_sexed' not in cam_flag:
            $ cam_flag.append('ae_lisa_sexed')
            Max_08 "{m}Жаль камеры не передают звук. Нужно будет обязательно спросить Лизу, о чём они разговаривали!{/m}"

    elif flags.lisa_sexed == 0:
        # первый урок
        if tm[-2:] < '10':
            $ renpy.show('Eric cams sexed 01-01'+eric.dress, at_list=[laptop_screen])
            $ renpy.show('Lisa cams sexed 01'+lisa.dress, at_list=[laptop_screen])
            show FG cam-shum-act at laptop_screen
            if 'ann_eric_lisa_sexed0' not in cam_flag:
                $ cam_flag.append('ann_eric_lisa_sexed0')
                Max_07 "{m}Лиза пришла на урок к маме и Эрику. Посмотрим, что будет...{/m}"

        elif tm[-2:] < '20':
            $ renpy.show('Eric cams sexed 02-01'+eric.dress, at_list=[laptop_screen])
            $ renpy.show('Lisa cams sexed 02'+lisa.dress, at_list=[laptop_screen])
            show FG cam-shum-act at laptop_screen
            if 'ann_eric_lisa_sexed1' not in cam_flag:
                $ cam_flag.append('ann_eric_lisa_sexed1')
                Max_09 "{m}Вот же Эрик! Член он свой вывесил... Интересно, что они ей там рассказывают?{/m}"

        elif tm[-2:] < '30':
            $ renpy.show('Eric cams sexed 03-01'+eric.dress, at_list=[laptop_screen])
            $ renpy.show('Lisa cams sexed 03'+lisa.dress, at_list=[laptop_screen])
            show FG cam-shum-act at laptop_screen
            if 'ann_eric_lisa_sexed2' not in cam_flag:
                $ cam_flag.append('ann_eric_lisa_sexed2')
                Max_08 "{m}Ага, дрочка пошла... И уговорил же Эрик маму на всё это...{/m}"

    elif flags.lisa_sexed == 1:
        # второй урок
        if tm[-2:] < '10':
            $ renpy.show('Eric cams sexed 01-01'+eric.dress, at_list=[laptop_screen])
            $ renpy.show('Lisa cams sexed 01'+lisa.dress, at_list=[laptop_screen])
            show FG cam-shum-act at laptop_screen
            if 'ann_eric_lisa_sexed0' not in cam_flag:
                $ cam_flag.append('ann_eric_lisa_sexed0')
                Max_07 "{m}Лиза пришла на урок к маме и Эрику. Посмотрим, что будет...{/m}"

        elif tm[-2:] < '20':
            $ renpy.show('Eric cams sexed 02-02'+eric.dress, at_list=[laptop_screen])
            $ renpy.show('Lisa cams sexed 02'+lisa.dress, at_list=[laptop_screen])
            show FG cam-shum-act at laptop_screen
            if 'ann_eric_lisa_sexed1' not in cam_flag:
                $ cam_flag.append('ann_eric_lisa_sexed1')
                Max_09 "{m}Мама при Лизе уже надрачивает Эрику как будто так и надо! Интересно, что они ей там рассказывают при этом?{/m}"

        elif tm[-2:] < '30':
            $ renpy.show('Eric cams sexed 03-02'+eric.dress, at_list=[laptop_screen])
            $ renpy.show('Lisa cams sexed 03'+lisa.dress, at_list=[laptop_screen])
            show FG cam-shum-act at laptop_screen
            if 'ann_eric_lisa_sexed2' not in cam_flag:
                $ cam_flag.append('ann_eric_lisa_sexed2')
                Max_08 "{m}Ага, мама повышает градус показом своей шикарной груди... И уговорил же Эрик маму на всё это!{/m}"

    elif flags.lisa_sexed == 2:
        # третий урок
        if tm[-2:] < '10':
            $ renpy.show('Eric cams sexed 01-01'+eric.dress, at_list=[laptop_screen])
            $ renpy.show('Lisa cams sexed 01'+lisa.dress, at_list=[laptop_screen])
            show FG cam-shum-act at laptop_screen
            if 'ann_eric_lisa_sexed0' not in cam_flag:
                $ cam_flag.append('ann_eric_lisa_sexed0')
                Max_07 "{m}Лиза пришла на урок к маме и Эрику. Посмотрим, что будет...{/m}"

        elif tm[-2:] < '20':
            $ renpy.show('Eric cams sexed 02-02'+eric.dress, at_list=[laptop_screen])
            $ renpy.show('Lisa cams sexed 02'+lisa.dress, at_list=[laptop_screen])
            show FG cam-shum-act at laptop_screen
            if 'ann_eric_lisa_sexed1' not in cam_flag:
                $ cam_flag.append('ann_eric_lisa_sexed1')
                Max_09 "{m}Подрочить Эрику на глазах Лизы в образовательных целях? Конечно, обычное дело, не обращайте внимания... Интересно, что они ей там рассказывают при этом?{/m}"

        elif tm[-2:] < '30':
            $ renpy.show('Eric cams sexed 03-03'+eric.dress, at_list=[laptop_screen])
            $ renpy.show('Lisa cams sexed 03'+lisa.dress, at_list=[laptop_screen])
            show FG cam-shum-act at laptop_screen
            if 'ann_eric_lisa_sexed2' not in cam_flag:
                $ cam_flag.append('ann_eric_lisa_sexed2')
                Max_08 "{m}О, от такого я бы не отказался! Только от одних мыслей о маминых руках, нежно массирующих мои шары, хочется кончить...{/m}"

    elif flags.lisa_sexed == 3:
        # четвертый урок
        if tm[-2:] < '10':
            $ renpy.show('Eric cams sexed 01-01'+eric.dress, at_list=[laptop_screen])
            $ renpy.show('Lisa cams sexed 01'+lisa.dress, at_list=[laptop_screen])
            show FG cam-shum-act at laptop_screen
            if 'ann_eric_lisa_sexed0' not in cam_flag:
                $ cam_flag.append('ann_eric_lisa_sexed0')
                Max_07 "{m}Лиза пришла на урок к маме и Эрику. Посмотрим, что будет...{/m}"

        elif tm[-2:] < '20':
            $ renpy.show('Eric cams sexed 03-02'+eric.dress, at_list=[laptop_screen])
            $ renpy.show('Lisa cams sexed 03'+lisa.dress, at_list=[laptop_screen])
            show FG cam-shum-act at laptop_screen
            if 'ann_eric_lisa_sexed1' not in cam_flag:
                $ cam_flag.append('ann_eric_lisa_sexed1')
                Max_09 "{m}Всё дрочат и дрочат... Видимо, закрепляют материал. Ну сколько можно?!{/m}"

        elif tm[-2:] < '30':
            $ renpy.show('Eric cams sexed 03-04'+eric.dress, at_list=[laptop_screen])
            $ renpy.show('Lisa cams sexed 03'+lisa.dress, at_list=[laptop_screen])
            show FG cam-shum-act at laptop_screen
            if 'ann_eric_lisa_sexed2' not in cam_flag:
                $ cam_flag.append('ann_eric_lisa_sexed2')
                Max_08 "{m}О, Эрик не выдержал и кончил... Хотя, вряд ли. Скорее всего, они решили показать Лизе для чего это всё было нужно.{/m}"

    return


label cam0_eric_shat:
    show FG cam-shum-act at laptop_screen
    if 'eric_bath0' not in cam_flag:
        $ cam_flag.append('eric_bath0')
        if len(house[3].cams)>1:
            Max_09 "{m}Ничего толком не видно... Стоит взглянуть через другую камеру...{/m}"
        else:
            Max_09 "{m}Ничего толком не видно...{/m}"
    return


label cam1_eric_shat:
    if tm < '22:00':
        $ renpy.show('Eric cams shat 01'+eric.dress, at_list=[laptop_screen])
    else:
        $ renpy.show('Eric cams shat 02'+eric.dress, at_list=[laptop_screen])

    show FG cam-shum-act at laptop_screen
    if 'eric_bath0' not in cam_flag:
        $ cam_flag.append('eric_bath0')
        if tm < '22:00':
            Max_02 "{m}Эрик во всю оценивает эффективность слабительного, которое я ему подмешал... Надеюсь, эта обезьяна знает, как пользоваться туалетной бумагой, потому что банановых листьев у нас тут нет!{/m}"
        else:
            Max_02 "{m}Ты что, Эрик, съел что-то не то, что ли?! Бедняга. Ну, держись там...{/m}"
    return


label cam0_eric_ann_resting:
    $ renpy.show('Eric cams relax2 '+cam_poses_manager(eric, ['01', '02', '03'])+eric.dress, at_list=[laptop_screen])
    show FG cam-shum-act at laptop_screen
    if 'eric_resting2' not in cam_flag:
        $ cam_flag.append('eric_resting2')
        Max_02 "{m}Похоже, потрахушек сегодня не намечается... Интересно, с чего бы это?!{/m}"
    return


label cam0_eric_sleep:
    $ renpy.show('Eric cams sleep '+cam_poses_manager(eric, ['01', '02'])+eric.dress, at_list=[laptop_screen])
    show FG cam-shum-act at laptop_screen

    if 'eric_sleep' not in cam_flag:
        $ cam_flag.append('eric_sleep')
        Max_07 "{m}Остаётся надеяться, что я подмешал ему не слишком много успокоительного... Главное, что он сейчас ни к кому не пристаёт.{/m}"

    return

##
label cam0_eric_ann_try_fucking:
    $ renpy.show('Eric cams nosex '+cam_poses_manager(eric, ['01', '02']), at_list=[laptop_screen])
    show FG cam-shum-act at laptop_screen
    if 'eric_nosex' not in cam_flag:
        $ cam_flag.append('eric_nosex')
        Max_01 "{m}Не стоит? Ну ничего, бывает... Но всё равно приятно осознавать, что это происходит из-за моих действий.{/m}"
    return

##
label cam0_lisa_eric_sex_ed_practice:
    show FG cam-shum-act at laptop_screen
    return


label cam_before_frame_eric:
    menu:
        Max_07 "{m}Отлично! Эрик именно там, где мне и нужно... Нужно дождаться, когда он вернётся к моей маме, и затем уже спокойно его подставлять...{/m}"
        "{i}подождать{/i}":
            pass
    scene BG char Max laptop-night-01t
    $ renpy.show('BG-cam house aliceroom-0 night', at_list=[laptop_screen,])
    $ renpy.show('Alice cams sleep night '+cam_poses_manager(alice, ['01', '02', '03']), at_list=[laptop_screen])
    show FG cam-shum-act at laptop_screen
    with dissolve
    pause 1
    # комната Анны с Эриком
    scene BG char Max laptop-night-01t
    $ renpy.show('BG-cam house annroom-0 night', at_list=[laptop_screen,])
    $ renpy.show('Eric cams sleep2 '+cam_poses_manager(eric, ['01', '02', '03']), at_list=[laptop_screen])
    show FG cam-shum-act at laptop_screen
    with dissolve
    menu:
        Max_01 "{m}Отлично! Пора...{/m}"
        "{i}идти к комнате Алисы{/i}":
            jump frame_eric


label cam0_eric_kira_night_swim:
    show FG cam-shum-noact at laptop_screen
    if 'kira_swim0' not in cam_flag:
        $ cam_flag.append('kira_swim0')
        if len(house[6].cams)>1:
            Max_09 "{m}Ничего толком не видно... Стоит взглянуть через другую камеру...{/m}"
        else:
            Max_09 "{m}Ничего не разглядеть... Нужно установить камеру, которая охватила бы весь бассейн...{/m}"
    return

label cam1_eric_kira_night_swim:
    $ renpy.show('Kira cams swim night '+cam_poses_manager(kira, ['01', '02', '03']), at_list=[laptop_screen])
    show FG cam-shum-act at laptop_screen
    if 'kira_swim1' not in cam_flag:
        $ cam_flag.append('kira_swim1')
        if GetRelMax('eric')[0] < 0:
            # война с Эриком
            Max_10 "{m}Вот чёрт! Похоже, Кира ублажает Эрика, чтобы он нас не заложил маме...{/m}"
    return
