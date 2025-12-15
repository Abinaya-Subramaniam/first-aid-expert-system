from experta import *

class FirstAidFact(Fact):
    pass

class FirstAidRules:
    
    @staticmethod
    def get_rules():
        
        class FirstAidKnowledge(KnowledgeEngine):
            def __init__(self):
                super().__init__()
                self.recommendations = []
                self.is_emergency = False
                self.explanations = {}
            
            @Rule(FirstAidFact(bleeding='uncontrollable'))
            def rule_emergency_bleeding(self):
                self.is_emergency = True
                self.recommendations.append({
                    "title": "EMERGENCY: Uncontrollable Bleeding",
                    "steps": [
                        "Call emergency services immediately!",
                        "Apply direct pressure with clean cloth/bandage",
                        "If bleeding soaks through, add more layers - DO NOT remove",
                        "Elevate wound above heart level if possible",
                        "Keep victim warm and lying down"
                    ],
                    "urgency": "critical"
                })
                self.explanations["emergency"] = "Uncontrollable bleeding can lead to shock and is life-threatening."
            
            @Rule(
                FirstAidFact(injury_type='burn'),
                FirstAidFact(degree='third')
            )
            def rule_emergency_third_degree_burn(self):
                self.is_emergency = True
                self.recommendations.append({
                    "title": "EMERGENCY: Third Degree Burn",
                    "steps": [
                        "Call emergency services immediately!",
                        "DO NOT remove burned clothing stuck to skin",
                        "DO NOT apply water, ointments, or ice",
                        "Cover loosely with sterile non-stick dressing",
                        "Elevate burned area above heart if possible",
                        "Check breathing and monitor for shock"
                    ],
                    "urgency": "critical"
                })
            
            @Rule(
                FirstAidFact(injury_type='burn'),
                FirstAidFact(size='large')
            )
            def rule_emergency_large_burn(self):
                self.is_emergency = True
                self.recommendations.append({
                    "title": "EMERGENCY: Large Burn Area",
                    "steps": [
                        "Call emergency services immediately!",
                        "Cover with clean, dry cloth",
                        "Do not break blisters",
                        "Monitor breathing and consciousness",
                        "Treat for shock if needed"
                    ],
                    "urgency": "critical"
                })
            
            @Rule(
                FirstAidFact(injury_type='insect_bite'),
                FirstAidFact(allergic_signs='severe')
            )
            def rule_emergency_allergic_reaction(self):
                self.is_emergency = True
                self.recommendations.append({
                    "title": "EMERGENCY: Severe Allergic Reaction (Anaphylaxis)",
                    "steps": [
                        "Call emergency services immediately!",
                        "Use epinephrine auto-injector (EpiPen) if available",
                        "Help victim into comfortable position (usually sitting up)",
                        "Loosen tight clothing",
                        "Monitor breathing - be prepared for CPR",
                        "Do not give food or drink"
                    ],
                    "urgency": "critical"
                })
            
            @Rule(
                FirstAidFact(injury_type='cut'),
                FirstAidFact(bleeding='minimal'),
                FirstAidFact(embedded_object='no')
            )
            def rule_minor_cut(self):
                self.recommendations.append({
                    "title": "Minor Cut/Scrape Treatment",
                    "steps": [
                        "Wash your hands with soap and water",
                        "Apply gentle pressure with clean cloth to stop bleeding",
                        "Clean wound with cool running water and mild soap",
                        "Apply antibiotic ointment",
                        "Cover with sterile bandage or gauze",
                        "Change bandage daily and watch for signs of infection"
                    ],
                    "urgency": "low"
                })
                self.explanations["cleaning"] = "Cleaning prevents infection by removing dirt and bacteria."
                self.explanations["pressure"] = "Gentle pressure helps platelets form a clot to stop bleeding."
            
            @Rule(
                FirstAidFact(injury_type='cut'),
                FirstAidFact(bleeding='moderate'),
                FirstAidFact(embedded_object='no')
            )
            def rule_moderate_cut(self):
                self.recommendations.append({
                    "title": "Moderate Cut Treatment",
                    "steps": [
                        "Apply firm pressure with clean cloth for 10-15 minutes",
                        "Elevate wound above heart level",
                        "Clean thoroughly with soap and water once bleeding slows",
                        "Apply antibiotic ointment and sterile dressing",
                        "Seek medical attention if: bleeding doesn't stop, wound is deep, or shows signs of infection"
                    ],
                    "urgency": "medium"
                })
            
            @Rule(
                FirstAidFact(injury_type='cut'),
                FirstAidFact(embedded_object='yes')
            )
            def rule_embedded_object(self):
                self.recommendations.append({
                    "title": "Embedded Object in Wound",
                    "steps": [
                        "DO NOT remove the embedded object",
                        "Stabilize object with bulky dressing around it",
                        "Apply pressure around the object, not directly on it",
                        "Seek medical attention immediately",
                        "If object is large, call emergency services"
                    ],
                    "urgency": "high"
                })
            
            @Rule(
                FirstAidFact(injury_type='burn'),
                FirstAidFact(degree='first'),
                FirstAidFact(size='small')
            )
            def rule_minor_burn(self):
                self.recommendations.append({
                    "title": "Minor Burn (First Degree) Treatment",
                    "steps": [
                        "Cool burn under cool (not cold) running water for 10-15 minutes",
                        "Do NOT use ice, butter, or ointments on fresh burns",
                        "Gently pat dry with clean cloth",
                        "Apply aloe vera gel or burn ointment",
                        "Cover loosely with sterile non-stick gauze",
                        "Take over-the-counter pain reliever if needed"
                    ],
                    "urgency": "low"
                })
            
            @Rule(
                FirstAidFact(injury_type='burn'),
                FirstAidFact(degree='second'),
                FirstAidFact(size='small')
            )
            def rule_small_second_degree_burn(self):
                self.recommendations.append({
                    "title": "Small Second Degree Burn Treatment",
                    "steps": [
                        "Cool with cool water for 10-15 minutes",
                        "Do NOT break blisters",
                        "Pat dry gently",
                        "Apply antibiotic ointment",
                        "Cover with non-stick sterile dressing",
                        "Change dressing daily",
                        "Watch for signs of infection (pus, increased redness)"
                    ],
                    "urgency": "medium"
                })
            
            @Rule(
                FirstAidFact(injury_type='sprain'),
                FirstAidFact(pain_level='mild'),
                FirstAidFact(deformity='no')
            )
            def rule_minor_sprain(self):
                self.recommendations.append({
                    "title": "Minor Sprain Treatment (R.I.C.E. Method)",
                    "steps": [
                        "R - Rest: Avoid using injured area",
                        "I - Ice: Apply ice pack for 20 minutes every 2-3 hours (wrap in cloth)",
                        "C - Compression: Wrap with elastic bandage (not too tight)",
                        "E - Elevation: Raise above heart level to reduce swelling",
                        "Use over-the-counter pain relievers if needed",
                        "See doctor if no improvement in 2-3 days"
                    ],
                    "urgency": "low"
                })
                self.explanations["RICE"] = "R.I.C.E. reduces swelling, pain, and promotes healing."
            
            @Rule(
                FirstAidFact(injury_type='sprain'),
                OR(
                    FirstAidFact(pain_level='severe'),
                    FirstAidFact(deformity='yes')
                )
            )
            def rule_severe_sprain_or_fracture(self):
                self.recommendations.append({
                    "title": "Possible Fracture or Severe Sprain",
                    "steps": [
                        "Do NOT try to realign bone",
                        "Immobilize area with splint if available",
                        "Apply ice wrapped in cloth",
                        "Elevate if possible",
                        "Seek medical attention immediately",
                        "Do not bear weight on injured limb"
                    ],
                    "urgency": "high"
                })
            
            @Rule(
                FirstAidFact(injury_type='insect_bite'),
                FirstAidFact(allergic_signs='none'),
                FirstAidFact(stinger='yes')
            )
            def rule_bee_sting_with_stinger(self):
                self.recommendations.append({
                    "title": "Bee Sting with Stinger",
                    "steps": [
                        "Remove stinger by scraping with credit card or fingernail",
                        "DO NOT use tweezers (may squeeze more venom)",
                        "Wash area with soap and water",
                        "Apply cold pack to reduce swelling",
                        "Take antihistamine for itching if needed",
                        "Watch for allergic reaction signs"
                    ],
                    "urgency": "low"
                })
            
            @Rule(
                FirstAidFact(injury_type='insect_bite'),
                FirstAidFact(allergic_signs='none'),
                FirstAidFact(stinger='no')
            )
            def rule_general_insect_bite(self):
                self.recommendations.append({
                    "title": "General Insect Bite Treatment",
                    "steps": [
                        "Wash area with soap and water",
                        "Apply cold pack or ice wrapped in cloth",
                        "Use calamine lotion or hydrocortisone cream for itching",
                        "Take oral antihistamine if needed",
                        "Avoid scratching to prevent infection",
                        "Seek help if bite worsens or shows infection signs"
                    ],
                    "urgency": "low"
                })
            
            @Rule(
                FirstAidFact(injury_type='insect_bite'),
                FirstAidFact(type='tick')
            )
            def rule_tick_bite(self):
                self.recommendations.append({
                    "title": "Tick Bite Special Instructions",
                    "steps": [
                        "Use fine-tipped tweezers to grasp tick close to skin",
                        "Pull upward with steady pressure - don't twist or jerk",
                        "Clean bite area and your hands with rubbing alcohol or soap",
                        "Save tick in sealed bag for identification if possible",
                        "Watch for rash or fever in following weeks",
                        "See doctor if you develop symptoms"
                    ],
                    "urgency": "medium"
                })
        
        return FirstAidKnowledge