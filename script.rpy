# You can place the script of your game in this file

# Declare characters used by this game. The color argument colorizes the
# name of the character.

#bg colour is 435772

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

# Topic Covers
    # What is a geologists?
image geo:
    "geo_1.jpg"
    .5
    "geo_1.1.jpg"
    .5
    repeat

    # layers of earth
image layers:
    "layers_1"
    .5
    "layers_2"
    .5
    repeat

    # igneous rocks
image ign:
    "ign.jpg"
    .5
    "ign2.jpg"
    .5
    repeat

    # sedimentary rocks
image sed:
    "sed.jpg"
    .5
    "sed2.jpg"
    .5
    repeat

    # metamorphic rocks
image met:
    "met.jpg"
    .5
    "met2.jpg"
    .5
    repeat

    # rock cycle
image rc:
    "rc_1.jpg"
    .5
    "rc_2.jpg"
    .5
    repeat

define a = Character("Amethyst")

#activity text
define b = Character(kind = centered, what_text_align = 0.0, what_color = "FFC53A")

#other central text
define c = Character(kind = centered, what_text_align = 0.0, what_color = "EDEBD7")

label start:

# title card

    play music "toy_piano.mp3"

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
    ""
# what is a geologists/geoscientists? what do they study?

    scene defi
    show ame_teach at left
    a "{cps=35}Geology is defined as above{/cps}"

# insert geologists at work image/sketch
    a "{cps=35}and those who study geology are known as geologists (geoscientists).{/cps}"

    a "{cps=35}There are various kinds of geologists:{/cps}"

    scene bg plain
    show paleo
    show ame_teach at left
    a "{cps=35}Some geologists study fossils who learn about dinosaurs and other extinct species{/cps}"
    a "{cps=35}that used to roam our world millions of years ago.{/cps}"


    scene bg plain
    show volc
    show ame_teach at left
    a "{cps=35}While others investigate volcanoes to study its characteristics and understand how they may erupt.{/cps}"

    scene bg plain
    show quake
    show ame_teach at left
    a "{cps=35}Other geologists study earthquakes and uses physics to learn how they behave{/cps}"

    scene bg plain
    show oil
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

# layers of the earth
    show layers
    ""
    scene bg plain
    show ame_blink:
        xalign 0.5
        yalign 0.5

    a "{cps=35}To begin, we first have to understand the different sections that makes up the Earth{/cps}"
    a "{cps=35}The planet Earth can be divided into different layers{/cps}"

    scene bg plain
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


# igneous rocks
    show ign
    " "
    scene magma
    show ame_blink at left
#    show magma at topright behind ame_blink with dissolve
    a "{cps=35}Igneous rocks are formed by melting existing rocks dep underground{/cps}"
    a "{cps=35}Eventually these rocks start melting until they become a liquid we call magma{/cps}"
    a "{cps=35}Depending on the type of magma, it can reach over 1500 degrees Celcius!{/cps}"
    a "{cps=35}Once the rock is a magma, this liquid rock can move, and eventually it will cool down{/cps}"
    a "{cps=35}This magma can cool very quickly or very slowly{/cps}"
    a "{cps=35}How do you think magma could cool quickly?{/cps}"

    scene bg plain
    show volc_photo at top with dissolve
    a "{cps=35}If you guessed volcanoes for cooling quickly, you'd be right!{/cps}"
    a "{cps=35}Volcanoes push magma to the surface so the hot magma is exposed to the much colder air, making the magma turn back into a solid really quickly{/cps}"
    hide volc_photo with dissolve


    scene bg plain
    show ame_blink at left
    a "{cps=35}Magma can cool slowly by moving away from a heat source and by staying underground{/cps}"
    a "{cps=35}Do you have any ideas on how a geologist can tell by looking at a rock how fast it cooled?{/cps}"

    scene bg plain
    show ame_teach at left
    show intrusiveig_wframe at topright behind ame_teach with dissolve
    a "{cps=35}This is an example of an igneous rock that cooled really slowly{/cps}"
    a "{cps=35} We can tell that by the big crystals that we can see in the rock{/cps}"
    a "{cps=35}The crystals had lots of time to grow big because it cooled slowly{/cps}"
    hide intrusiveig_wframe with dissolve

    show ext_igo_wframe at topright behind ame_teach with dissolve
    a "{cps=35}This is an example of an extrusive igneous rock{/cps}"
    a "{cps=35}Can you see any crystals in this one?{/cps}"
    a "{cps=35}This rock cooled so fast that the crystals are too small to be seen with your eyes.{/cps}"
    hide ext_igo_wframe with dissolve

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
    4 cups of sugar \n
    2 cup of boiling water \n
    2-3 clean jars \n
    cotton string\n
    food colouring (optional)"


    b "Once you have all of your materials and an {u}adult{/u} to help, you are ready to start growing your crystals \n
    {u}Adults will need to do all of the steps while the students can watch{/u}
    \n
    1. Boil the water on the stove and slowly add the sugar to it, stirring the whole time\n
    \n
    2. Once all the sugar is dissolved, remove it from the heat.\n
    \n
    3. Allow the sugar solution to cool a little before putting the liquid in the jars.  At this point you can add a drop of food colouring to the jar if you like\n
    \n
    3. Tie the string to pencils or sticks and hang one string in each jar\n
    \n
    4. Place the jars in a couple different places in your house where they won't be bothered.  Don't touch them for several days\n
    \n
    5. Wait several days.  This could take some time"


    a "{cps=35}Students - Look at your crystal growth. Did the crystals look different depending where they grew?{/cps}"




