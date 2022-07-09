
layeredimage tv_watch:
    image_format 'tv {image}'
    always 'tv-watch-01'
    always:
        pos (63, 48)
        '[var_film][var_stage]'
    attribute ann:
        'tv-watch-01-ann-01'
    attribute kira:
        'tv-watch-01-kira-01'
    attribute mgg:
        'tv-watch-01-max-01[mgg.dress]'
    attribute ann_max:
        'tv-watch-01-max&ann-01[mgg.dress]'
    attribute olivia:
        'tv-watch-01-lisa&olivia-01[lisa.dress]'
    attribute olivia_max:
        'tv-watch-01-lisa,olivia,max-01[lisa.dress]'

layeredimage tv_talk:
    image_format 'tv {image}'
    always 'lounge-tv-01'
    attribute alice:
        'tv-alice-[pose3_2][alice.dress]'
    attribute ann:
        'tv-ann-[pose3_3]'
    attribute olivia:
        'tv-watch-03-lisa&olivia-[var_stage][lisa.dress]'
    attribute kira:
        'tv-kira-[pose3_4]'
    attribute kira_m:
        'tv-kira-m-[pose3_4]'
    if tm < '06:00' and mgg.dress in ['a', 'b']:
        'tv-max-[var_pose]c'
    else:
        'tv-max-[var_pose][mgg.dress]'


################################    Ann     ####################################

layeredimage Ann_drink_cam:
    # cam-lounge-04a-night-829p + cam-lounge-ann-drunk-01a-829p
    image_format 'Ann cams drink {image}'
    always 'cam-lounge-04a-night-829p'
    always 'cam-lounge-ann-drunk-01a-829p'

layeredimage Ann_drink:
    image_format 'Ann drink {image}'

    group bg:
        attribute far default:
            'lounge-night-01-ann-01-drunk'
        attribute closer:
            'lounge-night-02'

    group body:
        attribute closer:
            'lounge-night-02-ann&max-01-drunk'

    group ann_clot:
        if_not 'ann_naked'
        attribute far default:
            'lounge-night-01-ann-01a-drunk'
        attribute closer:
            'lounge-night-02-ann-01a-drunk'

    group max_clot:
        if_not 'max_naked'
        attribute closer:
            'lounge-night-02-max-01[mgg.dress]-drunk'

    attribute ann_naked null
    attribute max_naked null

layeredimage Ann_sleep_drink:
    image_format 'Ann sleep-drink {image}'

    group bg:
        attribute door:
            'annroom-night-door-01'
        attribute bed default:
            if_not 'no_bg'
            'annroom-bedann-night-[var_stage]'
    group body:
        attribute door:
            'annroom-night-door-01-ann&max-01'
        attribute bed default:
            'annroom-bedann-night-[var_stage]-ann&max-[var_pose]'
    group ann_clot:
        attribute door:
            'annroom-night-door-01-ann-01a'
    group max_clot:
        attribute door:
            'annroom-night-door-01-max-01[mgg.dress]'

    if var_stage == '02' and var_pose in ['03', '04']:
        if_all 'mask'
        'annroom-bedann-night-02-ann-03z&04z'
    elif var_stage == '04' and var_pose in ['02', '03']:
        if_all 'mask'
        'annroom-bedann-night-04-ann-02z&03z'
    else:
        if_all 'mask'
        'annroom-bedann-night-[var_stage]-ann-[var_pose]z'

    attribute cum0:
        'annroom-bedann-night-[var_stage]-ann-01cum1'
    attribute cum:
        'annroom-bedann-night-[var_stage]-ann-[var_pose]cum'

    if var_stage == '02':
        if_not 'naked'
        'annroom-bedann-night-02-ann-[var_pose]a'
    elif var_stage in ['04', '05']:
        if_not 'naked'
        'annroom-bedann-night-[var_stage]-ann-[var_pose]b'

    if var_stage == '02':
        if_not 'naked'
        'annroom-bedann-night-02-max-01[mgg.dress]'
    elif var_stage == '03':
        'annroom-bedann-night-03-max-01[mgg.dress]02[mgg.dress]'
    else:
        if_not ['door', 'naked']
        'annroom-bedann-night-[var_stage]-max-[var_pose]c'

    if var_stage == '06':
        if_not 'naked'
        'annroom-bedann-night-06-ann-00b'
    elif var_stage == '03' and var_pose == '01':
        'annroom-bedann-night-03-ann-01a'
    elif var_stage == '03' and var_pose == '02':
        'annroom-bedann-night-03-ann-02b'

    attribute naked null
    attribute mask null
    attribute no_bg null

layeredimage Ann_Max_sleep:
    image_format 'Ann sleep {image}'
    always 'annroom-bedann-n-01'
    always 'annroom-bedann-n-01-ann&max-sleep-[var_pose]'
    always:
        if_not 'ann_naked'
        'annroom-bedann-n-01-ann&max-sleep-01b'
    always 'annroom-bedann-n-01-max-sleep-[var_pose]c'
    attribute mask:
        'annroom-bedann-n-01-ann&max-sleep-[var_pose]z'
    attribute ann_naked null

