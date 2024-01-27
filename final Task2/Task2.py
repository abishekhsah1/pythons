import sys
def analyze_cat_shelter_log(file_path):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
        catsvisits = 0
        intrudersvisit = 0
        totaltime = 0
        longest_visit = 0
        shortest_visit = float('inf')
        for line in lines:
            if line.startswith("OURS"):
                catsvisits += 1
                _, entry_time, exit_time = line.strip().split(',')
                entry_time = int(entry_time)
                exit_time = int(exit_time)
                visit_duration = exit_time - entry_time
                totaltime += visit_duration
                if visit_duration > longest_visit:
                    longest_visit = visit_duration
                if visit_duration < shortest_visit:
                    shortest_visit = visit_duration
            elif line.startswith("THEIRS"):
                intrudersvisit += 1
        if catsvisits == 0:
            print("No visits by the correct cat.")
        else:
            avg_duration = totaltime / catsvisits
            hours = totaltime // 60
            minutes = totaltime % 60
            longest_hours = longest_visit // 60
            longest_minutes = longest_visit % 60
            shortest_hours = shortest_visit // 60
            shortest_minutes = shortest_visit % 60
            print("\nLog File Analysis")
            print("==================")
            print(f"\nCat Visits: {catsvisits}")
            print(f"Other Cats: {intrudersvisit}")
            print(f"\nTotal Time in House: {hours} Hours, {minutes} Minutes")
            print(f"\nAverage Visit Length: {int(avg_duration)} Minutes")
            print(f"Longest Visit: {longest_hours} Hours, {longest_minutes} Minutes")
            print(f"Shortest Visit: {shortest_hours} Hours, {shortest_minutes} Minutes")
            print(f"\n```")
    except FileNotFoundError:
        print(f'Cannot open "{file_path}"!')
    except Exception as e:
        print(f"An error occurred: {e}")
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Missing command line argument!")
    else:
        log_file_path = sys.argv[1]
        analyze_cat_shelter_log(log_file_path)
