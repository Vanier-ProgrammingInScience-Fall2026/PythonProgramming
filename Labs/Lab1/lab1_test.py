import subprocess
import sys


def run_program(user_input):
    result = subprocess.run(
        [sys.executable, "lab1.py"],
        input=user_input,
        text=True,
        capture_output=True,
        timeout=5
    )

    return result.stdout


def test_task_1_hello_world():
    output = run_program("Alice\n25\n1.75\n")

    assert "Hello, World!" in output


def test_task_2_input_output():
    output = run_program("Alice\n25\n1.75\n")

    assert "Hello, Alice!" in output
    assert "You are 25 years old." in output
    assert "Your height is 1.75 meters." in output
