import gradio as gr
from databricks.sdk import WorkspaceClient

def get_databricks_info():
    w = WorkspaceClient()
    me = w.current_user.me()
    return f"Display name: {me.display_name}\nEmail: {me.user_name}\nUser ID: {me.id}"

with gr.Blocks(title="Databricks App Test 2.0") as demo:
    gr.Markdown("## Databricks Info 2.0")
    gr.Markdown("Fetches the current user from Databricks via the SDK.")
    btn = gr.Button("Fetch from Databricks")
    output = gr.Textbox(label="Result", lines=4)
    btn.click(get_databricks_info, outputs=output)

if __name__ == "__main__":
    demo.launch()
