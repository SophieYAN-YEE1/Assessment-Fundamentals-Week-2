from datetime import date


class Trainee:
    """Trainee Class"""

    def __init__(self, name: str, email: str, date_of_birth: date) -> None:
        """Initialising Trainee"""
        self.name = name
        self.email = email
        self.date_of_birth = date_of_birth
        self.assessments = []

    def get_age(self) -> int:
        """Returns the age of the trainee"""
        today = date.today()
        age = today.year - self.date_of_birth.year
        if today.month <= self.date_of_birth.month:
            if today.day < self.date_of_birth.day:
                age -= 1
        return age

    def add_assessment(self, assessment: Assessment) -> None:
        """Adds an Assessment to the trainee's list of assessments"""
        self.assessments.append(assessment)

    def get_assessment(self, name: str) -> Assessment | None:
        """Returns the Assessment object based on the name, returns non if not found"""
        for assessment in self.assessments:
            if assessment.name == name:
                return assessment
        return None


class Assessment:
    """Assessment Class"""

    def __init__(self, name: str, type: str, score: float) -> None:
        """Initialising Assessment"""
        self.name = name
        self.type = type.lower()
        self.score = score

        if self.type not in ["multiple-choice", "technical", "presentation"]:
            raise ValueError("Not a valid assessment type")
        if self.score < 0:
            raise ValueError("Score cannot be below 0")
        if self.score > 100:
            raise ValueError("Score cannot be above 100")


if __name__ == "__main__":
    trainee = Trainee("Sigma", "trainee@sigmalabs.co.uk", date(1990, 1, 1))
    print(trainee)
    print(trainee.get_age())
    trainee.add_assessment(Assessment(
        "Python Basics", "multiple-choice", 90.1))
    trainee.add_assessment(Assessment(
        "Python Data Structures", "technical", 67.4))
    trainee.add_assessment(Assessment("Python OOP", "multiple-choice", 34.3))
    print(trainee.get_assessment("Python Basics"))
    print(trainee.get_assessment("Python Data Structures"))
    print(trainee.get_assessment("Python OOP"))
