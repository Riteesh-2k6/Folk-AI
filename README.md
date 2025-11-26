# FOLKAI - Folk Song to Modern Art Transformer

FOLKAI is an innovative web application that transforms traditional folk songs into modern interpretations through AI-powered text and image generation. The project combines multiple AI technologies to create a unique artistic experience.

## Features

- **Folk Song Analysis**: Converts traditional folk songs into descriptive text
- **Modern Poem Generation**: Transforms folk song descriptions into contemporary poetry
- **AI Art Generation**: Creates visual artwork based on the folk song's themes
- **Multiple Art Styles**: Supports various artistic styles for image generation

## Project Structure

```
FOLKAI/
├── app.py              # Main Flask application
├── text2img.py         # Image generation module
├── txt2txt.py          # Text processing and generation module
├── folk_styles_config.py # Configuration for art styles
├── requirements.txt    # Project dependencies
├── static/            
│   ├── style.css      # CSS styling
│   └── script.js      # Frontend JavaScript
└── templates/         
    ├── index.html     # Main page template
    └── output.html    # Results page template
```

## Technologies Used

### AI Tools and Models
- **ChatGPT**: Used for text analysis and modern poem generation
- **Claude AI**: Additional text processing and analysis
- **V0 AI**: Image generation capabilities
- **Windsurf/Codeium**: Development environment and code assistance

### Web Framework
- **Flask**: Python web framework for backend development
- **HTML/CSS/JavaScript**: Frontend development

## Module Integration Challenges and Solutions

### Known Integration Issues:
1. **API Rate Limiting**: Some AI services have request limits that need to be managed
2. **Response Time Coordination**: Handling asynchronous responses from multiple AI services
3. **Memory Management**: Efficient handling of large image generation tasks

### Solutions Implemented:
1. **Request Queuing**: Implementation of request management system
2. **Error Handling**: Robust error handling for API failures
3. **Caching**: Local storage of generated content to reduce API calls

## Setup and Installation

1. Install required dependencies:
```bash
pip install -r requirements.txt
```

2. Configure API keys for various AI services (required):
   - OpenAI API key for ChatGPT
   - Claude AI API key
   - V0 AI API key

3. Run the application:
```bash
python app.py
```

4. Access the application at `http://localhost:5000`

## Usage

1. Enter a folk song text in the input field
2. Select desired art style from the available options
3. Submit and wait for the AI to process:
   - Generate descriptive text
   - Create modern poem
   - Generate artwork
4. View the combined results on the output page

## Future Improvements

- Implementation of user accounts and history
- Additional art style options
- Performance optimizations
- Mobile responsiveness improvements
- Batch processing capabilities

## Contributing

Feel free to submit issues and enhancement requests.

## License

[Add your chosen license here]

## Acknowledgments

- OpenAI team for ChatGPT
- Anthropic for Claude AI
- V0 AI team
- Codeium team for development tools
"# Folk-AI" 
