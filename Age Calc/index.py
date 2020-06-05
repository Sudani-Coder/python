age = int(input('what\'s your age? ').strip())

# Get age in all time units

months = age * 12
weeks = months * 4
days = age * 365
hours = days * 24
minutes = hours * 60
seconds = minutes * 60

result = f" \
You lived for:\n \
{months} Months.\n \
{weeks:,d} Weeks.\n \
{days:,d} Days.\n \
{hours:,d} Hours.\n \
{minutes:,d} Minutes.\n \
{seconds:,d} Seconds.\n \
"

print(result)
