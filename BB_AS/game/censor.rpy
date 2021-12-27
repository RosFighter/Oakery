init -100 python:
    from collections import OrderedDict
    replace_dict_ru = OrderedDict([
        ("родную сестру"    , "лучшую сожительницу"),
        ("родной сестрой"   , "лучшей сожительницей"),
        ("родная тётя"      , "лучшая соседка"),
        ("родной тёте"      , "лучшей соседке"),
        ("родной матери"    , "хозяйке"),
        ("родные дочери"    , "другие съёмщицы"),
        ("семейный рейтинг" , "семейный рейтинг"),
        ("по семейному"     , "по дружески"),
        ("с братьями и старшими сёстрами", "между сожителями"),
        ("тётя кира"        , "Кира"),
        ("тёти киры"        , "Киры"),
        ("тёте кире"        , "Кире"),
        ("тётю киру"        , "Киру"),
        ("тётей кирой"      , "Кирой"),
        ("сукин сын"        , "сукин сын"),
        ("моя дочь"         , "моя съемщица"),
        ("мою дочь"         , "мою съемщицу"),
        ("приёмная "        , ""),
        ("мать"             , "хозяйка"),
        ("матери"           , "хозяйке"),
        ("матерью"          , "хозяйкой"),
        ("ма-ам"            , "хозяйка"),
        ("мам"              , "хозяйка"),
        ("мама"             , "хозяйка"),
        ("мамы"             , "хозяйки"),
        ("маме"             , "хозяйке"),
        ("маму"             , "хозяйку"),
        ("мамой"            , "хозяйкой"),
        ("мамин"            , "хозяйкин"),
        ("мамина"           , "хозяйкина"),
        ("мамину"           , "хозяйкину"),
        ("мамино"           , "хозяйкино"),
        ("мамины"           , "хозяйкины"),
        ("маминого"         , "хозяйкиного"),
        ("маминых"          , "хозяйкиных"),
        ("маминой"          , "хозяйкиной"),
        ("мамином"          , "хозяйкином"),
        ("мамкай"           , "хозяйкай"),
        ("тётя"             , "соседка"),
        ("тёти"             , "соседки"),
        ("тёте"             , "соседке"),
        ("тётю"             , "соседку"),
        ("тётей"            , "соседкой"),
        ("дочка"            , "съёмщица"),
        ("сынок"            , "красавчик"),
        ("сын"              , "постоялец"),
        ("сына"             , "постояльца"),
        ("сыну"             , "постояльцу"),
        ("сыном"            , "постояльцем"),
        ("сыне"             , "постояльце"),
        ("сестрёнка"        , "сожительница"),
        ("сестрёнки"        , "сожительницы"),
        ("сестрёнке"        , "сожительнице"),
        ("сестрёнку"        , "сожительницу"),
        ("сестрёнкой"       , "сожительницей"),
        ("сестрёнкам"       , "сожительницам"),
        ("сестра"           , "сожительница"),
        ("сестры"           , "сожительницы"),
        ("сестре"           , "сожительнице"),
        ("сестру"           , "сожительницу"),
        ("сестрой"          , "сожительницей"),
        ("сёстры"           , "сожительницы"),
        ("сестёр"           , "сожительниц"),
        ("сёстрам"          , "сожительницам"),
        ("сёстрами"         , "сожительницами"),
        ("сёстрах"          , "сожительницах"),
        ("брат"             , "сожитель"),
        ("братьями"         , "сожителями"),
        ("брата"            , "сожителя"),
        ("брату"            , "сожителю"),
        ("братом"           , "сожителем"),
        ("братишка"         , "сожитель"),
        ("братика"          , "сожителя"),
        ("усыновила"        , "приютила"),
        ("семья"            , "тусовка"),
        ("семьи"            , "тусовки"),
        ("семье"            , "тусовке"),
        ("семью"            , "тусовку"),
        ("семьёй"           , "тусовкой"),
        ("семейный"         , "совместный"),
        ("семейной"         , "совместной"),
        ("семейное"         , "общее"),
        ("племянник"        , "сосед"),
        ("племянника"       , "соседа"),
        ("племянничек"      , "соседушка"),
        ("мои дети"         , "мои арендаторы"),
        ("твоих детей"      , "детей"),
        ("её дети"          , "её арендаторы"),
        ("ваши дети"        , "ваши арендаторы"),
        ("наш отец"         , "мой отец"),
        ("ваш отец"         , "мой бывший муж"),
        ("отец"             , "бывший муж Анны"),
        ("я папу"           , "я твоего бывшего мужа"),
    ])
    replace_dict_en = OrderedDict([
        ("own sister"       , "best friend"),
        ("own aunt"         , "best neighbor"),
        ("own mother"       , "best landlady"),
        ("daughters"        , "tenants"),
        ("mother"           , "landlady"),
        ("mom"              , "landlady"),
        ("mo-om"            , "landlady"),
        ("mo-o-om"          , "landlady"),
        ("aunt"             , "neighbor"),
        ("son"              , "tenant"),
        ("sis"              , "roommate"),
        ("sister"           , "roommate"),
        ("sisters"          , "roommates"),
        ("brother"          , "roommate"),
        ("siblings"         , "roommates"),
        ("adoptive "        , ""),
        ("adopted"          , "contracted"),
        ("family"           , "household"),
        ("nephew"           , "neighbor"),
        ("my children"      , "my tenants"),
        ("your children"    , "you tenants"),
        ("her children"     , "her tenants"),
        ("your father was"  , "my ex-husband was"),
        ("maybe dad used"   , "Maybe Ann's ex-husband used"),
    ])
    replace_dict_de = OrderedDict([
        ("eigenen schwester"    , "besten Freundinen"),
        ("eigene schwester"     , "beste Freundin"),
        ("eigenen tante"        , "besten Nachbarin"),
        ("eigene tante"         , "beste Nachbarin"),
        ("eigene mutter"        , "beste Vermieterin"),
        ("töchter"              , "mieterinnen"),
        ("mutter"               , "vermieterin"),
        ("moom"                 , "vermieterin"),
        ("mo-om"                , "vermieterin"),
        ("mo-o-om"              , "vermieterin"),
        ("mom"                  , "vermieterin"),
        ("moms"                 , "vermieterins"),
        ("tante"                , "nachbarin"),
        ("sohn"                 , "mieter"),
        ("schwester"            , "freundin"),
        ("schwestern"           , "freundinnen"),
        ("schwesterchen"        , "freundin"),
        ("schwesterherz"        , "freundinherz"),
        ("bruder"               , "freund"),
        ("bruders"              , "freunds"),
        ("brüdern"              , "freunden"),
        ("adoptierte"           , "zugezogene"),
        ("adoptivmutter"        , "Ersatz-Vermieterin"),
        ("familie"              , "haushalt"),
        ("familienunternehmen"  , "firma"),
        ("familienessen"        , "firmenfest"),
        ("neffe"                , "nachbar"),
        ("lieblingstante"       , "beste nachbarin"),
        ("meine kinder"         , "meine mieterinnen"),
        ("ihre kinder"          , "ihre mieterinnen"),
        ("unser vater"          , "mein Vater"),
        ("hat dein vater"       , "hat mein Ex-Mann"),
        ("vater"                , "vermieter"),
        ("hatte dad"            , "hatte Annas Ex-Mann"),
    ])
    replace_dict_fr = OrderedDict([
    ])
    replace_dict_it = OrderedDict([
    ])
    replace_dict_pl = OrderedDict([
    ])
    replace_dict_pr = OrderedDict([
    ])
    replace_dict_sp = OrderedDict([
    ])
    replace_dict_sl = OrderedDict([
    ])

