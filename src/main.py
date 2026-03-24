def print_author():
	from dotenv import load_dotenv 
	import os  
	load_dotenv(dotenv_path='C:/Users/Elena/documents/YandexP/second-project/.env')
	author = os.getenv('AUTHOR')
	return author

author = print_author()
print(f"Автор проекта: {author}")