label sedimentary:
# sedimentary rocks
    show sed
    " "
    scene bg plain
    show mountain with dissolve
    a "{cps=35}Let's move on to sedimentary rocks. This looks like a good place to start.{/cps}"
    a "{cps=35}There are three main types of sedimentary rocks.  Clastics, carbonates and evaporites.{/cps}"
    a "{cps=35}We'll talk about clastic sedimentary rocks first.{/cps}"
    a "{cps=35}Clastics are formed by the erosion of existing rocks into smaller pieces{/cps}"
    a "{cps=35}Think about years of water, wind and snow day after day wearing down these mountains{/cps}"
    a "{cps=35}Eventually this breaks the rock apart into pieces{/cps}"
    a "{cps=35}Those pieces may start off huge, but those pieces are also worn down{/cps}"
    a "{cps=35}They can eventually become tiny pieces of sand or mud.{/cps}"
    hide mountain with dissolve

# need a river scene
    a "{cps=35}These grains can be transported downhill and are washed into streams and rivers{/cps}"


    show beach with dissolve
    a "{cps=35}Those rivers carry the grains unti they can be tranported here, the beach!{/cps}"
    a "{cps=35}From there the grains can make their way underwater{/cps}"
    a "{cps=35}Grains can stack up on one another, with enough pressure to eventually squish them together, making a rock{/cps}"
    hide beach with dissolve

    scene bg plain
    show ame_teach at left
    a "{cps=35}We can classify clastic sedimentary rocks based on their grain size{/cps}"


    show cgl_wframe at topright behind ame_teach with dissolve
    a "{cps=35}This is a conglomerate.  Look at how big the grains, or clasts are in this example{/cps}"
    hide cgl_wframe with dissolve

    show sandstone_wframe at topright behind ame_teach with dissolve
    a "{cps=35}This is an example of sandstone.  It looks just like the beach sand all pressed together{/cps}"
    a "{cps=35}You can even see fossil shells in this sample!{/cps}"
    hide sandstone_wframe with dissolve


    show sed_layers behind ame_teach with dissolve
    a "{cps=35}Sedimentary rocks often form layers.{/cps}"
    a "{cps=35}This photo shows an example of these layers{/cps}"
    a "{cps=35}Some of the layers are sandstone, some of the layers are shale{/cps}"
    hide sed_layers with dissolve


# picture of mudstone/shale
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
    Water \n
    A place to find different sized grains (dirt, sand, gravel)"


    b "Once you have a bottle to use and and an {u}adult{/u} to help, you are ready to start building sedimentary layers \n
    \n
    1. With an {u}adult{/u}, explore your backyard and neighbourhood for different sized grains that fit in your bottle\n
    \n
    2. Fill the bottle about halfway with grains.\n
    \n
    3. Once you are at home, fill the bottle most of the way up to the top with water and put the lid on\n
    \n
    4. Take the bottle outside and give it a good shake to mix everything up\n
    \n
    5. Set the bottle down and wait."


    a "{cps=35}After a few minutes, look at your bottle.  Do you see layers?  What observations do you have about the layers?{/cps}"




