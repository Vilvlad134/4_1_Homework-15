from datetime import datetime
from application import salary
from application.db import people
from tqdm import tqdm


def main():
    salary.calculate_salary()
    people.get_employees()
    tt = datetime.today()
    dt = tt.timetuple()
    print(tt)
    for it in tqdm(dt, desc="DataTime", unit=" datetime", ncols=100):
        print(it)

if __name__ == '__main__':
    main()