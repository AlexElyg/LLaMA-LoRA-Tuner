import os
import sys

import fire
import gradio as gr

from llama_lora.globals import Global
from llama_lora.ui.main_page import main_page, get_page_title, main_page_custom_css
from llama_lora.utils.data import init_data_dir


def main():
    data_dir = os.path.abspath("./data")
    Global.default_base_model_name = Global.base_model_name = "decapoda-research/llama-7b-hf"
    Global.base_model_choices = ["decapoda-research/llama-7b-hf", "nomic-ai/gpt4all-j"]
    Global.data_dir = data_dir
    Global.load_8bit = False

    Global.ui_dev_mode = True
    Global.ui_dev_mode_title_prefix = ""
    Global.ui_show_sys_info = False

    Global.ui_subtitle = "This is a UI demo of <a href=\"https://github.com/zetavg/LLaMA-LoRA\" target=\"_blank\">LLaMA-LoRA</a>, toolkit for evaluating and fine-tuning LLaMA models. Run the actual one: <a href=\"https://colab.research.google.com/github/zetavg/LLaMA-LoRA/blob/main/LLaMA_LoRA.ipynb\" target=\"_parent\"><img style=\"display: inline;\" src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"

    os.makedirs(data_dir, exist_ok=True)
    init_data_dir()

    with gr.Blocks(title=get_page_title(), css=main_page_custom_css()) as demo:
        main_page()

    demo.queue().launch()


if __name__ == "__main__":
    fire.Fire(main)