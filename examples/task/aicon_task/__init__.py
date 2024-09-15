from dataclasses import dataclass
from typing import Union

@dataclass
class TaskEvaluation:
    point: Union[float,int] # REQUIRED
    correct: bool # add any variables that you want

# REQUIRED
def evaluate(submission) -> TaskEvaluation: # must return a dataclass or json-serializable data
    correct = submission.add(1,2) == 3
    return TaskEvaluation(point=100 if correct else 0, correct=correct)
