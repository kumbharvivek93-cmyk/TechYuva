"""
Grade-wise knowledge content for Techiva.

Kept as a plain Python data structure (not a DB table) for the MVP so it's
easy to read and extend. `get_topics_for_grade(grade)` and
`get_topic(grade, topic_id)` are the only functions the routes depend on —
swap the storage for a DB table later without touching route logic.

Each topic is one "lesson node" in the game path and has:
    id         - stable slug, used in URLs and to track progress
    title      - lesson name
    icon       - small emoji shown in a couple of places
    image      - filename of a static illustration (static/images/icons/...)
    simple     - explanation for younger grades
    technical  - deeper explanation for older grades
    quiz       - one multiple-choice question that must be answered
                 correctly to complete the lesson and earn XP
"""

GRADE_CONTENT = {
    3: [
        {
            "id": "computer",
            "title": "What is a Computer?",
            "icon": "💻",
            "image": "computer.svg",
            "simple": "A computer is a smart machine that can follow instructions, "
                      "show pictures, play games, and help us learn — just like a "
                      "very fast helper that never gets tired.",
            "technical": "A computer is an electronic device that takes input, "
                         "processes it using a set of instructions (a program), "
                         "and produces output.",
            "quiz": {
                "question": "What does a computer need to do a task?",
                "options": ["A set of instructions (a program)", "Sunlight", "Nothing, it guesses"],
                "correct": 0,
            },
        },
        {
            "id": "electricity",
            "title": "What is Electricity?",
            "icon": "⚡",
            "image": "electricity.svg",
            "simple": "Electricity is invisible energy that travels through wires "
                      "and makes things like lights and fans work.",
            "technical": "Electricity is the flow of electric charge (electrons) "
                         "through a conductor, which can be used to do work such "
                         "as producing light, heat, or motion.",
            "quiz": {
                "question": "Electricity travels through wires as a flow of...",
                "options": ["Water", "Electrons", "Air"],
                "correct": 1,
            },
        },
        {
            "id": "robot-3",
            "title": "What is a Robot?",
            "icon": "🤖",
            "image": "robot.svg",
            "simple": "A robot is a machine that can move and do tasks on its own, "
                      "sometimes copying what people or animals do.",
            "technical": "A robot is a programmable machine that senses its "
                         "environment and performs actions based on that "
                         "information, often using motors and sensors.",
            "quiz": {
                "question": "A robot uses sensors mainly to...",
                "options": ["Look pretty", "Sense its surroundings", "Make noise"],
                "correct": 1,
            },
        },
    ],
    4: [
        {
            "id": "keyboard",
            "title": "How Does a Keyboard Work?",
            "icon": "⌨️",
            "image": "keyboard.svg",
            "simple": "When you press a key, it sends a tiny signal to the "
                      "computer telling it which letter or number you touched.",
            "technical": "Each key sits above a switch. Pressing it completes a "
                         "circuit, and the keyboard controller sends a unique "
                         "code for that key to the computer.",
            "quiz": {
                "question": "Pressing a key sends a signal by completing a...",
                "options": ["Circuit", "Song", "Picture"],
                "correct": 0,
            },
        },
        {
            "id": "programming-4",
            "title": "What is Programming?",
            "icon": "📝",
            "image": "programming.svg",
            "simple": "Programming is giving step-by-step instructions to a "
                      "computer, like a recipe, so it knows exactly what to do.",
            "technical": "Programming is the process of writing code in a "
                         "language a computer can understand, to instruct it to "
                         "perform specific tasks.",
            "quiz": {
                "question": "Programming is best compared to giving a computer a...",
                "options": ["Recipe of steps", "Random guess", "Photograph"],
                "correct": 0,
            },
        },
        {
            "id": "logic-puzzles",
            "title": "Simple Logic Puzzles",
            "icon": "🧩",
            "image": "puzzle.svg",
            "simple": "Logic puzzles are brain games where you use clues to "
                      "figure out an answer — great practice for thinking like "
                      "a programmer!",
            "technical": "Logical reasoning involves using rules and given facts "
                         "to deduce new conclusions — a core skill in computer "
                         "science and mathematics.",
            "quiz": {
                "question": "Solving logic puzzles mainly builds which skill?",
                "options": ["Reasoning with clues", "Drawing", "Singing"],
                "correct": 0,
            },
        },
    ],
    5: [
        {
            "id": "sensor",
            "title": "What is a Sensor?",
            "icon": "📡",
            "image": "sensor.svg",
            "simple": "A sensor is like a sense organ for a machine. It helps a "
                      "machine understand what is happening around it.",
            "technical": "A sensor is an electronic device that detects a "
                         "physical quantity such as temperature, light, distance, "
                         "or motion and converts it into a signal a controller "
                         "can process.",
            "quiz": {
                "question": "A sensor converts a physical quantity into a...",
                "options": ["Signal a controller can use", "Sound only", "Smell"],
                "correct": 0,
            },
        },
        {
            "id": "led-resistor",
            "title": "LED and Resistor Basics",
            "icon": "💡",
            "image": "led_resistor.svg",
            "simple": "An LED is a small light that turns on with electricity. "
                      "A resistor is like a gate that controls how much "
                      "electricity flows so the LED doesn't get too much.",
            "technical": "An LED (Light Emitting Diode) emits light when current "
                         "flows through it in one direction. A resistor limits "
                         "current flow to protect components in the circuit.",
            "quiz": {
                "question": "What does a resistor do in an LED circuit?",
                "options": ["Limits current to protect the LED", "Makes the LED blink", "Stores data"],
                "correct": 0,
            },
        },
        {
            "id": "arduino-intro",
            "title": "Introduction to Arduino",
            "icon": "🔌",
            "image": "arduino.svg",
            "simple": "Arduino is a small computer board you can program to "
                      "control lights, motors, and sensors for your own "
                      "inventions.",
            "technical": "Arduino is an open-source microcontroller platform "
                         "that can be programmed (usually in C/C++) to read "
                         "sensor inputs and control outputs like motors or LEDs.",
            "quiz": {
                "question": "Arduino boards are typically programmed in...",
                "options": ["C/C++", "Only pictures", "You cannot program them"],
                "correct": 0,
            },
        },
    ],
    6: [
        {
            "id": "battery-current",
            "title": "Basic Electronics: Battery & Current",
            "icon": "🔋",
            "image": "battery.svg",
            "simple": "A battery stores energy and pushes electricity through a "
                      "circuit, kind of like a pump pushing water through a pipe.",
            "technical": "A battery converts stored chemical energy into "
                         "electrical energy, creating a potential difference "
                         "(voltage) that drives current through a circuit.",
            "quiz": {
                "question": "A battery converts stored chemical energy into...",
                "options": ["Electrical energy", "Sound energy", "Light only"],
                "correct": 0,
            },
        },
        {
            "id": "internet-basics",
            "title": "Internet Basics",
            "icon": "🌐",
            "image": "internet.svg",
            "simple": "The internet is a huge network that connects computers "
                      "all over the world so they can share information.",
            "technical": "The internet is a global system of interconnected "
                         "computer networks that communicate using standardized "
                         "protocols (like TCP/IP) to exchange data.",
            "quiz": {
                "question": "The internet connects computers using standardized...",
                "options": ["Protocols", "Colors", "Furniture"],
                "correct": 0,
            },
        },
        {
            "id": "simple-robotics",
            "title": "Simple Robotics Ideas",
            "icon": "🤖",
            "image": "robot.svg",
            "simple": "You can build simple robots using motors, wheels, and a "
                      "controller to make them move and avoid obstacles.",
            "technical": "Basic robotics combines actuators (motors), sensors "
                         "(e.g. ultrasonic), and a microcontroller running logic "
                         "that decides how the robot should respond.",
            "quiz": {
                "question": "A basic robot combines sensors, a controller, and...",
                "options": ["Actuators like motors", "Paint only", "Nothing else"],
                "correct": 0,
            },
        },
    ],
    7: [
        {
            "id": "arduino-projects",
            "title": "Arduino Projects",
            "icon": "🔧",
            "image": "arduino.svg",
            "simple": "With Arduino, you can build fun projects like a night "
                      "light that turns on by itself when it gets dark.",
            "technical": "Arduino projects combine sensor input (e.g. an LDR for "
                         "light) with conditional logic in code to trigger "
                         "outputs like relays or LEDs automatically.",
            "quiz": {
                "question": "An automatic night light decides to turn on using...",
                "options": ["Sensor input + logic", "Guessing", "A calendar only"],
                "correct": 0,
            },
        },
        {
            "id": "esp32",
            "title": "What is ESP32?",
            "icon": "📶",
            "image": "esp32.svg",
            "simple": "ESP32 is like Arduino's cousin that also has built-in "
                      "Wi-Fi, so it can connect your projects to the internet.",
            "technical": "The ESP32 is a low-cost microcontroller with "
                         "integrated Wi-Fi and Bluetooth, widely used for IoT "
                         "applications requiring wireless connectivity.",
            "quiz": {
                "question": "What makes ESP32 great for IoT projects?",
                "options": ["Built-in Wi-Fi/Bluetooth", "It has no chip", "It can't be programmed"],
                "correct": 0,
            },
        },
        {
            "id": "python-intro",
            "title": "Intro to Python",
            "icon": "🐍",
            "image": "python.svg",
            "simple": "Python is a programming language that reads almost like "
                      "English, making it a great first language to learn.",
            "technical": "Python is a high-level, interpreted programming "
                         "language known for readable syntax, widely used in "
                         "web development, automation, and data science.",
            "quiz": {
                "question": "Python is popular for beginners mainly because of its...",
                "options": ["Readable syntax", "Complicated symbols", "Lack of use"],
                "correct": 0,
            },
        },
    ],
    8: [
        {
            "id": "iot-intro",
            "title": "What is IoT?",
            "icon": "🌐",
            "image": "iot.svg",
            "simple": "IoT means connecting everyday objects, like a fan or a "
                      "plant sensor, to the internet so they can be controlled "
                      "or monitored from anywhere.",
            "technical": "The Internet of Things (IoT) refers to a network of "
                         "physical devices embedded with sensors and software "
                         "that connect and exchange data over the internet.",
            "quiz": {
                "question": "IoT devices are connected mainly to...",
                "options": ["The internet", "A landline phone only", "Nothing"],
                "correct": 0,
            },
        },
        {
            "id": "ai-basics",
            "title": "Basic AI Concepts",
            "icon": "🧠",
            "image": "ai.svg",
            "simple": "AI is when a computer learns to make decisions or "
                      "predictions, kind of like teaching it to recognize "
                      "patterns the way we do.",
            "technical": "Artificial Intelligence refers to systems that "
                         "perform tasks typically requiring human intelligence, "
                         "often by learning patterns from data.",
            "quiz": {
                "question": "AI systems often learn by finding...",
                "options": ["Patterns in data", "Random noise only", "Nothing at all"],
                "correct": 0,
            },
        },
        {
            "id": "printer3d",
            "title": "3D Printing Basics",
            "icon": "🖨️",
            "image": "printer3d.svg",
            "simple": "A 3D printer builds solid objects layer by layer from a "
                      "digital design, like a robot that draws in 3D.",
            "technical": "3D printing (additive manufacturing) creates objects "
                         "by depositing material layer by layer based on a "
                         "digital 3D model, commonly using FDM technology.",
            "quiz": {
                "question": "3D printing builds an object by...",
                "options": ["Adding material layer by layer", "Carving from a block", "Folding paper"],
                "correct": 0,
            },
        },
    ],
    9: [
        {
            "id": "ai-ml",
            "title": "AI & Machine Learning Fundamentals",
            "icon": "🤖",
            "image": "ai.svg",
            "simple": "Machine Learning is a way of teaching computers to get "
                      "better at a task by showing them lots of examples "
                      "instead of programming every rule by hand.",
            "technical": "Machine Learning is a subset of AI where models learn "
                         "statistical patterns from training data to make "
                         "predictions or decisions on new, unseen data.",
            "quiz": {
                "question": "Machine Learning models improve mainly by learning from...",
                "options": ["Training data/examples", "Guessing randomly forever", "Nothing, they're fixed"],
                "correct": 0,
            },
        },
        {
            "id": "computer-vision",
            "title": "Computer Vision Intro",
            "icon": "👁️",
            "image": "vision.svg",
            "simple": "Computer vision helps computers 'see' and understand "
                      "pictures, like recognizing a face or a stop sign.",
            "technical": "Computer vision is a field of AI that enables "
                         "computers to interpret and process visual information "
                         "from images or video, often using neural networks.",
            "quiz": {
                "question": "Computer vision lets computers interpret...",
                "options": ["Visual information", "Only sound", "Only text files"],
                "correct": 0,
            },
        },
        {
            "id": "cybersecurity",
            "title": "Cybersecurity Awareness",
            "icon": "🔒",
            "image": "cyber.svg",
            "simple": "Cybersecurity is about keeping your information and "
                      "devices safe from people who try to steal or misuse "
                      "them.",
            "technical": "Cybersecurity involves protecting systems, networks, "
                         "and data from digital attacks through practices like "
                         "encryption, authentication, and secure coding.",
            "quiz": {
                "question": "Cybersecurity practices include encryption and...",
                "options": ["Authentication", "Ignoring passwords", "Sharing passwords publicly"],
                "correct": 0,
            },
        },
    ],
    10: [
        {
            "id": "iot-advanced",
            "title": "Advanced IoT Systems",
            "icon": "🌐",
            "image": "iot.svg",
            "simple": "Advanced IoT projects connect many sensors and devices "
                      "together so they can work as a smart system, like a "
                      "smart home.",
            "technical": "Advanced IoT systems integrate multiple sensor nodes, "
                         "edge processing, and cloud services to enable "
                         "real-time monitoring, analytics, and automation.",
            "quiz": {
                "question": "Advanced IoT systems often combine sensors, cloud services, and...",
                "options": ["Edge processing/automation", "Nothing extra", "Only a battery"],
                "correct": 0,
            },
        },
        {
            "id": "career-exploration",
            "title": "Engineering Career Exploration",
            "icon": "🎓",
            "image": "career.svg",
            "simple": "There are many kinds of engineers — computer, "
                      "mechanical, electrical, and more — and each solves "
                      "different real-world problems.",
            "technical": "Engineering branches (Computer, Mechanical, "
                         "Electrical, Civil, etc.) apply scientific and "
                         "mathematical principles to design, build, and "
                         "maintain systems and infrastructure.",
            "quiz": {
                "question": "Different engineering branches mainly differ by...",
                "options": ["Which problems/systems they focus on", "Nothing, they're identical", "The color of their office"],
                "correct": 0,
            },
        },
        {
            "id": "problem-solving",
            "title": "Real-World Problem Solving",
            "icon": "🚀",
            "image": "problem.svg",
            "simple": "At this stage, you can start combining what you've "
                      "learned — electronics, code, and design — to build your "
                      "own project that solves a real problem.",
            "technical": "Real-world problem solving involves defining a "
                         "problem, researching constraints, prototyping a "
                         "solution, and iterating using engineering design "
                         "principles.",
            "quiz": {
                "question": "Good real-world problem solving involves prototyping and...",
                "options": ["Iterating on the solution", "Never testing anything", "Copying without understanding"],
                "correct": 0,
            },
        },
    ],
}


