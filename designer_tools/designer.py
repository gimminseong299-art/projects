import streamlit as st


st.set_page_config(page_title="Studio Palette", page_icon="🎨", layout="wide")

st.markdown(
    """
    <style>
    .stApp { background: #f5f4ef; }
    .block-container { max-width: 1180px; padding-top: 3rem; }
    .eyebrow { color: #536254; font-size: .78rem; font-weight: 700; text-transform: uppercase; }
    .hero-title { color: #17231c; font-family: Georgia, serif; font-size: 4.8rem; line-height: .98; margin: .45rem 0 1rem; }
    .hero-copy { color: #536254; font-size: 1.1rem; max-width: 650px; line-height: 1.65; }
    .swatch-ribbon { display: flex; height: 12px; margin: 2rem 0 2.5rem; overflow: hidden; }
    .swatch-ribbon span { flex: 1; }
    .card-index { color: #667267; font-size: .75rem; font-weight: 700; }
    @media (max-width: 640px) { .hero-title { font-size: 3rem; } }
    </style>
    <div class="eyebrow">STUDIO PALETTE / DESIGN TOOLS</div>
    <div class="hero-title">Color, with<br>intention.</div>
    <div class="hero-copy">색을 고르고, 이미지에서 발견하고, 새로운 분위기로 바꿔보세요.</div>
    <div class="swatch-ribbon"><span style="background:#dc6849"></span><span style="background:#efc84a"></span><span style="background:#436c5a"></span><span style="background:#86b7b2"></span><span style="background:#222c26"></span></div>
    """,
    unsafe_allow_html=True,
)

tools = [
    {
        "number": "01 / BUILD",
        "title": "컬러 픽커",
        "description": "RGB 값을 조정해 기본색과 조화로운 테마를 만듭니다.",
        "path": "pages/01_color_picker.py",
        "color": "#dc6849",
    },
    {
        "number": "02 / DISCOVER",
        "title": "이미지 팔레트",
        "description": "사진 속 분위기를 대표하는 다섯 가지 색을 추출합니다.",
        "path": "pages/02_image_color.py",
        "color": "#436c5a",
    },
    {
        "number": "03 / TRANSFORM",
        "title": "이미지 필터",
        "description": "흑백, 세피아, 블러 효과를 적용하고 결과를 저장합니다.",
        "path": "pages/03_image_filter.py",
        "color": "#d5a92f",
    },
]

columns = st.columns(3, gap="large")
for column, tool in zip(columns, tools):
    with column:
        with st.container(border=True):
            st.markdown(
                f'<div style="height:8px;background:{tool["color"]};margin:-1rem -1rem 1.4rem"></div>',
                unsafe_allow_html=True,
            )
            st.markdown(f'<div class="card-index">{tool["number"]}</div>', unsafe_allow_html=True)
            st.subheader(tool["title"])
            st.write(tool["description"])
            st.page_link(tool["path"], label="열기", icon=":material/arrow_forward:")