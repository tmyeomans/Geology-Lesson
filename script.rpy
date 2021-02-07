
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

# Topic Covers
    # What is a geologist?
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

image review:
    "review_1"
    .5
    "review_2"
    .5
    repeat

image inside:
    "inside_1"
    .5
    "inside_2"
    .5
    repeat

image scale:
    "scale_1"
    .5
    "scale_2"
    .5
    repeat

define a = Character("Amethyst")

#activity text
define b = Character(kind = centered, what_text_align = 0.0, what_color = "FFC53A")

#other central text
define c = Character(kind = centered, what_text_align = 0.0, what_color = "EDEBD7")


################################################################################


label start:

# title card


    play music "toy_piano.mp3"

    scene title

# scene for conditions of use
    scene bg plain


    c "Welcome to the geoadventure!  On the next screen you'll get to choose how to proceed.\n
    \n
    If this is your first time, select the lesson.\n
    \n
    If you're coming back for an activity you missed, follow the shortcut to the activity you want."

    menu:


        "I want to follow the lesson!":
            jump lesson
        "I'm coming back to make crystals!":
            jump crystal_activity
        "I'm coming back to make sedimentary layers!":
            jump sed_layers
        "I'm coming back to explore metamorphic changes with clay!":
            jump meta_layers






label lesson:


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
# what is a geologists/geoscientists? What do they study?


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

#Igneous Rocks
    show ign
    " "
    scene magma
    show ame_blink at left

    a "{cps=35}Igneous rocks are formed by heating existing rocks deep underground{/cps}"
    a "{cps=35}Eventually these rocks melt and become a liquid we call magma{/cps}"
    a "{cps=35}Depending on the type of magma, it can reach over 1500 degrees Celcius!{/cps}"
    a "{cps=35}This liquid rock can move, and will eventually move away from the heat and cool down{/cps}"
    a "{cps=35}This magma can cool very quickly or very slowly{/cps}"
    a "{cps=35}How do you think magma could cool quickly?{/cps}"

    scene bg plain
    show volc_photo at top with dissolve
    a "{cps=35}If you guessed volcanoes for cooling quickly, you'd be right!{/cps}"
    a "{cps=35}Volcanoes push magma to the surface so the hot magma is exposed to the much colder air, making the magma turn back into a solid really quickly{/cps}"
    hide volc_photo with dissolve


    #magma cool slowly image
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


    b "{b} CRYSTAL ACTIVITY TIME{/b}"
    b "{b}We can grow crystals at home{/b} \n
    \n
    For this activity we will need the following supplies: \n
    4 cups of sugar \n
    2 cup of boiling water \n
    2-3 clean jars \n
    cotton string\n
    food colouring (optional)"


    b "Once you have all of your materials and an {u}adult{/u} to help, you are ready to start growing your crystals \n
    \n
    {u}Adults will need to do all of the steps while the students can watch{/u}\n
    \n
    1. Boil the water on the stove and slowly add the sugar to it, stirring the whole time\n
    \n
    2. Once all the sugar is dissolved, remove it from the heat.  Allow the liquid to cool a little.\n
    \n
    3. Put the liquid in the jars. You can add food colouring to the jar if you like\n
    \n
    3. Tie the string to pencils or sticks and hang one string in each jar\n
    \n
    4. Place the jars in your house where they won't be bothered.  Don't touch them for several days\n
    \n
    5. After several days lift the pencil to look for crystals."

    show ame_blink at left
    show crystal_activity at topright behind ame_blink with dissolve
    a "{cps=35}Students - Look at your crystal growth. What do you see?{/cps}"
    a "{cps=35}These crystals grew as the water evaporated.  Does it look different from the sugar you first put in?{/cps}"
    a "{cps=35}My sugar crystals look bigger than sugar we first added!{/cps}"
    hide ame_blink
    hide crystal_activity with dissolve



