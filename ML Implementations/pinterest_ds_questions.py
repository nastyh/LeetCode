"""
SQL
Given three tables, events, users_d, and pins_classification below:
events
+--------------+------------------+----------+---------------------------------+
| Column | Description | Type | Example value(s) | +--------------+------------------+----------+---------------------------------+
| pin_id | the pin ID | bigint | 687198377919 |
| user_id | the user ID | bigint | 378372943601760476
| action_type | action type | string | 'IMPRESSION', 'CLICK', 'SAVE' | | num_actions | action count | bigint | 0, 1, 2 |
| dt | date | date | 2022-01-01 | +--------------+------------------+----------+---------------------------------+
users_d
+--------------+-----------------------------+----------+--------------------+
| Column | Description | Type | Example value(s) | +--------------+-----------------------------+----------+--------------------+
pins_classification +-----------------+---------------------+----------+--------------------+
| Column | Description | Type | Example value(s) | +-----------------+---------------------+----------+--------------------+
| pin_id | the pin ID | bigint | 687198377919 |
| pin_format | Pin Format Type | string | 'video', 'static' | +-----------------+---------------------+----------+--------------------+
Write a query to calculate the Click-Through-Rate by pin_format and date, for new Users in the US.
Notes:
Click-Through-Rate is defined as the number of clicks per number of impressions
A user is considered new on a given date, if they signed up less than 30 days prior to that date
*/

"""

WITH NewUsers AS (
    SELECT 
        user_id,
        signup_date,
        dt 
    FROM 
        users_d 
    CROSS JOIN
        (SELECT DISTINCT dt FROM events) AS event_dates
    WHERE
        signup_date >= dt - INTERVAL 30 DAY
),

AggregatedEvents AS (
    SELECT 
        e.dt,
        pc.pin_format,
        SUM(CASE WHEN e.action_type = 'CLICK' THEN e.num_actions ELSE 0 END) AS total_clicks,
        SUM(CASE WHEN e.action_type = 'IMPRESSION' THEN e.num_actions ELSE 0 END) AS total_impressions
    FROM 
        events e
    JOIN 
        pins_classification pc ON e.pin_id = pc.pin_id
    JOIN 
        NewUsers nu ON e.user_id = nu.user_id AND e.dt = nu.dt
    GROUP BY 
        e.dt, pc.pin_format
)

SELECT 
    dt,
    pin_format,
    total_clicks,
    total_impressions,
    CASE 
        WHEN total_impressions > 0 THEN total_clicks / total_impressions
        ELSE 0
    END AS click_through_rate
FROM 
    AggregatedEvents
ORDER BY 
    dt, pin_format


"""
# Code to generate dataframe import pandas as pd
import random
| bigint | 687198377919 | | string | 'female', 'male' |
| string | 'US', 'UK', 'BR' |
| user_id
| gender
| country
| signup_dt | date User joined Pinterest | date | 2022-09-01 | +--------------+-----------------------------+----------+--------------------+
| the User ID
| User gender | User country
|
 import datetime pd.set_option('display.max_columns', None) random.seed(5)
def random_date(start,l):
current = start while l >= 0:
curr = current + datetime.timedelta(minutes=random.randrange(60)) yield curr
l-=1
data = pd.DataFrame([ random.sample(range(100000000, 200000000), 100), ['Mobile_iOS'] * 25 + ['Mobile_Android'] * 25 + \ ['Desktop_Windows'] * 25 + ['Desktop_MacOS'] * 25, random.sample(range(0, 1000000), 100), random.sample(range(9000000000, 9800000000), 100), [random.choice([1,2,3,4,5, -100, 0
]) for i in range(100)],
[random.choice(['video', 'static']) for i in range(100)]
]).T
data.columns = ['user_id', 'app', 'time_spent', 'pin_id', 'category', 'pin_type'] data['time_spent'] = data['time_spent'].apply(int)
data['category'] = data['category'].apply(int)
data = data.sample(frac=1).reset_index(drop=True)
'''
------------------------------------------------------------------------
Part 1
------------------------------------------------------------------------
We have a dataframe that contains information about user engagement (time spent in milliseconds) with different formats and categories of Pins.
Using the following mapping of categories, can you find the category with the highest average time spent for video Pins? If there is a pin category value in our data that is not included in the dictionary below, we would like to map that to ‘Unknown’. ------------------------------------------------------------------------
'''
category_dict = {

1: 'Fashion',
2: 'Food',
3: 'Home Decor', 4: 'Art',
5: 'Travel'
}

"""
import pandas as pd
import random
import datetime

