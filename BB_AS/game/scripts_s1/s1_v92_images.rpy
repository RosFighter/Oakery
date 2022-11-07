
layeredimage alice_talk_terrace:
    if tm > '12:00':
        'BG talk-terrace-00'
    else:
        'BG after-breakfast'
    always 'Alice talk-terrace 02[alice.dress]'
    always 'Max talk-terrace 01[mgg.dress]'

layeredimage alice_dressed_in_shoping:
    always 'BG char Alice voyeur-[var_stage]'
    if var_stage == '00':
        'Alice voyeur [var_dress]'
    else:
        'Alice voyeur alt-[var_dress]'
    always 'FG voyeur-morning-[var_stage][mgg.dress]'

layeredimage alice_date_max:
    always 'BG delivery-00'
    always 'Alice date gate-max&alice-01'

layeredimage alice_roard_max:
    image_format 'Alice date {image}'
    always 'road-01'
    always 'road-01-max&alice-[var_stage]'

layeredimage thinking_max_terrace:
    if tm > '12:00':
        'BG talk-terrace-00'
    else:
        'BG after-breakfast'
    always 'Max talk-terrace 00[mgg.dress]'

layeredimage alice_wakes_max_up:
    always 'BG char Alice spider-night-[var_stage]'
    attribute mgg:
        'Max spider-night [var_stage]-[var_pose2]'
    always 'Alice spider-night [var_stage]-[var_pose][var_dress]'

layeredimage alice_talk_max_aliceroom:
    always 'BG char Alice spider-night-[var_stage]'
    always 'Alice spider-night [var_stage]-[var_pose][var_dress]'
    always 'Max spider-night [var_stage]-[var_pose2]'

layeredimage sleep_with_alice_night:
    # aliceroom-bedalice-night-02 + aliceroom-bedalice-n-01-alice&max-01 + одежда Алисы
    always 'BG char Alice bed-night-02'
    always 'Alice sleep-with-max n-01-alice&max-01'
    if alice.sleeptoples:
        'Alice sleep-with-max n-01-alice-01[alice.dress]1'
    elif not alice.sleepnaked:
        'Alice sleep-with-max n-01-alice-01[alice.dress]'

layeredimage sleep_with_alice_morning:
    image_format 'Alice sleep-with-max {image}'
    always 'aliceroom-bedalice-m-[var_stage]'
    group alice_max:
        attribute body default:
            'aliceroom-bedalice-m-[var_stage]-alice&max-[var_pose]'
        attribute full:
            'aliceroom-bedalice-m-[var_stage]-alice&max-[var_pose][var_dress]'
    if not alice.sleepnaked:
        if_not 'full'
        'aliceroom-bedalice-m-[var_stage]-alice-[var_pose][var_dress]'
    attribute top:
        'aliceroom-bedalice-m-[var_stage]-alice-[var_pose][var_dress]'
    attribute cum:
        'aliceroom-bedalice-m-[var_stage]-alice&max-[var_pose]cum[var_cum]'

layeredimage clothigshop_max_alice:
    image_format 'Alice clothingshop {image}'
    always 'clothingshop-01-max&alice-01'

layeredimage clothigshop_christine:
    image_format 'Alice clothingshop {image}'
    always 'clothingshop-02'
    always 'clothingshop-02-christine-[var_stage][var_dress2]'

layeredimage alice_fittingroom:
    image_format 'Alice fittingroom {image}'
    always 'fittingroom-[var_stage]-alice-[var_pose][var_dress]'
    if var_stage == '03':
        'fittingroom-[var_stage]-max-[var_pose2]d'

layeredimage alice_near_shower:
    always 'BG char Alice spider-bathroom-01'
    always 'Alice spider-shower [var_stage][var_pose]'
    attribute mgg:
        'Max spider-bathroom [var_pose2][mgg.dress]'

layeredimage alice_shower_closer:
    always 'bathroom-shower-01'
    always 'Alice shower-closer [var_pose]'
    always 'FG shower-water'