label sedimentary:
#Sedimentary Rocks
    show sed
    " "
    scene bg plain
    show ame_blink at left
    show mountain behind ame_blink with dissolve
    a "{cps=35}Let's move on to sedimentary rocks. This looks like a good place to start.{/cps}"
    a "{cps=35}There are three main types of sedimentary rocks.  Clastics, carbonates and evaporites.{/cps}"
    a "{cps=35}We'll talk about clastic sedimentary rocks first.{/cps}"
    a "{cps=35}Clastics are formed by the erosion of existing rocks into smaller pieces{/cps}"
    a "{cps=35}Think about years of water, wind and snow day after day wearing down these mountains{/cps}"
    a "{cps=35}Eventually this breaks the rock apart into pieces{/cps}"
    a "{cps=35}Those pieces may start off huge, but those pieces are also worn down{/cps}"
    a "{cps=35}They can eventually become tiny pieces of sand or mud.{/cps}"
    a "{cps=35}These tiny pieces of rocks have different names.  We call them grains, clasts or sediment.{/cps}"
    hide mountain with dissolve


    show river behind ame_blink with dissolve
    a "{cps=35}These grains can be transported downhill and are washed into streams and rivers{/cps}"
    hide river with dissolve

    show beach behind ame_blink with dissolve
    a "{cps=35}Those rivers carry the grains until they can be tranported here, the beach!{/cps}"
    a "{cps=35}From there the grains can make their way underwater{/cps}"
    a "{cps=35}Grains can stack up on one another, with enough pressure to eventually squish them together, making a rock{/cps}"
    a "{cps=35}Think of it like a bag of raisins or candy left in the back of your cupboard{/cps}"
    a "{cps=35}If you forget about them for awhile, they start to stick together, with each candy being an individual grain{/cps}"
    hide beach with dissolve
    hide ame_blink with dissolve

    scene bg plain
    show ame_teach at left
    a "{cps=35}We can classify clastic sedimentary rocks based on their grain size{/cps}"


    show cgl_wframe at topright behind ame_teach with dissolve
    a "{cps=35}This is a conglomerate.  Look at how big the grains are in this example{/cps}"
    a "{cps=35}Some of the grains are as big as the quarter in the picture. {/cps}"
    hide cgl_wframe with dissolve

    show sandstone_wframe at topright behind ame_teach with dissolve
    a "{cps=35}This is an example of sandstone.  It looks just like the beach sand all pressed together{/cps}"
    a "{cps=35}You can even see fossil shells in this sample!{/cps}"
    hide sandstone_wframe with dissolve

    show silt_wframe at topright behind ame_teach with dissolve
    a "{cps=35}Some sedimentary rocks have grains so small you can't really see them with just your eyes{/cps}"
    a "{cps=35}These are called siltstones or shales{/cps}"
    a "{cps=35}This is an example of a siltstone.  If you look really really close you can see some grains.  If you couldn't you would call it a shale{/cps}"
    hide silt_wframe with dissolve

    show sed_layers behind ame_teach with dissolve
    a "{cps=35}Sedimentary rocks often form layers.{/cps}"
    a "{cps=35}This photo shows an example of these layers{/cps}"
    a "{cps=35}Some of the layers are sandstone, some of the layers are shale{/cps}"
    hide sed_layers with dissolve



    hide ame_teach

    menu:
        "It's activity time!  Do you have a parent to help you?  And do you have an empty plastic bottle with a lid?\n
        If so, you can choose to do the activity now.  If not come back later."

        "Let's do the activity now!":
            jump sed_layers
        "I'll do the activity later!":
            jump carbonates





label sed_layers:


    b "{b}SEDIMENTARY LAYERS ACTIVITY TIME{/b}"
    b "{b}We can see how sedimentary rock layers are formed{/b} \n
    \n
    For this activity we will need the following supplies: \n
    \n
    Clear empty plastic bottle or plastic jar with a lid \n
    \n
    Water \n
    \n
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
    5. Set the bottle down and wait 10 minutes."

    show ame_blink at left with dissolve
    show seds_activity at topright with dissolve
    a "{cps=35}Look at the sediment in the bottle.  Do you see layers?  What observations do you have about the layers?{/cps}"
    a "{cps=35}These pictures show my sediment all mixed up before I added the water, and the layers after adding water, shaking it, and letting it rest{/cps}"
    hide ame_blink
    hide seds_activity with dissolve



