# Nattoguard-AI-Revenue-System
AI-powered customer intent prediction, segmentation, decision engine, and chatbot prototype for Nattoguard business optimization.

# AI Revenue Optimization & Customer Guidance System for Nattoguard

## Project Overview

This project was developed as part of an internship assessment for DSwiss Sdn Bhd. The goal was to demonstrate how AI tools can support business efficiency and growth using Nattoguard, a gastrointestinal health supplement, as the reference product.

The solution combines data analysis, machine learning, customer segmentation, a business decision engine, supplement-specific insight routing, and a Streamlit chatbot prototype.

## Business Objective

The project aims to help a business:

* Understand customer browsing behavior
* Predict purchase intent
* Segment customers into behavior-based groups
* Recommend campaign priorities and marketing channels
* Provide product-aware chatbot guidance
* Support customer service automation and marketing decision-making

## Main Features

### 1. Data Understanding and EDA

The project analyzes online shopper behavior to identify patterns linked to customer conversion, including product engagement, page value, exit rates, bounce rates, visitor type, and timing behavior.

### 2. Conversion Prediction Model

Machine learning models were trained to predict whether a customer session is likely to generate revenue. The output is a purchase probability score and customer intent segment.

Models tested:

* Logistic Regression
* Random Forest
* XGBoost

### 3. Customer Segmentation

K-Means clustering was used to group customers into behavior-based segments:

* Low Engagement Browsers
* Moderate Interest Visitors
* High-Value Intent Users

### 4. Decision Engine

A rule-based decision engine converts AI outputs into business actions such as:

* Campaign priority
* Campaign type
* Suggested marketing channel
* Chatbot route

### 5. Supplement Insight Layer

A Healthsea-style supplement insight layer was used to create product-aware chatbot routes for Nattoguard, including:

* Digestive comfort
* Usage guidance
* Product education
* Gut wellness
* General support

### 6. Streamlit Chatbot Demo

The final chatbot prototype displays:

* Customer purchase probability
* Customer intent segment
* Behavior segment
* Campaign recommendation
* Suggested marketing channel
* Supplement-specific chatbot guidance
* Customer-facing response

## Project Structure

```text
nattoguard-ai-revenue-system/
├── app/
│   └── chatbot_demo.py
├── data/
│   ├── raw/
│   └── processed/
├── notebooks/
│   ├── 01_data_understanding.ipynb
│   ├── 02_eda_analysis.ipynb
│   ├── 03_conversion_prediction.ipynb
│   ├── 04_customer_segmentation.ipynb
│   ├── 05_decision_engine.ipynb
│   └── 06_healthsea_supplement_insights.ipynb
├── outputs/
│   ├── figures/
│   ├── model_results/
│   ├── chatbot_inputs/
│   └── slide_assets/
├── requirements.txt
├── README.md
└── .gitignore
```

## How to Run the Chatbot Demo

1. Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/nattoguard-ai-revenue-system.git
cd nattoguard-ai-revenue-system
```

2. Create and activate a virtual environment:

```bash
python -m venv .venv
```

For Windows:

```bash
.venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the Streamlit app:

```bash
streamlit run app/chatbot_demo.py
```

## Business Value

This prototype shows how AI can help DSwiss improve customer targeting, automate customer guidance, support campaign decisions, and create a more data-driven customer journey for Nattoguard.

## Future Improvements

Future extensions could include:

* Connecting the system to real Nattoguard website and CRM data
* Adding live product and order information
* Integrating LLMs for dynamic content generation
* Adding A/B testing for campaign performance
* Deploying the chatbot on the website or WhatsApp
