
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

define a = Character("Amethyst")

#activity text
define b = Character(kind = centered, what_text_align = 0.0, what_color = "FFC53A")

#other central text
define c = Character(kind = centered, what_text_align = 0.0, what_color = "EDEBD7")


################################################################################


label start:

# title card

    jump carbonates

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

    a "{cps=35}Igneous rocks are formed by melting existing rocks deep underground{/cps}"
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
    4. Place the jars in your house where they won't be bothered.  Don't touch them for several days\n
    \n
    5. After several days lift the pencil to look for crystals."

    show ame_blink
    a "{cps=35}Students - Look at your crystal growth. What do you see?{/cps}"
    a "{cps=35}These crystals grew as the water evaporated.  Does it look different from the sugar you first put in?{/cps}"
    hide ame_blink



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
    hide mountain with dissolve


    show river behind ame_blink with dissolve
    a "{cps=35}These grains can be transported downhill and are washed into streams and rivers{/cps}"
    hide river with dissolve

    show beach with dissolve
    a "{cps=35}Those rivers carry the grains unti they can be tranported here, the beach!{/cps}"
    a "{cps=35}From there the grains can make their way underwater{/cps}"
    a "{cps=35}Grains can stack up on one another, with enough pressure to eventually squish them together, making a rock{/cps}"
    a "{cps=35}Think of this like a bag of raisins or candy left in the back of your cupboard{/cps}"
    a "{cps=35}If you forget about them for awhile, they start to stick together, with each candy being an individual grain{/cps}"
    hide beach with dissolve
    hide ame_blink with dissolve

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

    show silt_wframe at topright behind ame_teach with dissolve
    a "{cps=35}Some sedimentary rocks have grains so small you can't really see them{/cps}"
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


    b "{b} ACTIVITY TIME{/b}"
    b "We can see how sedimentary rock layers are formed \n
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
    hide ame_blink
    hide seds_activity with dissolve



label carbonates:
    scene bg plain
    show ame_teach at left

    a "{cps=35}Another type of sedimentary rocks we call carbonate rocks{/cps}"
    a "{cps=35}These sedimentary rocks are made by from the fossilized bodies of sea creatures{/cps}"
    a "{cps=35}Sometimes you can see the fossils in the rocks, sometimes you can't{/cps}"

    show coral_wframe at topright behind ame_teach with dissolve
    a "{cps=35}This is an example of a carbonate rock where you can see the fossils{/cps}"
    a "{cps=35}The circle shaped things you see on the rock are ancient corals formed under the sea.{/cps}"
    hide coral_wframe with dissolve

    show limemud_wframe at topright behind ame_teach with dissolve
    a "{cps=35}Not all carbonate rocks have fossils{/cps}"
    a "{cps=35}In this example you have the same carbonate that makes up shell material instead making mud to form the carbonate rock{/cps}"
    hide limemud_wframe with dissolve

    show evap_wframe at topright behind ame_teach with dissolve
    a "{cps=35}The last type of sedimentary rocks are called evaporites{/cps}"
    a "{cps=35}These sedimentary rocks are formed when water evaporates from a body of water{/cps}"
    a "{cps=35}Salt is an example of an evaporitic rock.  Geologists call it halite.{/cps}"
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
    a "{cps=35}Some of the differences are the minerals and what the bands look like.{/cps}"
    a "{cps=35}If you see a lot of shiny minerals, that could be a clue it is metamorhpic{/cps}"
    a "{cps=35}If the layers or bands are not straight but wiggly, that could be a clue it is metamorhpic{/cps}"

    hide meta_wframe with dissolve

    show meta2_wframe at topright behind ame_teach with dissolve
    a "{cps=35}Here is another metamorphic rock{/cps}"
    hide meta2_wframe with dissolve

    hide ame_teach




    menu:
        "It's activity time!  Do you have a parent to help you?  And do you have flour, salt, cream of tartar, food colouring and vegetable oil?\n
        If so, you can choose to do the activity now.  If not come back later."

        "Let's do the activity now!":
            jump meta_layers
        "I'll do the activity later!":
            jump rock_cycle







label meta_layers:


    b "{b} ACTIVITY TIME{/b}"
    b "We can see how metamorphic rock layers are formed\n
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

    "Melting is turning solid into liquid through high temperatures."
    "This will cause the rock to turn into magma."

    jump rock_cycle

label crystallization:
    hide screen rock_cycle
    show xtal

    "Crystallization is turning liquid into solid through cold temperatures."
    "This is the cooling down of the rock which turns into igneous rock."

    jump rock_cycle

label heat_pressure:
    hide screen rock_cycle
    show hp

    "As mentioned previously, we now know that as we go deeper into Earth's core the more heated the rocks get."
    "as well as, the deeper it gets the more pressure is applied on the rock due to overlying mass above it."
    "This then causes to form metamorphic rocks."

    jump rock_cycle

label weathering_erosion:
    hide screen rock_cycle
    show we

    "Weathering and erosion is breaking down rocks into smaller pieces."
    "We refer to these smaller pieces as sediments."

    jump rock_cycle

label compaction_cementation:
    hide screen rock_cycle
    show cc

    "The sediments are small pieces of rocks caused by weathering and erosion."
    "This can turn into sedimentary rocks by compaction and cementation,"
    "like how we glue objects to stick them together."

    jump rock_cycle



################################################################################


    #Rock quiz?
    #How to see inside the earth
    #Drilling
    #Seismic
    #Mapping


label scale:

    scene bg plain
    show ame_blink
    a "{cps=35}Geologists look at rocks at different scales{/cps}"
    a "{cps=35}What does this mean?{/cps}"
    a "{cps=35}You can tell different things about rocks depending how closely you look at them{/cps}"
    show mountains_from_air at right
    a "{cps=35}Sometimes they look at entire mountain ranges to understand what the past looked like in an area{/cps}"
    hide mountains_from_air with dissolve
    #add photo of rock in hand
    a "{cps=35}Sometimes they look at rocks they can hold in their hand to tell them about properties of the rocks themselves{/cps}"

    show ts_wframe at topright behind ame_blink with dissolve
    a "{cps=35}And sometimes they use microscopes to look at rocks to understand more about the grains and the spaces between the grains{/cps}"
    a "{cps=35}This is how a sandstone looks under the microscope.{/cps}"
    a "{cps=35}{/cps}"
    hide ts_wframe with dissolve

#Review


#Other resources



return