label carbonates:

    show ame_teach at left

    a "{cps=35}Another type of sedimentary rocks we call carbonate rocks{/cps}"
    a "{cps=35}These sedimentary rocks are made by from the fossilized bodies of sea creatures{/cps}"
    a "{cps=35}Sometimes you can see the fossils in the rocks, sometimes you can't{/cps}"

    show coral_wframe at topright behind ame_teach with dissolve
    a "{cps=35}This is an example of a carbonate rock where you can see the fossils{/cps}"
    a "{cps=35}The circle shaped things you see on the rock are ancient corals formed under the sea.{/cps}"

    hide coral_wframe with dissolve

# picture of lime mudstone or something less fossily


    a "{cps=35}The last type of sedimentary rocks are called evaporites{/cps}"
    a "{cps=35}These sedimentary rocks are formed when water evaporates from a body of water{/cps}"
    a "{cps=35}Salt is an example of an evaporitic rock!  Geologists call it halite.{/cps}"

# metamorphic rocks
    show met
    " "
    scene bg plain
    a "{cps=35}Let's move on to the last type of rock, the metamorphic rocks!{/cps}"
    a "{cps=35}Metamorphic rocks are made when an existing rock is put under heat and pressure.{/cps}"
    a "{cps=35}Not enough heat to melt it like an igneous rock, but enough to change it{/cps}"
    a "{cps=35}The original rock can be igneous, sedimentary or even another metamorphic rock!{/cps}"
    a "{cps=35}How can we tell if a rock is metamorphic?{/cps}"
    a "{cps=35}Just like sedimentary rocks, they will often have layers or bands in them.{/cps}"


    show meta_wframe at topright behind ame_teach with dissolve
    a "{cps=35}Some of the differences are the minerals and what the bands look like.{/cps}"
    a "{cps=35}If you see a lot of shiny minerals, that could be a clue it is metamorhpic{/cps}"
    a "{cps=35}If the layers or bands are not straight but wiggly, that could be a clue it is metamorhpic{/cps}"
    a "{cps=35}{/cps}"

    hide meta_wframe with dissolve
    hide ame_teach




    menu:
        "It's activity time!  Do you have a parent to help you?  And do you have flour, salt, cream of tartar, food colouring and vegetable oil?\n
        If so, you can choose to do the activity now.  If not come back later."

        "Let's do the activity now!":
            jump meta_layers
        "I'll do the activity later!":
            jump scale







label meta_layers:


    b "{b} ACTIVITY TIME{/b}"
    b "We can see how metamorphic rock layers are formed \n
    \n
    For this activity we will be making modelling clay as the first step.\n
    The colours will get mixed up. If you have nice clay, you may not want to use it and make this instead.
    \n
    \n
    We need the following supplies: \n
    \n
    2 cups all purpose flour \n
    3/4 cup salt \n
    4 teaspoons cream of tartar\n
    2 cups lukewarm water\n
    2 tablespoons of vegetable oil\n
    Food colouring\n
    Bag for storage"


    b "Once you have your supplies and an {u}adult{/u} to help, you are ready to start \n
    \n
    Have an {u} adult {/u} make the modelling clay for you (steps 1-5) and you can do the experiment after (steps 6-12)\n
    \n
    1.  Put the flour, salt and cream of tartar in a big pot and stir\n
    \n
    2. Add the water and oil\n
    \n
    3. Cook this over medium heat, stirring until it forms a ball\n
    \n
    4. Remove the modelling clay from the heat and let cool for a bit\n
    \n
    5. Once cooled, knead and separate into different piles for different colours (minimum 2 colours)"



    b "Now it's your turn {u}students!{/u}\n
    \n
    6. Take a small ball of clay of the first colours and shape it into a flat rectangle. This will be your first layer.\n
    \n
    7. Take a second ball of clay of the second colour and make a rectangle the same as the first one.  Stack this on top of the first layer\n
    \n
    8. Add a third layer on top of your two layers\n
    \n
    9. Look at the layers from the top, bottom and sides.  Can you see all three?  What does it look like?\n
    \n
    10. Press down on the top of the layers and squish them together.  Can you still see all three layers?  Any changes?\n
    \n
    11. If you fold your layers in half, what does it look like now?\n
    \n
    12. Fold, flatten, twist and experiment with your layers to see how it changes"



    a "{cps=35}Your metamorphic layers can be layered and folded.  What happened to the layers?  Do you still have your original colours or are new ones formed?{/cps}"
    a "{cps=35}Your original layers you built was like a sedimentary rock{/cps}"
    a "{cps=35}You then squished, folded and twisted the layers, which was acting like heat and pressure, changing the original rock{/cps}"
    a "{cps=35}New colours forming is like new metamorphic minerals forming from the heat and pressure requried to make the rocks{/cps}."
    a "{cps=35}How is this different from the sedimentary rocks?{/cps}"


    #Raisin/candy exercise

