image bg one:
    "rc_base.png"

default bg_toggle = False

screen rock_cycle:
    add "bg one"

    textbutton "Melting":
            action Jump("melting")
            hovered SetVariable("bg_toggle", True)
            unhovered SetVariable("bg_toggle", False)
            xalign 0.6
            yalign 0.25

    textbutton "Crystallization":
        action Jump("crystallization")
        hovered SetVariable("bg_toggle", True)
        unhovered SetVariable("bg_toggle", False)
        xalign 0.2
        yalign 0.10

    textbutton "Heat and Pressure":
        action Jump("heat_pressure")
        hovered SetVariable("bg_toggle", True)
        unhovered SetVariable("bg_toggle", False)
        xalign 0.95
        yalign 0.5

    textbutton "Weathering and Erosion":
        action Jump("weathering_erosion")
        hovered SetVariable("bg_toggle", True)
        unhovered SetVariable("bg_toggle", False)
        xalign 0.2
        yalign 0.65

    textbutton "Compaction and Cementation":
        action Jump("compaction_cementation")
        hovered SetVariable("bg_toggle", True)
        unhovered SetVariable("bg_toggle", False)
        xalign 0.6
        yalign 0.85

    textbutton "DONE":
        action Jump("scale")
        hovered SetVariable("bg_toggle", True)
        unhovered SetVariable("bg_toggle", False)
        xalign 1
        yalign 0
