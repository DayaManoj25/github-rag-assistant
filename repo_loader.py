#STEP 1

#We are creating a Python file that can:
# Take a GitHub repository URL
# Clone (download) the repository
# Save it inside our project folder


# Import Repo class from GitPython
# This library allows us to clone GitHub repositories using Python
from git import Repo

# Import os for file/folder operations
import os


def clone_repo(repo_url):
    """
    This function takes a GitHub repository URL
    and clones it into the cloned_repos folder.

    Example:
    https://github.com/user/project
    """

    # Extract repository name from URL
    # Example:
    # https://github.com/user/project
    # becomes:
    # project
    repo_name = repo_url.split("/")[-1]

    # Create destination path
    # Example:
    # cloned_repos/project
    save_path = os.path.join(
        "cloned_repos",
        repo_name
    )

    # Check whether repository already exists
    if not os.path.exists(save_path):

        print("Cloning repository...")

        # Download repository
        Repo.clone_from(
            repo_url,
            save_path
        )

        print("Repository cloned successfully!")

    else:
        print("Repository already exists.")

    # Return the path where repository is stored
    return save_path