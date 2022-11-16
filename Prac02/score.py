"""
CP1404/CP5632 - Practical
Roderick Mabo Broken Program status
"""

# Should have added another function
def main(score):
    if score < 0:
        print("Invaild Score")
    elif score > 100:
        print("Invaild Score")
    elif score > 90:
        print("Excellent")
    elif score >= 50:
        print("Passable")
    else:
        return "BAD"


main()


# def main():
#     """Get a numeric score and display its status."""
#     score = float(input("Enter score: "))
#     print(determine_status(score))
#
#
# def determine_status(score):
#     """Determine the status of a given score."""
#     if score < 0 or score > 100:
#         return "Invalid score"
#     elif score >= 90:
#         return "Excellent"
#     elif score >= 50:
#         return "Passable"
#     else:
#         return "Bad"
#
#
# main()