label carbonates:
    scene bg plain
    show ame_teach at left
    show reef at topright behind ame_teach with dissolve
    a "{cps=35}Another type of sedimentary rocks we call carbonate rocks{/cps}"
    a "{cps=35}These sedimentary rocks are formed under water.  A coral reef is a good place to form carbonate rocks.{/cps}"
    a "{cps=35}Carbonates are made up of the fossilized bodies of sea creatures{/cps}"
    a "{cps=35}Sometimes you can see the fossils in the rocks.{/cps}"
    a "{cps=35}And sometimes you can't because the fossils are broken up into small pieces like the clastic rocks.{/cps}"
    hide reef with dissolve

    show coral_wframe at topright behind ame_teach with dissolve
    a "{cps=35}This is an example of a carbonate rock where you can see the fossils{/cps}"
    a "{cps=35}The circle shaped things you see on the rock are ancient corals formed under the sea.{/cps}"
    hide coral_wframe with dissolve

    show limemud_wframe at topright behind ame_teach with dissolve

    a "{cps=35}In this example you have the same carbonate that is found in shells instead making mud to form the rock{/cps}"
    hide limemud_wframe with dissolve



    show evap_wframe at topright behind ame_teach with dissolve
    a "{cps=35}The last type of sedimentary rocks are called evaporites{/cps}"
    a "{cps=35}These sedimentary rocks are formed when water evaporates from a body of water{/cps}"
    a "{cps=35}Salt is an example of an evaporitic rock.  Geologists call it halite.{/cps}"
    a "{cps=35}Look really closely the next time you use salt at the dinner table.  What does it look like up close?{/cps}"
    hide evap_wframe with dissolve


#Metamorphic Rocks
    show met
    " "
    scene bg plain
    show ame_blink at left
    show meta_env behind ame_blink with dissolve
    a "{cps=35}Let's move on to the last type of rock, the metamorphic rocks!{/cps}"
    a "{cps=35}Metamorphic rocks are made when an existing rock is put under heat and pressure.{/cps}"
    a "{cps=35}Not enough heat to melt it like an igneous rock, but enough to change it{/cps}"
    a "{cps=35}The original rock can be igneous, sedimentary or even another metamorphic rock!{/cps}"
    a "{cps=35}How can we tell if a rock is metamorphic?{/cps}"
    a "{cps=35}Just like sedimentary rocks, they will often have layers or bands in them.{/cps}"
    hide meta_env with dissolve
    hide ame_blink with dissolve

    show ame_teach at left
    show meta_wframe at topright behind ame_teach with dissolve
    a "{cps=35}Some of the differences are the minerals you can find in it and what the bands look like.{/cps}"
    a "{cps=35}If you see a lot of shiny minerals, that could be a clue that your rock is metamorphic{/cps}"
    a "{cps=35}If the layers or bands are not straight but wiggly, that could be a clue it is metamorhpic{/cps}"

    hide meta_wframe with dissolve

    show meta2_wframe at topright behind ame_teach with dissolve
    a "{cps=35}Here is another metamorphic rock{/cps}"
    a "{cps=35}It looks kind of like the siltstone we saw earlier but it has more shiny minerals{/cps}"
    hide meta2_wframe with dissolve

    hide ame_teach




    menu:
        "It's activity time!  Do you have a parent to help you?  And do you have flour, salt, cream of tartar, food colouring and vegetable oil?\n
        If so, you can choose to do the activity now.  If not come back later."

        "Let's do the activity now!":
            jump meta_layers
        "I'll do the activity later!":
            jump rockcycle