# Set random seed for reproducibility
random.seed(5)

# Function to generate random dates
def random_date(start, l):
    current = start
    while l >= 0:
        curr = current + datetime.timedelta(minutes=random.randrange(60))
        yield curr
        l -= 1

# Generate sample data for the DataFrame
data = pd.DataFrame([
    random.sample(range(100000000, 200000000), 100),
    ['Mobile_iOS'] * 25 + ['Mobile_Android'] * 25 + ['Desktop_Windows'] * 25 + ['Desktop_MacOS'] * 25,
    random.sample(range(0, 1000000), 100),
    random.sample(range(9000000000, 9800000000), 100),
    [random.choice([1, 2, 3, 4, 5, -100, 0]) for i in range(100)],
    [random.choice(['video', 'static']) for i in range(100)]
]).T

data.columns = ['user_id', 'app', 'time_spent', 'pin_id', 'category', 'pin_type']

# Convert time_spent to int and category to int
data['time_spent'] = data['time_spent'].apply(int)
data['category'] = data['category'].apply(int)

# Shuffle the data
data = data.sample(frac=1).reset_index(drop=True)

# Define the category mapping
category_dict = {
    1: 'Fashion',
    2: 'Food',
    3: 'Home Decor',
    4: 'Art',
    5: 'Travel'
}

# Map categories to their names, mapping unknown values to 'Unknown'
data['category'] = data['category'].map(category_dict).fillna('Unknown')

# Filter for video Pins
video_data = data[data['pin_type'] == 'video']

# Calculate average time spent by category
average_time_spent = video_data.groupby('category')['time_spent'].mean().reset_index()

# Find the category with the highest average time spent
max_average_category = average_time_spent.loc[average_time_spent['time_spent'].idxmax()]

# Print the result
print(f"Category with the highest average time spent for video Pins: {max_average_category['category']}")
print(f"Average time spent: {max_average_category['time_spent']:.2f} milliseconds")

# SQL

CREATE TABLE user_engagement (
    user_id BIGINT,
    app VARCHAR(50),
    time_spent INT,
    pin_id BIGINT,
    category INT,
    pin_type VARCHAR(50)
);

-- Insert sample data into the table (using hypothetical data)
INSERT INTO user_engagement (user_id, app, time_spent, pin_id, category, pin_type)
VALUES
-- Sample data here (you would generate this programmatically as shown before or use an insert script)
(687198377919, 'Mobile_iOS', 500000, 1234567890, 1, 'video'),
(687198377920, 'Mobile_Android', 300000, 1234567891, 2, 'video'),
(687198377921, 'Desktop_Windows', 400000, 1234567892, 3, 'video'),
(687198377922, 'Desktop_MacOS', 600000, 1234567893, 1, 'static'),
(687198377923, 'Mobile_iOS', 700000, 1234567894, 4, 'video'),
(687198377924, 'Mobile_Android', 200000, 1234567895, 5, 'video'),
-- Add more rows similarly

-- Step 1: Create a mapping of categories
WITH category_mapping AS (
    SELECT 
        1 AS category_id, 'Fashion' AS category_name UNION ALL
    SELECT 
        2, 'Food' UNION ALL
    SELECT 
        3, 'Home Decor' UNION ALL
    SELECT 
        4, 'Art' UNION ALL
    SELECT 
        5, 'Travel'
),
-- Step 2: Joining the main table with category mapping
average_time_spent AS (
    SELECT
        COALESCE(cm.category_name, 'Unknown') AS category_name,
        AVG(ue.time_spent) AS avg_time_spent
    FROM
        user_engagement ue
    LEFT JOIN
        category_mapping cm ON ue.category = cm.category_id
    WHERE
        ue.pin_type = 'video'  -- Filter for video Pins
    GROUP BY
        cm.category_name
)

-- Step 3: Select the category with highest average time spent
SELECT 
    category_name, 
    avg_time_spent
