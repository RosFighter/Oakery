
label cam0_eric_ann_sleep:
    if flags['eric.jerk'] and '02:00'<=tm<'02:30':
        $ renpy.show('Ann cams sleep '+cam_poses_manager(ann, ['01', '02', '03'])+ann.dress, at_list=[laptop_screen])
    else:
        $ renpy.show('Eric cams sleep '+cam_poses_manager(eric, ['01', '02', '03']), at_list=[laptop_screen])
    show FG cam-shum-act at laptop_screen

    if all([flags['eric.jerk'], '02:00'<=tm<'02:30', not prenoted, not flags['eric.noticed']]):
        $ prenoted = 1
        if not flags['eric.firstjerk']:
            # 1-ое спаливание Эрика у окна Алисы
            Max_07 "Как же повезло, что у меня такая горячая мама... Стойте-ка, а Эрик где?! Может, пошёл в ванную комнату? Или ещё куда..."
        else:
            Max_07 "Как же повезло, что у меня такая горячая мама... А Эрик опять где-то полуночничает..."

    elif all([flags['eric.jerk'], '02:00'<=tm<'02:30', flags['eric.noticed'], 'ann_sleep_alone' not in cam_flag]) or not check_is_room('eric'):
        # Эрик уже замечен или с Кирой в ванной
        $ cam_flag.append('ann_sleep_alone')
        Max_01 "Как же повезло, что у меня такая горячая мама... Выглядит потрясающе, аж глаза отрывать не хочется!"

    if 'ann_sleep' not in cam_flag and not (flags['eric.jerk'] and '02:00'<=tm<'02:30'):
        $ cam_flag.append('ann_sleep')
        Max_01 "Мама и Эрик спят совсем голые. Ни стыда, ни совести..."
    return

label cam0_eric_ann_shower:
    default ann_eric_scene = ''
    if tm[-2:] < '30':
        show FG cam-shum-noact at laptop_screen
        if 'ann_not_shower' not in cam_flag:
            $ cam_flag.append('ann_not_shower')
            if len(house[3].cams)>1:
                Max_09 "Мамы и Эрика не видно через эту камеру... Может посмотреть через другую?"
            else:
                Max_09 "Мамы и Эрика не видно через эту камеру..."
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
            Max_07 "Вот это да... Похоже намечается что-то большее, чем просто принять душ!"
        elif tm[-2:]<'50' and 'ann_shower2' not in cam_flag:
            $ cam_flag.append('ann_shower2')
            if ann_eric_scene in ['04', '05']:
                # минет
                Max_08 "Да уж, устроился Эрик хорошо... Мама отсасывает ему с таким наслаждением, аж оторваться не может!"
            elif ann_eric_scene in ['06', '07']:
                # дрочка
                Max_04 "Охх... Вот же Эрику повезло... Ведь у мамы такие нежные и ласковые руки!"
            elif ann_eric_scene in ['08', '09']:
                # секс спереди
                Max_06 "Охренеть! Вот это страсть! Они так увлечены друг другом... И похоже, маме это очень нравится!"
            else:
                # секс ссзади
                Max_05 "Ого! Эрик трахает маму сзади, да так активно... И... кажется, ей это очень нравится, она даже двигается ему навстречу... и изнывает от страсти!"
        elif tm[-2:]=='50' and 'ann_shower3' not in cam_flag:
            $ cam_flag.append('ann_shower3')
            if ann_eric_scene in ['04', '05']:
                # минет
                Max_09 "Вот чёрт! Эрик кончает маме прямо на лицо, как в каком-то порно! Причём, ей это настолько нравится, что она улыбается и ловит его сперму своим ртом!"
            elif ann_eric_scene in ['06', '07', '08']:
                # дрочка
                Max_01 "Ну да! Кто бы сомневался, что Эрик не продержится слишком долго. Мама своё дело знает!"
            elif ann_eric_scene in ['08', '09']:
                # секс спереди
                Max_07 "Ох, чёрт... Эрик уже кончил... Хорошо, что не в маму... Счастливый сукин сын... И она ещё улыбается?!"
            else:
                # секс ссзади
                Max_08 "Чёрт возьми... он уже кончил... Счастливый ублюдок... забрызгал маме всю спину с попкой своей спермой!"
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
            Max_07 "Охх... Боже мой, какие нежности. Похоже, сейчас что-то начнётся..."
        elif __r1=='02' and 'ann_bath_mirror2' not in cam_flag:
            $ cam_flag.append('ann_bath_mirror2')
            Max_10 "Моя мама снова отсасывает этому... Эрику! Да с такой страстью! Ей что, действительно так нравится это делать или она его настолько любит?"
        elif __r1=='05' and 'ann_bath_mirror2' not in cam_flag:
            $ cam_flag.append('ann_bath_mirror2')
            Max_08 "О Боже! Как бы я мечтал оказаться на месте это счастливого ублюдка! Когда её мокрая попка так красиво скачет на члене, голова начинает идти кругом!"
        elif __r1=='06' and 'ann_bath_mirror2' not in cam_flag:
            $ cam_flag.append('ann_bath_mirror2')
            Max_10 "Ничего себе! Вот это они вытворяют! Эрик трахает маму, разложив её у зеркала как какую-то шлюшку..."
        elif __r1 == '03' and 'ann_bath_mirror3' not in cam_flag:
            $ cam_flag.append('ann_bath_mirror3')
            Max_08 "Чёрт возьми! Она приняла всю его сперму себе в рот и на лицо, и теперь с такой жадностью и удовольствием слизывает её с его члена..."
        elif __r1 == '04' and 'ann_bath_mirror3' not in cam_flag:
            $ cam_flag.append('ann_bath_mirror3')
            Max_10 "А вот и финал не заставил себя ждать! И похоже всем всё понравилось, как и всегда..."
    else:
        show FG cam-shum-noact at laptop_screen
        if 'ann_shower0' not in cam_flag:
            $ cam_flag.append('ann_shower0')
            Max_09 "Мамы и Эрика не видно через эту камеру... Может посмотреть через другую?"
    return