label meta_layers:


    b "{b}METAMORPHIC CHANGES ACTIVITY TIME{/b}"
    b "{b}We can see how metamorphic rock layers are formed{/b}\n
    \n
    For this activity we will be using modelling clay.\n
    \n
    The colours will get mixed up so you may not want to use nice clay.\n
    \n
    We have adapted a recipe from https://funlearningforkids.com/easy-play-dough-recipe-without-cream-tartar/ \n
    \n
    If using your own clay, you can skip to step 6."

    b "We need the following supplies: \n
    \n
    1 cup flour \n
    1/4 cup salt \n
    3 tablespoons lemon juice\n
    2 tablespoons of vegetable oil\n
    3/4 cup water\n
    Food colouring\n
    Bag for storage"



    b "Have an {u} adult {/u} make the modelling clay for you (steps 1-5) and you can do the experiment after (steps 6-12)\n
    \n
    1.  Put the lemon juice, oil and water in a pot on the stove and heat on medium heat until hot but not boiling.\n
    \n
    2. Add the dry ingredients.\n
    \n
    3. Cook this over medium heat for a couple of minute, stirring until it forms a ball\n
    \n
    4. Remove the modelling clay from the heat and let it cool\n
    \n
    5. Knead and separate into different piles.  Add a separate food colour to each pile (minimum 2 colours)"



    b "Now it's your turn {u}students!{/u}\n
    \n
    6. Take a small ball of clay of the first colours and shape it into a flat rectangle. This will be your first layer.\n
    \n
    7. Take a second ball of clay of the second colour and make another rectangle.  Stack this on top of the first layer\n
    \n
    8. Add a third layer on top of your two layers\n
    \n
    9. Look at the layers from the top, bottom and sides.  Can you see all three?  What does it look like?\n
    \n
    10. Press down on the top of the layers and squish them together.  What does it look like?\n
    \n
    11. Fold your layers in half and squish. What does it look like now?\n
    \n
    12. Fold, flatten, twist and experiment with your layers to see how it changes."

    show ame_blink at left
    show meta_activity behind ame_blink with dissolve
    a "{cps=35}Your metamorphic layers can be layered and folded.  What happened to the layers?  Do you still have your original colours or are new ones formed?{/cps}"
    a "{cps=35}Your original layers you built was like a sedimentary rock like in picture 1{/cps}"
    a "{cps=35}You then squished, folded and twisted the layers, which was acting like heat and pressure, changing the original rock{/cps}"
    a "{cps=35}By the time I got to picture 4, I saw bands of colours and new colours.{/cps}"
    a "{cps=35}New colours forming is like new metamorphic minerals forming from the heat and pressure requried to make the rocks{/cps}."
    a "{cps=35}How is this different from the sedimentary rocks?{/cps}"
    hide meta_activity with dissolve
    hide ame blink

################################################################################

# rock cycle

# Animated Images
image melt:
    "melt1.png"
    1
    "melt2.png"
    1
    repeat

image xtal:
    "xtal1.png"
    1
    "xtal2.png"
    1
    repeat

image we:
    "w&e1.png"
    1
    "w&e2.png"
    1
    repeat

image hp:
    "h&p1.png"
    1
    "h&p2.png"
    1
    repeat

image cc:
    "c&c1.png"
    1
    "c&c2.png"
    1
    repeat

label rockcycle:

    show rc
    " "

    scene bg plain
    show ame_blink:
        xalign 0.5
        yalign 0.5
    a "{cps=35}Now that we understand the different kinds of rocks, then we can look into the steps that forms rocks.{/cps}"
    a "{cps=35}The steps is called the rock cycle.{/cps}"
    a "{cps=35}The rock cycle is like recycling of old rocks and turning it into new rocks.{/cps}"
    a "{cps=35}This happens through repeated steps that rocks can go through depending on what kind of environment it is located in.{/cps}"

label rock_cycle:
    show screen rock_cycle
    hide ame_blink
    a "{cps=35}This diagram represents the rock cycle.{/cps}"

label melting:
    hide screen rock_cycle
    show melt

    "{cps=35}Melting is turning solid into liquid through high temperatures.{/cps}"
    "{cps=35}This will cause the rock to turn into magma.{/cps}"

    jump rock_cycle

label crystallization:
    hide screen rock_cycle
    show xtal

    "{cps=35}Crystallization is turning liquid into solid through cold temperatures.{/cps}"
    "{cps=35}This is the cooling down of the rock which turns into igneous rock.{/cps}"

    jump rock_cycle

label heat_pressure:
    hide screen rock_cycle
    show hp

    "{cps=35}As mentioned previously, we now know that as we go deeper into Earth's core the more heated the rocks get.{/cps}"
    "{cps=35}as well as, the deeper it gets the more pressure is applied on the rock due to overlying mass above it.{/cps}"
    "{cps=35}This then causes to form metamorphic rocks.{/cps}"

    jump rock_cycle

label weathering_erosion:
    hide screen rock_cycle
    show we

    "{cps=35}Weathering and erosion is breaking down rocks into smaller pieces.{/cps}"
    "{cps=35}We refer to these smaller pieces as sediments.{/cps}"

    jump rock_cycle

label compaction_cementation:
    hide screen rock_cycle
    show cc

    "{cps=35}The sediments are small pieces of rocks caused by weathering and erosion.{/cps}"
    "{cps=35}This can turn into sedimentary rocks by compaction and cementation,{/cps}"
    "{cps=35}like how we glue objects to stick them together.{/cps}"

    jump rock_cycle



################################################################################

#Rock quiz

label rock_quiz:

    hide screen rock_cycle

    show review
    " "
    scene bg plain
    show ame_blink at left

    a "{cps=35}I hope you have a better understanding of what geology is and familiar with different types of rocks.{/cps}"
    a "{cps=35}Therefore, I have prepared a short quiz to review what we have learned so far!{/cps}"

