"""
Program: haiku.py
This program creates a haiku which is a type of short poem that originated in Japan. It has 3 lines.
The first line has 5 syllables, the second has 7 syllables, and the third has 5 syllables again.
"""

from ai import call_gpt

def main():
    name = input("Enter your name: ")
    topic = input("Enter a topic: ")
    print("Creating your haiku...")
    print("")
    response = call_gpt(
    f"Write a haiku having {name} with {topic}. Format it with three lines: 5 syllables, 7 syllables, 5 syllables."
)
    print(response)

if __name__ == "__main__":
    main()