layeredimage alice_shower_with_max:
    always 'bathroom-shower-01'
    always 'Alice shower-closer [var_pose]' xpos -200
    always 'Max shower [var_pose2]' xpos 200
    always 'FG shower-water'

layeredimage alice_max_shower:
    always 'bathroom-shower-[var_stage]'
    always 'bathroom-shower-[var_stage]-max-[var_pose]'
    always 'bathroom-shower-[var_stage]-alice-[var_pose]'
    always 'FG shower-water'

layeredimage alice_max_shower_2:
    always 'bathroom-shower-[var_stage]'
    always 'bathroom-shower-[var_stage]-alice&max-[var_pose]'
    attribute cum:
        'bathroom-shower-[var_stage]-alice&max-[var_pose]cum[var_pose2]'
    attribute penis:
        'bathroom-shower-[var_stage]-alice&max-[var_pose]x'
    group fg:
        attribute water default:
            if_not 'no_water'
            'FG shower-water'
    attribute no_water null

layeredimage alice_max_shower_3:
    always 'bathroom-shower-[var_stage]'
    always 'shower-[var_stage]-alice-[var_pose]'
    always 'shower-[var_stage]-max-[var_pose2]'

layeredimage alice_max_shower_4:
    always 'bathroom-shower-[var_stage]'
    always 'bathroom-shower-[var_stage]-max-[var_pose2]'
    always 'bathroom-shower-[var_stage]-alice-[var_pose]'
    always 'FG shower-water'

layeredimage alice_max_shower_00_04:
    always 'BG char Alice spider-bathroom-00'
    always 'spider-bathroom-00-alice-04'
    always 'spider-bathroom-00-max-04'

layeredimage spider_out_gate:
    always 'BG delivery-01'
    always 'Alice spider-shower-max villa-spider-max-05'

layeredimage alice_near_shower_hug:
    always 'BG char Alice spider-bathroom-[var_stage]'
    always 'Alice spider-shower-max spider-shower-[var_stage]-max-[var_pose]c-alice-[var_pose]'

layeredimage alice_near_shower_hug2:
    always 'BG bathroom-shower-01'
    always 'Alice spider-shower-max spider-shower-[var_stage]-max-[var_pose]c-alice-[var_pose]'

layeredimage alice_before_punish_sun:
    always 'BG punish-sun 01'
    always 'punish-sun-01-alice-01'
    always 'punish-sun-01-max-01[mgg.dress]'

layeredimage alice_punish_sun:
    always 'BG punish-sun [var_stage]'
    always 'punish-sun-[var_stage]-max-[var_pose][mgg.dress]-alice-[var_pose][var_dress]'

layeredimage alice_hard_punish_sun:
    group back:
        attribute BG default:
            'BG punish-sun [var_stage]'
        attribute full:
            'punish-sun-[var_stage]-alice&max-[var_pose]c'
    group core:
        attribute body default:
            'punish-sun-[var_stage]-alice&max-[var_pose][mgg.dress]'
    if mgg.dress == 'b':
        if_all 'full'
        'punish-sun-[var_stage]-alice&max-[var_pose]b'
    attribute cum:
        'punish-sun-[var_stage]-alice&max-[var_pose]-cum[var_cum]'

layeredimage alice_before_domin:
    always 'BG char Alice evening'
    always 'domin-00-max-01[mgg.dress]'
    always 'domin-00-alice-01'

layeredimage alice_domin:
    always 'domin-[var_stage]'
    always 'domin-[var_stage]-max-[var_pose][var_dress2]-alice-[var_pose][var_dress]'
    attribute cum:
        'domin-[var_stage]-max-[var_pose][var_dress2]-alice-[var_pose][var_dress]-cum[var_cum]'

