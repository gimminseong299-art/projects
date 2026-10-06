from io import BytesIO

import streamlit as st
from PIL import Image, ImageOps, UnidentifiedImageError


st.set_page_config(page_title="이미지 팔레트 · Studio Palette", page_icon="🖼️", layout="wide")


st.page_link("designer.py", label="← Studio Palette")
st.title("이미지 팔레트")
st.caption("이미지의 색 분포를 분석해 가장 많이 쓰인 다섯 가지 색을 찾습니다.")

uploaded = st.file_uploader("이미지 선택", type=["png", "jpg", "jpeg", "webp"])
if uploaded is None:
    st.info("PNG, JPG 또는 WebP 이미지를 업로드하세요.")
    st.stop()

try:
    with Image.open(BytesIO(uploaded.getvalue())) as source:
        image = ImageOps.exif_transpose(source).convert("RGB")
except (UnidentifiedImageError, OSError, ValueError):
    st.error("이미지를 읽을 수 없습니다. 다른 이미지 파일을 선택해 주세요.")
    st.stop()

sample = image.copy()
sample.thumbnail((360, 360))
quantized = sample.quantize(colors=5, method=Image.Quantize.MEDIANCUT)
palette = quantized.getpalette()
color_counts = quantized.getcolors(maxcolors=360 * 360) or []
color_counts.sort(reverse=True)

colors: list[tuple[tuple[int, int, int], int]] = []
for count, index in color_counts[:5]:
    start = index * 3
    rgb = tuple(palette[start : start + 3])
    colors.append((rgb, count))

preview_column, palette_column = st.columns([1, 1.35], gap="large")
with preview_column:
    st.image(image, caption=uploaded.name, use_container_width=True)

with palette_column:
    st.subheader("추출된 컬러 테마")
    total_pixels = sample.width * sample.height
    for rank, (color, count) in enumerate(colors, start=1):
        hex_color = "#" + "".join(f"{channel:02X}" for channel in color)
        percentage = count / total_pixels * 100
        st.markdown(
            f'<div style="display:flex;align-items:center;gap:14px;margin:0 0 10px">'
            f'<div style="width:58px;height:48px;flex:0 0 58px;background:{hex_color};border:1px solid #d7d8d0"></div>'
            f'<div style="flex:1"><strong>{rank:02d} &nbsp; {hex_color}</strong>'
            f'<div style="height:4px;background:#e2e3dc;margin-top:8px">'
            f'<div style="height:4px;width:{percentage:.1f}%;background:#436c5a"></div></div></div>'
            f'<span style="color:#667267;font-size:.85rem">{percentage:.1f}%</span></div>',
            unsafe_allow_html=True,
        )