label cam0_eric_resting:
    $ renpy.show('Eric cams relax '+cam_poses_manager(eric, ['01', '02', '03'])+eric.dress, at_list=[laptop_screen])
    show FG cam-shum-act at laptop_screen
    if 'eric_resting' not in cam_flag:
        $ cam_flag.append('eric_resting')
        Max_01 "О, \"В мире животных\" показывают! То ли шимпанзе на стероидах, то ли горилла..."
    return

label cam0_eric_ann_tv:
    if tm[-2:] < '10' or tm[-2:] >= '50':
        $ tv_scene = ''
        $ pose2_3 = cam_poses_manager(eric, ['01', '02', '03'])
    elif tm[-2:] < '30' and flags['ae.tv.hj'] and not tv_scene:
        $ tv_scene = renpy.random.choice(['bj', 'hj']) if flags['ae.tv.hj'] > 0 else 'hj'
        $ pose2_3 = '01'
    elif tm[-2:]>='30' and tv_scene:
        $ pose2_3 = '02'

    $ renpy.show('Eric cams tv '+tv_scene+pose2_3+eric.dress, at_list=[laptop_screen])
    show FG cam-shum-act at laptop_screen

    if tv_scene == '':
        if 'eric_tv' not in cam_flag:
            $ cam_flag.append('eric_tv')
            if flags['ae.tv.hj']:
                Max_01 "Мама с Эриком смотрят какой-то фильм. Наверняка, опять порнушку..."
            else:
                Max_01 "Мама с Эриком смотрят какой-то фильм. Интересно, какой?"
    elif peeping['ann_eric_tv'] == 1:
        # начали смотреть еще в гостиной
        if 'eric_tv1' not in cam_flag:
            $ cam_flag.append('eric_tv1')
            if tv_scene == 'hj':
                Max_08 "Как же повезло Эрику! Я бы тоже с огромной радостью так посмотрел что угодно... если бы мамины нежные и умелые ручки ласкали мой член..."
            elif tv_scene == 'bj':
                Max_08 "Блин, мама, тебе что, настолько неинтересно то, что происходит на экране или ты просто любишь отсасывать Эрику?!"
    else:
        $ peeping['ann_eric_tv'] = 3
        if tv_scene and pose2_3 == '01':
            if 'eric_tv2' not in cam_flag:
                $ cam_flag.append('eric_tv2')
                Max_09 "Ну конечно, ведь просто так смотреть, что происходит на экране они не будут, обязательно надо вот это вот делать..."
        elif tv_scene:
            if 'eric_tv3' not in cam_flag:
                $ cam_flag.append('eric_tv3')
                Max_10 "А, ну да, без полотенца однозначно лучше... Но вы же в гостиной! А если зайдёт кто-то, а вы тут развлекаетесь..."
    return

