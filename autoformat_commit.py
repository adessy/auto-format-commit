#!/usr/bin/env python3

import re
import sys
from subprocess import check_output
from typing import Optional


def main():
    git_branch_name = current_git_branch_name()
    issue_key = extract_issue_key(git_branch_name)

    if not issue_key:
        sys.exit(0)

    commit_msg_filepath = sys.argv[1]
    commit_msg = read_file(commit_msg_filepath)
    new_commit_msg = reformat_msg(commit_msg, issue_key)

    if new_commit_msg != commit_msg:
        write_file(commit_msg_filepath, new_commit_msg)

    sys.exit(0)


def current_git_branch_name() -> str:
    return run_command("git symbolic-ref --short HEAD")


def run_command(command: str) -> str:
    return check_output(command.split()).decode("utf-8").strip()


def extract_issue_key(message: str) -> Optional[str]:
    key_regex = "[A-Z]{2,}-[0-9]+"
    match = re.search(key_regex, message)
    return match.group(0) if match else None


def reformat_msg(commit_msg: str, issue_key: str) -> str:
    commit_parts = commit_msg.split("\n", maxsplit=1)
    subject = reformat_subject(commit_parts[0], issue_key)
    body = commit_parts[1].strip() if len(commit_parts) > 1 else None
    return f'{subject}\n\n{body}' if body else subject


def reformat_subject(subject: str, issue_key: str) -> str:
    issue_key = extract_issue_key(subject) or issue_key

    if subject.startswith(issue_key):
        subject = subject[len(issue_key):]

    subject = subject.strip().rstrip('.')
    subject = subject[0].upper() + subject[1:]
    return f'{issue_key} {subject}'

def read_file(filepath: str) -> str:
    with open(filepath, "r") as f:
        return f.read()


def write_file(filepath: str, content: str) -> None:
    with open(filepath, "w") as f:
        f.write(content)


if __name__ == "__main__":
    main()
