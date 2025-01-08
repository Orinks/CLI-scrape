# Docs Scraper

A Python-based web scraping tool that converts web content to markdown format using the Firecrawl API.

## Features
- Converts web pages to clean markdown format
- Supports JavaScript rendering for dynamic content
- Configurable wait times for dynamic content loading
- Custom HTTP headers support
- Interactive or command-line output file selection
- Error handling for failed scrapes and file operations

## Requirements
- Python 3.6 or higher
- Firecrawl API key (sign up at firecrawl.dev)
- Required Python packages (installed via requirements.txt):
  - python-dotenv
  - firecrawl
  - requests

## Setup

1. Clone this repository
2. Create a `.env` file in the root directory with your Firecrawl API key:
   ```
   FIRECRAWL_API_KEY=your_api_key_here
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the script with a URL:
```bash
python main.py <url>
```

Optional arguments:
- `--wait <seconds>`: Time to wait for dynamic content
- `--js`: Enable JavaScript rendering
- `--headers "key1:value1,key2:value2"`: Custom headers
- `--output <file>`: Output markdown file path (if not provided, will prompt)

Examples:
```bash
# Basic usage with output prompt
python main.py https://example.com

# Enable JavaScript rendering and specify output file
python main.py https://example.com --js --output result.md

# Wait for dynamic content and add custom headers
python main.py https://example.com --wait 5 --headers "User-Agent:Mozilla/5.0"
```

## Error Handling
The script handles various error scenarios:
- Invalid URLs or connection errors
- Missing API key
- Invalid header format
- File write permission issues
- Failed JavaScript rendering

## Output
The script generates a markdown (.md) file containing:
- Converted web content in markdown format
- Preserved heading structure
- Formatted links and images
- Tables and lists (if present in source)

## Contributing
1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License
This project is open source and available under the MIT License.