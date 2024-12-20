universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]

def enrollment_stats(data):
    """Extracts student enrollments and tuition fees from the data."""
    enrollments = [university[1] for university in data]
    tuitions = [university[2] for university in data]
    return enrollments, tuitions

def mean(values):
    """Calculates the mean of a list of numbers."""
    return sum(values) / len(values) if values else 0

def median(values):
    """Calculates the median of a list of numbers."""
    sorted_values = sorted(values)
    n = len(sorted_values)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_values[mid - 1] + sorted_values[mid]) / 2
    else:
        return sorted_values[mid]

# Calculate statistics
enrollments, tuitions = enrollment_stats(universities)

total_students = sum(enrollments)
total_tuition = sum(tuitions)

student_mean = mean(enrollments)
student_median = median(enrollments)

tuition_mean = mean(tuitions)
tuition_median = median(tuitions)

print("******************************")
print(f"Total students: {total_students:,}")
print(f"Total tuition: $ {total_tuition:,}")
print()
print(f"Student mean: {student_mean:,.2f}")
print(f"Student median: {student_median:,}")
print()
print(f"Tuition mean: $ {tuition_mean:,.2f}")
print(f"Tuition median: $ {tuition_median:,}")
