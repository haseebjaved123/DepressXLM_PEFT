"""Three adapter stages described in the DepressXLM manuscript."""
STAGES = [
    ("LoRA-1", "binary depression screening"),
    ("LoRA-2", "severity prediction"),
    ("LoRA-3", "guidance and explanation"),
]
def main():
    for name, task in STAGES:
        print(f"{name}: {task}")
if __name__ == "__main__":
    main()
