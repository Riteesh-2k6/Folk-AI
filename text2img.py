from huggingface_hub import InferenceClient
from PIL import Image, ImageDraw, ImageFont
from folk_styles_config import FOLK_STYLES
import os
import time

client = InferenceClient(token = "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")

class ArtGen:
    def create_prompt(self,text,style):
        style_info = FOLK_STYLES[style]

        prompt = f"""Create  authentic {style} folk background inspired by lyrics:
        "{text}"
        Style: {style_info['description']}
        Required elements: {', '.join(style_info['elements'])}
        Colors: {style_info['color_palette']}
        Compo: {style_info['composition']}
        Reqs:
        - Maintain strict adherence to {style} art tradition
        - Create harmonious compo that reflects the song's emotion
        - Use only specified colors
        - Include symbolic elements that relate to lyrics
        - Ensure image works a background
        """
        return prompt

    def gen_images(self, text, style):
        if style not in FOLK_STYLES:
            raise ValueError(f"Style must be one of: {', '.join(FOLK_STYLES.keys())}")
        
        # Create output directory if it doesn't exist
        output_dir = 'static/generated'
        os.makedirs(output_dir, exist_ok=True)
        
        # Generate image
        prompt = self.create_prompt(text, style)
        image = client.text_to_image(prompt)
        
        # Save image with timestamp
        timestamp = int(time.time())
        filename = f'output_{timestamp}.png'
        output_path = os.path.join(output_dir, filename)
        image.save(output_path)
        
        # Return just the filename
        return filename

def main():
    try:
        generator = ArtGen()
        print("\nAvailable Folk Art Styles:")
        for style, info in FOLK_STYLES.items():
            print(f"\n- {style}:")
            print(f"  Description: {info['description']}")
            print(f"  Elements: {', '.join(info['elements'][:3])}...")

        text = input("\nEnter your folk song lyrics: ")
        style = input("Select a folk art style from the above options: ").lower()

        print("\nGenerating image... Please wait...")
        output_path = generator.gen_images(text, style)
        print(f"Image generated successfully and saved to: {output_path}")
        
    except Exception as e:
        print(f"Error: {str(e)}")
        raise

if __name__ == "__main__":
    main()
