number_of_snowballs = int(input())

best_snowball_stats = {
    'snowball_total_score': 0,
    'snowball_weight': 0,
    'snowball_travel_time': 0,
    'snowball_quality': 0
}

for i in range(number_of_snowballs):

    snowball_weight = int(input())
    snowball_travel_time = int(input())
    snowball_quality = int(input())

    current_snowball_score = (snowball_weight / snowball_travel_time) ** snowball_quality

    if current_snowball_score > best_snowball_stats["snowball_total_score"]:
        best_snowball_stats['snowball_total_score'] = current_snowball_score
        best_snowball_stats['snowball_weight'] = snowball_weight
        best_snowball_stats['snowball_travel_time'] = snowball_travel_time
        best_snowball_stats['snowball_quality'] = snowball_quality

print(f"{best_snowball_stats['snowball_weight']} : {best_snowball_stats['snowball_travel_time']} = {best_snowball_stats['snowball_total_score']:.0f} ({best_snowball_stats['snowball_quality']})")
