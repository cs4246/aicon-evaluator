import argparse
import json
import dataclasses
import importlib.util
import sys

class TaskNotFound(Exception):
    pass

class SubmissionNotFound(Exception):
    pass


def main() -> None:
    parser = argparse.ArgumentParser("aicon Evaluator")
    parser.add_argument('-o', '--output-path', default=None)
    args = parser.parse_args()

    try:
        task_module = "aicon_task"
        spec = importlib.util.find_spec(task_module)
        task = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(task)
        sys.modules[task_module] = object()
    except ModuleNotFoundError as e:
        raise TaskNotFound(e)
    try:
        import aicon_submission as submission
    except ModuleNotFoundError as e:
        raise SubmissionNotFound(e)

    output = task.evaluate(submission)

    if dataclasses.is_dataclass(output):
        output = dataclasses.asdict(output)

    if args.output_path is not None:
        with open(args.output_path, 'w') as f:
            json.dump(output, f)

    print(json.dumps(output))


if __name__ == "__main__":
    main()
