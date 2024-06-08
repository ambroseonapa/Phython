
class UniversityAdmission:
    def __init__(self):
        self.name = ""
        self.age = 0
        self.high_school_results = 0
        self.course_choice = ""

    def get_user_input(self):
        self.name = input("Enter your name: ")
        self.age = int(input("Enter your age: "))

    def check_eligibility(self):
        if self.age < 18:
            print("Sorry, you must be at least 18 years old to apply.")
            return False
        return True

    def apply_to_university(self):
        if self.course_choice.lower() == "engineering":
            cutoff = 50
        elif self.course_choice.lower() == "medicine":
            cutoff = 54
        elif self.course_choice.lower() == "business":
            cutoff = 40
        else:
            print("Invalid course choice. Please choose from Engineering, Medicine, or Business.")
            return False

        if self.high_school_results >= cutoff:
            print(f"Congratulations, {self.name}! You are admitted to {self.course_choice}.")
            return True
        else:
            print(f"Sorry, {self.name}, your results do not meet the cutoff for {self.course_choice}.")
            return False

if __name__ == "__main__":
    admission = UniversityAdmission()
    admission.get_user_input()

    if admission.check_eligibility():
        admission.high_school_results = float(input("Enter your high school results: "))
        admission.course_choice = input("Choose a course (Engineering, Medicine, Business): ")
        admission.apply_to_university()
