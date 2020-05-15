# You can place the script of your game in this file

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

# title card

label start:

play music "toy_piano.mp3"

scene title

" "

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
" "

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
" "

# layers of the earth

a "{cps=35}To begin, we first have to understand the different sections that makes up the Earth{/cps}"
a "{cps=35}The planet Earth can be divided into different layers{/cps}"
a "{cps=35}Imagine when you cut up an egg into half, you can see distinct layers.{/cps}"
a "{cps=35}The shell of the egg represents the crust.{/cps}"
a "{cps=35}Then, the white portion represent the mantle.{/cps}"
a "{cps=35}And the yolk is the core of the Earth.{/cps}"
a "{cps=35}Like the shell in an egg, the crust is the outermost and thinnest layer of the Earth where we live on.{/cps}"
a "{cps=35}The mantle underneath the crust consists of melted rocks and is the source of magma{/cps}"
a "{cps=35}which is the substance that erupts out from volcanoes.{/cps}"
a "{cps=35}Then, the core is made out of iron alloy that consists of two parts{/cps}"
a "{cps=35}The outer core that is in solid state{/cps}"
a "{cps=35}an the inner core in a liquid state.{/cps}"
a "{cps=35}As we go deeper down to the core, the hotter the Earth gets.{/cps}"
a "{cps=35}within the inner core, it can get hot as high  as 5000°C{/cps}"

return
