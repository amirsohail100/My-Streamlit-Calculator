# import streamlit as st

# पेज की सेटिंग और टाइटल
# st.set_page_config(page_title="Streamlit Calculator", page_icon="🔢")
# st.title("🔢 Modern Calculator")

# # कैलकुलेटर की स्टेट (State) को बनाए रखने के लिए session_state का उपयोग
# if 'expression' not in st.session_state:
#     st.session_state.expression = ""

# # डिस्प्ले स्क्रीन (जहाँ नंबर दिखेंगे)
# st.text_input("Display", value=st.session_state.expression, key="display", disabled=True)

# # बटन दबाने पर क्या होगा
# def click_button(label):
#     if label == "=":
#         try:
#             # eval() से गणितीय गणना करना
#             st.session_state.expression = str(eval(st.session_state.expression))
#         except:
#             st.session_state.expression = "Error"
#     elif label == "C":
#         st.session_state.expression = ""
#     else:
#         st.session_state.expression += str(label)

# # UI बटन का लेआउट (4 Columns)
# buttons = [
#     ['7', '8', '9', '/'],
#     ['4', '5', '6', '*'],
#     ['1', '2', '3', '-'],
#     ['C', '0', '=', '+']
# ]

# # ग्रिड बनाना
# for row in buttons:
#     cols = st.columns(4)
#     for i, label in enumerate(row):
#         if cols[i].button(label, use_container_width=True):
#             click_button(label)
#             st.rerun() # स्क्रीन को तुरंत अपडेट करने के लिए

# # कैलकुलेटर का स्टाइल बेहतर बनाने के लिए थोड़ा CSS
# st.markdown("""
# <style>
#     .stButton>button {
#         height: 3em;
#         font-size: 20px;
#         font-weight: bold;
#     }
# </style>
# """, unsafe_allow_html=True)



import streamlit as st


st.set_page_config(page_title="Circular Buttons Calculator", page_icon="🔢")

st.markdown("""
<style>
    /* एनिमेटेड बैकग्राउंड */
    .stApp {
        background: linear-gradient(-45deg, #4158D0, #C850C0, #FFCC70);
        background-size: 400% 400%;
        animation: gradient 10s ease infinite;
    }
    @keyframes gradient {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    /* डिस्प्ले स्क्रीन */
    .stTextInput input {
        background-color: rgba(0, 0, 0, 0.2) !important;
        color: white !important;
        font-size: 45px !important;
        text-align: right !important;
        border: none !important;
        border-radius: 15px !important;
        padding: 15px !important;
        margin-bottom: 20px !important;
    }

    /* सभी बटन्स की डिफ़ॉल्ट स्टाइलिंग */
    .stButton > button {
        /* ऊँचाई और चौड़ाई बराबर रखें ताकि गोल दिखें */
        height: 70px !important; 
        width: 70px !important; 
        border-radius: 50% !important; /* पूरी तरह गोल */
        font-size: 24px !important;
        font-weight: bold !important;
        border: none !important;
        background-color: rgba(255, 255, 255, 0.2) !important;
        color: white !important;
        margin: 5px auto !important; /* सेंटर अलाइनमेंट */
        display: block !important; /* ब्लॉक ताकि मार्जिन काम करे */
    }

    /* ऑपरेटर बटन्स (चौथी कॉलम) */
    div[data-testid="column"]:nth-of-type(4) button {
        background-color: #FF9F0A !important;
    }
    
    /* बटन होवर और एक्टिव इफेक्ट */
    .stButton > button:hover {
        background-color: rgba(255, 255, 255, 0.4) !important;
    }
    .stButton > button:active {
        transform: scale(0.95);
    }
</style>
""", unsafe_allow_html=True)

if 'expression' not in st.session_state:
    st.session_state.expression = "0"
if 'rerun_flag' not in st.session_state:
    st.session_state.rerun_flag = False

def handle_click(label):
    if label == "=":
        try:
            expr = st.session_state.expression.replace('×', '*').replace('÷', '/')
            st.session_state.expression = str(eval(expr))
        except:
            st.session_state.expression = "Error"
    elif label == "AC":
        st.session_state.expression = "0"
    elif label == "Del":
        st.session_state.expression = st.session_state.expression[:-1]
        if st.session_state.expression == "": st.session_state.expression = "0"
    else:
        if st.session_state.expression == "0" or st.session_state.expression == "Error":
            st.session_state.expression = str(label)
        else:
            st.session_state.expression += str(label)
    
    st.session_state.rerun_flag = True


st.title("🔢 Circular Buttons Calculator")


rows = [
    ['AC', 'Del', '%', '÷'],
    ['7', '8', '9', '×'],
    ['4', '5', '6', '-'],
    ['1', '2', '3', '+']
]


st.text_input(label="", value=st.session_state.expression, disabled=True)

for row in rows:
    cols = st.columns(4)
    for i, btn_label in enumerate(row):
        if btn_label != "":
            cols[i].button(btn_label, key=f"btn_{btn_label}", on_click=handle_click, args=(btn_label,))


col1, col2, col3, col4 = st.columns(4) 
col1.button("0", key="btn_0", on_click=handle_click, args=("0",))
col2.button(".", key="btn_.", on_click=handle_click, args=(".",))
col3.button("=", key="btn_=", on_click=handle_click, args=("=",))



if st.session_state.rerun_flag:
    st.session_state.rerun_flag = False
    st.rerun()
