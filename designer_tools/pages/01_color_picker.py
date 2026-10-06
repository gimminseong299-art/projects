import colorsys

import streamlit as st


st.set_page_config(page_title="컬러 픽커 · Studio Palette", page_icon="🎚️", layout="wide")


def to_hex(color: tuple[int, int, int]) -> str:
    return "#" + "".join(f"{channel:02X}" for channel in color)


st.page_link("designer.py", label="← Studio Palette")
st.title("컬러 픽커")
st.caption("RGB 값을 움직여 기본색을 고르고, 조화로운 테마를 만들어 보세요.")

with st.sidebar:
    st.subheader("기본색 조정")
    red = st.slider("Red", min_value=0, max_value=255, value=220)
    green = st.slider("Green", min_value=0, max_value=255, value=104)
    blue = st.slider("Blue", min_value=0, max_value=255, value=73)

primary = (red, green, blue)
hue, saturation, value = colorsys.rgb_to_hsv(red / 255, green / 255, blue / 255)
secondary_rgb = colorsys.hsv_to_rgb(
    (hue + 1 / 12) % 1,
    max(saturation, 0.45),
    max(0.62, min(value, 0.86)),
)
secondary = tuple(round(channel * 255) for channel in secondary_rgb)
background = tuple(round(channel * 0.12 + 255 * 0.88) for channel in primary)

st.markdown(
    f'<div style="background:{to_hex(primary)};height:190px;border-radius:4px;display:flex;align-items:end;padding:22px;color:{"#17231c" if sum(primary) > 390 else "#ffffff"};font-size:1.25rem;font-weight:700">'
    f'기본색&nbsp;&nbsp; {to_hex(primary)}</div>',
    unsafe_allow_html=True,
)

st.subheader("컬러 테마")
theme = [
    ("기본색", primary),
    ("보조색 · 조화색", secondary),
    ("배경색 · 88% 틴트", background),
]
columns = st.columns(3, gap="medium")
for column, (label, color) in zip(columns, theme):
    with column:
        st.markdown(
            f'<div style="height:110px;background:{to_hex(color)};border:1px solid #d7d8d0"></div>',
            unsafe_allow_html=True,
        )
        st.markdown(f"**{label}**")
        st.code(to_hex(color), language=None)

st.caption(f"RGB  {red}, {green}, {blue}")