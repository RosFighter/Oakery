
label kira_swim:
    scene image 'Kira swim '+pose3_3+kira.dress
    $ persone_button1 = 'Kira swim '+pose3_3+kira.dress+'b'
    return

label kira_sun:
    scene image 'BG char Alice sun'
    $ renpy.show('Kira sun '+pose3_3+kira.dress)
    $ persone_button1 = 'Kira sun '+pose3_3+kira.dress+'b'
    return
