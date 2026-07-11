SUSPICIOUS = [
    "nc",
    "netcat",
    "bash -i",
    "python -c",
    "socat",
    "curl | bash",
    "wget"
]

def check(cmd):
    cmd = cmd.lower()

    for item in SUSPICIOUS:
        if item in cmd:
            return True

    return False
