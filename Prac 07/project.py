"""
Prac 07
Do-from-scratch Exercises
Project Management Program
"""


class Project:
    def __int__(self, name="", start_date=0, priority=0, cost_estimate=0, completion_percentage=0):
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __str__(self):
        return f"Name{self.name}, Start{self.start_date.strftime("%d/%m/%Y")}, Priority {self.priority}, Estimate: ${self.cost_estimate}, " \
               f"completion: {self.completion_percentage}% "

    def __repr__(self):
        return f"{self.name}\t{self.start_date.strftime("%d/%m/%Y")}\t{self.priority}\t{self.cost_estimate}\t{self.completion_percentage}"
