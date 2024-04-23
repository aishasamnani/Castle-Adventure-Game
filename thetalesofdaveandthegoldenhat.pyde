add_library('minim') #import library for audio files

#Screens: 1 - welcome screen, 2 - instructions screen, 3 - the beginning, 4 - the golden hat, 5 - the maze, 6 - the end, 7 - End screen
screen = 1

#Variables for Screen 1
#start button
box_x = 750
box_y = 75
box_width = 200
box_height = 100

#Variables for screen 2
#next button
box2_x = 75
box2_y = 55
box2_width = 150
box2_height = 50

#Variables for Screen 3
#variables for dave image
dave_img = None
dave_width = 62
dave_height = 75
dave_x = 100
dave_y = 505 
dave_speed = 5
jumping = False #keeps track of whether dave is jumping or not
jump_height = 175  #how high dave jumps
fall_speed = 1 #gravity - how quickly dave falls after jumping

#log obstacle
log_width = 50
log_height = 30
log_x = 750
log_y = 620

#Health bar hearts
heart_img = None
heart_img_size = 30
heart_spacing = 10
heart_num = 3 #determine how many hearts to draw on screen

#Variables for screen 4
#fighter monkey
monkey_fighter_img = None
monkey_fighter_height = 75
monkey_fighter_width = 47
monkey_fighter_x = 500
monkey_fighter_y = 575

#boss monkey
final_boss_monkey_img = None
boss_monkey_x = 600
boss_monkey_y = 565
boss_monkey_width = 61
boss_monkey_height = 85
boss_monkey_speed = 3 

