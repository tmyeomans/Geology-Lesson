# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

    # 'n' for narrator

define n = Character ()

    #a for activity


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

    n "What is geology?  What do geologists study?"

    n "This program will introduce you to the types of rocks, how they are made and how geologists do their work"

    #Laters of the earth scene - maybe we don't need

    #Rock Cycle

    #Igneous Rocks
    scene black_screen
    n "Ingeous rocks are formed by melting existing rocks making magma"
    n "This magma can cool very quickly or very slowly"
    n "Do you have any ideas on how a geologist can tell how fast it cooled?"


    show intrusive_ig at top with dissolve

    n "This is an example of an igneous rock that cooled really slowly"
    n "We can tell that by the big crystals that we can see in the rock.
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
    n "{color=FFC53A} ACTIVITY TIME{/color}"
    "{color=FFC53A}We can grow crystals at home{/color}"
    "{color=FFC53A} For this activity parents we will need the following: \n
        3 cups of sugar \n
        1 cup of boiling water \n
        2-3 clean jars \n
        cotton string{/color}\n"


    "{color=FFC53A} Once you have all of your materials and a parent to help, you are ready to start growing your crystals \n
        1. Get a parent to help you dissolve the sugar in the boiling water\n
        2. Allow the sugar solution to cool a little before putting it in the jars\n{/color}"

    "{color=FFC53A} 3. Tie the string to pencils or sticks and hang one string in each jar\n
        4. Put the jars somewhere that they won't be touched for several days.  Try placing them in different places around the house\n
        5. Wait several days.  This could take some time{/color}"

    "{color=FFC53A}Look at your crystal growth. Did the crystals look different depending where they grew? {/color}"

    scene black_screen

    #Sedimentary rock
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