layeredimage alice_punishes_max:
    if var_stage == '00':
        'blog-desk-01'
    else:
        'aliceroom-punish-[var_stage]'
    always 'aliceroom-punish-[var_stage]-alice-[var_pose]'
    always 'aliceroom-punish-[var_stage]-max-[var_pose2][var_dress]'

layeredimage alice_sunscreen:
    if var_stage in ['07', '08']:
        'sun-alone-07'
    elif var_stage == '09':
        'sun-alone-01'
    else:
        'sun-alone-[var_stage]'
    if var_stage == '01':
        'sun-alone-01-alice-01[var_dress]'
    else:
        'sun-alone-[var_stage]-max-01[var_dress2]-alice-01[var_dress]'
    if var_stage == '01':
        'sun-alone-01-max-01[var_dress2]'
    attribute spider:
        'sun-alone-[var_stage]-spider'

layeredimage alice_sun_alone:
    always 'alice-sun-alone-00'
    if alice.req.result == 'bikini' or all([alice.daily.oiled in [2, 4], alice.flags.shower_max > 2]):
        'alice-sun-alone-01b'
    elif alice.daily.oiled in [2, 4]:
        'alice-sun-alone-01a'
    else:
        'alice-sun-alone-01'

layeredimage alice_spider_sun:
    always 'spider-sun-[var_stage]'
    always 'spider-sun-[var_stage]-max-[var_pose][var_dress2]-alice-[var_pose][var_dress]'
    if var_stage == '01':
        'spider-sun-01-spider'

layeredimage alice_hugging:
    group BG:
        attribute sun:
            'hugging-sun-01'
        attribute terrace:
            'hugging-terrace-01'
        attribute aliceroom:
            'BG char Alice newdress'
    group bpdy:
        attribute sun:
            'hugging-sun-max-[var_pose][var_dress2]-alice-[var_pose][var_dress]'
        attribute terrace:
            'hugging-terrace-max-[var_pose][var_dress2]-alice-[var_pose][var_dress]'
    if '09:00' <= tm < '20:00':
        if_all 'aliceroom'
        'hugging-aliceroom-max-[var_pose][var_dress2]-alice-01[var_dress]'
    else:
        if_all 'aliceroom'
        'hugging-aliceroom-max-[var_pose][var_dress2]-alice-02[var_dress]'

layeredimage alice_tv_01:
    always 'tv-mass-[var_stage]'
    always 'tv-mass-[var_pose]-max-01[var_dress2]-alice-01[var_dress]'

layeredimage alice_tv_02:
    if var_pose == '17':
        'tv-cun-01'
    elif var_pose in ['21', '24']:
        'tv-sex03-01'
    else:
        'tv-mass-[var_stage]'
    always 'tv-mass-[var_pose]-max-01[var_dress2]'
    always 'tv-mass-[var_pose]-alice-01[var_dress]'
    if var_dress == 'b':
        if_all 'nopants'
        'tv-mass-[var_pose]-alice-01bn'
    attribute nopants null

layeredimage alice_tv_03:
    always 'tv-mass-[var_stage]'
    always 'tv-mass-[var_pose]-max-01[var_dress2]-alice-01[var_dress]'
    if var_dress == 'b':
        if_all 'nopants'
        'tv-mass-[var_pose]-alice-01bn'
    attribute nopants null

layeredimage alice_tv_hj:
    if var_pose == '01':
        'tv-mass-03'
    else:
        'tv-mass-05'
    always 'tv-mass-hj01-max-[var_pose][var_dress2]'
    always 'tv-mass-hj01-alice-[var_pose][var_dress]'

layeredimage alice_tv_lick:
    if var_pose == '01':
        'tv-sex03-01'
    else:
        'after-club-s04-f'
    always 'tv-mass-lick01-max-[var_pose][var_dress2]'
    always 'tv-mass-lick01-alice-[var_pose][var_dress]'

layeredimage alice_tv_bj_01:
    if var_pose == '01':
        'lounge-tv-01'
    else:
        'tv-sex02-01'
    always 'tv-mass-bj01-max-[var_pose][var_dress2]'
    always 'tv-mass-bj01-alice-[var_pose][var_dress]'

