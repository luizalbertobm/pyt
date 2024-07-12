# Makefile for Gitflow utility commands

.DEFAULT_GOAL = help
.PHONY        : help build up start down logs sh composer vendor sf cc test

## —— Gitflow commands ——————————————————
help: ## Outputs this help screen
	@grep -E '(^[a-zA-Z0-9\./_-]+:.*?##.*$$)|(^##)' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}{printf "\033[32m%-30s\033[0m %s\n", $$1, $$2}' | sed -e 's/\[32m##/[33m/'

branch.check: ## Checkout an existing branch
	@echo "Checking out branch $(branch_name)"
	@git checkout $(branch_name)


branch.delete: ## Delete the current branch or the specified one
	@if [ -z "$(branch_name)" ]; then \
		branch_name=$$(git branch --show-current); \
		if [ -z "$$branch_name" ]; then \
			echo "Error getting the current branch."; \
			exit 1; \
		fi; \
	fi; \
	if [ "$$branch_name" = "main" ]; then \
		echo "Cannot delete the 'main' branch."; \
		exit 1; \
	fi; \
	echo "Switching to 'main' branch to delete $(branch_name)"; \
	git checkout main; \
	git branch -d $$branch_name; \
	echo "Branch '$$branch_name' deleted successfully."


feature.start: ## Start a new feature branch
	@echo "Enter the feature code:"
	@read feature_code; \
	branches=$$(git branch --list "$$feature_code*"); \
	if [ -n "$$branches" ]; then \
		echo "Branches existing with prefix $$feature_code:"; \
		echo "$$branches"; \
		echo "Do you want to checkout an existing branch or create a new one? (checkout/create):"; \
		read choice; \
		if [ "$$choice" = "checkout" ]; then \
			echo "Enter the branch number to checkout:"; \
			read branch_index; \
			branch_name=$$(echo $$branches | sed -n "$${branch_index}p"); \
			git checkout $$branch_name; \
			echo "Checked out existing branch: $$branch_name"; \
			exit 0; \
		fi; \
	fi; \
	echo "Enter a brief description for the new branch:"; \
	read description; \
	branch_name="$$feature_code-$$description"; \
	branch_name=$$(echo $$branch_name | sed 's/ /-/g'); \
	git checkout -b $$branch_name; \
	echo "New branch created and checked out: $$branch_name"


feature.finish: ## Finish a feature branch
	@current_branch=$$(git branch --show-current); \
	if [ -z "$$current_branch" ]; then \
		echo "Error getting the current branch."; \
		exit 1; \
	fi; \
	echo "Merging 'main' into '$$current_branch'"; \
	git checkout main; \
	git pull; \
	git checkout $$current_branch; \
	git merge --no-ff main; \
	git pull; \
	echo "Branch 'main' merged into '$$current_branch' and pulled the latest changes."

.PHONY: branch_exists create_branch delete_branch checkout_branch merge_branch pull_changes start_feature finish_feature
