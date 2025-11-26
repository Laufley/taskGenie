# Task Genie

Task Genie is a smart command-line task manager that helps you organize, track, and break down your tasks using AI. It supports both simple and complex tasks, leveraging OpenAI to decompose complex tasks into actionable subtasks.

## Features
- Add simple tasks
- Add complex tasks (decomposed into subtasks using AI)
- List all tasks
- Mark tasks as completed
- Delete tasks
- Persistent storage in `tasks.json`

## How It Works
- The main entry point is `main.py`, which provides a menu-driven CLI.
- Tasks are managed by the `TaskManager` class in `task_manager.py`.
- For complex tasks, the app uses OpenAI (via `ai_service.py`) to break down descriptions into subtasks.

## Installation
1. Clone the repository:
	```bash
	git clone <repo-url>
	cd taskGenie
	```
2. Install dependencies:
	```bash
	pip install -r requirements.txt
	```
3. Set up your OpenAI API key:
	- Create a `.env` file in the project root:
	  ```env
	  OPENAI_API_KEY=your_openai_api_key_here
	  ```

## Usage
Run the application:
```bash
python main.py
```
Follow the menu prompts to add, list, complete, or delete tasks.

## Dependencies
Main dependencies (see `requirements.txt`):
- openai
- python-dotenv
- tqdm

## Testing
Unit tests are provided in `test_task_manager.py`.
Run tests with:
```bash
python -m unittest test_task_manager.py
```

## File Structure
- `main.py` — CLI entry point
- `task_manager.py` — Task and TaskManager classes
- `ai_service.py` — AI-powered task decomposition
- `tasks.json` — Persistent task storage
- `test_task_manager.py` — Unit tests
- `requirements.txt` — Python dependencies

## License
See `LICENSE` for details.
