DISCLAIMER = """
**IMPORTANT DISCLAIMER**

This is a **basic first-aid guide only**. It is **NOT a substitute for professional medical advice, diagnosis, or treatment**.

"""

INJURY_TYPES = {
    "cut": {
        "name": "Cut/Scrape",
        "questions": [
            {
                "id": "bleeding",
                "text": "How severe is the bleeding?",
                "options": [
                    {"value": "minimal", "label": "Minimal - Slow oozing"},
                    {"value": "moderate", "label": "Moderate - Steady flow"},
                    {"value": "heavy", "label": "Heavy - Rapid flow"},
                    {"value": "uncontrollable", "label": "Uncontrollable - Soaking through bandages"}
                ]
            },
            {
                "id": "embedded_object",
                "text": "Is there an object embedded in the wound?",
                "options": [
                    {"value": "no", "label": "No"},
                    {"value": "yes", "label": "Yes - DO NOT remove it"}
                ]
            },
            {
                "id": "location",
                "text": "Where is the cut located?",
                "options": [
                    {"value": "limb", "label": "Arm or Leg"},
                    {"value": "face", "label": "Face"},
                    {"value": "torso", "label": "Torso"},
                    {"value": "joint", "label": "Near a joint"}
                ]
            }
        ]
    },
    "burn": {
        "name": "Burn",
        "questions": [
            {
                "id": "degree",
                "text": "What does the burn look like?",
                "options": [
                    {"value": "first", "label": "First Degree - Red, dry, painful (like sunburn)"},
                    {"value": "second", "label": "Second Degree - Blisters, swollen, wet-looking"},
                    {"value": "third", "label": "Third Degree - Charred, white, brown, leathery"}
                ]
            },
            {
                "id": "size",
                "text": "How large is the burn area?",
                "options": [
                    {"value": "small", "label": "Smaller than palm of hand"},
                    {"value": "medium", "label": "Palm-sized to arm-sized"},
                    {"value": "large", "label": "Larger than arm or multiple areas"}
                ]
            },
            {
                "id": "location",
                "text": "Where is the burn located?",
                "options": [
                    {"value": "limb", "label": "Arm or Leg"},
                    {"value": "face", "label": "Face, hands, feet, or groin"},
                    {"value": "airway", "label": "Possible airway involvement (difficulty breathing)"}
                ]
            }
        ]
    },
    "sprain": {
        "name": "Sprain/Strain",
        "questions": [
            {
                "id": "pain_level",
                "text": "How severe is the pain?",
                "options": [
                    {"value": "mild", "label": "Mild - Can move with some discomfort"},
                    {"value": "moderate", "label": "Moderate - Painful to move or bear weight"},
                    {"value": "severe", "label": "Severe - Cannot bear weight, extreme pain"}
                ]
            },
            {
                "id": "swelling",
                "text": "Is there swelling?",
                "options": [
                    {"value": "none", "label": "None or minimal"},
                    {"value": "moderate", "label": "Moderate - Noticeable swelling"},
                    {"value": "severe", "label": "Severe - Rapid, significant swelling"}
                ]
            },
            {
                "id": "deformity",
                "text": "Is the area deformed or misaligned?",
                "options": [
                    {"value": "no", "label": "No - Looks normal"},
                    {"value": "yes", "label": "Yes - Looks deformed or bone might be broken"}
                ]
            }
        ]
    },
    "insect_bite": {
        "name": "Insect Bite/Sting",
        "questions": [
            {
                "id": "allergic_signs",
                "text": "Are there signs of allergic reaction?",
                "options": [
                    {"value": "none", "label": "No - Just local pain/itching"},
                    {"value": "mild", "label": "Mild - Some swelling beyond bite area"},
                    {"value": "severe", "label": "Yes - Difficulty breathing, throat swelling, dizziness"}
                ]
            },
            {
                "id": "stinger",
                "text": "Is there a stinger present?",
                "options": [
                    {"value": "no", "label": "No stinger visible"},
                    {"value": "yes", "label": "Yes - Stinger is embedded"}
                ]
            },
            {
                "id": "type",
                "text": "What type of insect?",
                "options": [
                    {"value": "unknown", "label": "Don't know"},
                    {"value": "bee_wasp", "label": "Bee/Wasp"},
                    {"value": "spider", "label": "Spider"},
                    {"value": "tick", "label": "Tick"}
                ]
            }
        ]
    }
}

EMERGENCY_CONDITIONS = [
    "uncontrollable bleeding",
    "third degree burns",
    "large burns",
    "burns on face/hands/feet/groin",
    "airway burns",
    "severe allergic reaction",
    "deformity suggesting fracture",
    "unconsciousness",
    "difficulty breathing",
    "chest pain"
]

def get_injury_questions(injury_type):
    return INJURY_TYPES.get(injury_type, {}).get("questions", [])

def get_injury_name(injury_type):
    return INJURY_TYPES.get(injury_type, {}).get("name", "Unknown Injury")