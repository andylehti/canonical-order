import streamlit as st
import time

# Set page configuration for better layout
st.set_page_config(
    page_title="🧮 The Canonical Order",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Preface Content
preface_content = """
# Preface and Paper

Humans judge this prematurely, without understanding the implications. They judge because they assume their information is infallible and that humans could never make a mistake. The standard system remains easily broken when any assortment of the laws is applied correctly. These serious implications can even lead to death. Despite humans trying to patch this error for nearly 40 years, I doubt they will ever fully succeed. A misconception of this scale only arises when valid methods exist to assess it.  

I understand that people want an alternative source, so here is ChatGPT, which, mind you, I have to use because humans are so relunctant actually review this information, and ChatGPT: adamantly opposed this every time I presented it. However, after I established a full paper on the subject, it asserts differently now, but still remains skeptical at the incorporation of the new order, which is why legacy support was built to ensure a smooth and gradual transition:  
[Archived Source 1](http://archive.today/2024.11.14-075346/https://chatgpt.com/share/6735aa81-8d80-8008-b9c2-e65333637796)  

For the implications, see:  
[Archived Source 2](http://archive.today/2024.11.14-174520/https://chatgpt.com/share/67363708-506c-8008-91fd-5d8b53241453)

---

**The Canonical Order of operations** addresses a recurring error commonly made in calculations. This error is significant because incorrect interpretations have been repeatedly overwritten by newer material, amplifying a global error. While these issues persist, I recognize that overhauling the current system is impractical. To address this, this paper introduces a legacy model of the original system, referred to as the Standard Order, which contrasts with the Canonical Order by strictly adhering to the intended index laws.  
[Canonical Order: Index Laws](https://github.com/andylehti/canonical-order/blob/main/index_laws.md)

I believe academics must decide whether to prioritize correctness or maintain traditional systems that perpetuate real-world errors, akin to dogmatic belief structures. This decision ultimately weighs the pursuit of truth against preserving artificially upheld conventions. It is an important lesson that, regardless of how advanced humans become or how much understanding is achieved:

1. **Congruence ≠ Truth:** Logical consistency or alignment does not guarantee truth.  
2. **Well-established ≠ Truth:** Traditions, authority, or widespread acceptance do not inherently equate to truth.  
3. **Lying to Yourself ≠ Truth:** Personal bias or self-deception cannot substitute reality.  
4. **The Truth is Uncomfortable:** This feeling will always persist, and in my paper of Cognitive Impasse, it manifests **as the feeling of impending doom and guilt.**  

I am often misperceived as a beginner or novice because I choose not to follow conventional textbook examples. However, I adhered to the incorrect Standard Order for many years and was recognized as one of the best testers in mathematics in Minnesota. I have also made significant contributions to mathematical research, including developing the **Polyhedral Index Partition** ([10.6084/m9.figshare.27642783](https://doi.org/10.6084/m9.figshare.27642783)), a framework that incorporates negative numbers. While this work has not yet been incorporated into the core mathematical model, I am refining it to explore infinite partitions. My ongoing research aims to extend my discoveries of Pascal Dimensions and Pascal Laterals into negative dimensions—a realm that is inherently challenging for human comprehension.
"""

# Display preface in the sidebar
with st.sidebar.expander("📄 Preface and Paper", expanded=True):
    st.markdown(preface_content, unsafe_allow_html=True)

# Streamlit app title
st.title("🧮 The Canonical Order")

# Helper functions
def normEx(e):
    """Normalize the expression by removing spaces and standardizing exponentiation."""
    return e.replace(' ', '').replace('^', '**')

def nestEx(e):
    """
    Find the innermost parentheses in the expression.
    Returns the start and end indices of the innermost pair.
    """
    s = []
    for i, c in enumerate(e):
        if c == '(':
            s.append(i)
        elif c == ')':
            if s:
                return s.pop(), i
            else:
                return -1, -1
    return -1, -1

def simpEx(e):
    """
    Simplify the expression step-by-step by evaluating innermost parentheses first.
    Returns a list of simplification steps.
    """
    e = normEx(e)
    x = [e]
    while '(' in e:
        a, b = nestEx(e)
        if a == -1 or b == -1:
            return ["Error: Unmatched parentheses."]
        try:
            # Safely evaluate the expression within the parentheses
            r = str(eval(e[a + 1:b]))
        except Exception as ex:
            return [f"Error: {ex}"]
        e = e[:a] + r + e[b + 1:]
        x.append(e)
    try:
        final_result = str(eval(e))
        x.append(f"= {final_result}")
    except Exception as ex:
        x.append(f"Error: {ex}")
    return x

def calcEx(e):
    """Calculate the simplification steps."""
    steps = simpEx(e)
    return steps  # Return steps in forward order

# User input
input_expression = st.text_input(
    "Enter a PEMDAS equation only (without variables | not to be used in production):",
    "(-25)^2 * (-5^2)^2 + (-5^(1/2))^2 - (-5^2)^2 / (-8^(3/5))^(2/3)"
)

# Function to display results step-by-step
def display_steps(results):
    st.subheader("Simplification Steps:")
    step_container = st.container()  # Create a container to hold all steps
    for step in results:
        step_container.code(step)
        time.sleep(0.5)  # Adjust the delay as needed (in seconds)

# Display the simplification steps
if input_expression:
    with st.spinner("Simplifying your expression..."):
        results = calcEx(input_expression)
        display_steps(results)
    st.success("Simplification Complete!")
