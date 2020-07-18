
label cam0_alice_read:
    # if '06:00' <= cam_tm < '21:00':
    #     scene BG char Max laptop-day-01
    # else:
    #     scene BG char Max laptop-night-01
    show BG-cam house terrace-0 day at laptop_screen
    $ renpy.show('Alice cams reading '+renpy.random.choice(['01', '02', '03'])+alice.dress, at_list=[laptop_screen])
    show FG cam-shum-act at laptop_screen
    return
