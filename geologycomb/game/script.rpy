# You can place the script of your game in this file

# Declare characters used by this game. The color argument colorizes the
# name of the character.

#bg colour is 435772


# KAvila

# Animated Images
image ame_blink:
    "qtz_2.png"
    1
    "qtz_2.1.png"
    .1
    "qtz_2.png"
    2
    "qtz_2.1.png"
    .1
    repeat

image ame_teach:
    "qtz_pt.png"
    1
    "qtz_pt.1.png"
    .1
    "qtz_pt45.png"
    2
    "qtz_pt45.1.png"
    .1
    "qtz_pt.png"
    1.5
    "qtz_pt.1.png"
    .1
    "qtz_pt45.png"
    2
    "qtz_pt45.1.png"
    .1
    repeat

# Topic Cover
image geo:
    "geo_1.jpg"
    .5
    "geo_1.1.jpg"
    .5
    repeat

image layers:
    "layers_1"
    .5
    "layers_2"
    .5
    repeat

define a = Character("Amethyst")

#activity text
define b = Character(kind = centered, what_text_align = 0.0, what_color = "FFC53A")

label start:

# title card

    play music "toy_piano.mp3"

    scene title

    scene bg plain
    show ame_blink:
        xalign 0.5
        yalign 0.5

    a "{cps=35}Greetings everyone, welcome students and parents!{/cps}"
    a "{cps=35}I am Amethyst and I will be joining you today to go through the wonders of geology{/cps}"
    a "{cps=35}From unfolding 4.5 billion years history of Earth to putting resources to practical use{/cps}"
    a "{cps=35}We will explore and learn what geology is.{/cps}"

    hide ame_blink
    show qtz_4:
        xalign 0.5
        yalign 0.5

    a "{cps=35}A lot of unknown about the Earth are still yet to be discovered,{/cps}"
    a "{cps=35}but that's what I think makes geology so exciting!{/cps}"

    show geo
# what is a geologists/geoscientists? What do they study?
    # position Amethyst at the corner

    scene defi
    show ame_teach at left
    a "{cps=35}Geology is defined as above{/cps}"

# insert geologists at work image/sketch
    a "{cps=35}and those who study geology are known as geologists (geoscientists).{/cps}"

    a "{cps=35}There are various kinds of geologists:{/cps}"

    scene paleo
    show ame_teach at left
    a "{cps=35}Some geologists study fossils who learn about dinosaurs and other extinct species{/cps}"
    a "{cps=35}that used to roam our world millions of years ago.{/cps}"

    scene volc
    show ame_teach at left
    a "{cps=35}While others investigate volcanoes to study its characteristics and understand how they may erupt.{/cps}"

    scene quake
    show ame_teach at left
    a "{cps=35}Other geologists study earthquakes and uses physics to learn how they behave{/cps}"

    scene oil
    show ame_teach at left
    a "{cps=35}Another are geologists who explores oil and gas, who provides us with energy for our homes and transportations{/cps}"

    scene bg plain
    show ame_blink:
        xalign 0.5
        yalign 0.5
    a "{cps=35}I can go on of how much geologists can do, but one thing for sure{/cps}"
    a "{cps=35}is that geologists provides us with a better understanding of our world{/cps}"
    show qtz_1:
        xalign 0.5
        yalign 0.5
    a "{cps=35}and increases our quality of life.{/cps}"

    show layers


# layers of the earth

    scene bg plain
    show ame_blink:
        xalign 0.5
        yalign 0.5

    a "{cps=35}To begin, we first have to understand the different sections that makes up the Earth{/cps}"
    a "{cps=35}The planet Earth can be divided into different layers{/cps}"

    scene bg plain
    show tle 1
    a "{cps=35}Imagine when you cut up an egg into half, you can see distinct layers.{/cps}"

    scene bg plain
    show tle 3
    a "{cps=35}Like the shell in an egg, the crust is the outermost and thinnest layer of the Earth where we live on.{/cps}"

    scene bg plain
    show tle 4
    a "{cps=35}Then, the white portion represent the mantle.{/cps}"
    a "{cps=35}The mantle underneath the crust consists of melted rocks and is the source of magma{/cps}"
    a "{cps=35}which is the substance that erupts out from volcanoes.{/cps}"

    scene bg plain
    show tle 5
    a "{cps=35}And the yolk is the core of the Earth.{/cps}"
    a "{cps=35}The core is made out of iron alloy that consists of two parts{/cps}"
    a "{cps=35}The outer core is solid, while the inner core is liquid.{/cps}"
    a "{cps=35}As we go deeper down the core, the hotter the Earth gets.{/cps}"
    a "{cps=35}within the inner core, it can get hot as high  as 5000°C{/cps}"




