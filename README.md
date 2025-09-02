# AI-Powered Web Scraper

A simple yet powerful Python application that scrapes website content and uses OpenAI's GPT-4o-mini to generate intelligent summaries in markdown format.

## 🚀 Features

- **Web Scraping**: Extracts clean content from websites using BeautifulSoup
- **AI Analysis**: Leverages OpenAI's GPT-4o-mini model for intelligent content summarization
- **Content Cleaning**: Automatically removes navigation, scripts, and other irrelevant elements
- **Markdown Output**: Generates well-formatted markdown summaries
- **Environment Configuration**: Secure API key management using environment variables

## 🛠️ Technologies Used

- **Python 3.11+**
- **BeautifulSoup4** - Web scraping and HTML parsing
- **OpenAI API** - AI-powered content analysis
- **Requests** - HTTP requests for web scraping
- **python-dotenv** - Environment variable management

## 📦 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Kshitiz-Lall/ai0.git
   cd ai0
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv .venv
   # On Windows
   .venv\Scripts\activate
   # On macOS/Linux
   source .venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   Create a `.env` file in the project root:
   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   ```

## 🎯 Usage

1. **Configure the target website**
   Edit the `url` variable in `app.py`:
   ```python
   url = "https://your-target-website.com"
   ```

2. **Run the application**
   ```bash
   python app.py
   ```

3. **View the AI-generated summary**
   The application will output a markdown-formatted summary of the website content.

## 📁 Project Structure

```
ai0/
├── app.py              # Main application script
├── requirements.txt    # Python dependencies
├── .env               # Environment variables (not tracked)
├── .gitignore         # Git ignore rules
├── pyproject.toml     # Project configuration
└── README.md          # Project documentation
```

## 🔧 Configuration

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `OPENAI_API_KEY` | Your OpenAI API key | Yes |

### Website Class

The `Website` class handles content extraction:
- Fetches HTML content
- Extracts page title
- Removes navigation and irrelevant elements
- Converts to clean text format

### AI Prompts

- **System Prompt**: Instructs the AI to analyze and summarize website content
- **User Prompt**: Provides website content and requests markdown summary

## 🎨 Example Output

```markdown
# Summary of Example Website

This website provides information about...

## Key Features
- Feature 1
- Feature 2
- Feature 3

## Recent News
- Announcement 1 (Date)
- Announcement 2 (Date)
```

## 🔒 Security

- API keys are stored securely in environment variables
- The `.env` file is excluded from version control
- Web scraping includes proper User-Agent headers

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🙏 Acknowledgments

- OpenAI for the GPT-4o-mini API
- BeautifulSoup4 for web scraping capabilities
- The Python community for excellent libraries

## 📧 Contact

**Kshitiz Lall**
- GitHub: [@Kshitiz-Lall](https://github.com/Kshitiz-Lall)
- Repository: [ai0](https://github.com/Kshitiz-Lall/ai0)

---

*Built with ❤️ and AI*