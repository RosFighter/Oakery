
label cam0_olivia_lisa_sun:
    $ renpy.show('Olivia cams 2sun '+cam_poses_manager(olivia, ['01', '02', '03'])+olivia.dress, at_list=[laptop_screen])
    $ renpy.show('Lisa cams sun '+cam_poses_manager(lisa, ['01', '02', '03'])+lisa.dress, at_list=[laptop_screen])
    show FG cam-shum-act at laptop_screen
    if 'olivia_lisa_sun' not in cam_flag:
        $ cam_flag.append('olivia_lisa_sun')
        Max_01 "Благодаря натуризму Оливии, внимания ко двору станет побольше..."
    return


label cam1_olivia_lisa_sun:
    call cam1_lisa_sun from _call_cam1_lisa_sun
    return


label cam0_olivia_lisa_swim:
    call cam0_lisa_swim from _call_cam0_lisa_swim
    return


label cam1_olivia_lisa_swim:
    $ renpy.show('Lisa cams swim '+cam_poses_manager(lisa, ['01', '02', '03'])+lisa.dress, at_list=[laptop_screen])
    $ renpy.dynamic('olivia_pose_list')
    # Под Лизу 01 подойдут все три варианта с Оливией. Под Лизу 02 подойдет только Оливия 03. Под Лизу 03 подойдет только Оливия 01 и 02.
    $ olivia_pose_list = {'01' : ['01', '02', '03'], '02' : ['03'], '03' : ['01', '02']}[cam_poses_manager(lisa, ['01', '02', '03'])]
    $ renpy.show('Olivia cams 2swim '+cam_poses_manager(olivia, olivia_pose_list)+olivia.dress, at_list=[laptop_screen])
    show FG cam-shum-act at laptop_screen
    if 'lisa_swim1' not in cam_flag:
        $ cam_flag.append('lisa_swim1')
        Max_01 "Приятно наблюдать за младшей сестрёнкой у водички и тем, как Оливия светит своими прелестями..." id cam1_olivia_lisa_swim_c66f3478
    return


label cam0_olivia_lisa_tv:
    $ renpy.show('Olivia cams night-tv '+cam_poses_manager(olivia, ['01', '02', '03'])+lisa.dress, at_list=[laptop_screen])
    show FG cam-shum-act at laptop_screen

    if 'olivia_lisa_tv' not in cam_flag:
        $ cam_flag.append('olivia_lisa_tv')
        if lisa.dress < 'd':
            Max_01 "Девчонки смотрят сериалы... Жду не дождусь, когда Лиза тоже начнёт смотреть их голой, как Оливия!"
        else:
            pass
            # Max_01 ""
    return


label cam0_olivia_lisa_sleep:
    $ renpy.show('Olivia cams sleep '+cam_poses_manager(olivia, ['02', '03'])+lisa.dress, at_list=[laptop_screen])
    show FG cam-shum-act at laptop_screen
    if 'olivia_lisa_sleep' not in cam_flag:
        $ cam_flag.append('olivia_lisa_sleep')
        Max_01 "Красавицы сладко спят..."
    return
