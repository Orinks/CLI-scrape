import os
import argparse
from dotenv import load_dotenv
from firecrawl import FirecrawlApp

# Load environment variables
load_dotenv()

# Get API key from environment
api_key = os.getenv('FIRECRAWL_API_KEY')

if not api_key:
	raise ValueError("FIRECRAWL_API_KEY not found in .env file")

# Initialize Firecrawl app
app = FirecrawlApp(api_key=api_key)

def scrape_website(url, wait_time=None, render_js=False, headers=None):
	"""
	Scrape a website and return the markdown content
	
	Args:
		url (str): The website URL to scrape
		wait_time (int, optional): Time to wait for dynamic content in seconds
		render_js (bool): Whether to render JavaScript
		headers (dict, optional): Custom headers for the request
	"""
	try:
		options = {}
		
		if render_js:
			options['javascript'] = True
		
		if headers:
			options['headers'] = headers

		# First get the HTML content
		scrape_result = app.scrape_url(url, **options)
		
		# If wait time is specified, sleep after getting the content
		if wait_time:
			import time
			time.sleep(wait_time)

		return scrape_result['markdown']
	except Exception as e:
		print(f"Error scraping {url}: {str(e)}")
		return None

def parse_headers(headers_str):
	"""Parse headers string into dictionary"""
	if not headers_str:
		return None
	try:
		headers_dict = {}
		for header in headers_str.split(','):
			key, value = header.split(':')
			headers_dict[key.strip()] = value.strip()
		return headers_dict
	except:
		print("Invalid headers format. Using default headers.")
		return None

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description='Scrape websites using Firecrawl API')
	parser.add_argument('url', help='Website URL to scrape')
	parser.add_argument('--wait', type=int, help='Time to wait for dynamic content (seconds)')
	parser.add_argument('--js', action='store_true', help='Enable JavaScript rendering')
	parser.add_argument('--headers', help='Custom headers (format: "key1:value1,key2:value2")')
	parser.add_argument('--output', help='Output markdown file path (if not provided, will prompt)')
	
	args = parser.parse_args()
	
	# Get output file path from args or prompt user
	output_file = args.output
	if not output_file:
		output_file = input("Enter the output markdown file path: ").strip()
	
	headers = parse_headers(args.headers)
	content = scrape_website(args.url, args.wait, args.js, headers)
	
	if content:
		# Write content to the specified file
		try:
			with open(output_file, 'w', encoding='utf-8') as f:
				f.write(content)
			print(f"\nContent from {args.url} has been saved to {output_file}")
		except Exception as e:
			print(f"Error saving to file: {str(e)}")