layeredimage alice_tv_bj_02:
    always 'tv-mass-01'
    always 'tv-mass-bj02-max-03[var_dress2]'
    always 'tv-mass-bj02-alice-03[var_dress]'

layeredimage alice_tv_cum:
    always 'tv-mass-15'
    always 'tv-mass-cum01-alice-01[var_dress]'
    always 'tv-mass-cum01-max-01[var_dress2]'
    always 'tv-mass-cum01-max&alice-01[var_pose]'

layeredimage alice_tv_jeens_off:
    always 'tv-mass-03'
    if alice.req.result == 'nopants':
        'tv-mass-[var_pose]-max-02[var_dress2]-alice-02a'
    else:
        'tv-mass-[var_pose]-max-02[var_dress2]-alice-02'

layeredimage alice_tv_ups:
    always 'tv-mass-03'
    always 'tv-mass-[var_pose]-alice-03[var_dress]'
    always 'tv-mass-[var_pose]-max-03[var_dress2]'

layeredimage alice_bath_mirror:
    always 'after-club-01'
    always 'after-club-01-alice-[var_pose][var_dress]'
    always 'after-club-01-max-[var_pose2]'

layeredimage alice_bath_mirror_01:
    always 'after-club-[var_stage]'
    always 'after-club-[var_stage]-max-[var_pose]-alice-[var_pose][var_dress]'

layeredimage alice_bath_mirror_02:
    always 'after-club-[var_stage]'
    group body:
        attribute alice_max default:
            'after-club-[var_stage]-max&alice-[var_pose]'
        attribute bj:
            'after-club-[var_stage]-max&alice-bj[var_pose]'
        attribute cum:
            'after-club-[var_stage]-max&alice-cum[var_pose]'
    attribute cum:
        'after-club-[var_stage]-max&alice-cum[var_pose][var_pose2]'

layeredimage alice_open_bath:
    always 'bath-open-00'
    always 'bath-open-alice-01'

layeredimage alice_bath_talk:
    if var_pose == '01':
        'bath-talk-03-max&alice-01-f'
    else:
        'bath-talk-02'
    if var_pose == '01':
        'bath-talk-03-max&alice-01'
    else:
        'bath-talk-02-alice-01'
    if var_pose != '01':
        'bath-talk-02-max-[var_pose]'

layeredimage alice_in_bath_01:
    always 'bath-talk-03-max&alice-01-f'
    if var_pose == '01':
        'after-club-bathbj01-max&alice-01a'
    else:
        'after-club-bath[var_pose]b-max&alice-01'

layeredimage alice_in_bath_02:
    always 'after-club-bath01-max&alice-01-f'
    always 'after-club-bath[var_pose]-max&alice-01'

layeredimage alice_in_bath_03:
    always 'after-club-bath[var_pose]-max&alice-02-f'
    always 'after-club-bath[var_pose]-max&alice-02'

layeredimage alice_in_bath_bj:
    always 'after-club-bath02a-max&alice-02-f'
    always 'after-club-bathbj01-max&alice-02'

layeredimage alice_in_bath_bj_01:
    always 'after-club-bathbj01-max&alice-02a-f'
    always 'after-club-bathbj01-max&alice-[var_pose]'

layeredimage alice_in_bath_bj:
    always 'after-club-bathbj01-max&alice-03-f'
    always 'after-club-bathbj01-max&alice-[var_pose]'

layeredimage alice_in_bath_cum:
    always 'after-club-bathbj01-max&alice-03-f'
    always 'after-club-bathbj01-max&alice-[var_pose]'
    always 'after-club-bathbj01-max&alice-[var_pose]a'

layeredimage alice_in_bath_cun:
    always 'bath-cun-02'
    if var_pose == '01':
        'after-club-bathbj01-max&alice-01'
    else:
        'after-club-bath01-max&alice-02'
