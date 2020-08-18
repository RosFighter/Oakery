
label cam0_eric_ann_sleep:
    $ renpy.show('Eric cams sleep '+renpy.random.choice(['01', '02', '03']), at_list=[laptop_screen])
    show FG cam-shum-act at laptop_screen
    if 'ann_sleep' not in cam_flag:
        $ cam_flag.append('ann_sleep')
        Max_01 "Красавица и чудовище на одной кровати..."
    return

label cam0_eric_ann_shower:
    default ann_eric_scene = ''
    if tm[-2:] < '30':
        show FG cam-shum-act at laptop_screen
        if 'ann_not_shower' not in cam_flag:
            $ cam_flag.append('ann_not_shower')
            if len(house[3].cams)>1:
                Max_00 "Мамы и Эрика не видно, они скорее всего у зеркал... Надо взглянуть через другую камеру."
            else:
                Max_00 "Мамы и Эрика не видно, они скорее всего у зеркал... Но обзора этой камеры не хватает..."
    else:
        $ ann.dress_inf = '00a'
        if not ann_eric_scene:
            $ ann_eric_scene = renpy.random.choice(['01', '02', '03'])
        elif ann_eric_scene in ['01', '02', '03']:
            $ ann_eric_scene = {
                    '01' : renpy.random.choice(['04', '05', '06']),
                    '02' : renpy.random.choice(['08', '10']),
                    '03' : renpy.random.choice(['07', '09', '11']),
                }[ann_eric_scene]

        if tm[-2:] < '50':
            $ renpy.show('Eric cams shower '+ann_eric_scene, at_list=[laptop_screen])
        else:
            $ renpy.show('Eric cams shower '+ann_eric_scene+'a', at_list=[laptop_screen])
        show other cam-shower-water at laptop_screen
        show FG cam-shum-act at laptop_screen
        if 'ann_shower1' not in cam_flag:
            $ cam_flag.append('ann_shower1')
            Max_07 "Вот это да... Похоже намечается что-то большее, чем просто принять душ!"
        elif 'ann_shower2' not in cam_flag:
            $ cam_flag.append('ann_shower2')
            if ann_eric_scene in ['04', '05']:
                # минет
                Max_00 "Да уж, устроился Эрик хорошо... Мама отсасывает ему с таким наслаждением, аж оторваться не может!"
            elif ann_eric_scene in ['06', '07']:
                # дрочка
                Max_04 "Охх... Вот же Эрику повезло... Ведь у мамы такие нежные и ласковые руки!"
            elif ann_eric_scene in ['08', '09']:
                # секс спереди
                Max_06 "Охренеть! Вот это страсть! Они так увлечены друг другом... И похоже, маме это очень нравится!"
            else:
                # секс ссзади
                Max_05 "Ого! Эрик трахает маму сзади, да так активно... И... кажется, ей это очень нравится, она даже двигается ему навстречу... и изнывает от страсти!"
        elif tm[-2:] == '50' and 'ann_shower3' not in cam_flag:
            $ cam_flag.append('ann_shower3')
            if ann_eric_scene in ['04', '05']:
                # минет
                Max_09 "Вот чёрт! Эрик кончает маме прямо на лицо, как в каком-то порно! Причём, ей это настолько нравится, что она улыбается и ловит его сперму своим ртом! Неужели она настолько развратна?!"
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

        if tm[-2:] < '10':
            $ __r1 = '01'
        elif tm[-2:] < '20':
            $ __r1 = renpy.random.choice(['02', '05', '06'])
        else:
            $ __r1 = '03' if __r1=='02' else '04'
        $ renpy.show('Eric cams bath-mirror '+__r1, at_list=[laptop_screen])
        show FG cam-shum-act at laptop_screen
        if 'ann_bath_mirror1' not in cam_flag:
            $ cam_flag.append('ann_bath_mirror1')
            Max_00  "Похоже, мама с Эриком просто не могут спокойно принять душ... Им обязательно нужно заняться чем-нибудь этаким..."

    else:
        show FG cam-shum-act at laptop_screen
        if 'ann_shower0' not in cam_flag:
            $ cam_flag.append('ann_shower0')
            Max_00 "Через эту камеру ничего не видно... Может посмотреть через другую?"
    return

