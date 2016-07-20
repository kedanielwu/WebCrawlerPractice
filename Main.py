from ProgramFinder import *
from FileSystem import *
from CourseFinder import *

# test


def main():
    # set up programs
    program_finder = ProgramFinder("http://www.artsandscience.utoronto.ca/ofr/timetable/winter/")
    programs = program_finder.get_programs()
    program_file = FileSystem("programs.txt", programs)
    program_file.writing() 
    print "Programs loaded"
    
    # set up user menu
    menu = {}
    index = 1
    for program in programs:
        if programs[program].is_visible():
            menu[index] = program
            index += 1

    # Prompt user for selecting program and term
    for i in menu:
        print "{}: {}".format(i, menu[i])

    in_code = input("Enter a program code: ")

    while int(in_code) not in menu:
        print("Invalid Program Code!")
        in_code = input("Enter a program code: ")

    term_code = raw_input('Enter F for searching Fall term, S for Winter: ')

    while term_code != 'F' and term_code != 'S':
        print("Invalid Term Code!")
        term_code = raw_input("Enter F for searching Fall term, S for Winter: ")

    program_name = menu[in_code]
    url = programs[program_name].get_url()
    spider = CourseFinder(url, term_code)
    course_file = FileSystem("course.txt", spider.get_courses())
    course_file.writing()
    print "finished"

main()