def get_available_grades():
    """Grades 3 through 10, in order."""
    return sorted(GRADE_CONTENT.keys())


# Board Lab is a reference space in addition to the grade-by-grade quests.
# It introduces boards safely; hands-on builds should happen with adult support.
DEVELOPMENT_BOARDS = [
    {"name": "Arduino Uno", "badge": "Great first board", "icon": "🔵", "best_for": "Classes 5–7 · LEDs, buzzers, sensors and simple robots", "brain": "A microcontroller — a tiny computer that repeats the code you give it.", "superpower": "Reads sensors and controls things in the real world.", "first_build": "Traffic-light LEDs or a plant-watering reminder.", "language": "Arduino code (C/C++)", "safety": "Use USB power and an adult/teacher for batteries, motors or soldering."},
    {"name": "BBC micro:bit", "badge": "Made for young inventors", "icon": "🟪", "best_for": "Classes 3–6 · First code, games and classroom inventions", "brain": "A pocket-sized microcontroller with lights, buttons and motion sensing built in.", "superpower": "You can start creating without a box of extra parts.", "first_build": "A step counter, name badge or tiny reaction game.", "language": "MakeCode blocks or Python", "safety": "Connect it by USB; ask an adult before adding external power."},
    {"name": "ESP32", "badge": "The internet inventor", "icon": "📶", "best_for": "Classes 7–9 · Smart-home and IoT ideas", "brain": "A microcontroller with Wi-Fi and Bluetooth inside.", "superpower": "Lets projects share readings or receive commands wirelessly.", "first_build": "A room-temperature display or Wi-Fi plant monitor.", "language": "Arduino code (C/C++) or MicroPython", "safety": "Use the correct 3.3V parts; check connections with a teacher first."},
    {"name": "Raspberry Pi Pico", "badge": "Code + make", "icon": "🟩", "best_for": "Classes 6–9 · Physical computing and Python projects", "brain": "A small microcontroller board designed for quick experiments.", "superpower": "A lovely bridge between block coding and real Python.", "first_build": "A button-controlled pixel art light or mini music maker.", "language": "MicroPython or C/C++", "safety": "Power it through USB while learning and keep loose wires tidy."},
    {"name": "Raspberry Pi", "badge": "A mini desktop computer", "icon": "🍓", "best_for": "Classes 8–9 · Python, cameras and bigger projects", "brain": "A single-board computer that can run a desktop operating system.", "superpower": "Can use a screen, keyboard, camera and the internet like a tiny PC.", "first_build": "A photo booth, weather station or simple coding game.", "language": "Python, Scratch and more", "safety": "Use its official power supply and never force connector pins."},
    {"name": "Arduino Nano", "badge": "Small robot helper", "icon": "🔹", "best_for": "Classes 6–9 · Compact wearables and robots", "brain": "A smaller Arduino with the same friendly maker spirit.", "superpower": "Fits into projects where space is tight.", "first_build": "A tiny wearable LED badge.", "language": "Arduino code (C/C++)", "safety": "Check the board voltage before powering sensors."},
    {"name": "Arduino Mega", "badge": "Lots of connections", "icon": "🟦", "best_for": "Classes 8–10 · Bigger robots with many parts", "brain": "An Arduino with many more input and output pins.", "superpower": "Controls many sensors, motors and displays together.", "first_build": "A multi-sensor robot dashboard.", "language": "Arduino code (C/C++)", "safety": "Motors need their own suitable power supply."},
    {"name": "Arduino Leonardo", "badge": "Keyboard trickster", "icon": "⌨️", "best_for": "Classes 7–10 · Interactive input projects", "brain": "An Arduino that can act like a USB keyboard or mouse.", "superpower": "Turns buttons and sensors into computer controls.", "first_build": "A safe custom game controller.", "language": "Arduino code (C/C++)", "safety": "Test keyboard-style code carefully so it does not type unexpectedly."},
    {"name": "ESP8266", "badge": "Wi-Fi starter", "icon": "📡", "best_for": "Classes 7–10 · Simple wireless sensors", "brain": "An affordable Wi-Fi microcontroller.", "superpower": "Connects a small project to the internet.", "first_build": "A Wi-Fi temperature reporter.", "language": "Arduino code or MicroPython", "safety": "It is a 3.3V board; do not give its pins 5V signals."},
    {"name": "ESP32-CAM", "badge": "Camera inventor", "icon": "📷", "best_for": "Classes 8–10 · Camera and smart-security experiments", "brain": "An ESP32 with a tiny camera connector.", "superpower": "Can take images while using Wi-Fi.", "first_build": "A classroom nature camera prototype.", "language": "Arduino code (C/C++)", "safety": "Use responsibly: get permission before photographing people."},
    {"name": "Raspberry Pi 5", "badge": "Powerful mini PC", "icon": "🖥️", "best_for": "Classes 9–10 · AI, cameras and advanced code", "brain": "A modern single-board computer for demanding projects.", "superpower": "Runs desktop apps and larger coding tools.", "first_build": "A camera-powered nature journal.", "language": "Python, Scratch and more", "safety": "Use cooling and the official USB-C supply when needed."},
    {"name": "Raspberry Pi Zero", "badge": "Tiny Pi", "icon": "⚪", "best_for": "Classes 8–10 · Small lightweight computer projects", "brain": "A very small Raspberry Pi computer.", "superpower": "Brings computer power to compact inventions.", "first_build": "A mini photo display.", "language": "Python, Scratch and more", "safety": "Handle connectors gently and use the correct power adapter."},
]