label rock_cycle:

# rock cycle
    show rc
    " "

    scene bg plain
    show ame_blink:
        xalign 0.5
        yalign 0.5
    a "{cps=35}Now that we understand the different kinds of rocks, then we can look into the steps that forms rocks.{/cps}"
    a "{cps=35}Do you know that a rock could have been a metamorphic rock before it was a sedimentary rock?{/cps}"
    a "{cps=35}or an igneous rock that used to be a metamorphic rock?{/cps}"
    a "{cps=35}All of these are possible through repeated steps that rocks can go through{/cps}"
    a "{cps=35}depending on what kind of the environment it is located in.{/cps}"
    a "{cps=35}These steps are known as the rock cycle{/cps}"

    scene rockcycle
    hide ame_blink
    a "{cps=35}This diagram represents the rock cycle.{/cps}"
    a "{cps=35}Repeated steps that a rock can go through.{/cps}"
    a "{cps=35}We want to understand the basic steps that forms a rock.{/cps}"
    a "{cps=35}Starting out with crystallization, as mentioned before, crystallization happens when a magma cools down{/cps}"
    a "{cps=35}and becomes solid, which forms igneous rocks.{/cps}"
    a "{cps=35}Whereas, the opposite of crystallization is melting where solid becomes liquid, turning back the rock back to magma.{/cps}"
    a "{cps=35}While, heat and pressure occurs within the underground that is really deep down the Earth{/cps}"
    a "{cps=35}Like we have learned, as we go deeper the Earth, the hotter a rock gets{/cps}"
    a "{cps=35}and the deeper it gets, heavier objects accumulates above the rocks which causes the overlying pressure.{/cps}"
    a "{cps=35}Another is weathering and erosion that breaks down rocks into pieces, called sediments{/cps}"
    a "{cps=35}Then, the sediments goes through compaction and cementation like gluing objects together, that forms sedimentary rocks.{/cps}"
    a "{cps=35}This steps can go several other ways and return back as controlled by the environment it is located in.{/cps}"

    a "{cps=35}In conclusion the rock cycle is what gives rocks their different characteristics making the different places in Earth unique.{/cps}"



# rock type quiz

# how to see inside the earth

    # drilling

    # seismic

    # mapping

label scale:

    scene bg plain
    show ame_blink

    a "{cps=35}Geologists look at rocks at different scales{/cps}"
    a "{cps=35}What does this mean?{/cps}"
    show mountains_from_air at right
    a "{cps=35}Sometimes they like the big picture and look at entire mountain ranges{/cps}"
    hide mountains_from_air with dissolve
    #add photo of rock in hand
    a "{cps=35}Sometimes they look at rocks they can hold in their hand{/cps}"

    show thin_section at topright
    a "{cps=35}And sometimes they use microscopes to look at rocks{/cps}"
    a "{cps=35}This is an example of a sandstone rock from Alberta seen under a microscope{/cps}"
    a "{cps=35}{/cps}"
    hide thin_section with dissolve

#Geologists at work/school

#Review

#Other resources



return
