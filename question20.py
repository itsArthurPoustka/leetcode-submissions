closed_open ={
            ")":"(",
            "}":"{",
            "]":"["}


def solve_problem(s):
    stack = []
        
    for i in s:
        if i in closed_open:
            if not stack:
                return False
            if stack.pop() != closed_open[i]:
                return False
                    
        else:
            stack.append(i)
            print(i)


    if not stack:
        return True
    else:
        return False
    
solve_problem("[(")