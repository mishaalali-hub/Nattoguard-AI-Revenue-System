import streamlit as st
import pandas as pd
from pathlib import Path


# ------------------------------------------------------
# Page configuration
# ------------------------------------------------------
st.set_page_config(
    page_title="Nattoguard AI Customer Guidance Assistant",
    page_icon="💬",
    layout="centered"
)


# ------------------------------------------------------
# Project paths
# ------------------------------------------------------
BASE_DIR = Path(__file__).resolve().parents[1]

DECISION_DATA_PATH = BASE_DIR / "outputs" / "chatbot_inputs" / "decision_engine_chatbot_input.csv"
HEALTH_INSIGHT_PATH = BASE_DIR / "outputs" / "chatbot_inputs" / "healthsea_supplement_chatbot_routes.csv"

# Backup path in case the older file name is still being used
if not DECISION_DATA_PATH.exists():
    DECISION_DATA_PATH = BASE_DIR / "outputs" / "chatbot_inputs" / "decision_engine_chatbot_llm_input.csv"


# ------------------------------------------------------
# Load data
# ------------------------------------------------------
@st.cache_data
def load_csv(path):
    return pd.read_csv(path)


# ------------------------------------------------------
# Business response logic
# ------------------------------------------------------
def create_business_guidance(customer_row):
    intent_segment = customer_row["intent_segment"]
    behavior_segment = customer_row["behavior_segment"]
    decision_priority = customer_row["decision_priority"]
    campaign_type = customer_row["campaign_type"]
    suggested_channel = customer_row["suggested_channel"]
    chatbot_route = customer_row["chatbot_route"]
    purchase_probability = customer_row["purchase_probability"]

    probability_percentage = round(purchase_probability * 100, 1)

    if chatbot_route == "checkout_support":
        return (
            f"This customer is classified as **{intent_segment}** with a purchase probability of "
            f"**{probability_percentage}%**. They are also part of the **{behavior_segment}** segment.\n\n"
            f"Business priority: **{decision_priority}**.\n\n"
            f"Recommended action: focus on helping the customer complete their purchase. "
            f"A suitable approach would be a checkout reminder, a gentle limited-time offer, "
            f"or a direct product purchase link.\n\n"
            f"Recommended campaign type: **{campaign_type}**.\n"
            f"Suggested channel: **{suggested_channel}**."
        )

    elif chatbot_route == "product_benefits":
        return (
            f"This customer shows a strong conversion opportunity. Their purchase probability is "
            f"**{probability_percentage}%**, and their behavior segment is **{behavior_segment}**.\n\n"
            f"Business priority: **{decision_priority}**.\n\n"
            f"Recommended action: reinforce the value of Nattoguard using benefit-focused messaging. "
            f"The customer may need more confidence before purchasing, so the response should explain "
            f"the product clearly without being too aggressive.\n\n"
            f"Recommended campaign type: **{campaign_type}**.\n"
            f"Suggested channel: **{suggested_channel}**."
        )

    elif chatbot_route == "digestive_health_education":
        return (
            f"This customer is classified as **{intent_segment}**, which suggests they may need more "
            f"information before making a purchase decision.\n\n"
            f"Business priority: **{decision_priority}**.\n\n"
            f"Recommended action: provide educational content about digestive wellness, product usage, "
            f"and how Nattoguard fits into a general gut health routine. This customer should be nurtured "
            f"before being pushed toward conversion.\n\n"
            f"Recommended campaign type: **{campaign_type}**.\n"
            f"Suggested channel: **{suggested_channel}**."
        )

    else:
        return (
            f"This customer is currently classified as **{intent_segment}** with a purchase probability "
            f"of **{probability_percentage}%**.\n\n"
            f"Business priority: **{decision_priority}**.\n\n"
            f"Recommended action: use awareness-focused content to introduce Nattoguard, explain the product "
            f"category, and build trust before direct conversion.\n\n"
            f"Recommended campaign type: **{campaign_type}**.\n"
            f"Suggested channel: **{suggested_channel}**."
        )


# ------------------------------------------------------
# Supplement response logic
# ------------------------------------------------------
def create_supplement_guidance(health_row):
    concern = health_row["extracted_concern"]
    effect_direction = health_row["effect_direction"]
    message_angle = health_row["message_angle"]
    health_route = health_row["health_chatbot_route"]
    response_template = health_row["chatbot_response_template"]

    if health_route == "digestive_comfort":
        return (
            f"The selected supplement concern is **{concern}**, with a **{effect_direction}** direction.\n\n"
            f"Recommended supplement message angle: **{message_angle}**.\n\n"
            f"Chatbot guidance: explain digestive comfort in a simple and customer-friendly way. "
            f"The response should position Nattoguard as part of a general digestive wellness routine, "
            f"without making medical treatment claims.\n\n"
            f"Template direction: {response_template}"
        )

    elif health_route == "usage_guidance":
        return (
            f"The selected supplement concern is **{concern}**, with a **{effect_direction}** direction.\n\n"
            f"Recommended supplement message angle: **{message_angle}**.\n\n"
            f"Chatbot guidance: provide safe and general product usage guidance. The chatbot should remind "
            f"customers to follow the product label and avoid giving medical advice.\n\n"
            f"Template direction: {response_template}"
        )

    elif health_route == "product_education":
        return (
            f"The selected supplement concern is **{concern}**, with a **{effect_direction}** direction.\n\n"
            f"Recommended supplement message angle: **{message_angle}**.\n\n"
            f"Chatbot guidance: focus on product education. The customer may need a clearer explanation of "
            f"what Nattoguard is, what digestive wellness means, and how supplement routines are usually "
            f"supported through consistent use.\n\n"
            f"Template direction: {response_template}"
        )

    elif health_route == "gut_wellness":
        return (
            f"The selected supplement concern is **{concern}**, with a **{effect_direction}** direction.\n\n"
            f"Recommended supplement message angle: **{message_angle}**.\n\n"
            f"Chatbot guidance: introduce Nattoguard as part of a general gut wellness routine. "
            f"The response should focus on daily support, prevention-oriented wellness, and customer education.\n\n"
            f"Template direction: {response_template}"
        )

    else:
        return (
            f"The selected supplement concern is **{concern}**.\n\n"
            f"Recommended supplement message angle: **{message_angle}**.\n\n"
            f"Chatbot guidance: provide general product awareness and encourage the customer to learn more "
            f"about Nattoguard in a safe and non-medical way.\n\n"
            f"Template direction: {response_template}"
        )


