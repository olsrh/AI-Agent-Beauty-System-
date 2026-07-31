import streamlit as st

# 페이지 기본 설정
st.set_page_config(
    page_title="BeautyLens",
    page_icon="✨",
    layout="centered",
)

# 제목 영역
st.title("BeautyLens")
st.caption(
    "AI Agent가 필요한 리뷰 분석 정보를 구매해 "
    "뷰티 제품 구매 결정을 돕는 서비스"
)

st.divider()

# 입력 폼
with st.form("beauty_request_form"):
    st.subheader("제품 추천 조건")

    user_request = st.text_area(
        "어떤 제품을 찾고 있나요?",
        placeholder=(
            "예: 민감성 피부에 자극이 적고 "
            "2만 원 이하인 제모크림을 추천해줘."
        ),
        height=110,
    )

    col1, col2 = st.columns(2)

    with col1:
        product_category = st.selectbox(
            "제품 종류",
            ["제모크림", "스킨케어", "헤어케어"],
            index=0,
        )

        skin_type = st.selectbox(
            "피부 타입",
            ["민감성", "건성", "지성", "복합성", "잘 모르겠음"],
            index=0,
        )

    with col2:
        product_budget = st.number_input(
            "제품 구매 예산(원)",
            min_value=0,
            max_value=1_000_000,
            value=20_000,
            step=1_000,
        )

        information_budget = st.number_input(
            "정보 구매 한도(SOL)",
            min_value=0.0,
            max_value=1.0,
            value=0.01,
            step=0.001,
            format="%.3f",
        )

    priorities = st.multiselect(
        "중요하게 보는 기준",
        [
            "낮은 자극",
            "제모 효과",
            "냄새",
            "사용 편의성",
            "가격",
            "성분",
        ],
        default=["낮은 자극", "제모 효과"],
    )

    submitted = st.form_submit_button(
        "제품 추천받기",
        use_container_width=True,
    )

# 제출 결과
if submitted:
    if not user_request.strip():
        st.warning("원하는 제품 조건을 문장으로 입력해 주세요.")
    else:
        st.success("입력 조건이 저장되었습니다.")

        st.subheader("입력한 조건")
        st.write(f"**요청:** {user_request}")
        st.write(f"**제품 종류:** {product_category}")
        st.write(f"**피부 타입:** {skin_type}")
        st.write(f"**제품 구매 예산:** {product_budget:,}원")
        st.write(f"**정보 구매 한도:** {information_budget:.3f} SOL")
        st.write(
            f"**중요 기준:** "
            f"{', '.join(priorities) if priorities else '선택하지 않음'}"
        )

        st.info(
            "다음 단계에서는 이 조건을 바탕으로 "
            "무료 제품 정보를 검색하고, 추가 리뷰 정보가 필요한지 판단합니다."
        )
