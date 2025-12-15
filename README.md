# First Aid Expert System

A rule-based expert system that provides basic first aid guidance for common injuries. Built with Python and Streamlit.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28%2B-red)
![Expert System](https://img.shields.io/badge/Type-Rule_Based-orange)

## ⚠️ Disclaimer

**This is an educational project and should NOT be used as a substitute for professional medical advice, diagnosis, or treatment.**

## Features

- **Injury Assessment**: Interactive guided questions about injury symptoms
- **Rule-Based Reasoning**: Expert rules for accurate first aid recommendations
- **Emergency Detection**: Automatic identification of life-threatening situations
- **Modern Web Interface**: Clean, responsive Streamlit application


## Quick Start

### Prerequisites

- Python 3.8 or higher
- pip package manager
- Virtual environment (recommended)

### Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/Abinaya-Subramaniam/first-aid-expert-system.git
   cd first-aid-expert-system
   ```

2. **Create Virtual Environment** (Optional but recommended)
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate

   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**
   ```bash
   streamlit run app.py
   ```

5. **Open Your Browser**
   
   Navigate to `http://localhost:8501`

## Usage

1. **Select Injury Type**: Choose from the available injury categories
2. **Answer Questions**: Respond to system questions about your symptoms
3. **Review Assessment**: System analyzes your responses using expert rules
4. **Follow Instructions**: Receive step-by-step first aid guidance
5. **Emergency Alert**: System will indicate if immediate medical attention is needed


### Rule-Based Expert System Architecture

```
┌─────────────────┐
│  User Interface │
│   (Streamlit)   │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Inference Engine│
│  (Rules Logic)  │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Knowledge Base  │
│ (Facts & Rules) │
└─────────────────┘
```