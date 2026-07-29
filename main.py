import streamlit as st
from few_shot import FewShotPosts
from post_generator import generate_post

st.set_page_config(
    page_title="AI LinkedIn Content Studio",
    layout="wide"
)

# ---------------------- CSS ----------------------

st.markdown("""
<style>

.main {
    padding-top: 2rem;
}

h1 {
    text-align:center;
}

.block-container{
    padding-top:2rem;
    padding-bottom:2rem;
    max-width:1000px;
}

.stButton>button{
    width:100%;
    height:52px;
    border-radius:12px;
    font-size:18px;
    font-weight:bold;
}

textarea{
    border-radius:12px !important;
}

div[data-baseweb="select"] > div{
    border-radius:10px;
}

</style>
""", unsafe_allow_html=True)

# ---------------------- Options ----------------------

length_options = ["Short", "Medium", "Long"]
language_options = ["English", "Hinglish"]

# ---------------------- App ----------------------


def main():

    st.title("AI LinkedIn Content Studio")

    st.markdown(
        "<p style='text-align:center;color:gray;'>Generate engaging LinkedIn posts in seconds using AI.</p>",
        unsafe_allow_html=True
    )

    st.divider()

    fs = FewShotPosts()
    tags = fs.get_tags()

    left, right = st.columns([1, 1])

    with left:

        st.subheader("⚙️ Post Settings")

        selected_tag = st.selectbox(
            "Topic",
            tags
        )

        selected_length = st.selectbox(
            "Length",
            length_options
        )

        selected_language = st.selectbox(
            "Language",
            language_options
        )

        tone = st.selectbox(
            "Tone",
            [
                "Professional",
                "Friendly",
                "Motivational",
                "Educational",
                "Storytelling"
            ]
        )

        generate = st.button("🚀 Generate Post")

    with right:

        st.subheader("📝 Generated Post")

        if generate:

            with st.spinner("Generating your LinkedIn post..."):

                post = generate_post(
                    selected_length,
                    selected_language,
                    selected_tag
                )

            st.text_area(
                "",
                value=post,
                height=450
            )

            c1, c2 = st.columns(2)

            with c1:
                st.download_button(
                    "📥 Download",
                    post,
                    file_name="linkedin_post.txt"
                )

            with c2:
                st.button("🔄 Regenerate")

        else:

            st.info(
                "Configure your settings and click **Generate Post**."
            )


if __name__ == "__main__":
    main()