FROM 
    average_time_spent
ORDER BY 
    avg_time_spent DESC
LIMIT 1;  -- Get the top category


"""
Part 2
----------------------------------------------------------------------------
Next, we also have some data on video pins seen by each user, in the format of a dictionary, where each user has
an associated list of pins that they have seen over a given period of time.
Using this data, can you write a function to calculate the average number of unique video pins seen per user?
----------------------------------------------------------------------------
'''
user_dict = { 'user1' : [1,2,1], 'user2' : [2,3,1], 'user3' : [1,2,3,4]
}
"""
def average_unique_pins(user_dict):
    # Initialize a list to store the count of unique pins for each user
    unique_counts = []

    # Iterate over each user in the user_dict
    for user, pins in user_dict.items():
        # Use a set to get unique pins for the user
        unique_pins = set(pins)
        # Append the count of unique pins to the list
        unique_counts.append(len(unique_pins))

    # Calculate the average number of unique pins seen per user
    if unique_counts:  # Check if there are any users
        average = sum(unique_counts) / len(unique_counts)
    else:
        average = 0  # If there are no users, average is 0

    return average

# Given user_dict
user_dict = {
    'user1': [1, 2, 1],
    'user2': [2, 3, 1],
    'user3': [1, 2, 3, 4]
}

# Calculate and print the average number of unique video pins seen per user
average_unique = average_unique_pins(user_dict)
print(f"Average number of unique video pins seen per user: {average_unique:.2f}")

# SQL

WITH UniquePinCounts AS (
    SELECT 
        user_id, 
        COUNT(DISTINCT pin_id) AS unique_pin_count
    FROM 
        user_video_pins
    GROUP BY 
        user_id
)
SELECT 
    AVG(unique_pin_count) AS average_unique_pins 
FROM 
    UniquePinCounts;

"""
What pin category in each country has the highest number of impressions today?
pin_impressions: each row is an impression (impression defined as seeing a pin) +----------+----------------------------------+----------+----------------------------------+
| Column | Description | Type | Example value(s) |
+----------+----------------------------------+----------+----------------------------------+
| pin_id | the pin ID | bigint | 687198377919 |
| user_id | the user ID | bigint | 378372943601760476
| app | the app the user was using | string | 'ios', 'android', 'web' |
| surface | Pinterest surface of impression | string | ‘homefeed’, ’search’, ’related’ |
| dt | date of impression | string | '2019-01-01' +----------+----------------------------------+----------+----------------------------------+
user_dimension: each row is a user +-------------+--------------------------------+----------+----------------------+
| Column | Description | Type | Example value(s) | +-------------+--------------------------------+----------+----------------------+
|
| user_id
| country
| gender
| interest | interest selected on sign-up | string | ‘travel’
| signup_dt | date user created account | string | ‘2021-01-01’ +-------------+--------------------------------+----------+----------------------+
| the user ID
| country of the user | gender of the user
| bigint | 378372943601760476 |
| string | 'US'
| string | 'female'
|
|
|
pins_dimension: each row is a pin +------------------+-----------------------------------+----------+---------------------+
| Column | Description | Type | Example value(s) | +------------------+-----------------------------------+----------+---------------------+
| pin_id | the pin ID | bigint | 687198377919 |
| user_id | the user ID that created the pin | bigint | 378372943601760476 | | pin_creation_dt | date the pin was created | string | '2021-01-01’ |
| category | category of the pin | string | ‘travel’ | +------------------+-----------------------------------+----------+---------------------+
"""
WITH ImpressionsToday AS (
    SELECT 
        pi.pin_id,
        ud.country,
        pd.category
    FROM 
        pin_impressions pi
    JOIN 
        user_dimension ud ON pi.user_id = ud.user_id
    JOIN 
        pins_dimension pd ON pi.pin_id = pd.pin_id
    WHERE 
        pi.dt = CURRENT_DATE  -- Assuming this is set to the current date
),
CategoryImpressions AS (
    SELECT 
        country, 
        category, 
        COUNT(*) AS impression_count
    FROM 
        ImpressionsToday
    GROUP BY 
        country, 
        category
),
RankedCategories AS (
    SELECT 
        country, 
        category, 
        impression_count,
        RANK() OVER (PARTITION BY country ORDER BY impression_count DESC) AS rank
    FROM 
        CategoryImpressions
)