label cam0_eric_ann_fucking:
    if peeping['ann_eric_sex1'] > 2:
        # уже все посмотрели через окно или камеру
        $ renpy.show('Eric cams fuck relax '+cam_poses_manager(eric, ['01', '02', '03'], 1), at_list=[laptop_screen])
        show FG cam-shum-act at laptop_screen
        if 'eric_fuck_end' not in cam_flag:
            $ cam_flag.append('eric_fuck_end')
            Max_09 "Утомлённые мама с Эриком лежат на кровати. Благо, они не только трахаются всё время, но ещё и разговаривают..."
    else:
        if 'eric_fuck0' not in cam_flag:
            $ cam_flag.append('eric_fuck0')
            $ fuck_scene = cam_poses_manager(eric, [6,1,2,3,4,5,6,7,1,2,3,4,5,6,7,1,2,3,4,5,6,7])
            if fuck_scene == 6:
                show CamAnnEric1 at laptop_screen
            else:
                $ renpy.show('Eric cams fuck 0'+str(fuck_scene), at_list=[laptop_screen])
            show FG cam-shum-act at laptop_screen
            if peeping['ann_eric_sex1'] == 2:
                # Макса поймали на подглядывании
                Max_07 "Через окно подсмотреть мне не дали, значит заценим через камеру... А они тут развлекаются, только в путь!"
            elif peeping['ann_eric_sex1'] == 1:
                # ушли от закрытой двери
                Max_07 "Подсмотреть через окно я не рискнул, могут заметить, а вот через камеру могу наслаждаться безнаказанно, сколько захочу... И посмотреть есть на что!"
            else:
                # вообще не подходили к двери
                Max_07 "Ого! Вот это я удачно заглянул! Всё равно, что порно посмотреть..."
        elif tm[-2:] == '50' and 'eric_fuck_fin' not in cam_flag:
            # конец часа, финал траха
            if fuck_scene not in globals():
                $ fuck_scene = cam_poses_manager(eric, [6,1,2,3,4,5,6,7,1,2,3,4,5,6,7,1,2,3,4,5,6,7])
            $ peeping['ann_eric_sex1'] = 4
            $ cam_flag.append('eric_fuck_fin')
            $ renpy.show('Eric cams fuck 0'+str(fuck_scene)+'a', at_list=[laptop_screen])
            show FG cam-shum-act at laptop_screen
            Max_08 "Ну вот они и кончили. По крайней мере, Эрик так точно, а вот мама..."
        else:
            $ fuck_scene = cam_poses_manager(eric, [6,1,2,3,4,5,6,7,1,2,3,4,5,6,7,1,2,3,4,5,6,7])
            if fuck_scene == 6:
                show CamAnnEric1 at laptop_screen
            else:
                $ renpy.show('Eric cams fuck 0'+str(fuck_scene), at_list=[laptop_screen])
            show FG cam-shum-act at laptop_screen

    return