label cam0_eric_resting:
    $ renpy.show('Eric cams relax '+renpy.random.choice(['01', '02', '03'])+eric.dress, at_list=[laptop_screen])
    show FG cam-shum-act at laptop_screen
    if 'eric_resting' not in cam_flag:
        $ cam_flag.append('eric_resting')
        Max_01 "Обезъян в маминой кровати... Бррр..."
    return

label cam0_eric_ann_tv:
    if tm[-2:] < '10':
        $ tv_scene = ''
        $ pose2_3 = renpy.random.choice(['01', '02', '03'])
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
                Max_00 "Мама с Эриком смотрят какой-то фильм... Наверняка, опять порно..."
            else:
                Max_00 "Мама с Эриком смотрят какой-то фильм... Интересно, какой?"
    elif peeping['ann_eric_tv'] == 1:
        # начали смотреть еще в гостиной
        if 'eric_tv1' not in cam_flag:
            $ cam_flag.append('eric_tv1')
            if tv_scene == 'hj':
                Max_00 "Как же повезло этому... Эрику. Мамины мягкие, нежные и умелые ручки просто творят чудеса..."
            elif tv_scene == 'bj':
                Max_00 "Блин, мама, ну почему ты отсасываешь этому... Эрику? Неужели тебе самой это нравится?"
    else:
        $ peeping['ann_eric_tv'] = 3
        if tv_scene and pose2_3 == '01':
            if 'eric_tv2' not in cam_flag:
                $ cam_flag.append('eric_tv2')
                Max_00 "И конечно же они не могут просто смотреть, им надо принять участие..."
        elif tv_scene:
            if 'eric_tv3' not in cam_flag:
                $ cam_flag.append('eric_tv3')
                Max_00 "А теперь мама настолько распалилась, что скинула свое полотенце..."
    return

label cam0_eric_ann_fucking:
    if peeping['ann_eric_sex1'] > 2:
        # уже все посмотрели через окно или камеру
        if 'eric_fuck_end' not in cam_flag:
            $ cam_flag.append('eric_fuck_end')
            $ pose2_3 = renpy.random.choice(['01', '02', '03'])
            $ renpy.show('Eric cams fuck relax '+pose2_3, at_list=[laptop_screen])
            show FG cam-shum-act at laptop_screen
            Max_00 "Утомлённые мама с Эриком лежат на кровати, но всё самое интересное уже закончилось..."
        else:
            $ renpy.show('Eric cams fuck relax '+pose2_3, at_list=[laptop_screen])
            show FG cam-shum-act at laptop_screen
    else:
        if 'eric_fuck0' not in cam_flag:
            $ cam_flag.append('eric_fuck0')
            $ fuck_scene = renpy.random.choice([6,1,2,3,4,5,6,7,1,2,3,4,5,6,7,1,2,3,4,5,6,7])
            if fuck_scene == 6:
                show CamAnnEric1 at laptop_screen
            else:
                $ renpy.show('Eric cams fuck 0'+str(fuck_scene), at_list=[laptop_screen])
            show FG cam-shum-act at laptop_screen
            if peeping['ann_eric_sex1'] == 2:
                # Макса поймали на подглядывании
                Max_00 "Через окно посмотреть не удалось, заценим через камеру... А они тут развлекаются, как могут..."
            elif peeping['ann_eric_sex1'] == 1:
                # ушли от закрытой двери
                Max_00 "Посмотреть через окно я не рискнул, могут поймать, а вот через камеру могу наслаждаться безнаказанно... А посмотреть есть на что..."
            else:
                # вообще не подходили к двери
                Max_00 "Ого! Вот это я удачно заглянул! Ничуть не хуже порно!!!"
        elif tm[-2:] == '50' and 'eric_fuck_fin' not in cam_flag:
            # конец часа, финал траха
            $ peeping['ann_eric_sex1'] = 4
            $ cam_flag.append('eric_fuck_fin')
            $ pose2_3 = renpy.random.choice(['01', '02', '03'])
            $ renpy.show('Eric cams fuck 0'+str(fuck_scene)+'a', at_list=[laptop_screen])
            show FG cam-shum-act at laptop_screen
            Max_00 "Ну вот и закономерный финал..."
        else:
            if fuck_scene == 6:
                show CamAnnEric1 at laptop_screen
            else:
                $ renpy.show('Eric cams fuck 0'+str(fuck_scene), at_list=[laptop_screen])
            show FG cam-shum-act at laptop_screen

    return
