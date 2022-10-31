"""
CP1404/CP5632 Practical - Roderick Mabo
Programming Language Program

"""

from Prac_06.programming_language import ProgrammingLanguage


def main():
    ruby = ProgrammingLanguage("Java", "Static", True, 1995)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    programmes = [ruby, python, visual_basic]
    print("The dynamically typed languages are:")
    for language in programmes:
        if language.is_dynamic() is True:
            print(language.name)


main()

