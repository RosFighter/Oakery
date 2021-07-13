init python:
    import re
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
        ("тётя кира"        , "Кира"),
        ("тёти киры"        , "Киры"),
        ("тёте кире"        , "Кире"),
        ("тётю киру"        , "Киру"),
        ("тётей кирой"      , "Кирой"),
        ("сукин сын"        , "сукин сын"),
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
        ("маминого"         , "хозяйкиного"),
        ("маминых"          , "хозяйкиных"),
        ("маминой"          , "хозяйкиной"),
        ("мамином"          , "хозяйкином"),
        ("тётя"             , "соседка"),
        ("тёти"             , "соседки"),
        ("тёте"             , "соседке"),
        ("тётю"             , "соседку"),
        ("тётей"            , "соседкой"),
        ("дочь"             , "съёмщиц"),
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
    ])

    replace_dict_en = OrderedDict([
        ("own sister"   , "best friend"),
        ("own aunt"     , "best neighbor"),
        ("own mother"   , "best landlady"),
        ("daughters"    , "tenants"),
        ("mother"       , "landlady"),
        ("mom"          , "landlady"),
        ("aunt"         , "neighbor"),
        ("son"          , "tenant"),
        ("sis"          , "roommate"),
        ("sister"       , "roommate"),
        ("sisters"      , "roommates"),
        ("brother"      , "roommate"),
        ("siblings"     , "roommates"),
        ("adoptive "    , ""),
        ("adopted"      , "contracted"),
        ("family"       , "household"),
        ("nephew"       , "neighbor"),
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
        ("mom"                  , "vermieterin"),
        ("moms"                 , "vermieterins"),
        ("tante"                , "nachbarin"),
        ("sohn"                 , "mieter"),
        ("schwester"            , "mieterin"),
        ("schwestern"           , "mieterinen"),
        ("bruder"               , "mitbewohner"),
        ("brüdern"              , "mitbewohner"),
        ("adoptierte"           , "zugezogene"),
        ("adoptivmutter"        , "Ersatz-Vermieterin"),
        ("familie"              , "haushalt"),
        ("familienunternehmen"  , "firma"),
        ("familienessen"        , "firmenfest"),
        ("neffe"                , "nachbar"),
    ])

    def game_text_mod(st0):
        if _preferences.language is None:
            replace_dict = replace_dict_ru
        elif _preferences.language=='english':
            replace_dict = replace_dict_en
        elif _preferences.language=='deutsch':
            replace_dict = replace_dict_de
        else:
            return st0
        rc = re.compile('\\b|\\b'.join(map(re.escape, replace_dict)), re.U+re.I)
        def transplate(match):
            key = match.group(0).lower()
            # print key, match.group(0)
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
        return rc.sub(transplate, st0)


default persistent.patch_enabled = False
default code_input = ""

init:
    $ config.say_menu_text_filter = game_text_mod
