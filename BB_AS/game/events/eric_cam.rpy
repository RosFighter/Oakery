
label cam0_eric_resting:
    $ renpy.show('Eric cams relax '+renpy.random.choice(['01', '02', '03'])+eric.dress, at_list=[laptop_screen])
    if 'eric_resting' not in cam_flag:
        $ cam_flag.append('eric_resting')
        Max_01 "Обезъян в маминой кровати... Бррр..."
    return
