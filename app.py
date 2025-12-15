import streamlit as st
import sys
import os


from knowledge_base import DISCLAIMER, get_injury_name
from user_interface import (
    display_disclaimer,
    render_injury_selection,
    render_questions,
    render_results,
    render_sidebar
)
from inference_engine import InferenceEngine

st.set_page_config(
    page_title="First Aid Expert System",
    page_icon="",
    layout="wide",
    initial_sidebar_state="expanded"
)

def main():
    
    if 'engine' not in st.session_state:
        st.session_state.engine = InferenceEngine()
    if 'current_injury' not in st.session_state:
        st.session_state.current_injury = None
    if 'answers' not in st.session_state:
        st.session_state.answers = {}
    if 'results' not in st.session_state:
        st.session_state.results = None
    
    render_sidebar()
    
    st.title("First Aid Expert System")
    st.markdown("### AI-powered basic first aid guidance")
    
    display_disclaimer()
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.header("Step 1: Select Injury Type")
        selected_injury = render_injury_selection()
        
        if selected_injury:
            st.header("Step 2: Answer Questions")
            answers = render_questions(selected_injury)
            
            if answers:
                st.header("Step 3: Get Recommendations")
                
                if st.button("Get First Aid Instructions", type="primary", use_container_width=True):
                    with st.spinner("Analyzing situation and generating recommendations..."):
                        facts = {"injury_type": selected_injury}
                        facts.update(answers)
                        
                        st.session_state.engine.reset()
                        st.session_state.engine.add_facts(facts)
                        st.session_state.results = st.session_state.engine.run_inference()
                        st.session_state.current_injury = selected_injury
                        st.session_state.answers = answers
                        
                        st.rerun()
    
    with col2:
        st.header(" Quick Tips")
        
        if selected_injury:
            injury_name = get_injury_name(selected_injury)
            st.info(f"**Currently assessing:** {injury_name}")
            
            quick_tips = {
                "cut": [
                    "Always wash hands before treating wounds",
                    "Apply pressure for at least 10-15 minutes",
                    "Watch for signs of infection (redness, pus, fever)"
                ],
                "burn": [
                    "Cool with water, not ice",
                    "Don't pop blisters",
                    "Remove jewelry near burned area"
                ],
                "sprain": [
                    "Use R.I.C.E. method",
                    "Don't apply heat for first 48 hours",
                    "Seek help if you can't bear weight"
                ],
                "insect_bite": [
                    "Remove stinger by scraping, not squeezing",
                    "Watch for allergic reaction signs",
                    "Save tick for identification if possible"
                ]
            }
            
            tips = quick_tips.get(selected_injury, ["Assess carefully and seek professional help if unsure."])
            
            for tip in tips:
                st.write(f"• {tip}")
        else:
            st.info("Select an injury type to see specific tips")
    
    if st.session_state.results and "error" not in st.session_state.results:
        st.markdown("---")
        render_results(
            st.session_state.results,
            st.session_state.current_injury,
            st.session_state.answers
        )
    
    if st.session_state.results:
        if st.button("Start New Assessment", use_container_width=True):
            for key in ['current_injury', 'answers', 'results']:
                if key in st.session_state:
                    del st.session_state[key]
            st.rerun()

if __name__ == "__main__":
    main()