layeredimage Ann_Max_wakeup:
    if var_pose == '01':
        'BG char Kira annroom-shot 03 02'
    else:
        'Ann sleep annroom-bedann-m-01'
    always 'Ann sleep annroom-bedann-m-01-ann&max-[var_pose]'
    always 'Ann sleep annroom-bedann-m-01-max-[var_pose]c'

layeredimage ann_in_bath_open:
    # bath-open-00 + bath-open-ann-01
    always 'BG bath-open-00'
    always 'Ann bath bath-open-ann-01'

layeredimage ann_in_bath_enter:
    # bathrooom-bath-02 + bathrooom-bath-02-ann-00
    always 'BG bathrooom-bath-02'
    always 'Ann bath bathrooom-bath-02-ann-[var_pose]'

layeredimage ann_in_bath_talk:
    always 'BG after-club-bath01'
    always 'Ann bath bathrooom-bath-[var_stage]-ann&max-[var_pose]'
    always 'Ann bath bathrooom-bath-[var_stage]-max-01[mgg.dress]'

layeredimage ann_in_bath1:
    image_format 'Ann bath {image}'
    always 'bathrooom-bath-[var_stage]'
    always 'bathrooom-bath-[var_stage]-ann&max-[var_pose]'
    attribute cum:
        'bathrooom-bath-[var_stage]-ann&max-[var_pose]cum'

layeredimage ann_in_bath2:
    image_format 'Ann bath {image}'
    always 'bathrooom-bath-[var_stage]'
    if var_stage == '10':
        'bathrooom-bath-01-max-01'
    else:
        'bathrooom-bath-[var_stage]-ann-[var_pose]'
    if var_stage == '10':
        'bathrooom-bath-01-ann-[var_pose]'
    else:
        'bathrooom-bath-[var_stage]-max-[var_pose]'
    attribute cum:
        'bathrooom-bath-[var_stage]-max-[var_pose]cum'

layeredimage ann_in_bath3_cum:
    always 'BG bath-sex-01'
    always 'Ann bath bathrooom-bath-05-ann&max-03'
    always 'Ann bath bathrooom-bath-05-ann&max-03cum'

layeredimage ann_tv_ero_00:
    always 'BG tv-kiss-03'
    always 'tv tv-ero-00-max-[var_pose][mgg.dress]'
    always 'tv tv-ero-00-ann-[var_pose]'

layeredimage ann_tv_ero_01:
    always 'BG tv-mass-03'
    always 'tv tv-ero-01-max-01[mgg.dress]'
    always 'tv tv-ero-01-ann-[var_pose]'

layeredimage ann_tv_ero_02:
    always 'BG tv-mass-05'
    always 'tv tv-ero-01-max-02[mgg.dress]'
    always 'tv tv-ero-01-ann-[var_pose]'

layeredimage ann_tv_ero_03:
    always 'BG tv-mass-07'
    always 'tv tv-ero-01-max-03[mgg.dress]'
    always 'tv tv-ero-01-ann-[var_pose]'

layeredimage ann_tv_ero_04:
    always 'BG after-club-s08a-f'
    always 'tv tv-ero-03-max-01[mgg.dress]-ann-01'
    attribute towel:
        'tv tv-ero-03-ann-01a'

layeredimage ann_tv_ero_05:
    always 'BG tv-kiss-03'
    always 'tv tv-ero-05-max-02[mgg.dress]-ann-02'

layeredimage ann_tv_ero_06:
    always 'BG tv-sex03-01'
    always 'tv tv-ero-05-max-03[mgg.dress]-ann-03'

layeredimage ann_tv_ero_07:
    always 'BG after-club-s04-f'
    always 'tv tv-ero-05-max-[var_pose][mgg.dress]-ann-[var_pose]'

layeredimage ann_caught_01:
    always 'BG after-club-s04-f'
    always 'tv tv-caught-ann-01[ann.dress]'
    always 'tv tv-caught-max&kira-01'

layeredimage ann_caught_02:
    always 'BG tv-cun-01'
    attribute ann:
        'tv tv-caught-ann-02[ann.dress]'
    always 'tv tv-caught-max&kira-02'

layeredimage ann_caught_03:
    always 'BG after-club-s06-f'
    always 'tv tv-caught-max&kira-03'
    always 'tv tv-caught-ann-03[ann.dress]'

layeredimage ann_caught_04:
    always 'BG after-club-s04-f'
    always 'tv tv-caught-ann-04[ann.dress]'
    always 'tv tv-caught-max&kira-04'

layeredimage ann_caught_05:
    always 'BG lounge-tv-talk-00'
    always 'tv tv-caught-ann-05[ann.dress]'


################################    Kira    ####################################

layeredimage kira_watch_play_02:
    always 'BG tv-mass-05'
    always 'tv tv-wp-02-max-01[var_stage]-kira-01[var_stage]'
