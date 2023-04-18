def index_all(ll, val):

    ind = []
    i = 0

    if isinstance(ll, int):
        if ll == val:
            ind.append(0)
    elif ll == val:
        return "All"
    else:
        while i < len(ll):
            if isinstance(ll[i], int) and ll[i] == val:
                ind.append(i)
                i += 1
            elif not isinstance(ll[i], int):
                sub_ll = ll[i]
                sub_ind = index_all(sub_ll, val)
                if sub_ind == "All":
                    upper_ind = [i]
                    ind.append(upper_ind)
                elif len(sub_ind) != 0:
                    for j in sub_ind:
                        if isinstance(j, int):
                            upper_ind = [i]
                            upper_ind.append(j)
                            ind.append(upper_ind)
                        else:
                            upper_ind = [i]
                            upper_ind.extend(j)
                            ind.append(upper_ind)

                i += 1
            else:
                i += 1

    return ind
