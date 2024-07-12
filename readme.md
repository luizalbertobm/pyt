
# Gitflow Utility Commands

This script provides utility commands for working with Git using the Gitflow workflow. It simplifies common Git operations such as starting a new feature branch, finishing a feature branch, checking out or creating a branch, and deleting a branch.

## Requirements

- Python 3.x
- Git

## Installation

1. Save the script as `pyt`.
2. Make the script executable:
   ```bash
   chmod +x pyt
   ```
3. Move the script to a directory that is in your PATH, for example:
   ```bash
   mv pyt /usr/local/bin/
   ```

## Usage

### Start a New Feature Branch

To start a new feature branch:

```bash
pyt start
```

The script will prompt you to enter the feature code (e.g., `FEAT-321`). If branches with this code already exist, you will be given the option to checkout an existing branch or create a new one. You will also be prompted to provide a brief description for the new branch.

### Finish a Feature Branch

To finish a feature branch by merging `main` into the current branch and pulling the latest changes:

```bash
pyt finish
```

### Check if a Branch Exists and Checkout/Create It

To check if a branch exists and either checkout or create it:

```bash
pyt check <branch_name>
```

Replace `<branch_name>` with the name of the branch you want to check.

### Delete a Branch

To delete a specific branch:

```bash
pyt delete <branch_name>
```

Replace `<branch_name>` with the name of the branch you want to delete.

To delete the current branch (after switching to `main`):

```bash
pyt delete
```

## Script Overview

### Functions

- `branch_exists(branch_code)`: Checks if branches that start with the given code exist.
- `create_branch(branch_name)`: Creates and checks out a new branch.
- `delete_branch(branch_name=None)`: Deletes the specified branch. If no branch name is provided, it deletes the current branch after switching to `main`.
- `checkout_branch(branch_name)`: Checks out the specified branch.
- `merge_branch(current_branch)`: Merges `main` into the current branch.
- `pull_changes()`: Pulls the latest changes from the remote repository.
- `start_feature()`: Starts a new feature branch, prompting for the feature code and description.
- `finish_feature()`: Finishes a feature branch by merging `main` into the current branch and pulling the latest changes.

### Command Parsing

The script uses `argparse` to handle command-line arguments and subcommands:

- `start`: Starts a new feature branch.
- `finish`: Finishes a feature branch.
- `check <branch_name>`: Checks if a branch exists and either checkouts or creates it.
- `delete <branch_name>`: Deletes a branch. If no branch name is provided, deletes the current branch after switching to `main`.

## License

This project is licensed under the MIT License.

> Developed by [Luiz Mesquita](https://github.com/luizalbertobm)