init python:
    import re
    def game_text_mod(st0):
        if _preferences.language is None:
            replace_dict = replace_dict_ru
        elif _preferences.language=='english':
            replace_dict = replace_dict_en
        elif _preferences.language=='german':
            replace_dict = replace_dict_de
        elif _preferences.language=='french':
            replace_dict = replace_dict_fr
        elif _preferences.language=='italian':
            replace_dict = replace_dict_it
        elif _preferences.language=='polish':
            replace_dict = replace_dict_pl
        elif _preferences.language=='portuguese':
            replace_dict = replace_dict_pr
        elif _preferences.language=='spanish':
            replace_dict = replace_dict_sp
        elif _preferences.language=='slovak':
            replace_dict = replace_dict_sl
        else:
            return st0
        rc = re.compile('\\b|\\b'.join(map(re.escape, replace_dict)), re.U+re.I)
        def transplate(match):
            key = match.group(0).lower()
            suffix = ""
            value = ""
            if "'s" in key:
                key = key[:-2]
                suffix = "'s"
            if match.group(0).istitle():
                value = replace_dict[key].title()
            elif match.group(0).isupper():
                value = replace_dict[key].upper()
            elif match.group(0).islower():
                value = replace_dict[key]
            elif match.group(0)[0].isupper():
                value = replace_dict[key].title()
            else:
                value = replace_dict[key]
            return value + suffix
        st1 = rc.sub(transplate, st0)

        return st1

default persistent.patch_enabled = False

init:
    $ config.say_menu_text_filter = game_text_mod
