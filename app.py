from flask import Flask, render_template, request, jsonify, redirect, url_for
from txt2txt import poem_describer, poem_creator
from text2img import ArtGen
import os

app = Flask(__name__)
art_generator = ArtGen()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/transform', methods=['POST'])
def transform():
    try:
        # Debug: Print all form data
        print("=== Form Data Received ===")
        print(request.form)
        print("=== Raw Data ===")
        print(request.get_data())
        print("=== Headers ===")
        print(request.headers)
        
        # Get input data
        folk_song = request.form.get('folkSongInput')
        art_style = request.form.get('artworkType')
        
        print(f"Folk Song: {folk_song}")
        print(f"Art Style: {art_style}")
        
        if not folk_song:
            print("Error: No folk song provided")
            return "Error: Please enter a folk song", 400
            
        if not art_style:
            print("Error: No art style selected")
            return "Error: Please select an art style", 400

        # Generate description
        try:
            description = poem_describer(folk_song)
            print(f"Description generated: {description[:100]}...")
        except Exception as e:
            print(f"Error in poem_describer: {str(e)}")
            return f"Error generating description: {str(e)}", 500

        # Generate poem
        try:
            modern_poem = poem_creator(description)
            print(f"Poem generated: {modern_poem[:100]}...")
        except Exception as e:
            print(f"Error in poem_creator: {str(e)}")
            return f"Error generating poem: {str(e)}", 500

        # Generate art
        try:
            image_filename = art_generator.gen_images(description, art_style)
            print(f"Art generated: {image_filename}")
        except Exception as e:
            print(f"Error in art_generator: {str(e)}")
            return f"Error generating art: {str(e)}", 500

        # Prepare result
        result = {
            'description': description,
            'modern_poem': modern_poem,
            'image_path': f'/static/generated/{image_filename}'
        }
        
        return render_template('output.html', result=result)
        
    except Exception as e:
        print(f"General error: {str(e)}")
        return f"An error occurred: {str(e)}", 500

if __name__ == '__main__':
    os.makedirs('static/generated', exist_ok=True)
    app.run(debug=True, port=5000)
