
import streamlit as st
from ai_engine import generate_business_plan
from database import create_database, save_plan, get_plans
from pdf_engine import create_pdf
create_database()

st.set_page_config(
    page_title="AI Business Plan Generator",
    page_icon="💼",
    layout="wide"
)

st.title("💼 AI-Based Business Plan Generation System")

st.write(
    "Generate business plans, marketing strategies, "
    "financial estimates and startup ideas using AI."
)

st.divider()

st.subheader("Enter Your Business Details")

business_idea = st.text_area(
    "What business do you want to start?",
    placeholder="Example: I want to start a bakery business..."
)

col1, col2 = st.columns(2)

with col1:
    category = st.selectbox(
        "Business Category",
        [
            "Retail",
            "Food and Bakery",
            "Technology",
            "Education",
            "Healthcare",
            "Agriculture",
            "Other"
        ]
    )

with col2:
    budget = st.number_input(
        "Investment Budget (₹)",
        min_value=0,
        value=50000,
        step=5000
    )

target = st.text_input(
    "Target Customers",
    placeholder="Example: Students, families, working people"
)

st.divider()

st.subheader("Ask AI Anything")

question = st.text_area(
    "Enter your question",
    placeholder="Example: How can I promote my business?"
)

generate = st.button(
    "Generate Business Plan",
    type="primary"
)



if generate:

    if not business_idea.strip() and not question.strip():

        st.warning("Please enter a business idea or question.")

    else:

        with st.spinner("AI is generating your business plan..."):

            try:

                result = generate_business_plan(
                    business_idea,
                    category,
                    budget,
                    target,
                    question
                )

                save_plan(
                    business_idea,
                    question,
                    result
                )

                st.subheader("Generated Business Plan")

                st.markdown(result)
                pdf_file = create_pdf(result)

                st.download_button(
                  label="Download Business Plan PDF",
                  data=pdf_file,
                  file_name="business_plan.pdf",
                  mime="application/pdf"
               )

            except Exception as e:

                st.error(f"Error: {e}")


st.divider()

st.subheader("Previous Business Plans")

plans = get_plans()

if plans:

    for plan in plans:

        with st.expander(
            f"Business Plan {plan[0]}: {plan[1]}"
        ):

            st.write("Question:", plan[2])

            st.markdown(plan[3])

            st.caption(
                "Created at: " + str(plan[4])
            )

else:

    st.info("No business plans saved yet.")