# These compact records power explorer cards while keeping lessons easy to extend.
SENSORS = [
    {"name": "HC-SR04 Ultrasonic", "category": "Distance", "icon": "📏", "detects": "Distance using sound echoes", "works": "Sends a high-pitched sound pulse and times its return.", "power": "5V", "boards": "Arduino Uno/Nano, ESP32 (level-shift ECHO)", "project": "Obstacle avoiding robot", "difficulty": "Beginner", "precaution": "Keep its two round transmitters clear."},
    {"name": "IR Proximity", "category": "Distance", "icon": "👁️", "detects": "Nearby objects", "works": "Looks for reflected infrared light.", "power": "3.3–5V", "boards": "Arduino, ESP32, Raspberry Pi Pico", "project": "Line-following robot", "difficulty": "Beginner", "precaution": "Sunlight can affect readings."},
    {"name": "DHT11 / DHT22", "category": "Temperature", "icon": "🌡️", "detects": "Temperature and humidity", "works": "A tiny chip measures air conditions and sends digital data.", "power": "3.3–5V", "boards": "Arduino, ESP32, Pico", "project": "Weather station", "difficulty": "Beginner", "precaution": "Wait a few seconds between readings."},
    {"name": "PIR Motion", "category": "Motion", "icon": "🏃", "detects": "Warm moving bodies", "works": "Notices changes in infrared heat.", "power": "5V", "boards": "Arduino, ESP32", "project": "Smart security light", "difficulty": "Beginner", "precaution": "Let it settle after switching on."},
    {"name": "LDR Light Sensor", "category": "Light", "icon": "☀️", "detects": "Light level", "works": "Its resistance changes in light and darkness.", "power": "3.3–5V", "boards": "Arduino, ESP32, Pico", "project": "Automatic night lamp", "difficulty": "Beginner", "precaution": "Use a resistor to make a voltage divider."},
    {"name": "Soil Moisture", "category": "Water", "icon": "🌱", "detects": "How wet soil is", "works": "Measures how easily electricity travels through soil.", "power": "3.3–5V", "boards": "Arduino, ESP32", "project": "Plant monitoring", "difficulty": "Beginner", "precaution": "Use briefly to reduce probe corrosion."},
    {"name": "MQ-2 Gas", "category": "Environment", "icon": "💨", "detects": "Smoke and combustible gases", "works": "A heated sensing material changes resistance.", "power": "5V", "boards": "Arduino, ESP32 with care", "project": "Fire alarm", "difficulty": "Intermediate", "precaution": "Needs warm-up; never use it as a life-safety device."},
    {"name": "MPU6050", "category": "Motion", "icon": "🎮", "detects": "Tilt, acceleration and rotation", "works": "Combines an accelerometer and gyroscope over I2C.", "power": "3.3–5V", "boards": "Arduino, ESP32, Pico", "project": "Gesture controller", "difficulty": "Intermediate", "precaution": "Keep wires short for reliable I2C."},
]

