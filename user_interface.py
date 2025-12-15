import streamlit as st
from knowledge_base import INJURY_TYPES, get_injury_questions, DISCLAIMER

def display_disclaimer():
    st.warning(DISCLAIMER)
    
    agreed = st.checkbox(
        "I understand this is for informational purposes only and not medical advice",
        value=False,
        key="disclaimer_agreed"
    )
    
    if not agreed:
        st.error(" You must acknowledge the disclaimer to continue")
        st.stop()
    
    return agreed

def render_injury_selection():
    st.subheader(" What type of injury?")
    
    injury_options = list(INJURY_TYPES.keys())
    injury_names = [INJURY_TYPES[inj]["name"] for inj in injury_options]
    
    selected_index = st.radio(
        "Select the injury type:",
        range(len(injury_names)),
        format_func=lambda x: injury_names[x],
        key="injury_selection"
    )
    
    selected_injury = injury_options[selected_index]
    
    return selected_injury

def render_questions(injury_type):
    questions = get_injury_questions(injury_type)
    
    if not questions:
        st.error("No questions available for this injury type")
        return {}
    
    st.subheader(f" {INJURY_TYPES[injury_type]['name']} Assessment")
    st.write("Please answer the following questions:")
    
    answers = {}
    
    for question in questions:
        question_id = question["id"]
        question_text = question["text"]
        options = question["options"]
        
        option_values = [opt["value"] for opt in options]
        option_labels = [opt["label"] for opt in options]
        
        answer = st.selectbox(
            question_text,
            option_values,
            format_func=lambda x: dict(zip(option_values, option_labels))[x],
            key=f"q_{injury_type}_{question_id}"
        )
        
        answers[question_id] = answer
    
    return answers

def render_results(results, injury_type, answers):

    if results.get("is_emergency"):
        st.error("""
         **EMERGENCY SITUATION DETECTED**
        
        **Call emergency services immediately** (911/112/000 or your local emergency number)
        
        Follow the steps below while waiting for help:
        """)
    
    with st.expander(" Your Assessment Summary", expanded=True):
        st.write(f"**Injury Type:** {INJURY_TYPES[injury_type]['name']}")
        for q_id, answer in answers.items():
            question = next((q for q in get_injury_questions(injury_type) if q['id'] == q_id), None)
            if question:
                option_label = next((opt['label'] for opt in question['options'] if opt['value'] == answer), answer)
                st.write(f"**{question['text']}:** {option_label}")
    
    st.subheader("Recommended First Aid Steps")
    
    for i, rec in enumerate(results.get("recommendations", []), 1):
        with st.container():
            urgency = rec.get("urgency", "unknown")
            urgency_colors = {
                "critical": "red",
                "high": "orange",
                "medium": "yellow",
                "low": "green"
            }
            
            st.markdown(f"### {i}. {rec.get('title', 'Recommendation')}")
            
            for step in rec.get("steps", []):
                st.markdown(f"• {step}")
            
            st.markdown("---")
    
    if results.get("explanations"):
        st.subheader(" Understanding Why")
        for key, explanation in results["explanations"].items():
            st.info(f"**{key.replace('_', ' ').title()}:** {explanation}")
    
    st.markdown("---")

def render_sidebar():
    with st.sidebar:
        st.title("First Aid Guide")
        
        st.markdown("### Quick Reference")
        
        with st.expander("Emergency Numbers"):
            st.write("""
            **Sri Lanka:** 1990
            **Check your local emergency number**
            """)
        
        with st.expander("When to call emergency services"):
            st.write("""
            - Unconsciousness
            - Difficulty breathing
            - Severe bleeding
            - Chest pain or pressure
            - Choking
            - Severe burns
            - Suspected poisoning
            - Head injury with confusion
            - Seizures lasting >5 minutes
            """)
        
        with st.expander(" Basic First Aid Kit"):
            st.write("""
            - Adhesive bandages (various sizes)
            - Sterile gauze pads
            - Adhesive tape
            - Antiseptic wipes
            - Antibiotic ointment
            - Burn ointment
            - Elastic bandage
            - Scissors and tweezers
            - Disposable gloves
            - Digital thermometer
            - Pain relievers
            - Emergency blanket
            """)
        
        st.markdown("---")
