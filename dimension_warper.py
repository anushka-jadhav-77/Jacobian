import streamlit as st
import sympy as sp

# ==========================================
# PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="Jacobian Calculator",
    page_icon="🤓",
    layout="centered"
)

# ==========================================
# BACKGROUND + STYLING
# ==========================================

st.markdown(
    """
    <style>

    /* MAIN BACKGROUND */

    .stApp {
        background: linear-gradient(
            135deg,
            #020617,
            #0F172A,
            #1E3A8A,
            #312E81
        );

        color: white;
    }

    /* FLOATING MATH SYMBOLS */

    .math-bg {

        position: fixed;

        top: 0;

        left: 0;

        width: 100%;

        height: 100%;

        opacity: 0.05;

        font-size: 48px;

        color: #38BDF8;

        z-index: -1;

        overflow: hidden;

        line-height: 2.5;

        padding: 30px;

        font-weight: bold;

        transform: rotate(-15deg);
    }

    /* TITLE */

    h1 {

        text-align: center;

        color: #7DD3FC;

        font-size: 55px;

        text-shadow:
            0 0 10px #38BDF8,
            0 0 20px #2563EB,
            0 0 40px #1D4ED8;
    }

    /* GLASSMORPHISM INPUTS */

    .stTextInput input,
    .stTextArea textarea {

        background: rgba(255,255,255,0.08) !important;

        border: 1px solid rgba(255,255,255,0.2) !important;

        backdrop-filter: blur(10px);

        color: white !important;

        border-radius: 15px !important;

        padding: 10px !important;
    }

    /* BUTTON */

    .stButton>button {

        background: linear-gradient(
            90deg,
            #2563EB,
            #7C3AED
        );

        color: white;

        border: none;

        border-radius: 15px;

        font-size: 18px;

        padding: 12px 25px;

        transition: 0.3s;
    }

    .stButton>button:hover {

        transform: scale(1.05);

        box-shadow:
            0 0 15px #2563EB,
            0 0 25px #7C3AED;
    }

    </style>

    <!-- FLOATING SYMBOLS -->

    <div class="math-bg">

    ∫ ∑ π ∂ √ ∇ θ λ μ α β γ Δ
    <br><br>

    x² + y² = r²
    <br><br>

    det(J)
    <br><br>

    ∂u/∂x
    <br><br>

    ∂v/∂y
    <br><br>

    sinθ cosθ
    <br><br>

    ∫∫ f(x,y) dxdy
    <br><br>

    J = ∂(u,v)/∂(x,y)
    <br><br>

    Σ Δ λ θ π
    <br><br>

    ∇f(x,y)

    </div>

    """,
    unsafe_allow_html=True
)

# ==========================================
# SIDEBAR
# ==========================================

st.sidebar.title("💻 Navigation")

st.sidebar.write("📐 Jacobian Calculator")

st.sidebar.write("🧠 Mathematics Learning Tool")

st.sidebar.write("🚀 Python + Streamlit Project")

# ==========================================
# TITLE
# ==========================================

st.markdown(
    "<h1>💻🤓 Jacobian Calculator</h1>",
    unsafe_allow_html=True
)

st.write("✨ Solve Jacobian Problems Easily")

st.divider()

# ==========================================
# INPUTS
# ==========================================

vars_input = st.text_input(
    "📌 Enter Variables (Example: x,y)"
)

functions_input = st.text_area(
    "✏️ Enter Functions (One Per Line)"
)

user_answer = st.text_input(
    "📝 Enter Your Determinant Answer"
)

# ==========================================
# CALCULATE BUTTON
# ==========================================

if st.button("🚀 Calculate Jacobian"):

    with st.spinner("⏳ Calculating Jacobian..."):

        try:

            # VARIABLES
            var_names = [
                v.strip()
                for v in vars_input.split(",")
                if v.strip() != ""
            ]

            vars = sp.symbols(var_names)

            # FUNCTIONS
            function_lines = [
                f.strip()
                for f in functions_input.split("\n")
                if f.strip() != ""
            ]

            functions = []

            for f in function_lines:

                f = f.replace("^", "**")

                functions.append(sp.sympify(f))

            # MATRICES
            F = sp.Matrix(functions)

            V = sp.Matrix(vars)

            # JACOBIAN MATRIX
            J = F.jacobian(V)

            st.subheader("📐 Jacobian Matrix")

            st.latex(sp.latex(J))

            # DETERMINANT
            if J.shape[0] == J.shape[1]:

                det = sp.simplify(J.det())

                st.subheader("✨ Determinant")

                st.latex(sp.latex(det))

                # MATRIX SIZE
                st.metric(
                    label="📏 Matrix Size",
                    value=f"{J.shape[0]} x {J.shape[1]}"
                )

                # ANSWER CHECKING
                if user_answer.strip() != "":

                    try:

                        user_answer = user_answer.replace("^", "**")

                        user_expr = sp.sympify(user_answer)

                        # CORRECT ANSWER
                        if sp.simplify(user_expr - det) == 0:

                            st.success("😄 Correct Answer!")

                            st.markdown(
                                """
                                <div style='text-align:center;
                                            font-size:40px;
                                            color:#7DD3FC;'>
                                    👍 🤓 Excellent Work!
                                </div>
                                """,
                                unsafe_allow_html=True
                            )

                        # WRONG ANSWER
                        else:

                            st.error(
                                "😢 Incorrect Answer! Try Again."
                            )

                            with st.expander(
                                "💡 Do You Want Hint?"
                            ):

                                st.subheader(
                                    "📘 Step-by-Step Explanation"
                                )

                                st.write(
                                    "### Step 1️⃣ : Find Partial Derivatives"
                                )

                                st.write(
                                    "Differentiate every function "
                                    "with respect to each variable."
                                )

                                st.write(
                                    "### Step 2️⃣ : Form Jacobian Matrix"
                                )

                                st.latex(sp.latex(J))

                                st.write(
                                    "### Step 3️⃣ : Compute Determinant"
                                )

                                st.write(
                                    "Take determinant of the Jacobian Matrix."
                                )

                                st.write(
                                    "### ✅ Final Answer"
                                )

                                st.latex(sp.latex(det))

                                st.success(
                                    "✨ Complete Solution Displayed Above"
                                )

                    except Exception as e:

                        st.error(
                            f"⚠️ Invalid Answer Expression: {e}"
                        )

            else:

                st.error(
                    "❌ Determinant Not Defined "
                    "(Jacobian Matrix is not square)"
                )

        except Exception as e:

            st.error(f"⚠️ Error: {e}")

# ==========================================
# SAMPLE QUESTIONS
# ==========================================

st.divider()

with st.expander("📚 Sample Questions"):

    st.code(
        """Variables:
r,theta

Functions:
r*cos(theta)
r*sin(theta)

Answer:
r"""
    )

    st.code(
        """Variables:
x,y

Functions:
x+y
x-y

Answer:
-2"""
    )

    st.code(
        """Variables:
x,y

Functions:
x + (y^2/x)
y^2/x

Answer:
2*y/x"""
    )

# ==========================================
# FOOTER
# ==========================================

st.markdown(
    """
    <hr>
    <center>
    💻 Developed using Python + Streamlit
    </center>
    """,
    unsafe_allow_html=True
)