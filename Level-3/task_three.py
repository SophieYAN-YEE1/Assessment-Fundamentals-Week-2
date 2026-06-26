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


class Question:

    def __init__(self, question: str, chosen_answer: str, correct_answer: str):
        self.question = question
        self.chosen_answer = chosen_answer
        self.correct_answer = correct_answer

    def check(self) -> bool:
        return self.chosen_answer == self.correct_answer


class Quiz:

    def __init__(self, questions: list, name: str, type: str):
        self.questions = questions
        self.name = name
        self.type = type


class Marking:

    def __init__(self, quiz: Quiz) -> None:
        self._quiz = quiz

    def mark(self) -> int:
        """Return the total score for the assessment as a percentage"""
        if len(self._quiz.questions) == 0:
            return 0
        score = 0
        for question in self._quiz.questions:
            if question.check():
                score += 1
        return int((score / len(self._quiz.questions)) * 100)

    def generate_assessment(self) -> Assessment:
        """Returns an instance of an `Assessment` of the correct subclass with the correct name and score"""
        name = self._quiz.name
        score = self.mark()
        if self._quiz.type == "multiple-choice":
            return MultipleChoiceAssessment(name, score)
        elif self._quiz.type == "technical":
            return TechnicalAssessment(name, score)
        else:
            return PresentationAssessment(name, score)


if __name__ == "__main__":
    # Example questions and quiz
    questions = [
        Question("What is 1 + 1? A:2 B:4 C:5 D:8", "A", "A"),
        Question("What is 2 + 2? A:2 B:4 C:5 D:8", "B", "B"),
        Question("What is 3 + 3? A:2 B:4 C:6 D:8", "C", "C"),
        Question("What is 4 + 4? A:2 B:4 C:5 D:8", "D", "D"),
        Question("What is 5 + 5? A:10 B:4 C:5 D:8", "A", "A"),
    ]
    quiz = Quiz(questions, "Maths Quiz", "multiple-choice")

    # Add an implementation for the Marking class below to test your code