# ------------------------------------------------------
# Combined chatbot response
# ------------------------------------------------------
def generate_chatbot_response(customer_row, health_row):
    business_guidance = create_business_guidance(customer_row)
    supplement_guidance = create_supplement_guidance(health_row)

    final_response = (
        "### Customer Guidance Recommendation\n\n"
        f"{business_guidance}\n\n"
        "---\n\n"
        "### Supplement-Specific Guidance\n\n"
        f"{supplement_guidance}\n\n"
        "---\n\n"
        "### Final Chatbot Action\n\n"
        "The chatbot should combine the customer priority with the selected supplement concern. "
        "This means the response should not only recommend a campaign action, but also address the "
        "customer’s digestive wellness concern in a safe, simple, and product-aware way."
    )

    return final_response


# ------------------------------------------------------
# Streamlit user interface
# ------------------------------------------------------
st.title("💬 Nattoguard AI Customer Guidance Assistant")

st.write(
    "This prototype uses conversion prediction, customer segmentation, decision-engine output, "
    "and supplement insight routes to recommend customer engagement actions for Nattoguard."
)

st.caption(
    "This is a rule-based chatbot prototype. It does not use an LLM. "
    "The goal is to demonstrate a stable AI-supported chatbot workflow."
)

st.divider()


try:
    decision_df = load_csv(DECISION_DATA_PATH)
    health_df = load_csv(HEALTH_INSIGHT_PATH)

    st.success("Decision engine and supplement insight data loaded successfully.")

    # ------------------------------------------------------
    # Customer/session selection
    # ------------------------------------------------------
    st.subheader("1. Select Customer Scenario")

    max_rows = min(len(decision_df), 100)

    selected_customer_index = st.slider(
        "Choose a customer/session example",
        min_value=0,
        max_value=max_rows - 1,
        value=0
    )

    selected_customer = decision_df.iloc[selected_customer_index]

    # ------------------------------------------------------
    # Health concern selection
    # ------------------------------------------------------
    st.subheader("2. Select Supplement Concern")

    health_options = health_df["extracted_concern"].tolist()

    selected_concern = st.selectbox(
        "Choose a supplement-related customer concern",
        options=health_options
    )

    selected_health = health_df[health_df["extracted_concern"] == selected_concern].iloc[0]

    st.divider()

    # ------------------------------------------------------
    # AI customer profile
    # ------------------------------------------------------
    st.subheader("3. Customer AI Profile")

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Purchase Probability",
            f"{selected_customer['purchase_probability'] * 100:.1f}%"
        )

        st.write("**Intent Segment:**")
        st.info(selected_customer["intent_segment"])

        st.write("**Campaign Type:**")
        st.success(selected_customer["campaign_type"])

    with col2:
        st.write("**Behavior Segment:**")
        st.info(selected_customer["behavior_segment"])

        st.write("**Decision Priority:**")
        st.warning(selected_customer["decision_priority"])

        st.write("**Suggested Channel:**")
        st.success(selected_customer["suggested_channel"])

    # ------------------------------------------------------
    # Supplement insight profile
    # ------------------------------------------------------
    st.subheader("4. Supplement Insight Profile")

    col3, col4 = st.columns(2)

    with col3:
        st.write("**Extracted Concern:**")
        st.info(selected_health["extracted_concern"])

        st.write("**Effect Direction:**")
        st.info(selected_health["effect_direction"])

    with col4:
        st.write("**Message Angle:**")
        st.success(selected_health["message_angle"])

        st.write("**Health Chatbot Route:**")
        st.warning(selected_health["health_chatbot_route"])

    # ------------------------------------------------------
    # Chatbot recommendation
    # ------------------------------------------------------
    st.subheader("5. Chatbot Recommendation")

    response = generate_chatbot_response(selected_customer, selected_health)

    st.chat_message("assistant").write(response)

    # ------------------------------------------------------
    # Technical explanation
    # ------------------------------------------------------
    with st.expander("Show technical routing details"):
        st.write("**Customer chatbot route:**", selected_customer["chatbot_route"])
        st.write("**Health chatbot route:**", selected_health["health_chatbot_route"])
        st.write("**Decision priority:**", selected_customer["decision_priority"])
        st.write("**Campaign type:**", selected_customer["campaign_type"])
        st.write("**Suggested channel:**", selected_customer["suggested_channel"])

except FileNotFoundError as error:
    st.error("Required chatbot input file was not found.")
    st.write(error)
    st.write(
        "Please make sure Notebook 05 and Notebook 06 have been run successfully "
        "and that the required CSV files exist inside outputs/chatbot_inputs/."
    )