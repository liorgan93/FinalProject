import streamlit as st

def Song_3_page():
    from Intro import set_background
    set_background("Backround.jpeg")
    if "song_feedback" not in st.session_state:
        st.session_state.song_feedback = {}
    st.markdown(
        """
        <style>
        .container {
            background-color: black;
            color: white;
            border-radius: 25px;
            padding: 20px;
            text-align: center;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            max-width: 400px;
            margin: auto;
            font-family: Arial, sans-serif;
        }
        .song-title {
            font-size: 24px;
            font-weight: bold;
            margin-bottom: 20px;
        }
        .song-image {
            display: flex;
            justify-content: center;
            margin: 20px 0;
        }
        .stButton button {
            font-size: 16px;
            padding: 10px 40px; /* Adjust padding for better emoji display */
            border-radius: 8px;
            margin: 10px;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    # Song title
    st.markdown(
        """
        <div class="container">
            <div class="song-title">Now Playing: Stairway to Heaven By Led Zeppelin</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Centering the song image
    try:
        image_path = "song3_image.jpeg"  # Replace with your image file name
        st.image(image_path, caption="Album Cover", use_container_width=True)
    except FileNotFoundError:
        st.error("Could not load the album cover image. Please check the file path.")

    # Song audio
    st.audio("song3_audio.mp3", format="audio/mp3")  # Replace with your song file name

    # Feedback buttons with emojis
    col1, col2, col3 = st.columns([1, 3, 1])  # Adjust proportions for alignment
    with col1:
        if st.button("👍", key="like_song_3"):
            st.success("You liked this song!")
            st.session_state.song_feedback["Stairway to Heaven By Led Zeppelin"] = "Like"
            st.session_state.page = "Song_4"
            st.rerun()

    with col3:
        if st.button("👎", key="dislike_song_3"):
            st.warning("You disliked this song!")
            st.session_state.song_feedback["Stairway to Heaven By Led Zeppelin"] = "Dislike"
            st.session_state.page = "Song_4"
            st.rerun()


