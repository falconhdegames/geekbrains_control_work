def NotNullInput(message):
    return_=''
    while True:
        return_ = input(message)
        if return_ == '' or return_ == '\n' or return_ == None:
            print('Please enter something that\'s not empty')
            continue
        else:
            return return_
        
def DateInput(message):
    return_=''
    while True:
        return_ = input(message)
        split = return_.split('/')
        if len(split) == 3:
            err = None
            for i, e in enumerate(split):
                if i == 0:
                    if e.isdigit() and len(e) == 4:
                        ...
                    else:
                        err=True
                        break
                elif i == 1:
                    if e.isdigit() and int(e) <= 12 and len(e) == 2:
                        ...
                    else:
                        err=True
                        break
                elif i == 2:
                    if e.isdigit() and int(e) <= 31 and len(e) == 2:
                        ...
                    else:
                        err=True
                        break
            if err:
                print('Enter a vaid date (ex: 2023/12/31)')
                continue
            else:
                return return_
        else:
            print('Enter a vaid date (ex: 2023/12/31)')
            continue