label cam0_sexed_lisa:
    if talk_var['ae_lisa_number'] < 0:
        # вводный урок
        $ renpy.show('Eric cams sexed 01-01'+eric.dress, at_list=[laptop_screen])
        $ renpy.show('Lisa cams sexed 01'+lisa.dress, at_list=[laptop_screen])

        show FG cam-shum-act at laptop_screen

        if 'ae_lisa_sexed' not in cam_flag:
            $ cam_flag.append('ae_lisa_sexed')
            Max_08 "{i}( Жаль камеры не передают звук. Нужно будет обязательно спросить Лизу, о чём они разговаривали! ){/i}"

    elif talk_var['ae_lisa_number'] == 0:
        # первый урок
        if tm[-2:] < '10':
            $ renpy.show('Eric cams sexed 01-01'+eric.dress, at_list=[laptop_screen])
            $ renpy.show('Lisa cams sexed 01'+lisa.dress, at_list=[laptop_screen])
            show FG cam-shum-act at laptop_screen
            if 'ann_eric_lisa_sexed0' not in cam_flag:
                $ cam_flag.append('ann_eric_lisa_sexed0')
                Max_07 "{i}( Лиза пришла на урок к маме и Эрику. Посмотрим, что будет... ){/i}"

        elif tm[-2:] < '20':
            $ renpy.show('Eric cams sexed 02-01'+eric.dress, at_list=[laptop_screen])
            $ renpy.show('Lisa cams sexed 02'+lisa.dress, at_list=[laptop_screen])
            show FG cam-shum-act at laptop_screen
            if 'ann_eric_lisa_sexed1' not in cam_flag:
                $ cam_flag.append('ann_eric_lisa_sexed1')
                Max_09 "{i}( Вот же Эрик! Член он свой вывесил... Интересно, что они ей там рассказывают? ){/i}"

        elif tm[-2:] < '30':
            $ renpy.show('Eric cams sexed 03-01'+eric.dress, at_list=[laptop_screen])
            $ renpy.show('Lisa cams sexed 03'+lisa.dress, at_list=[laptop_screen])
            show FG cam-shum-act at laptop_screen
            if 'ann_eric_lisa_sexed2' not in cam_flag:
                $ cam_flag.append('ann_eric_lisa_sexed2')
                Max_08 "{i}( Ага, дрочка пошла... И уговорил же Эрик маму на всё это... ){/i}"

    elif talk_var['ae_lisa_number'] == 1:
        # второй урок
        if tm[-2:] < '10':
            $ renpy.show('Eric cams sexed 01-01'+eric.dress, at_list=[laptop_screen])
            $ renpy.show('Lisa cams sexed 01'+lisa.dress, at_list=[laptop_screen])
            show FG cam-shum-act at laptop_screen
            if 'ann_eric_lisa_sexed0' not in cam_flag:
                $ cam_flag.append('ann_eric_lisa_sexed0')
                Max_07 "{i}( Лиза пришла на урок к маме и Эрику. Посмотрим, что будет... ){/i}"

        elif tm[-2:] < '20':
            $ renpy.show('Eric cams sexed 02-02'+eric.dress, at_list=[laptop_screen])
            $ renpy.show('Lisa cams sexed 02'+lisa.dress, at_list=[laptop_screen])
            show FG cam-shum-act at laptop_screen
            if 'ann_eric_lisa_sexed1' not in cam_flag:
                $ cam_flag.append('ann_eric_lisa_sexed1')
                Max_09 "{i}( Мама при Лизе уже надрачивает Эрику как будто так и надо! Интересно, что они ей там рассказывают при этом? ){/i}"

        elif tm[-2:] < '30':
            $ renpy.show('Eric cams sexed 03-02'+eric.dress, at_list=[laptop_screen])
            $ renpy.show('Lisa cams sexed 03'+lisa.dress, at_list=[laptop_screen])
            show FG cam-shum-act at laptop_screen
            if 'ann_eric_lisa_sexed2' not in cam_flag:
                $ cam_flag.append('ann_eric_lisa_sexed2')
                Max_08 "{i}( Ага, мама повышает градус показом своей шикарной груди... И уговорил же Эрик маму на всё это! ){/i}"

    elif talk_var['ae_lisa_number'] == 2:
        # третий урок
        if tm[-2:] < '10':
            $ renpy.show('Eric cams sexed 01-01'+eric.dress, at_list=[laptop_screen])
            $ renpy.show('Lisa cams sexed 01'+lisa.dress, at_list=[laptop_screen])
            show FG cam-shum-act at laptop_screen
            if 'ann_eric_lisa_sexed0' not in cam_flag:
                $ cam_flag.append('ann_eric_lisa_sexed0')
                Max_07 "{i}( Лиза пришла на урок к маме и Эрику. Посмотрим, что будет... ){/i}"

        elif tm[-2:] < '20':
            $ renpy.show('Eric cams sexed 02-02'+eric.dress, at_list=[laptop_screen])
            $ renpy.show('Lisa cams sexed 02'+lisa.dress, at_list=[laptop_screen])
            show FG cam-shum-act at laptop_screen
            if 'ann_eric_lisa_sexed1' not in cam_flag:
                $ cam_flag.append('ann_eric_lisa_sexed1')
                Max_09 "{i}( Подрочить Эрику на глазах Лизы в образовательных целях? Конечно, обычное дело, не обращайте внимания... Интересно, что они ей там рассказывают при этом? ){/i}"

        elif tm[-2:] < '30':
            $ renpy.show('Eric cams sexed 03-03'+eric.dress, at_list=[laptop_screen])
            $ renpy.show('Lisa cams sexed 03'+lisa.dress, at_list=[laptop_screen])
            show FG cam-shum-act at laptop_screen
            if 'ann_eric_lisa_sexed2' not in cam_flag:
                $ cam_flag.append('ann_eric_lisa_sexed2')
                Max_08 "{i}( О, от такого я бы не отказался! Только от одних мыслей о маминых руках, нежно массирующих мои шары, хочется кончить... ){/i}"

    elif talk_var['ae_lisa_number'] == 3:
        # четвертый урок
        if tm[-2:] < '10':
            $ renpy.show('Eric cams sexed 01-01'+eric.dress, at_list=[laptop_screen])
            $ renpy.show('Lisa cams sexed 01'+lisa.dress, at_list=[laptop_screen])
            show FG cam-shum-act at laptop_screen
            if 'ann_eric_lisa_sexed0' not in cam_flag:
                $ cam_flag.append('ann_eric_lisa_sexed0')
                Max_07 "{i}( Лиза пришла на урок к маме и Эрику. Посмотрим, что будет... ){/i}"

        elif tm[-2:] < '20':
            $ renpy.show('Eric cams sexed 03-02'+eric.dress, at_list=[laptop_screen])
            $ renpy.show('Lisa cams sexed 02'+lisa.dress, at_list=[laptop_screen])
            show FG cam-shum-act at laptop_screen
            if 'ann_eric_lisa_sexed1' not in cam_flag:
                $ cam_flag.append('ann_eric_lisa_sexed1')
                Max_09 "{i}( Всё дрочат и дрочат... Видимо, закрепляют материал. Ну сколько можно?! ){/i}"

        elif tm[-2:] < '30':
            $ renpy.show('Eric cams sexed 03-04'+eric.dress, at_list=[laptop_screen])
            $ renpy.show('Lisa cams sexed 03'+lisa.dress, at_list=[laptop_screen])
            show FG cam-shum-act at laptop_screen
            if 'ann_eric_lisa_sexed2' not in cam_flag:
                $ cam_flag.append('ann_eric_lisa_sexed2')
                Max_08 "{i}( О, Эрик не выдержал и кончил... Хотя, вряд ли. Скорее всего, они решили показать Лизе для чего это всё было нужно. ){/i}"

    return