#Igneous Rocks
    scene bg plain
    show ame_blink at left

    a "{cps=35}Igneous rocks are formed by melting exiting rocks dep underground{/cps}"
    a "{cps=35}Eventually these rocks start melting until they become a liquid we call magma{/cps}"
    a "{cps=35}Depending on the type of magma, it can reach over 1500 degrees Celcius!{/cps}"
    a "{cps=35}Once the rock is a magma, this liquid rock can move, and eventually it will cool down{/cps}"
    a "{cps=35}This magma can cool very quickly or very slowly{/cps}"
    a "{cps=35}How do you think magma could cool quickly?{/cps}"

    scene volc
    a "{cps=35}If you guessed volcanoes for cooling quickly, you'd be right!{/cps}"
    a "{cps=35}Volcanoes push magma to the surface so the hot magma is exposed to the much colder air, making the magma turn back into a solid really quickly{/cps}"

#add drawing of magma chamber
    scene bg plain
    show ame_blink at left
    a "{cps=35}Magma can cool slowly by moving away from a heat source and by staying underground{/cps}"
    a "{cps=35}Do you have any ideas on how a geologist can tell by looking at a rock how fast it cooled?{/cps}"

    scene bg plain
    show ame_teach at left
    show intrusive_ig at topright
    a "{cps=35}This is an example of an igneous rock that cooled really slowly{/cps}"
    a "{cps=35} We can tell that by the big crystals that we can see in the rock{/cps}"
    a "{cps=35}The crystals had lots of time to grow big because it cooled slowly{/cps}"
    hide intrusive_ig with dissolve

    show ext_igo at topright with dissolve
    a "{cps=35}This is an example of an extrusive igneous rock{/cps}"
    a "{cps=35}Can you see any crystals in this one?{/cps}"
    a "{cps=35}This rock cooled so fast that the crystals are too small to be seen with your eyes.{/cps}"
    hide ext_igo with dissolve

    show ext_igv at topright with dissolve
    a "{cps=35}What do you think about this one?  Do you think it's extrusive or intrustive?{/cps}"
    a "{cps=35}This one is extrusive like the last one.  It's different because it has bubbles trapped in it.{/cps}"
    a "{cps=35}The bubbles were trapped when it left the volcano {/cps}"
    hide ext_igv with dissolve
    hide ame_teach

    menu:
        "It's activity time!  Do you have a parent to help you?  And do you have sugar, string and jars at home?\n
        If so, you can choose to do the activity now.  If not come back later."

        "Let's do the activity now!":
            jump crystal_activity
        "I'll do the activity later!":
            jump sedimentary


label crystal_activity:


    b "{b} ACTIVITY TIME{/b}"
    b "We can grow crystals at home \n
    \n
    For this activity we will need the following supplies: \n
    3 cups of sugar \n
    1 cup of boiling water \n
    2-3 clean jars \n
    cotton string\n"


    b "Once you have all of your materials and an {u}adult{/u} to help, you are ready to start growing your crystals \n
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


    a "Look at your crystal growth. Did the crystals look different depending where they grew?"




label sedimentary:
#Sedimentary Rocks
    scene bg plain

    show mountain
    a "{cps=35}Let's move on to sedimentary rocks. This looks like a good place to start.{/cps}"
    a "{cps=35}There are three main types of sedimentary rocks.  Clastics, carbonates and evaporites.{/cps}"
    a "{cps=35}We'll talk about clastic sedimentary rocks first.{/cps}"
    a "{cps=35}Clastics are formed by the erosion of existing rocks into tiny pieces{/cps}"
    a "{cps=35}Think about years of water, wind and snow day after day wearing down these mountains{/cps}"
    a "{cps=35}Eventually this breaks the rock apart into pieces{/cps}"
    a "{cps=35}Those pieces may start off huge, but then are worn down themselves{/cps}"
    hide mountain with dissolve

