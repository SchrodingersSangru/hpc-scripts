# Load the Tk package
package require Tk

# Create the main window
wm title . "Text Editor"
wm geometry . 800x600

# Create a text widget for editing
text .text -wrap word
pack .text -fill both -expand 1

# Create a menu bar
menu .menubar -tearoff 0
. configure -menu .menubar
.menubar add cascade -label "File" -menu [menu .menubar.file]
.menubar.file add command -label "Open" -command open_file
.menubar.file add command -label "Save" -command save_file
.menubar.file add separator
.menubar.file add command -label "Exit" -command exit

# Function to open a file
proc open_file {} {
    set filename [tk_getOpenFile -filetypes {{Text Files {.txt}}}]
    if {$filename ne ""} {
        set file_handle [open $filename r]
        .text delete 1.0 end
        .text insert end [read $file_handle]
        close $file_handle
    }
}

# Function to save a file
proc save_file {} {
    set filename [tk_getSaveFile -defaultextension ".txt" -filetypes {{Text Files {.txt}}}]
    if {$filename ne ""} {
        set file_handle [open $filename w]
        puts -nonewline $file_handle [.text get 1.0 end]
        close $file_handle
    }
}

# Function to exit the program
proc exit {} {
    exit
}

# Start the Tk event loop
tkwait window .

