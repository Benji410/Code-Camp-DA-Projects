import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df.race.value_counts()

    # What is the average age of men?
    average_age_men = round(df[df.sex == 'Male'].age.mean(), 1)

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = round(sum(df.education == 'Bachelors') / len(df) * 100, 1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    # data transformation and cleaning
    df['education3'] = df.education.apply(lambda x : 'Advanced' if x in ['Bachelors', 'Masters', 'Doctorate'] else 'Not Advanced')
    salary = df.groupby('education3').salary.value_counts().to_frame()
    salary.columns = ['cnt']
    salary.reset_index(drop=False, inplace=True)

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = salary[salary.education3 == 'Advanced']
    lower_education = salary[salary.education3 == 'Not Advanced']
    # add % of total
    higher_education['pct_of_total'] = higher_education.cnt / sum(higher_education.cnt)
    lower_education['pct_of_total'] = lower_education.cnt / sum(lower_education.cnt)

    # percentage with salary >50K
    higher_education_rich = round(higher_education[higher_education.salary == ">50K"].pct_of_total.iloc[0] * 100, 1)
    lower_education_rich = round(lower_education[lower_education.salary == ">50K"].pct_of_total.iloc[0] * 100, 1) 

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = min(df['hours-per-week'])

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = df[df['hours-per-week'] == min_work_hours]['salary'] == '>50K'
    min_workers = df[df['hours-per-week'] == min_work_hours]['salary'] == '>50K'
    
    rich_percentage = sum(min_workers) / len(min_workers) * 100

    # What country has the highest percentage of people that earn >50K?
    salaries = df.groupby('native-country')['salary'].value_counts().to_frame(name='user_cnt').reset_index()
    df_salary = salaries.pivot(index='native-country', columns='salary', values='user_cnt')
    df_salary['total_users'] = df_salary['>50K'] + df_salary['<=50K']
    df_salary['pct_salary_50k_plus'] = round(df_salary['>50K'] / df_salary['total_users'] * 100, 1)
    df_salary_sorted = df_salary.sort_values('pct_salary_50k_plus', ascending=False)

    highest_earning_country = df_salary_sorted.head(1).index[0]
    highest_earning_country_percentage = df_salary_sorted.head(1)['pct_salary_50k_plus'][0]

    # Identify the most popular occupation for those who earn >50K in India.
    IN_df = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
    IN_df_occ = IN_df.occupation.value_counts().to_frame()

    top_IN_occupation = IN_df_occ.head(1).index[0]

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