#need a river scene
    a "{cps=35}These pieces can be transported downhill and are washed into streams and rivers{/cps}"


    show beach with dissolve
    a "{cps=35}Those tiny pieces can eventually be tranported here, the beach!{/cps}"
    a "{cps=35}From there the grains can make their way underwater{/cps}"
    a "{cps=35}Grains can stack up on one another, with enough pressure to eventually squish them together, making a rock{/cps}"
    hide beach with dissolve

    scene bg plain
    show ame_teach at left
    a "{cps=35}We can classify clastic sedimentary rocks based on their grain size{/cps}"


    show cgl at right
    a "{cps=35}This is a conglomerate.  Look at how big the grains, or clasts are in this example{/cps}"
    hide cgl with dissolve

    show sandstone at topright
    a "{cps=35}This is an example of sandstone.  It looks just like the beach sand all pressed together{/cps}"
    a "{cps=35}You can even see fossil shells in this sample!{/cps}"
    hide sandstone with dissolve
    hide ame_teach





    menu:
        "It's activity time!  Do you have a parent to help you?  And do you have an empty plastic bottle with a lid?\n
        If so, you can choose to do the activity now.  If not come back later."

        "Let's do the activity now!":
            jump sed_layers
        "I'll do the activity later!":
            jump carbonates





label sed_layers:


    b "{b} ACTIVITY TIME{/b}"
    b "We can see how sedimentary rock layers are formed \n
    \n
    For this activity we will need the following supplies: \n
    \n
    Clear empty plastic bottle with a lid \n
    \n
    Water \n
    \n
    A place to find different sized grains (dirt, sand, gravel)"


    b "Once you have a bottle to use and and an {u}adult{/u} to help, you are ready to start building sedimentary layers \n
    \n
    1. With your {u}adult{/u}, explore your backyard and neighbourhood for different sized grains that will fit in your bottle\n
    \n
    2. Fill the bottle about halfway with grains, making sure you have lots of different sizes.\n
    \n
    3. Once you are at home, fill the bottle most of the way up to the top with water and put the lid on\n
    \n
    4. Take the bottle outside and give it a good shake to mix everythign up\n
    \n
    5. Set the bottle down and wait."


    a "After a few minutes, look at your bottle.  Do you see layers?  What observations do you have about the layers?"




label carbonates:

    show ame_teach at left

    a "{cps=35}Another type of sedimentary rocks we call carbonate rocks{/cps}"
    a "{cps=35}These sedimentary rocks are made by from the fossilized bodies of sea creatures{/cps}"
    a "{cps=35}Sometimes you can see the fossils in the rocks, sometimes you can't{/cps}"

    show coral2 at right with dissolve
    a "{cps=35}This is an example of a carbonate rock where you can see the fossils{/cps}"
    a "{cps=35}The circle shaped things you see on the rock are ancient corals formed under the sea.{/cps}"
    hide coral2 with dissolve
    show coral at right with dissolve
    a "{cps=35}Here is another example!{/cps}"

    hide coral with dissolve




    a "{cps=35}The last type of sedimentary rocks are called evaporites{/cps}"
    a "{cps=35}These sedimentary rocks are formed when water evaporates from a body of water{/cps}"
    a "{cps=35}Salt is an example of an evaporitic rock!  Geologists call it halite.{/cps}"


    a "{cps=35}{/cps}"




#Metamorphic Rocks



    #Bottle with gravel, sand, silt exercise
    #Raisin/candy exercise

    #Clay exercise
    #Rock quiz?
    #How to see inside the earth
    #Drilling
    #Seismic
    #Mapping


#Scale
    show mountain

    a "{cps=35}Geologists look at rocks at different scales{/cps}"
    a "{cps=35}What does this mean?{/cps}"
    a "{cps=35}Sometimes they like the big picture and look at entire mountain ranges{/cps}"
    a "{cps=35}Sometimes they look at rocks they can hold in their hand{/cps}"
    a "{cps=35}And sometimes they use microscopes to look at rocks{/cps}"
    hide mountain with dissolve


    show thin_section
    a "{cps=35}This is an example of a sandstone rock from Alberta seen under a microscope{/cps}"
    a "{cps=35}{/cps}"
    hide thin_section with dissolve



#Geologists at work/school
#Review


#Other resources





return
