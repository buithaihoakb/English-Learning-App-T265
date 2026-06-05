# English Learning App T265

A comprehensive desktop application for learning English with interactive features and progress tracking.

## Features

- **Vocabulary Learning**: Learn and practice English vocabulary with flashcards
- **Listening Practice**: Improve listening skills with audio exercises
- **Speaking Practice**: Practice pronunciation with speech recognition
- **Reading Comprehension**: Read and understand English texts
- **Quiz & Assessment**: Take tests to evaluate your knowledge
- **Progress Tracking**: Monitor your learning progress over time
- **B2 Level Content**: All exercises aligned with B2 level standards

## Technologies

- **GUI Framework**: PyQt6
- **Text-to-Speech**: pyttsx3
- **Speech Recognition**: SpeechRecognition
- **Database**: SQLite3
- **Language**: Python 3.8+

## Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Setup

1. Clone the repository:
```bash
git clone https://github.com/buithaihoakb/English-Learning-App-T265.git
cd English-Learning-App-T265
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the application:
```bash
python main.py
```

## Project Structure

```
English-Learning-App-T265/
├── main.py                    # Entry point of the application
├── requirements.txt           # Project dependencies
├── config/
│   └── settings.py           # Configuration and settings
├── ui/
│   ├── main_window.py        # Main application window
│   ├── styles.py             # UI styling and themes
│   └── dialogs.py            # Custom dialog windows
├── modules/
│   ├── vocabulary.py         # Vocabulary management
│   ├── listening.py          # Listening exercises
│   ├── speaking.py           # Speaking practice
│   ├── reading.py            # Reading comprehension
│   ├── quiz.py               # Quiz and testing
│   └── progress.py           # Progress tracking
├── database/
│   ├── db_manager.py         # Database operations
│   └── schema.sql            # Database schema
├── data/
│   ├── vocabulary.json       # Vocabulary data
│   └── exercises.json        # Exercise data
└── assets/
    ├── icons/                # Application icons
    └── sounds/               # Audio files
```

## Usage

1. Launch the application
2. Create or login to your account
3. Choose a learning module (Vocabulary, Listening, Speaking, Reading, or Quiz)
4. Complete exercises and track your progress
5. View your performance statistics

## Learning Levels

- **A1-A2**: Beginner
- **B1**: Intermediate
- **B2**: Upper Intermediate (Current Focus)
- **C1-C2**: Advanced (Future Updates)

## Contributing

Feel free to submit pull requests and issues to improve the application.

## License

MIT License

## Author

Bùi Thái Hoà

## Contact

For questions or suggestions, please create an issue in the repository.
