import gradio as gr
import os
from typing import Optional
from PIL import Image
from rembg import remove, new_session
from rembg.sessions import sessions_names

# Initialize session storage
sessions = {}

def process_image(
    image: Image.Image,
    model: str = "u2net",
    alpha_matting: bool = False,
    alpha_matting_foreground_threshold: int = 240,
    alpha_matting_background_threshold: int = 10,
    alpha_matting_erode_size: int = 10,
    only_mask: bool = False,
    post_process_mask: bool = False,
) -> Image.Image:
    """Remove background from image"""
    
    # Get or create session
    if model not in sessions:
        print(f"Loading model: {model}")
        sessions[model] = new_session(model)
    
    # Process image
    result = remove(
        image,
        session=sessions[model],
        alpha_matting=alpha_matting,
        alpha_matting_foreground_threshold=alpha_matting_foreground_threshold,
        alpha_matting_background_threshold=alpha_matting_background_threshold,
        alpha_matting_erode_size=alpha_matting_erode_size,
        only_mask=only_mask,
        post_process_mask=post_process_mask,
    )
    
    return result

# Create Gradio interface
with gr.Blocks(title="Background Remover") as demo:
    gr.Markdown("""
    # Background Remover
    Remove backgrounds from images using various AI models.
    """)
    
    with gr.Row():
        with gr.Column():
            input_image = gr.Image(
                label="Input Image",
                type="pil",
                image_mode="RGBA",
            )
            
            model = gr.Dropdown(
                choices=sessions_names,
                value="u2net",
                label="Model",
                info="Choose the model for background removal"
            )
            
            with gr.Accordion("Advanced Options", open=False):
                alpha_matting = gr.Checkbox(
                    label="Enable Alpha Matting",
                    value=False,
                    info="Improves edges but slower"
                )
                
                alpha_matting_foreground_threshold = gr.Slider(
                    minimum=0,
                    maximum=255,
                    value=240,
                    step=1,
                    label="Foreground Threshold",
                    info="Higher values keep more foreground"
                )
                
                alpha_matting_background_threshold = gr.Slider(
                    minimum=0,
                    maximum=255,
                    value=10,
                    step=1,
                    label="Background Threshold",
                    info="Lower values remove more background"
                )
                
                alpha_matting_erode_size = gr.Slider(
                    minimum=0,
                    maximum=40,
                    value=10,
                    step=1,
                    label="Erode Size",
                    info="Shrinks the foreground mask"
                )
                
                only_mask = gr.Checkbox(
                    label="Output Mask Only",
                    value=False,
                    info="Return only the segmentation mask"
                )
                
                post_process_mask = gr.Checkbox(
                    label="Post Process Mask",
                    value=False,
                    info="Clean up the mask"
                )
            
            process_btn = gr.Button("Remove Background", variant="primary")
        
        with gr.Column():
            output_image = gr.Image(
                label="Output",
                type="pil",
                image_mode="RGBA",
            )
    
    process_btn.click(
        fn=process_image,
        inputs=[
            input_image,
            model,
            alpha_matting,
            alpha_matting_foreground_threshold,
            alpha_matting_background_threshold,
            alpha_matting_erode_size,
            only_mask,
            post_process_mask,
        ],
        outputs=output_image,
    )
    
    gr.Examples(
        examples=[
            ["examples/girl-1.jpg", "u2net", False, 240, 10, 10, False, False],
            ["examples/animal-1.jpg", "u2net", False, 240, 10, 10, False, False],
            ["examples/car-1.jpg", "u2net", False, 240, 10, 10, False, False],
        ],
        inputs=[
            input_image,
            model,
            alpha_matting,
            alpha_matting_foreground_threshold,
            alpha_matting_background_threshold,
            alpha_matting_erode_size,
            only_mask,
            post_process_mask,
        ],
    )

if __name__ == "__main__":
    demo.launch(
        server_name="0.0.0.0",
        server_port=7860,
        share=False,
    )