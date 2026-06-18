# Nattoguard AI Revenue System

AI-powered customer intent prediction, customer segmentation, decision engine, and chatbot prototype for Nattoguard business optimization.

## Project Overview

This project demonstrates how AI tools can support business efficiency and growth using Nattoguard, a gastrointestinal health supplement, as the reference product.

The solution combines data analysis, machine learning, customer segmentation, a business decision engine, supplement-specific insight routing, and a Streamlit chatbot prototype.

Rather than using AI only as a content generation tool, this project shows how AI can support real business decisions by turning customer behavior into campaign priorities, marketing recommendations, and product-aware chatbot guidance.

## Business Objective

The project aims to help a business:

* Understand customer browsing behavior
* Predict customer purchase intent
* Segment customers into behavior-based groups
* Recommend campaign priorities and marketing channels
* Provide product-aware chatbot guidance
* Support customer service automation
* Improve marketing and conversion decision-making

## Key Business Areas Covered

This project supports several business areas related to AI-driven business optimization:

| Business Area                       | How AI Supports It                                   | Output Generated                                             |
| ----------------------------------- | ---------------------------------------------------- | ------------------------------------------------------------ |
| Funnel & Conversion Optimization    | Predicts customer purchase probability and intent    | High, medium, and low intent groups                          |
| Advertising & Campaign Optimization | Maps customers to campaign priorities                | Conversion, retargeting, education, and awareness campaigns  |
| Email & SMS Marketing               | Suggests suitable communication channels             | Email, SMS, and retargeting recommendations                  |
| Customer Service Automation         | Provides structured chatbot guidance                 | Streamlit chatbot prototype                                  |
| Analytics & Business Insights       | Uses EDA, feature importance, and segmentation       | Charts, summaries, and customer segments                     |
| Product Research & Trend Analysis   | Maps supplement-related concerns into chatbot routes | Digestion, bloating, gut wellness, and usage guidance routes |

## Main Features

### 1. Data Understanding and EDA

The project analyzes online shopper behavior to identify patterns linked to customer conversion.

Key areas explored include:

* Revenue distribution
* Product page engagement
* Page value
* Exit rate and bounce rate
* Visitor type
* Month and weekend behavior
* Features correlated with purchase behavior

### 2. Conversion Prediction Model

Machine learning models were trained to predict whether a customer session is likely to generate revenue.

Models tested:

* Logistic Regression
* Random Forest
* XGBoost

The model output is converted into customer intent groups:

* High Intent
* Medium Intent
* Low Intent

These groups help the business prioritize customers and reduce one-size-fits-all marketing.

### 3. Customer Segmentation

K-Means clustering was used to group customers based on behavioral features such as product page visits, product page duration, bounce rate, exit rate, and page value.

Customer segments created:

* Low Engagement Browsers
* Moderate Interest Visitors
* High-Value Intent Users

These segments support more personalized marketing actions.

### 4. Decision Engine

A rule-based decision engine converts AI outputs into business actions.

Inputs include:

* Purchase probability
* Intent segment
* Behavior segment
* Supplement chatbot route

Outputs include:

* Campaign priority
* Campaign type
* Suggested marketing channel
* Chatbot route

Example:

High Intent + High-Value Intent User
→ Priority 1: Immediate Conversion
→ Email/SMS reminder + checkout support chatbot route

### 5. Supplement Insight Layer

A Healthsea-style supplement insight layer was used to make the chatbot more relevant to Nattoguard as a gastrointestinal health supplement.

Supplement chatbot routes include:

* Digestive comfort
* Usage guidance
* Product education
* Gut wellness
* General support

This layer helps the chatbot provide safer and more product-aware responses without making medical claims.

### 6. Streamlit Chatbot Demo

The final chatbot prototype displays:

* Customer purchase probability
* Customer intent segment
* Customer behavior segment
* Campaign recommendation
* Suggested marketing channel
* Supplement-specific chatbot route
* Customer-facing response
* Internal business recommendation

The chatbot is rule-based and powered by the machine learning outputs, segmentation results, decision engine, and supplement insight routes.

## Project Structure

```text
Nattoguard-AI-Revenue-System/
├── app/
│   └── chatbot_demo.py
├── data/
│   └── processed/
│       └── online_shoppers_cleaned.csv
├── notebooks/
│   ├── 01_data_understanding.ipynb
│   ├── 02_eda_analysis.ipynb
│   ├── 03_conversion_prediction.ipynb
│   ├── 04_customer_segmentation.ipynb
│   ├── 05_decision_engine.ipynb
│   └── 06_healthsea_supplement_insights.ipynb
├── outputs/
│   ├── Figures/
│   ├── chatbot_inputs/
│   ├── model_results/
│   └── slide_assets/
├── .gitignore
├── README.md
└── requirements.txt
```

## Data Note

The full raw Healthsea source folder was not uploaded because it contained large source files and assets that are not required to run the final prototype.

Instead, this repository includes:

* The notebook that documents how the Healthsea-style supplement routes were created
* The processed supplement insight outputs used by the chatbot
* The final chatbot input files required to run the Streamlit demo

This keeps the repository clean, lightweight, and focused on the final working prototype.

## How to Run the Chatbot Demo

### 1. Clone the repository

```bash
git clone https://github.com/mishaalali-hub/Nattoguard-AI-Revenue-System.git
cd Nattoguard-AI-Revenue-System
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the virtual environment

For Windows:

```bash
.venv\Scripts\activate
```

For macOS/Linux:

```bash
source .venv/bin/activate
```

### 4. Install the required libraries

```bash
pip install -r requirements.txt
```

### 5. Run the Streamlit chatbot demo

```bash
streamlit run app/chatbot_demo.py
```

## Key Outputs

The project generates several business and technical outputs, including:

* Cleaned customer dataset
* EDA charts
* Model performance comparison
* Feature importance outputs
* Customer intent recommendations
* Customer behavior segments
* Decision engine outputs
* Campaign priority groups
* Supplement chatbot routes
* Streamlit chatbot prototype

## Business Value

This prototype shows how AI can help improve customer targeting, automate customer guidance, support marketing decisions, and create a more data-driven customer journey for Nattoguard.

The system can help the business:

* Focus marketing effort on higher-priority customers
* Reduce generic campaign targeting
* Improve campaign timing and channel selection
* Automate repeated customer guidance
* Support safer supplement-related communication
* Turn customer behavior data into practical business actions

## Limitations

This is a prototype built using available public/customer behavior data and processed supplement insight routes rather than live Nattoguard customer data.

The chatbot does not currently use a large language model. Instead, it uses structured rule-based responses powered by the ML outputs, decision engine, and supplement-specific routes.

## Future Improvements

Future extensions could include:

* Connecting the system to real Nattoguard website and CRM data
* Adding live product and order information
* Integrating LLMs for dynamic content generation
* Adding A/B testing to evaluate campaign performance
* Building a real-time business dashboard
* Deploying the chatbot on the website or WhatsApp
* Connecting customer intent scores to email/SMS automation tools

## Conclusion

This project demonstrates how AI can move beyond isolated tools and become a practical business decision system.

By combining machine learning, customer segmentation, a decision engine, supplement-specific insight routes, and a chatbot prototype, the system turns customer behavior into clear business actions.

The final value is that AI can help improve customer targeting, automate guidance, support marketing decisions, and create a more data-driven customer journey for Nattoguard.
