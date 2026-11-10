def greet(name: str) -> str:
    cleaned_name = name.strip()
    return f"Hello, {cleaned_name}!" if cleaned_name else "Hello, friend!"