label question_1:

    show screen question_1

    a "{cps=35}Which of the following is not a type of rock? (Click on the answer){/cps}"
    a "Which of the following is not a type of rock? (Click on the answer)"
    a "Which of the following is not a type of rock? (Click on the answer)"
    a "Which of the following is not a type of rock? (Click on the answer)"

label question_1_answer:
    a "{cps=35}That is correct! The three main types of rock are Igneous, Sedimentary and Metamorphic rocks{/cps}"

label question_2:

    hide screen question_1
    scene bg plain
    scene bg plain
    show ame_blink at left
    show intrusiveig_wframe with dissolve:
        size(622, 350)
        xalign .5
        yalign 0
    show screen question_2

    a "{cps=35}What type or rock is formed by cooling down the magma?{/cps}"
    a "What type or rock is formed by cooling down the magma?"
    a "What type or rock is formed by cooling down the magma?"
    a "What type or rock is formed by cooling down the magma?"


label question_2_answer:

    a "{cps=35}Great job! Igneous rocks forms from magma that has cooled down and turned into solid which is a process called crystallization.{/cps}"

label question_3:

    hide screen question_2
    scene bg plain
    show ame_blink at left
    show coral_wframe with dissolve:
        size(622, 350)
        xalign .5
        yalign 0
    show screen question_3

    a "{cps=35}Fill in the blank: The carbonate sedimentary rock forms under _________.{/cps}"
    a "Fill in the blank: The carbonate sedimentary rock forms under _________."
    a "Fill in the blank: The carbonate sedimentary rock forms under _________."
    a "Fill in the blank: The carbonate sedimentary rock forms under _________."

label question_3_answer:

    a "{cps=35}That is right! The carbonate seimentary rock are formed from fossilized bodies of sea creatures found under water.{/cps}"

label question_4:

    hide screen question_3
    scene bg plain
    show ame_blink at left
    show tle 2 with dissolve:
        size(622, 350)
        xalign .5
        yalign 0
    show screen question_4

    a "{cps=35}Which layer of Earth is composed of two sections and is made out of iron alloy?{/cps}"
    a "Which layer of Earth is composed of two sections and is made out of iron alloy?"
    a "Which layer of Earth is composed of two sections and is made out of iron alloy?"
    a "Which layer of Earth is composed of two sections and is made out of iron alloy?"


label question_4_anwser:

    a "{cps=35}Doing great so far! Yes, The core is made out of iron alloy and has two parts which are the outer core and inner core.{/cps}"

label question_5:

    hide screen question_4
    scene bg plain
    show ame_blink at left
    show meta2_wframe with dissolve:
        size(622, 350)
        xalign .5
        yalign 0
    show screen question_5

    a "{cps=35}Onto the last question!{/cps}"
    a "{cps=35}Which type of rock is formed by heat and pressure?{/cps}"
    a "Which type of rock is formed by heat and pressure?"
    a "Which type of rock is formed by heat and pressure?"
    a "Which type of rock is formed by heat and pressure?"


label question_5_answer:

    a "{cps=35}Yes! The answer is metamorphic rock. Metamorphic rock forms under pressure from overlying mass, which often forms the banded feature.{/cps}"
    a "{cps=35}while the increasing heat can form shiny minerals, which is distinctive of metamorphic rocks.{/cps}"
    a "{cps=35}Amazing job on getting all the correct answers!{/cps}"
    a "{cps=35}We will now continue on to next topics.{/cps}"

################################################################################

# How to see inside the earth

# Animated images
image drilling:
    "dr_1.png"
    .5
    "dr_2.png"
    .5
    "dr_3.png"
    .5
    "dr_4.png"
    .5
    "dr_5.png"
    .5
    repeat

label inside_earth:

    hide screen question_5

    show inside
    " "

    scene bg plain
    show earth:
        size(889, 500)
        xalign .5
        yalign 0
    show ame_blink at left

    a "{cps=35}Now that we have covered what geology is and what rocks are. We now want to understand the application of geology to real world.{/cps}"
    a "{cps=35}Geologists are interested with the data that rocks provide.{/cps}"
    a "{cps=35}Geologists analyze the data and make an interpretation to optimize the information of the rocks, which then is used to solve real life problems.{/cps}"
    a "{cps=35}But before analyzing the rocks, geologists need to obtain the data and see what is inside the Earth.{/cps}"
    a "{cps=35}Many methods are used to obtain and record data from inside the Earth,{/cps}"
    a "{cps=35}some of which are drilling, observing outcrop and mapping.{/cps}"

