
label cam0_ann_read:
    show BG-cam house terrace-0 day at laptop_screen
    $ renpy.show('Ann cams reading '+renpy.random.choice(['01', '02', '03'])+ann.dress, at_list=[laptop_screen])
    show FG cam-shum-act at laptop_screen
    return


label cam0_ann_yoga:
    show BG-cam house courtyard-0 morning at laptop_screen
    if int(tm[3:4])%3 == 0: # смена позы каждые 10 минут
        $ renpy.show('Ann cams yoga 0'+str(renpy.random.randint(1, 3)), at_list=[laptop_screen])
    elif int(tm[3:4])%3 == 1:
        $ renpy.show('Ann cams yoga 0'+str(renpy.random.randint(4, 6)), at_list=[laptop_screen])
    else:
        $ renpy.show('Ann cams yoga 0'+str(renpy.random.randint(7, 9)), at_list=[laptop_screen])
    show FG cam-shum-act at laptop_screen
    return
