#!/usr/bin/env python3

import subprocess
import argparse

def branch_exists(branch_code):
    result = subprocess.run(['git', 'branch', '--list', f"{branch_code}*"], stdout=subprocess.PIPE)
    branches = result.stdout.decode('utf-8').strip().split('\n')
    branches = [branch.strip() for branch in branches if branch]
    return branches

def create_branch(branch_name):
    subprocess.run(['git', 'checkout', '-b', branch_name])

def delete_branch(branch_name=None):
    if branch_name is None:
        # Get the current branch name
        branch_name = subprocess.run(['git', 'branch', '--show-current'], stdout=subprocess.PIPE).stdout.decode('utf-8').strip()
        if not branch_name:
            print("Erro ao obter a branch atual.")
            return
    
    if branch_name == 'main':
        print("Não é possível deletar a branch 'main'.")
        return

    # Check out to the main branch before deleting the current branch
    subprocess.run(['git', 'checkout', 'main'])
    subprocess.run(['git', 'branch', '-d', branch_name])
    print(f"Branch '{branch_name}' deletada com sucesso.")


def checkout_branch(branch_name):
    subprocess.run(['git', 'checkout', branch_name])

def merge_branch(current_branch):
    subprocess.run(['git', 'checkout', 'main'])
    subprocess.run(['git', 'pull'])
    subprocess.run(['git', 'checkout', current_branch])
    subprocess.run(['git', 'merge', '--no-ff', 'main'])

def pull_changes():
    subprocess.run(['git', 'pull'])

def start_feature():
    feature_code = input("Qual o código da feature a ser trabalhada? ")
    existing_branches = branch_exists(feature_code)

    if existing_branches:
        print(f"Branches existentes que iniciam com {feature_code}:")
        for i, branch in enumerate(existing_branches):
            print(f"{i+1}. {branch}")

        choice = input("Deseja fazer checkout em uma dessas branches existentes ou criar uma nova? (checkout/criar): ").strip().lower()

        if choice == 'checkout':
            branch_index = int(input("Digite o número da branch na lista para fazer checkout: ")) - 1
            if 0 <= branch_index < len(existing_branches):
                checkout_branch(existing_branches[branch_index])
                print(f"Feito checkout na branch existente: {existing_branches[branch_index]}")
            else:
                print("Número da branch inválido.")
            return

    description = input("Digite uma breve descrição da nova branch: ").strip().replace(' ', '-')
    new_branch_name = f"{feature_code}-{description}"
    create_branch(new_branch_name)
    print(f"Nova branch criada e feito checkout: {new_branch_name}")

def finish_feature():
    current_branch = subprocess.run(['git', 'branch', '--show-current'], stdout=subprocess.PIPE).stdout.decode('utf-8').strip()
    if not current_branch:
        print("Erro ao obter a branch atual.")
        return

    print(f"Branch atual: {current_branch}")
    merge_branch(current_branch)
    pull_changes()
    print(f"Branch 'main' mesclada na branch '{current_branch}' e feito pull das mudanças.")

def main():
    parser = argparse.ArgumentParser(description='Gitflow utility commands')
    subparsers = parser.add_subparsers(dest='command')

    start_parser = subparsers.add_parser('start', help='Start a new feature branch')
    start_parser.add_argument('type', choices=['feat'], help='The type of branch to start (currently only supports feat)')

    finish_parser = subparsers.add_parser('finish', help='Finish a feature branch')

    check_parser = subparsers.add_parser('check', help='Check if a branch exists and checkout/create it')
    check_parser.add_argument('branch_name', help='The name of the branch to check')

    delete_parser = subparsers.add_parser('delete', help='Delete a branch')
    delete_parser.add_argument('branch_name', nargs='?', default=None, help='The name of the branch to delete')

    args = parser.parse_args()

    if args.command == 'check':
        if branch_exists(args.branch_name):
            print(f"Branch '{args.branch_name}' exists. Checking out.")
            checkout_branch(args.branch_name)
        else:
            print(f"Branch '{args.branch_name}' does not exist. Creating and checking out.")
            create_branch(args.branch_name)
    
    if args.command == 'start' and args.type == 'feat':
        start_feature()
    elif args.command == 'finish':
        finish_feature()
    elif args.command == 'delete':
        delete_branch(args.branch_name)

if __name__ == '__main__':
    main()
