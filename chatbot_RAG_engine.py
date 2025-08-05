import os
import pandas as pd
import google.generativeai as genai
import ast
import re
# 🔐 Set your Gemini API key
GOOGLE_API_KEY = ""  # Replace this with your key
genai.configure(api_key=GOOGLE_API_KEY)

# 🔧 Load Excel all sheets
def load_all_sheets(file_path: str):
    sheets = pd.read_excel(file_path, sheet_name=None)
    combined = []
    for name, df in sheets.items():
        df_copy = df.copy()
        df_copy['SheetName'] = name
        combined.append(df_copy)
    return pd.concat(combined, ignore_index=True)

# 🧠 Gemini Prompt Builder
def build_prompt(df: pd.DataFrame, user_question: str) -> str:
    schema = "\n".join(f"- {col}: {dtype}" for col, dtype in df.dtypes.items())
    prompt = f"""
You are a data analyst. The user has a pandas DataFrame with the following columns and dtypes:

{schema}

The user wants to: "{user_question}"

Write ONLY the Python code using pandas to perform this task.
Assume the DataFrame is named `df`. Do not write explanations. Just give raw code. And assign the code to a 'result' variable.
    """
    return prompt.strip()

def ensure_result_assignment(code: str) -> str:
    try:
        code = textwrap.dedent(code)
        lines = code.strip().split('\n')
        last_line = lines[-1].strip()

        # If last line is print(...)
        if last_line.startswith("print(") and last_line.endswith(")"):
            inner = re.match(r"print\((.*)\)", last_line).group(1)
            lines[-1] = f"result = {inner}"
            return '\n'.join(lines)

        # If last line is a bare expression, wrap it
        parsed = ast.parse(code)
        if isinstance(parsed.body[-1], ast.Expr):
            lines[-1] = f"result = {lines[-1]}"
            return '\n'.join(lines)

    except Exception as e:
        print("Wrapping error:", e)

    return code


# ✅ Get code from Gemini and wrap if needed
def get_pandas_code_from_gemini(prompt: str) -> str:
    model = genai.GenerativeModel("gemini-2.5-pro")
    response = model.generate_content(prompt)
    raw_code = response.text.strip().strip("```python").strip("```")
    return ensure_result_assignment(raw_code)

# ✅ Safely run code and return `result`
def run_code(df: pd.DataFrame, code: str):
    local_vars = {"df": df}
    try:
        exec(code, {}, local_vars)
        if "result" in local_vars:
            return local_vars["result"]
        else:
            return "✅ Code executed, but no 'result' variable found.\nTip: End your code with `result = ...`"
    except Exception as e:
        return f"❌ Error while executing code:\n{e}\n\n🔍 Code that caused the error:\n{code}"
    # 🧭 Main driver
def main():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(BASE_DIR, "data", "client_abc.xlsx")
    df = load_all_sheets(file_path)

    user_question = "?"

    prompt = build_prompt(df, user_question)
    print("\n🧠 Prompt sent to Gemini:\n", prompt)

    generated_code = get_pandas_code_from_gemini(prompt)
    print("\n📜 Code generated:\n", generated_code)

    result = run_code(df, generated_code)
    print("\n✅ Result:\n", result)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print("🔥 Exception occurred:", e)