#Variables for screen 5
#cartesian grid for maze using 2D lists
#0 - open path, 1 - wall
maze_grid = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1],
             [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
             [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1],
             [1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1],
             [1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1],
             [1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 1], 
             [1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 1, 0, 1],
             [1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1],
             [1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1],
             [1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1],
             [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1],
             [1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0, 1],
             [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1],
             [1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1],
             [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

#grid maze features
m_columns = 25
m_rows = 16
cell_size = 40 #each cell is 40 x 40 pixels

#frame rate variables for speed of dave in the maze
frame_delay = 15 #to control dave's speed
frame_counter = 0     
  
#dave's coordinates in maze
start_cell = (0, 1) #beginning position
m_dave_x, m_dave_y = start_cell

#keeps track of movement for keyPressed() and keyReleased() functions
moving_up = False
moving_down = False
moving_left = False
moving_right = False

#monkeys
monkey_images = []  #list to store images of monkeys
monkeys = [(19, 12), (17, 6), (6, 3), (11, 11)]  #Coordinates (grid) of the four monkeys in maze
eliminated_monkeys = [] #list keeps track of how many monkeys were defeated

#power-ups
powerup_images = []  # List to store images of power-ups
powerups = [(13, 1), (3, 5), (23, 2), (5, 14), (16, 14)] #Coordinates (grid) of the four monkeys in maze
powerups_collected = 0 #keeps trak of power ups collected


#######################################################################
# Function Name: setup()   
# Function Purpose: Defines initial screen features (screen size, stroke color, background image)
# Parameters: No parameters
# Variables: 
#img variables - used to load the image on the screen
#minim - initializes the Minim Object
#music variables - used to load music to play later on in the game
# Return: An empty 1000x650 screen, loads images and music used in game screens
#######################################################################
def setup():
    global title_screen_img, dave_img, golden_dave_img, heart_img, maze_screen_img, earth_img, end_screen_img, monkey_fighter_img, final_boss_monkey_img, keyboard_img, insructions_img, beginning_img, golden_img, castle_img, hearts_img
    global intro_music, outro_music, screen, minim
    size(1000, 650)
    stroke(0)
    #Load sounds
    minim = Minim(this) #this initializes the Minim Object and assigns it to a variable which we can use later
    intro_music = minim.loadFile("intro_music.mp3")
    outro_music = minim.loadFile("outro_music.mp3")
    
    if screen == 1:
        intro_music.play() #plays music

    elif screen == 7:
        outro_music.play() #plays music 
        
    #load images
    title_screen_img = loadImage("dungeon.jpg") #Loads title screen background image
    keyboard_img = loadImage("keyboard.png") #loads keyboard diagram
    insructions_img = loadImage("blackstar.png") 
    beginning_img = loadImage("grassy.jpg") #Loads beginning screen background
    dave_img = loadImage("dave.png") #Loads the main character image, dave
    heart_img = loadImage("heart.png") #loads heart images for health bar
    golden_img = loadImage("sunset.png") #Loads a sunset backgroudn fro golden hat screen
    monkey_fighter_img = loadImage("fighter_monkeys.png") #loads the fighter monkey image
    final_boss_monkey_img = loadImage("golden_monkey.png") #loads the final boss monkey image
    castle_img = loadImage("castle.png") #loads dungeon exterior for golden screen
    #maze screen
    maze_screen_img = loadImage("dungeon_floor.jpg") #loads maze background image
    for i in range(4):
        monkey_images.append(loadImage("fighter_monkeys.png"))
    for i in range(5):
        powerup_images.append(loadImage("powerup.png"))
    #end screen
    end_screen_img = loadImage("stars.jpg") #loads end screen background image
    earth_img = loadImage("earth.png") #loads a picture of the earth for last screen
    golden_dave_img = loadImage("dave_golden_hat.png") #loads a picture of dave wearing a golden hat
    
    
#######################################################################
# Function Name: draw()
# Function Purpose: All code in the function is continuously executed. The draw function executes all the code and functions used to draw and create the game itself
# Parameters: No parameters
# Variables: No variables
# Return: Draws all of the game screens for the game mostly through using functions
#######################################################################
def draw():
    
    if screen == 1:
        welcome_screen()
        
    if screen == 2:
        instruction_screen()
        
    if screen == 3:
        beginning_play()
        
        
    if screen == 4:
        golden_hat_play()
        
        
    if screen == 5:
        maze_play()
        dave_x = 100
        dave_y = 575
        dave_width = 62
        dave_height = 75
        dave_speed = 5
        jumping = False
        jump_height = 175  #adjust the jump height as needed
        fall_speed = 1 
        
    if screen == 6:
        end_play()
        
    if screen == 7:
        end_screen()
    
    
#######################################################################
# Function Name: welcome_screen()
# Function Purpose: This function uses shapes to draw the title of the game on the welcome screen. The title reads "The Tales of Dave and the Golden Hat".
# Parameters: No parameters
# Variables: No variables
# Return: text: "The Tales of Dave and the Golden Hat"
#######################################################################
def welcome_screen(): 
    global title_screen_img
    background(255)
    image(title_screen_img, 0, 0) #sets background to title screen image
    
    #draw title
    #THE                
    stroke(255) #white
    strokeWeight(1)
    fill(255) #white
    rect(55, 50, 100, 25)
    rect(95, 75, 25, 75) 
    rect(170, 50, 25, 100)
    rect(230, 50, 25, 100)
    rect(170, 85, 75, 25)
    rect(275, 50, 25, 100)
    rect(275, 50, 75, 20)
    rect(275, 90, 75, 20)
    rect(275, 130, 75, 20)
    
    #TALES
    rect(170, 185, 25, 150)
    rect(120, 185, 125, 25)
    rect(260, 185, 25, 150)
    rect(260, 185, 100, 25)
    rect(335, 185, 25, 150)
    rect(260, 250, 100, 25)
    rect(375, 185, 25, 150)
    rect(375, 310, 85, 25)
    rect(475, 185, 25, 150)
    rect(475, 185, 100, 25)
    rect(475, 250, 100, 25)
    rect(475, 310, 100, 25)
    rect(590, 185, 25, 75)
    rect(590, 185, 100, 25)
    rect(590, 250, 100, 25)
    rect(665, 250, 25, 75)
    rect(590, 310, 100, 25)
    
    #OF
    rect(55, 375, 75, 20)
    rect(55, 375, 20, 75)
    rect(55, 430, 75, 20)
    rect(110, 375, 20, 75)
    rect(145, 375, 20, 75)
    rect(145, 375, 75, 15)
    rect(145, 410, 55, 15)
    
    #DAVE
    stroke(121, 184, 232) #blue
    fill(121, 184, 232) #blue
    rect(260, 375, 25, 150)
    rect(260, 375, 100, 25)
    rect(335, 375, 25, 150)
    rect(260, 500, 100, 25)
    rect(375, 375, 100, 25)
    rect(375, 375, 25, 150)
    rect(450, 375, 25, 150)
    rect(375, 435, 100, 25)
    textSize(210)
    text("V", 480, 530) 
    rect(625, 375, 100, 25)
    rect(625, 375, 25, 150)
    rect(625, 440, 100, 25)
    rect(625, 505, 100, 25)
    
    #AND 
    stroke(255)
    fill(255) 
    rect(55, 550, 40, 10)
    rect(55, 550, 10, 60)
    rect(55, 575, 40, 10)
    rect(85, 550, 10, 60)
    rect(105, 550, 10, 60)
    rect(105, 550, 20, 10) 
    rect(120, 550, 10, 60)
    rect(120, 600, 20, 10)
    rect(135, 550, 10, 60)
    rect(155, 550, 10, 60)
    rect(155, 550, 40, 10)
    rect(155, 550, 10, 60)
    rect(155, 600, 40, 10)
    rect(185, 550, 10, 60)
    
    #THE
    rect(225, 550, 40, 10)
    rect(240, 550, 10, 60)
    rect(275, 550, 10, 60)
    rect(275, 575, 40, 10)
    rect(305, 550, 10, 60)
    rect(325, 550, 10, 60)
    rect(325, 550, 40, 10)
    rect(325, 575, 40, 10)
    rect(325, 600, 40, 10)
    
    #GOLDEN 
    stroke(235, 197, 12) #yellow
    fill(235, 197, 12) #yellow
    rect(395, 550, 10, 60)
    rect(395, 550, 40, 10)
    rect(395, 600, 40, 10)
    rect(425, 580, 10, 25) 
    rect(445, 550, 10, 60)
    rect(445, 550, 50, 10)
    rect(445, 600, 50, 10)
    rect(485, 550, 10, 60)
    rect(505, 550, 10, 60)
    rect(505, 600, 40, 10)
    rect(555, 550, 10, 60)
    rect(555, 550, 40, 10)
    rect(555, 600, 40, 10)
    rect(585, 550, 10, 60)
    rect(605, 550, 10, 60)
    rect(605, 550, 40, 10)
    rect(605, 575, 40, 10)
    rect(605, 600, 40, 10)
    rect(655, 550, 10, 60)
    rect(655, 550, 20, 10)
    rect(670, 550, 10, 60)
    rect(670, 600, 20, 10)
    rect(685, 550, 10, 60)
    
    #HAT 
    rect(725, 550, 10, 60)
    rect(755, 550, 10, 60)
    rect(725, 575, 40, 10)
    rect(775, 550, 10, 60)
    rect(775, 550, 40, 10)
    rect(775, 575, 40, 10)
    rect(805, 550, 10, 60)
    rect(825, 550, 40, 10)
    rect(840, 550, 10, 60)
    
    #hat drawing 
    stroke(0)
    fill(0)
    rect(825, 435, 100, 15)
    stroke(235, 197, 12)
    fill(235, 197, 12)
    rect(800, 450, 150, 25)
    rect(825, 360, 100, 75)
    
    #Start game button
    stroke(121, 184, 232)
    strokeWeight(10)
    rect(box_x, box_y, box_width, box_height)
    fill(121, 184, 232)
    textSize(50)
    text("START", box_x + 23, box_y + 20, box_width, box_height)

#######################################################################
# Function Name: instruction_screen()
# Function Purpose: This function organizes all the code for the intruction screen. 
# Parameters: No parameters
# Variables: No variables
# Return: text: Displays text and helpful images on the screen so that the user can learn how to play the game. 
#######################################################################
def instruction_screen():
    global keyboard_img, insructions_img
    
    background(0)
    image(insructions_img, 0, 0)
    stroke(255)
    textSize(65)
    fill(255)
    text("Instructions:", 300, 100)
    textSize(35)
    text("TO MOVE AROUND:", 135, 200)
    noFill()
    textSize(20)
    
    image(keyboard_img, 100, 225)
    
    text("TO USE POWER-UPS:", 550, 225)
    text("- Click on a power-up to pick it up, then touch an enemy to defeat them.               - One power-up can defeat only one enemy.", 550, 250, 400, 300)
    text("HEALTH", 550, 425)
    text("- Your health bar will be displayed in the top left corner of the screen.                  - You will lose lives if you touch an enemy without a power-up eqquiped.", 550, 450, 400, 300)
    
    #Next button
    fill(235, 197, 12)
    stroke(121, 184, 232)
    strokeWeight(5)
    rect(box2_x, box2_y, box2_width, box2_height)
    fill(121, 184, 232)
    textSize(35)
    text("NEXT>", box2_x + 20, box2_y + 5, box2_width, box2_height)
    
#######################################################################
# Function Name: the_beginning_play()
# Function Purpose: Creates the first screen of the game
# Parameters: No parameters
# Variables: No variables
# Return: Draws the first screen of the game: a sun, the main character, and dialogue, user will also be able to move character back and forth (+ jump) in side veiw, plays music
#######################################################################
def beginning_play():
    global dave_y, beginning_img
    image(beginning_img, 0, 0)
    stroke(247, 211, 119)
    fill(247, 211, 119)
    circle(500, 0, 450)
    
    update_jump()
    
    #simulate the gravity of the jump
    if not jumping and dave_y < height - dave_height:
        dave_y += fall_speed
    
    fill(138, 72, 11)
    textSize(40)
    
    #The sun's dialogue 
    if dave_x < 150:
        text("Welcome to earth, Dave.", 275, 290)
    elif 150 < dave_x < 200:
        text("I am the sun, your creator.", 250, 290) 
    elif 200 < dave_x < 250:
        text("I made you for a purpose..", 250, 290)
    elif 250 < dave_x < 300:
        text("That is, to reclaim..", 315, 290)
    elif 300 < dave_x < 350:
        fill(235, 197, 12)
        text("THE GOLDEN HAT", 325, 290)
    elif 350 < dave_x < 450:
        fill(138, 72, 11)
        text("You will need to defeat the evil monkeys.", 115, 290)
    elif 450 < dave_x < 550:
        text("Now, the journey won't be easy...", 200, 290)
    elif 550 < dave_x < 700:
        text("...but I belive in you...", 300, 290)
    elif 700 < dave_x:
        fill(196, 30, 8)
        text("...my creation.", 350, 290)
    
    strokeWeight(1)
    stroke(138, 72, 11)
    fill(138, 72, 11)
    rect(log_x, log_y, log_width, log_height)
    
    image(dave_img, dave_x, dave_y, dave_width, dave_height) #loads dave's image
    
    #Next button
    if dave_x >= 925:
        fill(235, 197, 12)
        stroke(121, 184, 232)
        strokeWeight(5)
        rect(850, 450, 100, 50)
        fill(121, 184, 232)
        textSize(25)
        text("NEXT>", 850 + 12, 450 + 10, 100, 50)
    
#######################################################################
# Function Name: golden_hat_play()
# Function Purpose: Draws the second screen of the game
# Parameters: No parameters
# Variables: No variables
# Return: Draws the second screen of the game: sun, the main character, evil monkeys, animation of a monkey leaving with the golden hat into a dungeon, still in side veiw
#######################################################################
def golden_hat_play():
    global dave_y, dave_width, dave_x, dave_height, dave_speed, dave_img, golden_img
    global monkey_fighter_img, monkey_fighter_x, monkey_fighter_y, monkey_fighter_width, monkey_fighter_height, final_boss_monkey_img, boss_monkey_x
    global heart_num, jumping, jump_height, fall_speed
    image(golden_img, 0, 0)
    strokeWeight(10)
    stroke(237, 122, 50) #dark orange
    fill(240, 163, 41) #light orange
    circle(500, 0, 450)
     
    update_jump()
    
    if not jumping and dave_y < height - dave_height:
        dave_y += fall_speed
    
    image(final_boss_monkey_img, boss_monkey_x, boss_monkey_y, boss_monkey_width, boss_monkey_height) #draws monkey
    image(castle_img, 770, 435) #draws dungeon
    image(dave_img, dave_x, dave_y, dave_width, dave_height) #Draws dave
    
    
    #the sun's Dialogue
    fill(0)
    textSize(30)
    if dave_x < 150:
        text("The night falls...soon I will no longer be here.", 175, 300)
    elif 150 < dave_x < 200:
        text("Follow that monkey into the dungeon!", 225, 300)
        boss_monkey_x += boss_monkey_speed
    elif 200 < dave_x < 250:
        text("This is where we part, Dave...", 275, 300)
        boss_monkey_x += boss_monkey_speed
    elif 250 < dave_x < 300:
        text("Be wary of the monkeys and reclaim...", 225, 300)
        boss_monkey_x += boss_monkey_speed
    elif 300 < dave_x < 400:
        fill(235, 197, 12)
        text("THE GOLDEN HAT", 375, 300)
        boss_monkey_x += boss_monkey_speed
            
    #draws health bar hearts 
    draw_heart_image()
    
    #Draws the fighter monkey
    image(monkey_fighter_img, monkey_fighter_x, monkey_fighter_y, monkey_fighter_width, monkey_fighter_height)
    
    #Draws next button
    if dave_x >= 770:
        fill(235, 197, 12)
        stroke(121, 184, 232)
        strokeWeight(5)
        rect(850, 350, 100, 50)
        fill(121, 184, 232)
        textSize(15)
        text("Enter Dungeon>", 850 + 10, 350 + 5, 100, 50)
    
    #Checks if dave touches the fighter monkey
    if dave_x + dave_width > monkey_fighter_x and dave_x < monkey_fighter_x + monkey_fighter_width and dave_y + dave_height > monkey_fighter_y:
        heart_num -= 1
        dave_x = 50  #resets dave's position after losing a life
        dave_y = 300
        boss_monkey_x = 600
        if heart_num == 0:
            game_over()
    
#######################################################################
# Function Name: maze_play()
# Function Purpose: Creates the third screen of the game
# Parameters: No parameters
# Variables: No variables
# Return: Draws the third screen of the game: the main character, a maze, a dungeon background image, a golden hat monkey in the center, power-ups, evil monkeys, top veiw (up, down, left, right)
#######################################################################
def maze_play():
    global m_dave_x, m_dave_y, moving_up, moving_down, moving_left, moving_right, frame_counter, frame_delay
    global heart_num, powerups_collected, final_boss_monkey_img
    image(maze_screen_img, -16, 0) #Sets the background to maze background image + clears canvas
    
    #draw maze
    for row in range(m_rows):
        for column in range(m_columns):
            if maze_grid[row][column] == 1:
                fill(0)
                rect(column * cell_size, row * cell_size, cell_size, cell_size)
            
    #moves character through arrow keys
    #uses frame delay to slow down the character
    if frame_counter % frame_delay == 0:
        if moving_up and m_dave_y > 0 and maze_grid[m_dave_y - 1][m_dave_x] == 0:
            m_dave_y -= 1
        elif moving_down and m_dave_y < m_rows - 1 and maze_grid[m_dave_y + 1][m_dave_x] == 0:
            m_dave_y += 1
        elif moving_left and m_dave_x > 0 and maze_grid[m_dave_y][m_dave_x - 1] == 0:
            m_dave_x -= 1
        elif moving_right and m_dave_x < m_columns - 1 and maze_grid[m_dave_y][m_dave_x + 1] == 0:
            m_dave_x += 1
    
    frame_counter += 1
    
    #draw character image in the maze
    image(dave_img, m_dave_x * cell_size, m_dave_y * cell_size, cell_size, cell_size)
    
    #draws monkeys in the maze
    #checks if user touches the monkeys
    for monkey_x, monkey_y in monkeys:
        if (monkey_x, monkey_y) not in eliminated_monkeys:
            image(monkey_images[monkeys.index((monkey_x, monkey_y))], monkey_x * cell_size, monkey_y * cell_size, cell_size, cell_size)
            if m_dave_x == monkey_x and m_dave_y == monkey_y: #if dave touches a monkey
                if powerups_collected > 0: #if user has a power-up
                    powerups_collected -= 1
                    eliminated_monkeys.append((monkey_x, monkey_y)) #adds monkey to list of eliminated monkeys, deletes from screen
                else: #no power-ups
                    heart_num -= 1 #user loses a life
                    m_dave_x, m_dave_y = start_cell  #moves character back to starting cell after losing a life
    
    #draws power-ups
    for powerup_x, powerup_y in powerups:
        if (powerup_x, powerup_y) not in eliminated_monkeys and (powerup_x, powerup_y) not in eliminated_monkeys:
            image(powerup_images[powerups.index((powerup_x, powerup_y))], powerup_x * cell_size, powerup_y * cell_size, cell_size, cell_size)
    
    #draws health bar
    draw_heart_image()
    
    image(final_boss_monkey_img, 470, 260) #draws final boss monkey

#######################################################################
# Function Name: end_play()
# Function Purpose: Creates the fourth screen of the game
# Parameters: No parameters
# Variables: No variables
# Return: Draws the fourth screen of the game: a sun, the main character, dialogue box, user will also be able to move character back and forth (+ jump) in side veiw, a golden hat on the screen.
#######################################################################
def end_play():
    global dave_y, dave_width, dave_x, dave_height, dave_speed, dave_img
    image(beginning_img, 0, 0)
    #draws sun
    stroke(247, 211, 119)
    fill(247, 211, 119)
    circle(500, 0, 450)
    
    update_jump()
    
    if not jumping and dave_y < height - dave_height:
        dave_y += fall_speed
        
    image(dave_img, dave_x, dave_y, dave_width, dave_height) #draws dave
    
    fill(138, 72, 11)
    textSize(30)
    
    #dialogue from the sun
    if dave_x < 150:
        text("Well done, Dave.", 375, 290)
    elif 150 < dave_x < 200:
        text("You have reclaimed the Golden Hat from the evil monkeys.", 90, 290)
    elif 200 < dave_x < 250:
        text("Their reign of terror finally comes to an end...", 175, 290)
    elif 250 < dave_x < 300:
        text("...and peace has been restored.", 275, 290)
    elif 300 < dave_x < 350:
        text("I do wonder however...", 325, 290)
    elif 350 < dave_x < 400:
        fill(196, 30, 8)
        text("What will you do now?", 325, 290)
    elif dave_x > 400: #next button
        fill(235, 197, 12)
        stroke(121, 184, 232)
        strokeWeight(5)
        rect(850, 550, 100, 50)
        fill(121, 184, 232)
        textSize(12)
        text("Next Chapter", 850 + 10, 550 + 5, 100, 50)
        
    #hat drawing 
    stroke(0)
    fill(0)
    rect(825, 435, 100, 15)
    stroke(235, 197, 12)
    fill(235, 197, 12)
    rect(800, 450, 150, 25)
    rect(825, 360, 100, 75)
    
#######################################################################
# Function Name: end_screen()
# Function Purpose: Creates the end screen of the game
# Parameters: No parameters
# Variables: No variables
# Return: Draws the end screen of the game: a sun, space background image, earth, plays music
#######################################################################
def end_screen():
    
    image(end_screen_img, 0, 0) #draws the end background image
    #sun drawing
    stroke(247, 211, 119)
    fill(247, 211, 119)
    circle(250, 0, 400)
    
    image(earth_img, 500, 425) #draws the earth
    image(golden_dave_img, 700, 375) #draws dave on top of earth
    textSize(100)
    text("THE END", 275, 350)
    
    #next button (back to screen 1)
    fill(235, 197, 12)
    stroke(121, 184, 232)
    strokeWeight(10)
    rect(100, 450, 200, 100)
    fill(121, 184, 232)
    textSize(25)
    text("Back to Main Menu>>", 100 + 20, 450 + 15, 200, 150)
        
    #draws health bar
    draw_heart_image()
    
#######################################################################
# Function Name: mousePressed()
# Function Purpose: manages all mouse inputs by the user
# Parameters: No parameters
# Variables: clicked_powerup - uses the coordinates of the mouse on the screen to determine if the area that the user clicked has a power-up in it
# Return: increases the value of the power-ups collected and allows the character to defeat one monkey
#######################################################################
def mousePressed():
    global powerups_collected, screen
    
    if (box_x + box_width > mouseX > box_x) and (box_y + box_height > mouseY > box_y) and screen == 1: #screen 1 button
        screen = 2
    
    if (box2_x + box2_width > mouseX > box2_x) and (box2_y + box2_height > mouseY > box2_y) and screen == 2: #screen 2 button
        screen = 3

    if (850 + 100 > mouseX > 850) and (450 + 50 > mouseY > 450) and screen == 3: #screen 3 button
        dave_x = 100
        dave_y = 575
        dave_width = 62
        dave_height = 75
        dave_speed = 5
        jumping = False
        jump_height = 175  #adjust the jump height as needed
        fall_speed = 1
        screen = 4
    
    if (850 + 100 > mouseX > 850) and (350 + 50 > mouseY > 350) and screen == 4: #screen 4 button
        noStroke()
        screen = 5
    
    #checks if the mouse is clicked on a power-up
    clicked_powerup = (int(mouseX / cell_size), int(mouseY / cell_size)) 
    if clicked_powerup in powerups and clicked_powerup not in eliminated_monkeys and screen == 5: #if valid powerup clicked
        powerups_collected += 1
        eliminated_monkeys.append(clicked_powerup)
    
    if (531 > mouseX > 470) and (345 > mouseY > 260) and screen == 5: #if user clicks on boss monkey
        screen = 6
        print(screen)
        
    if (850 + 100 > mouseX > 850) and (550 + 50 > mouseY > 550) and screen == 6: #button for screen 6 
        screen = 7 

    if (100 + 200 > mouseX > 100) and (450 + 100 > mouseY > 450) and (screen == 3 or screen == 4 or screen == 5 or screen == 7): #next button for screen 7 (back to screen 1)
        screen = 1
        
        
#######################################################################
# Function Name: keyPressed()
# Function Purpose: manages all keyboard inputs by the user
# Parameters: No parameters
# Variables: No variables
# Return: side veiw: left (left arrow), right (right arrow), jump (up arrow). top veiw: up (up arrow), left (left arrow), right (right arrow), down (down arrow)
#######################################################################
def keyPressed():
    global dave_x, jumping, screen
    global moving_up, moving_down, moving_left, moving_right
    global dave_speed

    #moves dave to the right when the right arrow key is pressed
    if keyCode == RIGHT and (screen == 3 or screen == 4 or screen == 6):
        dave_x += dave_speed
    
    #moves dave to the left when the left arrow key is pressed
    elif keyCode == LEFT and (screen == 3 or screen == 4 or screen == 6):
        dave_x -= dave_speed

    #ensures that dave stays within the screen boundaries
    dave_x = constrain(dave_x, 0, width - dave_width)
    
    #jumps when the up arrow is pressed
    if keyCode == UP and not jumping and dave_y == height - dave_height:
        jumping = True

    #adjusts variables based on arrow keys
    if keyCode == UP and screen == 5:
        moving_up = True
    elif keyCode == DOWN and screen == 5:
        moving_down = True
    elif keyCode == LEFT and screen == 5:
        moving_left = True
    elif keyCode == RIGHT and screen == 5:
        moving_right = True
        
#######################################################################
# Function Name: keyReleased()
# Function Purpose: stops applying inputs from the keyboard from the user into the game when user releases key 
# Parameters: No parameters
# Variables: No variables
# Return: stops the main character from jumping after the up arrow is released
#######################################################################
def keyReleased():
    global jumping
    global moving_up, moving_down, moving_left, moving_right
    
    #stops jumping when the up arrow is released
    if keyCode == UP:
        jumping = False    
    
    #reset variables when arrow keys are released
    if keyCode == UP and screen == 5:
        moving_up = False
    elif keyCode == DOWN and screen == 5:
        moving_down = False
    elif keyCode == LEFT and screen == 5:
        moving_left = False
    elif keyCode == RIGHT and screen == 5:
        moving_right = False
        
#######################################################################
# Function Name: update_jump()
# Function Purpose: "updates" the jump feature by making the main character fall back down after it has reached max jump height
# Parameters: No parameters
# Variables: No variables
# Return: returns main character back to ground level after jumping
#######################################################################
def update_jump():
    global dave_y, jumping

    #simulates the jump
    if jumping and dave_y > height - dave_height - jump_height:
        dave_y -= 5
    else:
        jumping = False
        
    #checks if dave is above the obstacle
    if dave_x + dave_width > log_x and dave_x < log_x + log_width and screen == 3:
        dave_y = min(dave_y, log_y - dave_height)
        
    #checks if dave is above fighter monkey
    if dave_x + dave_width > monkey_fighter_x and dave_x < monkey_fighter_x + monkey_fighter_width and screen == 4:
        dave_y = min(dave_y, monkey_fighter_y - dave_height)
        
#######################################################################
# Function Name: draw_heart_image()
# Function Purpose: to draw heart images in the corner of the game screen
# Parameters: No parameters
# Variables: No variables
# Return: returns the heart images part of the health bar
#######################################################################
def draw_heart_image():
    for i in range(heart_num): # 3 hearts - max health
        x = width - (i + 1) * (heart_img_size + heart_spacing)
        y = heart_spacing
        image(heart_img, x, y, heart_img_size, heart_img_size) #draws health bar
        
#######################################################################
# Function Name: gome_over()
# Function Purpose: To stop the player from continuing to play after they have lost all of their lives
# Parameters: No parameters
# Variables: No variables
# Return: Sends the user to the end of the game if they lose all their lives
#######################################################################
def game_over():
    global heart_num, screen
    background(0)
    fill(204, 14, 14) #red
    textSize(75)
    if frameCount % 2 == 0: #causes 'game over' to blink 
        text("GAME OVER", 400, 300)
        fill(255)
        textSize(20)
        fill(235, 197, 12)
        stroke(121, 184, 232)
        strokeWeight(10)
        rect(100, 450, 200, 100)
        fill(121, 184, 232)
        textSize(25)
        text("Back to Main Menu>>", 100 + 20, 450 + 15, 200, 150)
        screen = 7
        
#######################################################################
# Function Name: constrain()
# Function Purpose: limits the values of the main character's a and y positions so that it move past the limit of the screen size
# Parameters: value, min_val - the minimum value (coordinate x or y point it is limited to), max_val - the maximum value (coordinate x or y point it is limited to)
# Variables: No variables
# Return: main character stops once it reaches one of the four corners of the screen
#######################################################################
def constrain(value, min_val, max_val):
    return min(max_val, max(min_val, value)) #uses min an max values of the screen to create boundaries to limit how far the character can move
    
