# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# n for narrator
define n = Character ()

# a for activity
define a = Character(kind = centered, what_text_align = 0.0, what_color = "FFC53A")

#for text in center of screen
define b = Character(kind = centered, what_text_align = 0.0, what_color = "EDEBD7")


define q = Character ("Amethyst", what_color = "D972FF")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    #Title slide

    scene title_slide

    n "Geology at Home"
    n "An at-home exploration by K. Avila and T.Yeomans"

    # add title, authours, distribution


    scene black_screen

    n "For parents, there are some activities to do together and talk about throughout this lesson"
    n "Activities are optional, and will be written in {color=FFC53A} colour {/color}"



    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    #Slides on what is geology and geologists

    b " What is geology?  What do geologists study?
    \n
    This program will introduce you to the types of rocks, how they are made and how geologists do their work"


    #Laters of the earth scene - maybe we don't need

    #Rock Cycle

    #Igneous Rocks
    scene black_screen
    b "Igneous rocks are formed by melting existing rocks deep underground\n
    \n
     Eventually these rocks start melting until it becomes a liquid or magma.\n
    \n
     Depending on the type of magma, it can reach over 1500 degrees Celcius!"

    "Once it's a magma, this liquid rock can move, and eventually it will cool down\n
    \n
     This magma can cool very quickly or very slowly"


    "How do you think magma could cool quickly?  How do you think it could cool slowly?"
    "If you guessed volcanoes for cooling quickly, you'd be right!"

    "Volcanoes push magma to the surface so the hot magma is exposed to the cool surface air, making the magma turn back into a solid really quickly"

    "For magma cooling slowly, as the liquid rock moves underground away from heat and pressure, eventually it starts to cool down, eventually turning to rock"
    "Do you have any ideas on how a geologist can tell by looking at a rock how fast it cooled?"


    show intrusive_ig at top with dissolve

    n "This is an example of an igneous rock that cooled really slowly"
    "We can tell that by the big crystals that we can see in the rock.
    The crystals had time to form as it grew slowly"

    hide intrusive_ig with dissolve

    show ext_igo at top with dissolve

    "This is an example of an extrusive igneous rock"
    "Can you see any crystals in this one?"

    "This rock cooled so fast that the crystals are too small to be seen with your eyes"

    hide ext_igo with dissolve

    show ext_igv at top with dissolve
    "What do you think about this one?  Do you think it is intrustive or extrusive?"
    "Do we have any clues?"

    "What do you think those little holes in the rock are from?"

    scene black_screen



    #Igneous rock crystal growning activity


    a "{b} ACTIVITY TIME{/b}"
    a "We can grow crystals at home \n
    \n
        For this activity we will need the following supplies: \n
        3 cups of sugar \n
        1 cup of boiling water \n
        2-3 clean jars \n
        cotton string\n"


    a "Once you have all of your materials and an {u}adult{/u} to help, you are ready to start growing your crystals \n
        \n
        1. Get an {u}adult{/u} to help you boil some water and dissolve the sugar in it\n
        \n
        2. Allow the sugar solution to cool a little before asking an {u}adult{/u} to put the liquid in the jars\n
        \n
        3. Tie the string to pencils or sticks and hang one string in each jar\n
        \n
        4. Place the jars in a couple different places in your house.  Don't touch them for several days\n
        \n
        5. Wait several days.  This could take some time"

    show quartz_down
    q "Look at your crystal growth. Did the crystals look different depending where they grew?"

    scene black_screen

    #Sedimentary rock

    show beach

    n "This looks like a good place to start thinking about sedimentary rocks"
    "Sedimentary rocks are formed by the erosion of existing rocks into tiny pieces"
    "Think about years of water, wind and snow day after day beating down on a rock"
    "Eventually this breaks the rock apart into pieces"
    "Those pieces may start off huge, but then are worn down themselves"
    "Eventually when the pieces of those rocks are tiny, they can end up at a place like this, the beach!"


    #Bottle with gravel, sand, silt exercise
    #Raisin/candy exercise
    #Metamorphic rock
    #Clay exercise
    #Rock quiz?
    #How to see inside the earth
    #Drilling
    #Seismic
    #Mapping
    #Scale
    scene mountain

    n "Geologists look at rocks at different scales"
    "Sometimes they like the big picture and look at entire mountain ranges"
    "Sometimes they look at rocks they can hold in their hand"
    "And sometimes they use microscopes to look at rocks"

    show thin_section

    n "This is an example of a sandstone rock from Alberta seen under a microscope"

    scene black_screen

    n "What do we do with rocks and minerals?"

    #Cake example
    #What are rocks used for
    #Geologists at work/school
    #Review


    #Other resources









    # This ends the game.

    return
