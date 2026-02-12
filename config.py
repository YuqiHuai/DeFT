from pathlib import Path


class Config:
    PROJECT_ROOT = Path(__file__).parent
    APOLLO_ROOT = Path(PROJECT_ROOT, 'apollo-7.0.0')


CONFIG = Config()

if __name__ == '__main__':
    print(CONFIG.PROJECT_ROOT)
    print(CONFIG.APOLLO_ROOT)
