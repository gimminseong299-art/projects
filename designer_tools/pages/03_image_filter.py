from io import BytesIO

import streamlit as st
from PIL import Image, ImageFilter, ImageOps, UnidentifiedImageError


st.set_page_config(page_title="이미지 필터 · Studio Palette", page_icon="🪄", layout="wide")


st.page_link("designer.py", label="← Studio Palette")
st.title("이미지 필터")
st.caption("이미지에 분위기를 더하고 결과를 PNG로 저장합니다.")

uploaded = st.file_uploader("이미지 선택", type=["png", "jpg", "jpeg", "webp"])
if uploaded is None:
    st.info("PNG, JPG 또는 WebP 이미지를 업로드하세요.")
    st.stop()

try:
    with Image.open(BytesIO(uploaded.getvalue())) as source:
        if source.width * source.height > 40_000_000:
            st.error("이미지 크기는 4천만 픽셀 이하로 제한됩니다.")
            st.stop()
        image = ImageOps.exif_transpose(source).convert("RGB")
except (UnidentifiedImageError, OSError, ValueError, Image.DecompressionBombError):
    st.error("이미지를 읽을 수 없습니다. 다른 이미지 파일을 선택해 주세요.")
    st.stop()

control_column, _ = st.columns([1, 2])
with control_column:
    effect = st.selectbox("필터", ["흑백", "세피아", "블러"])
    blur_radius = 4.0
    if effect == "블러":
        blur_radius = st.slider("블러 강도", min_value=0.5, max_value=20.0, value=4.0, step=0.5)

if effect == "흑백":
    result = ImageOps.grayscale(image).convert("RGB")
elif effect == "세피아":
    grayscale = ImageOps.grayscale(image)
    result = ImageOps.colorize(grayscale, black="#35251E", white="#E7C89A")
else:
    result = image.filter(ImageFilter.GaussianBlur(radius=blur_radius))

original_column, result_column = st.columns(2, gap="large")
with original_column:
    st.markdown("**원본**")
    st.image(image, use_container_width=True)
with result_column:
    st.markdown(f"**{effect} 결과**")
    st.image(result, use_container_width=True)

output = BytesIO()
result.save(output, format="PNG")
st.download_button(
    "결과 이미지 다운로드",
    data=output.getvalue(),
    file_name="designer-filter.png",
    mime="image/png",
    icon=":material/download:",
)