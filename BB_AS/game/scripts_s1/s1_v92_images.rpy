
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

layeredimage alice_talk_about_sleepeng:
    always 'BG char Alice spider-night-03'
    always 'Max spider-night 03-02'
    always 'Alice spider-night 03-04[var_dress]'

layeredimage sleep_with_alice_night:
    # aliceroom-bedalice-night-02 + aliceroom-bedalice-n-01-alice&max-01 + одежда Алисы
    always 'BG char Alice bed-night-02'
    always 'Alice sleep-with-max n-01-alice&max-01'
    if alice.sleeptoples:
        'Alice sleep-with-max n-01-alice-01[alice.dress]a'
    elif not alice.sleepnaked:
        'Alice sleep-with-max n-01-alice-01[alice.dress]'

layeredimage sleep_with_alice_morning:
    image_format 'Alice sleep-with-max {image}'
    always 'aliceroom-bedalice-m-[var_stage]'
    always 'aliceroom-bedalice-m-[var_stage]-alice&max-[var_pose]'
    # if alice.sleeptoples:
    #     'aliceroom-bedalice-m-[var_stage]-alice-[var_pose][alice.dress]1'
    if not alice.sleepnaked:
        'aliceroom-bedalice-m-[var_stage]-alice-[var_pose][alice.dress]'

layeredimage sleep_with_alice_morning_1:
    image_format 'Alice sleep-with-max {image}'
    always 'aliceroom-bedalice-m-[var_stage]'
    always 'aliceroom-bedalice-m-[var_stage]-alice&max-[var_pose][alice.dress]'

layeredimage sleep_with_alice_morning_2:
    image_format 'Alice sleep-with-max {image}'
    always 'aliceroom-bedalice-m-[var_stage]'
    always 'aliceroom-bedalice-m-[var_stage]-alice&max-[var_pose]'
    always 'aliceroom-bedalice-m-[var_stage]-alice-[var_pose][alice.dress]1'

layeredimage sleep_with_alice_morning_3:
    image_format 'Alice sleep-with-max {image}'
    always 'aliceroom-bedalice-m-[var_stage]'
    always 'aliceroom-bedalice-m-[var_stage]-alice&max-[var_pose][alice.dress]'
    always 'aliceroom-bedalice-m-[var_stage]-alice-[var_pose][alice.dress]'

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

layeredimage alice_shower_with_max:
    always 'BG shower-01'
    always 'Alice shower-closer [var_pose]' xpos -200
    always 'Max shower [var_pose2]' xpos 200
    always 'FG shower-water'

layeredimage alice_max_shower:
    always 'Alice spider-shower-max bathroom-shower-[var_stage]'
    always 'Alice spider-shower-max bathroom-shower-[var_stage]-max-[var_pose]'
    always 'Alice spider-shower-max bathroom-shower-[var_stage]-alice-[var_pose]'
    always 'FG shower-water'

layeredimage alice_max_shower_2:
    always 'Alice spider-shower-max bathroom-shower-[var_stage]'
    always 'Alice spider-shower-max bathroom-shower-[var_stage]-alice&max-[var_pose]'
    attribute cum:
        'Alice spider-shower-max bathroom-shower-[var_stage]-alice&max-[var_pose]cum[var_pose2]'
    always 'FG shower-water'

layeredimage alice_max_shower_3:
    always 'BG shower-[var_stage]'
    always 'Alice spider-shower-max bathroom-shower-[var_stage]-alice&max-[var_pose]'
    always 'FG shower-water'

layeredimage alice_max_shower_4:
    always 'BG shower-[var_stage]'
    always 'Alice spider-shower-max shower-[var_stage]-alice-[var_pose]'
    always 'Alice spider-shower-max shower-[var_stage]-max-[var_pose2]'

layeredimage alice_max_shower_5:
    always 'Alice spider-shower-max bathroom-shower-[var_stage]'
    always 'Alice spider-shower-max bathroom-shower-[var_stage]-alice&max-[var_pose]'
    attribute penis:
        'Alice spider-shower-max bathroom-shower-[var_stage]-alice&max-[var_pose]x'

layeredimage alice_max_shower_6:
    always 'Alice spider-shower-max bathroom-shower-[var_stage]'
    always 'Alice spider-shower-max bathroom-shower-[var_stage]-max-[var_pose2]'
    always 'Alice spider-shower-max bathroom-shower-[var_stage]-alice-[var_pose]'
    always 'FG shower-water'

layeredimage alice_max_shower_00_04:
    always 'BG char Alice spider-bathroom-00'
    always 'Alice spider-shower-max spider-bathroom-00-alice-04'
    always 'Alice spider-shower-max spider-bathroom-00-max-04'

layeredimage spider_out_gate:
    always 'BG delivery-01'
    always 'Alice spider-shower-max villa-spider-max-05'

layeredimage alice_near_shower_hug:
    always 'BG char Alice spider-bathroom-[var_stage]'
    always 'Alice spider-shower-max spider-shower-[var_stage]-max-[var_pose]c-alice-[var_pose]'

layeredimage alice_near_shower_hug2:
    always 'BG shower-01'
    always 'Alice spider-shower-max spider-shower-[var_stage]-max-[var_pose]c-alice-[var_pose]'
