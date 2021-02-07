screen question_1:

    frame:
        xalign 0.5 ypos 300

        textbutton "a. Igneous Rock":
            action Notify("Incorrect! Try again.")

    frame:
        xalign 0.5 ypos 350

        textbutton "b. Terrestrial Rock":
            action Jump("question_1_answer")

    frame:
        xalign 0.5 ypos 400

        textbutton "c. Sedimentary Rock":
            action Notify("Incorrect! Try again.")

    frame:
        xalign 0.5 ypos 450

        textbutton "d. Metamorphic Rock":
            action Notify("Incorrect! Try again.")

screen question_2:

    frame:
        xalign 0.5 ypos 350

        textbutton "a. Igneous Rock":
            action Jump("question_2_answer")

    frame:
        xalign 0.5 ypos 400

        textbutton "b. Sedimentary Rock":
            action Notify("Incorrect! Try again.")

    frame:
        xalign 0.5 ypos 450

        textbutton "c. Metamorphic Rock":
            action Notify("Incorrect! Try again.")


screen question_3:

    frame:
        xalign 0.5 ypos 350

        textbutton "a. pressure":
            action Notify("Incorrect! Try again.")

    frame:
        xalign 0.5 ypos 400

        textbutton "b. water":
            action Jump("question_3_answer")

    frame:
        xalign 0.5 ypos 450

        textbutton "c. soil":
            action Notify("Incorrect! Try again.")

screen question_4:

    frame:
        xalign 0.5 ypos 350

        textbutton "a. Mantle":
            action Notify("Incorrect! Try again.")

    frame:
        xalign 0.5 ypos 400

        textbutton "b. Asthenosphere":
            action Notify("Incorrect! Try again.")

    frame:
        xalign 0.5 ypos 450

        textbutton "c. Core":
            action Jump("question_4_anwser")

screen question_5:

    frame:
        xalign 0.5 ypos 350

        textbutton "a. Igneous Rock":
            action Notify("Incorrect! Try again.")

    frame:
        xalign 0.5 ypos 400

        textbutton "b. Sedimentary Rock":
            action Notify("Incorrect! Try again.")

    frame:
        xalign 0.5 ypos 450

        textbutton "c. Metamorphic Rock":
            action Jump("question_5_answer")
