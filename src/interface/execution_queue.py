import os


def get_execution_queue(path: str) -> list[str]:
    """
    Get the execution queue from the given file.

    Parameters:
        path (str): Path to the file containing the execution queue.

    Returns:
        list[str]: The execution queue.
    """

    execution_queue = []
    if os.path.exists(path) == False:
        raise FileNotFoundError(f"File not found: {path}")
    if os.path.isdir(path) == True:
        execution_queue = [
            f"{path}/{f}"
            for f in os.listdir(path)
            if f.endswith(".mp3") or f.endswith(".wav")
        ]

    else:
        execution_queue = [path]
    return execution_queue
