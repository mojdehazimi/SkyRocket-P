# hello_world.py

def say_hello(name: str) -> str:
    """
    Returns a personalized greeting.
    
    Args:
        name (str): The name of the person to greet.
        
    Returns:
        str: A greeting message.
    """
    return f"Hello, {name}! Welcome to the SNS Automation Project 🚀"


if __name__ == "__main__":
    user_name = input("Enter your name: ")
    greeting = say_hello(user_name)
    print(greeting)