SELECT 
    country, 
    category, 
    impression_count
FROM 
    RankedCategories
WHERE 
    rank = 1;  -- Selects categories with the highest impressions per country

"""
What percent of active users are highly active by country for today?
Active is defined as having at least one impression that day. Highly active is defined as: 1) been active at least 4 days in the past week
2) visited all 3 surfaces (there are only 3 surfaces) on at least one of those days
"""
WITH ActiveUsersToday AS (
    SELECT 
        user_id,
        ud.country
    FROM 
        pin_impressions pi
    JOIN 
        user_dimension ud ON pi.user_id = ud.user_id
    WHERE 
        pi.dt = CURRENT_DATE  -- Set to today's date
    GROUP BY 
        user_id, 
        ud.country
),

UserActivityHistory AS (
    SELECT 
        user_id,
        COUNT(DISTINCT dt) AS active_days,
        COUNT(DISTINCT surface) AS distinct_surfaces,
        ud.country
    FROM 
        pin_impressions pi
    JOIN 
        user_dimension ud ON pi.user_id = ud.user_id
    WHERE 
        pi.dt >= CURRENT_DATE - INTERVAL '6 DAYS'  -- Last 7 days including today
    GROUP BY 
        user_id, 
        ud.country
),

HighlyActiveUsers AS (
    SELECT 
        country,
        COUNT(user_id) AS highly_active_count
    FROM 
        UserActivityHistory
    WHERE 
        active_days >= 4 
        AND distinct_surfaces = 3  -- Visited all 3 surfaces
    GROUP BY 
        country
),

UserCounts AS (
    SELECT 
        country,
        COUNT(user_id) AS active_user_count
    FROM 
        ActiveUsersToday
    GROUP BY 
        country
)
SELECT 
    uc.country,
    (COALESCE(hu.highly_active_count, 0) * 100.0 / uc.active_user_count) AS percent_highly_active
FROM 
    UserCounts uc
LEFT JOIN 
    HighlyActiveUsers hu ON uc.country = hu.country
ORDER BY 
    uc.country;


"""
# At Pinterest, Boards are where you save, collect, and organize your Pins
# (where Pins are bookmarks that people use to save content they love). We have a dictionary of boards,
# where each board has an associated list of pins on that board.
# boards = {
# # # # # #}
# Write a function that, for a given pin, will calculate the similarity score for each pin it shares a board with. Similarity is defined as the number of times it appears within the same board.
# For example, for pin ‘a’, the following pins and similarity scores should be returned: c=3, d=1, e=2, f=1, g=1, i=1.
"""
def calculate_similarity_score(boards, target_pin):
    # A dictionary to store similarity scores
    similarity_scores = {}

    # Iterate through each board in the dictionary
    for board, pins in boards.items():
        # If the target pin is in the current board, calculate the scores
        if target_pin in pins:
            for pin in pins:
                if pin != target_pin:  # Skip the target pin itself
                    # Increment the similarity score for the pin
                    if pin in similarity_scores:
                        similarity_scores[pin] += 1
                    else:
                        similarity_scores[pin] = 1

    return similarity_scores

"""
Can you update your function so that the output is a list of the top N pins ordered by
(descending) similarity score? So in the example above, if we wanted the top 2 pins for pin ‘a’
it would output [‘c’,’e’] (in that order).
"""
def calculate_top_n_similar_pins(boards, target_pin, N):
    # A dictionary to store similarity scores
    similarity_scores = {}

    # Iterate through each board in the dictionary
    for board, pins in boards.items():
        # If the target pin is in the current board, calculate the scores
        if target_pin in pins:
            for pin in pins:
                if pin != target_pin:  # Skip the target pin itself
                    # Increment the similarity score for the pin
                    if pin in similarity_scores:
                        similarity_scores[pin] += 1
                    else:
                        similarity_scores[pin] = 1

    # Sort the pins by similarity scores in descending order
    sorted_pins = sorted(similarity_scores.items(), key=lambda item: item[1], reverse=True)

    # Get the top N pins
    top_n_pins = [pin for pin, score in sorted_pins[:N]]

    return top_n_pins