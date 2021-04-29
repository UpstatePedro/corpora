import fire

from src.core import orchestration

if __name__ == '__main__':
    fire.Fire(orchestration.summarise_directory)