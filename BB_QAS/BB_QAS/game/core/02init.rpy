init 9999 python:
    renpy.config.rollback_enabled = False
    renpy.config.hard_rollback_limit = 0
    renpy.config.rollback_length = 0

define lime = "#00FF00"
define weekdays = (
                  (_("ВС"), _("ВОСКРЕСЕНЬЕ")),
                  (_("ПН"), _("ПОНЕДЕЛЬНИК")),
                  (_("ВТ"), _("ВТОРНИК")),
                  (_("СР"), _("СРЕДА")),
                  (_("ЧТ"), _("ЧЕТВЕРГ")),
                  (_("ПТ"), _("ПЯТНИЦА")),
                  (_("СБ"), _("СУББОТА"))
                  )
