# https://api.github.com/search/repositories?q=bottle&sort=start&order=asc
# https://api.github.com/search/repositories?q=django
import requests

def get_names():
    print('Separate each name with Space:')
    names = input()
    return names.split()


def check_repos(names):
    repo_api = 'https://api.github.com/search/repositories?q='
    ecosys_api = 'https://api.github.com/search/repositories?q=topic:'
    for name in names:
        repo_info = requests.get(repo_api + name).json()['items'][0]
        # 1/json --2/dict --3/dict['items'] -- list[0]--django {name:django.star:123}
        star = repo_info['stargazers_count']
        forks = repo_info['forks_count']

        ecosys_info = requests.get(ecosys_api + name).json()['total_count']

        print(name)
        print('Star:' + str(star))
        print('ecosys_info:' + str(ecosys_info))
        print('Forks:' + str(forks))


check_repos(get_names())
