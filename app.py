import streamlit as st
import os

from diet import bmi_calculator, bmr_calculator, tdee_calculator, calorie_target
from rag import load_rag

from openai import OpenAI
from dotenv import load_dotenv


# --------------------- LLM --------------------- #

load_dotenv(r"C:\ai health assistant project\.env")

HF_TOKEN = os.getenv("HF_TOKEN")

# print("HF TOKEN FOUND:", HF_TOKEN is not None)

if not HF_TOKEN:
    st.error("HF_TOKEN not found. Please check your .env file.")
    st.stop()

client = OpenAI(
   base_url="https://router.huggingface.co/v1",
    api_key=HF_TOKEN
)


# --------------------- LLM --------------------- #

st.set_page_config(layout="wide")

st.title("AI HEALTH ASSISTANT 🏋️")

st.write("Personal Health Assistance and Diet Recommendation Agent")

st.header("Health Information")


st.sidebar.header("🤷‍♂️ Your Information")


# --------------------- USER INFORMATION --------------------- #

gender = st.sidebar.selectbox(
    "Gender",
    ["Male", "Female"]
)

age = st.sidebar.number_input(
    "Age",
    1,
    100
)

weight = st.sidebar.number_input(
    "Weight(Kg)",
    1,
    120
)

height = st.sidebar.number_input(
    "Height(cm)",
    100,
    200
)

activity = st.sidebar.selectbox(
    "Activity",
    [
        "Sedentary",
        "Lightly Active",
        "Moderately Active",
        "Very Active",
        "Extra Active"
    ]
)
aim = st.sidebar.selectbox(
    "AIM",
    [
        "weight maintain",
        "weight loss",
        "weight gain"
    ]
)

diet_type = st.sidebar.selectbox(
    "Diet Type",
    [
        "Vegeterian",
        "Non Vegetarian"
    ]
)

allergies = st.sidebar.selectbox(
    "Allergies",
    [
        "Allergies",
        "None"
    ]
)


# --------------------- CALCULATIONS --------------------- #

bmi = bmi_calculator(weight, height)

bmr = bmr_calculator(
    weight,
    height,
    age,
    gender
)

tdee = tdee_calculator(
    bmr,
    activity
)

calories = calorie_target(
    tdee,
    aim
)


# --------------------- METRICS --------------------- #

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "BMI",
    bmi
)

col2.metric(
    "BMR",
    f"{bmr} Kcal"
)

col3.metric(
    "TDEE",
    f"{tdee} Kcal"
)

col4.metric(
    "Calorie Target",
    f"{calories} Kcal"
)


# --------------------- TABS --------------------- #

tab1, tab2 = st.tabs(
    [
        "Diet Recommendation",
        "Health Assistance"
    ]
)


# =========================================================
# DIET RECOMMENDATION
# =========================================================

with tab1:

    if st.button("ASK AI"):

        with st.spinner("Creating Diet..."):

            try:

                db = load_rag()

                search_query = f"""
                Diet Type: {diet_type}

                Healthy food

                Protein

                Allergies: {allergies}
                """

                docs = db.similarity_search(
                    search_query,
                    3
                )

                context = "\n\n".join(
                    [doc.page_content for doc in docs]
                )


                prompt = f"""
You are a helpful AI nutrition assistant.

Use the following nutrition knowledge
to create a simple one-day diet plan.

NUTRITION KNOWLEDGE:

{context}


USER INFORMATION:

Age: {age}

Gender: {gender}

Height: {height} cm

Weight: {weight} kg

Activity Level: {activity}

Aim: {aim}

Diet Type: {diet_type}

Food Allergy: {allergies}

Estimated BMI: {bmi}

Estimated BMR: {bmr} kcal/day

Estimated TDEE: {tdee} kcal/day

Estimated Daily Calorie Target:
{calories} kcal/day


Create the following:

1. Breakfast
2. Morning Snack
3. Lunch
4. Evening Snack
5. Dinner


For every meal provide:

- Food
- Portion
- Approximate calories
- Approximate protein


IMPORTANT RULES:

- Respect the user's diet type.
- Do not recommend foods containing
  the stated allergy.
- Use the provided nutrition knowledge
  when possible.
- Keep the plan simple and practical.
- Do not diagnose diseases.
- Do not prescribe medicines.
- Do not claim to cure diseases.
- This is general wellness information,
  not medical advice.
"""


                response = client.chat.completions.create(
                    model="openai/gpt-oss-120b",
                    messages=[
                        {
                            "role": "user",
                            "content": prompt
                        }
                    ]
                )


                answer = response.choices[0].message.content

                st.markdown(answer)


            except Exception as e:

                st.error(
                    f"Error: {e}"
                )


# =========================================================
# HEALTH ASSISTANCE
# =========================================================

# with tab2:

#     question = st.text_area(
#         "Ask about health",
#         placeholder="eg: good source of vegetarian protein"
#     )


#     if st.button("Ask AI"):

#         if question:

#             try:

#                 db = load_rag()

#                 docs = db.similarity_search(
#                     question,
#                     3
#                 )


#                 context = "\n\n".join(
#                     [doc.page_content for doc in docs]
#                 )


#                 prompt = f"""
# You are an AI health and nutrition
# assistant.

# Use the following knowledge to answer
# the user's question.


# NUTRITION KNOWLEDGE:

# {context}


# USER QUESTION:

# {question}


# INSTRUCTIONS:

# - Answer clearly.
# - Keep the explanation beginner-friendly.
# - Use the provided knowledge when possible.
# - Do not invent medical facts.
# - Do not diagnose diseases.
# - Do not prescribe medicines.
# - Do not claim to cure diseases.
# - If the question concerns a serious
#   medical problem, recommend consulting
#   a qualified healthcare professional.


# This application provides general health
# and nutrition information for educational
# and wellness purposes.
# """


#                 response = client.chat.completions.create(
#                     model="openai/gpt-oss-120b",
#                     messages=[
#                         {
#                             "role": "user",
#                             "content": prompt
#                         }
#                     ]
#                 )


#                 answer = response.choices[0].message.content

#                 st.markdown(answer)


#             except Exception as e:

#                 st.error(
#                     f"Error: {e}"
#                 )

#         else:

#             st.warning(
#                 "Please enter a health question."
#             )

# =========================================================
# HEALTH ASSISTANCE
# =========================================================

with tab2:

    question = st.text_area(
        "Ask about health",
        placeholder="eg: good source of vegetarian protein"
    )

    if st.button("Ask AI"):

        if question:

            with st.spinner("Thinking..."):

                try:

                    db = load_rag()

                    docs = db.similarity_search(
                        question,
                        3
                    )

                    context = "\n\n".join(
                        [doc.page_content for doc in docs]
                    )

                    prompt = f"""
You are an AI health and nutrition assistant.

Use the following nutrition knowledge to answer
the user's question.

NUTRITION KNOWLEDGE:

{context}

USER QUESTION:

{question}

INSTRUCTIONS:

- Answer clearly.
- Keep the explanation beginner-friendly.
- Use the provided knowledge when possible.
- Do not diagnose diseases.
- Do not prescribe medicines.
- Do not claim to cure diseases.
"""

                    response = client.chat.completions.create(
                        model="openai/gpt-oss-120b",
                        messages=[
                            {
                                "role": "user",
                                "content": prompt
                            }
                        ]
                    )

                    answer = response.choices[0].message.content

                    st.markdown(answer)

                except Exception as e:

                    st.error(f"Error: {e}")

        else:

            st.warning("Please enter a health question.")