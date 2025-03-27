#!/bin/bash

# Generate two random hours between 4 AM and 16 PM UTC (10 AM to 10 PM IST)
hour1=$((4 + RANDOM % 13))
hour2=$((4 + RANDOM % 13))

# Ensure they are different
while [ "$hour1" -eq "$hour2" ]; do
  hour2=$((4 + RANDOM % 13))
done

# Pick random minutes (0, 15, 30, 45)
minute1=$((15 * (RANDOM % 4)))
minute2=$((15 * (RANDOM % 4)))

echo "Generated Times: $hour1:$minute1 and $hour2:$minute2 UTC"

# Update the workflow file
sed -i "s|cron: .* # Auto-generated 1|cron: \"$minute1 $hour1 * * *\" # Auto-generated 1|" .github/workflows/main.yml
sed -i "s|cron: .* # Auto-generated 2|cron: \"$minute2 $hour2 * * *\" # Auto-generated 2|" .github/workflows/main.yml
