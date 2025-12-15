from experta import *
from rules import FirstAidRules, FirstAidFact

class InferenceEngine:
    
    def __init__(self):
        self.engine_class = FirstAidRules.get_rules()
        self.engine = None
    
    def reset(self):
        self.engine = self.engine_class()
        self.engine.reset()
    
    def add_facts(self, facts_dict):
        if not self.engine:
            self.reset()
        
        for key, value in facts_dict.items():
            fact_data = {key: value}
            self.engine.declare(FirstAidFact(**fact_data))
    
    def run_inference(self):
        if not self.engine:
            return {"error": "Engine not initialized"}
        
        try:
            self.engine.run()
            
            results = {
                "recommendations": self.engine.recommendations,
                "is_emergency": self.engine.is_emergency,
                "explanations": self.engine.explanations,
                "fact_count": len(self.engine.facts)
            }
            
            return results
            
        except Exception as e:
            return {"error": str(e)}
    
    def get_explanations(self):
        if self.engine and hasattr(self.engine, 'explanations'):
            return self.engine.explanations
        return {}
    
    def format_recommendations(self, results):
        if "error" in results:
            return f"Error: {results['error']}"
        
        formatted = []
        
        if results.get('is_emergency'):
            formatted.append("#  EMERGENCY SITUATION DETECTED")
            formatted.append("**Call emergency services immediately and follow these steps:**\n")
        
        for i, rec in enumerate(results.get('recommendations', []), 1):
            formatted.append(f"### {i}. {rec.get('title', 'Recommendation')}")
            formatted.append(f"*Urgency: {rec.get('urgency', 'unknown').upper()}*")
            
            for step in rec.get('steps', []):
                formatted.append(f"- {step}")
            
            formatted.append("") 
        
        if results.get('explanations'):
            formatted.append("---")
            formatted.append("### Why these steps?")
            for key, explanation in results['explanations'].items():
                formatted.append(f"**{key.replace('_', ' ').title()}:** {explanation}")
        
        return "\n".join(formatted)