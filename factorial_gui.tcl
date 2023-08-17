# Load the Tk package
package require Tk

# Create the main window
wm title . "Factorial Calculator"
wm geometry . 300x150

# Create GUI elements
label .label -text "Enter a number:"
entry .entry -width 10
button .calculate -text "Calculate" -command calculate_factorial
label .result -text ""

# Arrange GUI elements using grid layout
grid .label - .entry
grid .calculate - -sticky w
grid .result - -sticky w

# Function to calculate factorial using recursion
proc factorial {n} {
    if {$n <= 1} {
        return 1
    } else {
        return [expr $n * [factorial [expr $n - 1]]]
    }
}

# Function to calculate factorial and display result
proc calculate_factorial {} {
    set input [.entry get]
    if {[string is integer $input]} {
        set number [string trim $input]
        set result [factorial $number]
        .result configure -text "Factorial of $number is $result"
    } else {
        .result configure -text "Invalid input. Please enter a valid integer."
    }
}

# Start the Tk event loop
tkwait window .

