try:
    f =open('testfile.txt')
    var = bad_var
except FileNotFoundError:
        print('Error! File not found') 
except Exception:
    print('Sorry something went wrong')
#else:
#   print(f.read())
#    f.close
#finally:
#    pass