# Drilling

label drilling:

    scene bg plain
    show ame_blink at left

    a "{cps=35}By drilling, geologists are able to collect rock samples from the subsurface that they can observe and analyze.{/cps}"

    show drilling with dissolve:
        size(711, 400)
        xalign .5
        yalign 0.2
    show ame_blink at left

    a "{cps=35}To drill, the common method is using an equipment such as a drilling rig{/cps}"
    a "{cps=35}What a drilling rig does is it will make a hole into the ground and drill down the subsurface.{/cps}"
    a "{cps=35}Then, after reaching a desired depth, a rock sample is extracted within a protective case{/cps}"

    hide drilling
    show core_wframe with dissolve:
        size(300, 450)
        xalign .5
        yalign 0.2
    show ame_teach at left


    a "{cps=35}These rock samples are also referred to as cores that provides a physical evidence that geologists use to observe and record detailed properties within the subsurface.{/cps}"

# Outcrop

label outcrop:

    scene bg plain
    show outcrop with dissolve:
        size(300, 450)
        xalign .5
        yalign 0.2
    show ame_teach at left


    a "{cps=35}Another method is by observing outcrops. Outcrops are defined as exposed bodies of rocks.{/cps}"
    a "{cps=35}This is when geologists go out on the field to observe and collect data from the outcrop.{/cps}"

    hide outcrop
    hide ame_blink
    show fieldnotes with dissolve:
        size(711, 400)
        xalign .5
        yalign 0.2
    show ame_blink at left

    a "{cps=35}On the field, geologists uses field notebooks which serves like a journal where they record every detail they observe on site.{/cps}"
    a "{cps=35}Therefore, even after geologists have no access to the site, they can go back to their notes to recall what they saw.{/cps}"
    a "{cps=35}This is very important when geologists tries to put the pieces together to make sense of the data to be able to analyze effectively.{/cps}"
    a "{cps=35}These recorded data from the outcrop help geologists understand the environment, composition and geological structures in three dimensions.{/cps}"

#Mapping

label mapping:

    scene bg plain
    show ame_blink at left
    show map at topright  behind ame_blink with dissolve
    a "{cps=35}Many geologists take all the data they get from rocks and put them on a map.{/cps}"
    a "{cps=35}These maps can help geologists think about the subsurface in three dimensions{/cps}"
    a "{cps=35}These maps can help geologists understand the past, and know where resouces or hazards may occur.{/cps}"
    hide map with dissolve

label scale:

    show scale
    " "

    scene bg plain
    show ame_blink
    a "{cps=35}Geologists look at rocks at different scales{/cps}"
    a "{cps=35}What does this mean?{/cps}"
    a "{cps=35}You can tell different things about rocks depending how closely you look at them{/cps}"
    show mountains_from_air at right
    a "{cps=35}Sometimes they look at entire mountain ranges to understand what the past looked like in an area{/cps}"
    hide mountains_from_air with dissolve
    a "{cps=35}Sometimes they look at rocks they can hold in their hand to tell them about properties of the rocks themselves{/cps}"


    show ts_2 at topleft behind ame_blink with dissolve
    a "{cps=35}And sometimes they use microscopes to look at rocks to understand more about the grains and the spaces between the grains{/cps}"
    a "{cps=35}This is a microscope slide with a very thin slice of rock. {/cps}"
    show ts_wframe at topright behind ame_blink with dissolve
    a "{cps=35}And this is how a sandstone looks under the microscope.{/cps}"
    a "{cps=35}When you go exploring, try and look at things up really, really close AND look at things from far away.{/cps}"
    a "{cps=35}That way you can get a better picture overall of how things look.{/cps}"


    hide ts_wframe with dissolve
    hide ts_2



    a "{cps=35}{/cps}"

#Review

label ending:

#add major takeaways - ask questions, explore your world, be curious, etc.
    a "{cps=35}This ends our adventure today{/cps}"
    a "{cps=35}I hope you had fun and learned something new{/cps}"
    a "{cps=35}{/cps}"
    a "{cps=35}{/cps}"
    a "{cps=35}{/cps}"
    a "{cps=35}{/cps}"

return
