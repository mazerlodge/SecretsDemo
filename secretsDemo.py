import sys
import os
from dotenv import load_dotenv
from pathlib import Path

def main():
	# Validate arguments
	if len(sys.argv) != 2:
		print("Usage: python app.py <word>")
		sys.exit(1)

	# Get secret word from command line
	input_word = sys.argv[1]

	# Read secrets file
	env_path = Path(__file__).parent / "secrets.env"
	if env_path.exists():
		load_dotenv(dotenv_path=env_path)
		print(f"Loaded env variables from {env_path}")
	else:
		print(f"WARNING: {env_path} not found.")
	secret_word = os.getenv("SECRET_WORD")

	# Evaluate the secret word provided
	if secret_word is None:
		print("Error: SECRET_WORD not found in .env file")
		sys.exit(1)

	if input_word == secret_word:
		print("Matched")
	else:
		print("No match")

# The entrypoint
if __name__ == "__main__":
	main()
