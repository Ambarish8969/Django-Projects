from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Print the value of BASE_DIR
print("BASE_DIR:", BASE_DIR)
print(os.path.join(BASE_DIR,'user_react/build/'))