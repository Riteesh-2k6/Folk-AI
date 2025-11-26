from huggingface_hub import InferenceClient
client = InferenceClient(token = "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")

def poem_creator(description):
    """Generate a new poem based on the description"""
    prompt = f"""Transform this into a short, beautiful poem that captures its essence:
    
    Description: {description}
    
    Create a poem with 2-3 stanzas, each having 4 lines. Use rhyming where appropriate."""
    
    try:
        response = client.text_generation(
            prompt,
            max_new_tokens=500,
            model="mistralai/Mistral-7B-Instruct-v0.1"
        )
        return response
    except Exception as e:
        print(f"Error in poem_creator: {str(e)}")
        raise

def poem_describer(folk_song):
    """Create a descriptive paragraph about the folk song"""
    try:
        prompt = f"""Write me a paragraph of 500 words that accurately describes this folk song's core moral values, its nuances and its plot points:

        Folk Song:
        {folk_song}
        
        Focus on the emotional depth and cultural significance of the song."""

        description = client.text_generation(
            prompt,
            max_new_tokens=500,
        )
        return description
    except Exception as e:
        print(f"Error in poem_describer: {str(e)}")
        raise

def main():
    print("\n=== Folk Song Analysis System ===")
    print("Please enter your folk song lyrics (press Enter twice when done):")
    
    # Collect multiline input from user
    lines = []
    while True:
        line = input()
        if line:
            lines.append(line)
        else:
            break
    
    folk_song = "\n".join(lines)
    
    if not folk_song.strip():
        print("No lyrics entered. Exiting...")
        return
        
    print("\nAnalyzing your folk song...")
    try:
        description = poem_describer(folk_song)
        print("\nAnalysis Result:")
        print(description)
        
        print("\nGenerating a new poem based on the analysis...")
        new_poem = poem_creator(description)
        print("\nInspired Poem:")
        print(new_poem)
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
