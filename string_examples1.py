# a python program to creat a string:
if __name__ =="__main__":
    s1='welcome to core python learning 1'
    print(s1) # Output: welcome to core python learning 1
    s2="welcome to core python learning 2"
    print(s2) # Output: welcome to core python learning 2
    s3='welcome to "core python" learning 3'
    print(s3) # Output: welcome to "core python" learning 3
    s4="welcome to 'core python' learning 4"
    print(s4) # Output: welcome to 'core python' learning 4
    s5="welcome to\tcore python\nlearning 5"
    print(s5)
    '''    # Output: welcome to      core python
                 learning 5
    '''
    s6=r"welcome to\tcore python\nlearning 6"
    print(s6) # Output: welcome to\tcore python\nlearning 6
    s7=u'\u0915\u094b\u0930 \u092a\u0948\u0925\u0964\u0928'
    print(s7) # Output: कोर पैथ।