PROJECTS = [
    {"id": "night-lamp", "title": "Automatic Night Lamp", "icon": "💡", "level": "Beginner", "time": "45 min", "board": "Arduino Uno", "components": "LDR, LED, 220Ω resistor, 10kΩ resistor, breadboard", "idea": "Read the light level; when it gets dark, turn the LED on.", "flow": "LDR → Arduino analog input → decision → LED", "steps": ["Build an LDR voltage divider to A0.", "Connect LED positive leg through 220Ω resistor to pin 9.", "Read A0, choose a darkness threshold, then light the LED."], "challenge": "Can you make the lamp fade in using PWM?"},
    {"id": "robot-car", "title": "Obstacle Avoiding Robot Car", "icon": "🚗", "level": "Intermediate", "time": "2–3 hours", "board": "Arduino Uno", "components": "HC-SR04, L298N driver, 2 DC motors, chassis, battery pack", "idea": "A distance sensor helps the robot stop, reverse and turn before it bumps into something.", "flow": "HC-SR04 → Arduino → decision logic → L298N → motors", "steps": ["Test the distance sensor before attaching it to the chassis.", "Connect motor driver inputs to digital pins; use a separate motor supply.", "If distance is below 20 cm: stop, reverse briefly, then turn."], "challenge": "Add a servo so the sensor can look left and right."},
    {"id": "plant-monitor", "title": "Smart Plant Monitor", "icon": "🌱", "level": "Intermediate", "time": "90 min", "board": "ESP32", "components": "Soil moisture sensor, DHT11, LED, breadboard", "idea": "Measure soil and air, then show when a plant needs attention.", "flow": "Sensors → ESP32 → Wi-Fi / display → plant reminder", "steps": ["Read the soil sensor and calibrate dry and wet values.", "Add the DHT11 for air conditions.", "Show a friendly alert when soil becomes dry."], "challenge": "Send readings to a simple web dashboard."},
    {"id": "weather-station", "title": "IoT Weather Station", "icon": "🌦️", "level": "Advanced", "time": "3 hours", "board": "ESP32", "components": "BME280, OLED display, Wi-Fi connection", "idea": "Collect temperature, humidity and pressure, then share the data.", "flow": "BME280 → ESP32 → Wi-Fi → dashboard", "steps": ["Use I2C to connect the BME280 and test its readings.", "Display data locally on an OLED.", "Post a reading to a safe classroom dashboard."], "challenge": "Graph a full day of readings."},
]


def get_development_boards():
    return DEVELOPMENT_BOARDS


def get_topics_for_grade(grade: int):
    """Return the ordered topic list for a grade, or [] if unknown."""
    return GRADE_CONTENT.get(grade, [])


def get_topic(grade: int, topic_id: str):
    """Return a single topic dict, or None if grade/topic_id doesn't exist."""
    for topic in get_topics_for_grade(grade):
        if topic["id"] == topic_id:
            return topic
    return None
