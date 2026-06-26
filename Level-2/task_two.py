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
        if not isinstance(assessment, Assessment):
            raise TypeError("Can only add type Assessment to assessment lists")
        else:
            self.assessments.append(assessment)

    def get_assessment(self, name: str) -> Assessment | None:
        """Returns the Assessment object based on the name, returns non if not found"""
        for assessment in self.assessments:
            if assessment.name == name:
                return assessment
        return None

    def get_assessment_of_type(self, type: str) -> list[Assessment]:
        """Returns a list of all the assessments of a given type"""
        assessment_type_list = []
        for assessment in self.assessments:
            if assessment.type == type:
                assessment_type_list.append(assessment)
        return assessment_type_list


class Assessment:
    """Assessment Class"""

    def __init__(self, name: str, score: float, type: str) -> None:
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


class MultipleChoiceAssessment(Assessment):
    """Multiple Choice Assessment Class"""

    def __init__(self, name: str, score: float, type="multiple-choice"):
        super().__init__(name, score, type)
        self.type = "multiple-choice"

    def calculate_score(self):
        """Returns the score after considering the weight of the assessment"""
        return 0.7 * self.score


class TechnicalAssessment(Assessment):
    """Technical Assessment Class"""

    def __init__(self, name: str, score: float, type="technical"):
        super().__init__(name, score, type)
        self.type = "technical"

    def calculate_score(self):
        """Returns the score after considering the weight of the assessment"""
        return self.score


class PresentationAssessment(Assessment):
    """Presentation Assessment Class"""

    def __init__(self, name: str, score: float, type="presentation"):
        super().__init__(name, score, type)
        self.type = "presentation"

    def calculate_score(self):
        """Returns the score after considering the weight of the assessment"""
        return 0.6 * self.score


if __name__ == "__main__":
    trainee = Trainee("Sigma", "trainee@sigmalabs.co.uk", date(1990, 1, 1))
    print(trainee)
    print(trainee.get_age())
    trainee.add_assessment(MultipleChoiceAssessment(
        "Python Basics", 90.1))
    trainee.add_assessment(TechnicalAssessment(
        "Python Data Structures", 67.4))
    trainee.add_assessment(MultipleChoiceAssessment("Python OOP", 34.3))
    print(trainee.get_assessment("Python Basics"))
    print(trainee.get_assessment("Python Data Structures"))
    print(trainee.get_assessment("Python OOP"))
