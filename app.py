import streamlit as st
from organizer import scan_folder, get_ai_organization_plan, parse_plan, execute_plan

st.set_page_config(
    page_title="AI Folder Organizer",
    page_icon="🗂️",
    layout="centered"
)

st.title("🗂️ AI Folder Organizer")
st.write("Point this at any messy folder and AI will organize it for you automatically.")

with st.sidebar:
    st.header("Settings")
    groq_key = st.text_input("Groq API Key", type="password")
    st.caption("Get a free key at console.groq.com")

st.divider()

folder_path = st.text_input(
    "Folder Path",
    placeholder="e.g. /home/dashya/Downloads"
)

if "moves" not in st.session_state:
    st.session_state.moves = None

if "scanned" not in st.session_state:
    st.session_state.scanned = False

if st.button("Scan Folder", type="primary"):
    if not folder_path:
        st.warning("Please enter a folder path.")
    elif not groq_key:
        st.warning("Please enter your Groq API key in the sidebar.")
    else:
        try:
            with st.spinner("Scanning folder..."):
                files = scan_folder(folder_path)

            if not files:
                st.warning("No files found in that folder.")
            else:
                with st.spinner("AI is creating organization plan..."):
                    plan_text = get_ai_organization_plan(files, groq_key)
                    st.session_state.moves = parse_plan(plan_text)
                    st.session_state.scanned = True
                    st.session_state.folder_path = folder_path

        except FileNotFoundError:
            st.error("Folder not found. Please check the path and try again.")
        except Exception as e:
            st.error(f"Something went wrong: {str(e)}")

if st.session_state.scanned and st.session_state.moves:
    st.success(f"Found {len(st.session_state.moves)} files")
    st.subheader("📋 Organization Plan")
    st.caption("Review this before confirming. AI will move your files like this:")

    for move in st.session_state.moves:
        st.write(f"📄 **{move['original']}** → 📁 {move['folder']}/{move['new_name']}")

    st.divider()
    st.warning("⚠️ Once you confirm, files will be moved. This cannot be undone automatically.")

    if st.button("✅ Confirm and Organize", type="primary"):
        with st.spinner("Organizing your files..."):
            results = execute_plan(st.session_state.folder_path, st.session_state.moves)

        st.subheader("✅ Done!")
        for result in results:
            st.write(result)

        st.session_state.scanned = False
        st.session_state.moves = None

    if st.button("❌ Cancel"):
        st.session_state.scanned = False
        st.session_state.moves = None
        st.info("Cancelled. No files were moved.")

st.divider()
st.caption("Built with Groq AI + Streamlit")