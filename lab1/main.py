from SysOfLinEq import SysOfLinEq





if __name__ == "__main__":
    sle = SysOfLinEq("lab1/pars.txt") # pars.txt

    print(sle.get_solution())
    print(sle.get_matrix_norm())
    print(sle.get_iteration_count())
    print(sle.get_variance())
