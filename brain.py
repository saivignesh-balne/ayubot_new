# Ayurvedic Dosha Configuration
dosha_types = {
    "vata": {"element": "Air+Ether", "color": "#7FB3D5"},
    "pitta": {"element": "Fire+Water", "color": "#F1948A"},
    "kapha": {"element": "Earth+Water", "color": "#7DCEA0"}
}

# Assessment Questions (6 Questions)
questions = (
    "How would you describe your body frame?",
    "What is your typical body temperature?",
    "Do you tend to have dry skin or hair?",
    "How would you describe your appetite?",
    "How do you typically handle stress?",
    "When do you feel most energetic?"
)

# Answer Mappings (Index 0-5对应 Questions 1-6)
ans_1 = ["skinny", "cold", "yes", "variable", "anxious", "morning"]        # Vata
ans_2 = ["medium", "warm", "no", "strong", "angry", "afternoon"]           # Pitta
ans_3 = ["large", "normal", "sometimes", "steady", "calm", "evening"]      # Kapha

# Dosha Descriptions
dosha_descriptions = {
    'vata': {
        'title': "Vata Dosha 🌬️",
        'characteristics': "Creative, Energetic, Lively",
        'traits': '''
            • Light, thin build<br>
            • Enthusiastic, imaginative<br>
            • Quick to learn, quick to forget<br>
            • Tendency toward anxiety<br>
            • Irregular hunger patterns
        '''
    },
    'pitta': {
        'title': "Pitta Dosha 🔥",
        'characteristics': "Intense, Focused, Driven",
        'traits': '''
            • Medium, muscular build<br>
            • Strong digestion<br>
            • Natural leadership qualities<br>
            • Competitive nature<br>
            • Dislike of hot weather
        '''
    },
    'kapha': {
        'title': "Kapha Dosha 💧", 
        'characteristics': "Calm, Grounded, Nurturing",
        'traits': '''
            • Solid, powerful build<br>
            • Excellent endurance<br>
            • Natural resistance to disease<br>
            • Slow to anger<br>
            • Affectionate, tolerant
        '''
    }
}

# Lifestyle Recommendations
dosha_recommendations = {
    'vata': {
        'diet': "Warm, nourishing foods\nCooked grains, stews, nuts",
        'yoga': "Gentle flows, grounding poses\nTree Pose, Child's Pose",
        'routine': "Regular sleep schedule\nDaily oil massage"
    },
    'pitta': {
        'diet': "Cooling foods\nSweet fruits, salads, coconut",
        'yoga': "Moderate-paced practice\nMoon salutations, forward bends",
        'routine': "Avoid excessive heat\nEvening meditation"
    },
    'kapha': {
        'diet': "Light, stimulating foods\nSteamed veggies, legumes, spices",
        'yoga': "Energetic flows\nSun salutations, backbends",
        'routine': "Regular exercise\nDry brushing before shower"
    }
}

# Conversation Flow
greetings = ["namaste", "hello", "hi", "hey", "hola", "welcome"]
farewells = ["goodbye", "bye", "see you", "farewell", "take care"]
clarifications = ["could you repeat that?", "please explain again", "not sure what you mean"]
confirmations = ["yes", "yeah", "yep", "sure", "absolutely"]

# Response Templates
response_templates = {
    'welcome': "Welcome to AyurBot! Let's discover your Prakriti through 6 simple questions.",
    'instructions': "For each question, choose the option that feels most true to you.",
    'invalid_answer': "Please choose from the given options or type 'skip' to continue.",
    'result_intro': "Based on your responses, your dominant dosha is:"
}