import utils

def main():
    year = utils.get_user_year()
    percent = utils.get_user_percentage()
    utils.create_commits(year, percent)
    utils.push_commits()
    
if __name__ in "__main__":
    main()