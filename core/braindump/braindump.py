from pathlib import Path

# TODO: configureation .file


KNOWLEDGE_BASE_PATH = Path("~/Documents/Zaldis Notes").expanduser()
EXCLUDE_PATH_PART = ('.obsidian', '.trash', '.space', '.tmp.driveupload', '.DS_Store')


def dump_knowledge_base(
    knowledge_base_path: Path,
    exclude_parts: tuple[str, ...],
):
    print("Dumping knowledge from:", knowledge_base_path)
    markdown_context = []
    dumped_files_count = 0
    for path in knowledge_base_path.rglob('*'):
        if path.suffix == '.md' and all(part not in exclude_parts for part in path.parts):
            markdown_context.append(f"\n--- FILE: {path.name} ---\n")
            with open(path, 'r') as file:
                markdown_context.extend(file.readlines())
            markdown_context.append(f"\n--- FILE END ---\n")
            dumped_files_count += 1
    with open('/tmp/knowledge.txt', 'w') as file:
        file.writelines(markdown_context)
    print(f"Dumped {dumped_files_count} into /tmp/knowledge.txt file.")


if __name__ == '__main__':
    dump_knowledge_base(
        KNOWLEDGE_BASE_PATH,
        EXCLUDE_PATH_PART,
    )
