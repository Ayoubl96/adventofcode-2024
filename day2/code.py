# Open and read the file
with open("data.txt", "r") as file:
    file_open = file.read()

array = file_open.strip().split("\n")
lines = [list(map(int, line.split())) for line in array if line.strip()]

print(f"Parsed lines (reports): {lines}")


def is_safe(report):
    differences = [abs(report[i + 1] - report[i]) for i in range(len(report) - 1)]
    is_increasing = all(report[i + 1] > report[i] for i in range(len(report) - 1))
    is_decreasing = all(report[i + 1] < report[i] for i in range(len(report) - 1))
    return (is_increasing or is_decreasing) and all(1 <= diff <= 3 for diff in differences)


def count_safe_reports_with_dampener(lines):
    safe_count = 0

    for report in lines:
        if is_safe(report):
            ## print(f"{report} is safe without dampener.")
            safe_count += 1
        else:
            for i in range(len(report)):
                modified_report = report[:i] + report[i + 1:]
                if is_safe(modified_report):
                    ## print(f"{report} becomes safe by removing {report[i]}")
                    safe_count += 1
                    break
    return safe_count


safe_reports_count = count_safe_reports_with_dampener(lines)
print(f"Number of safe reports: {safe_reports_count}")
