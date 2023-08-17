#!/bin/awk -f

# AWK script to process website visits log

# Initialize an associative array to store visit counts per website
# The array index will be the website URL
# The array value will be the visit count
BEGIN {
    FS = "\t"  # Set the field separator to tab
}

# For each line in the log file, update the visit count for the corresponding website
{
    website = $1
    visits[website]++
}

# After processing all lines, display the total visit counts for each website
END {
    print "Website\tVisits"
    for (website in visits) {
        print website "\t" visits[website]
    }
}
