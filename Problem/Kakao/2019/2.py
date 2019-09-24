def solution(p):
    if p=='':
        return p
    rs = ''
    idx=0
    s_left = []
    s_right = []
    s = []
    
    def chk_right(tmp):
        flag = 0
        for t in tmp:
            if t=='(':
                flag+=1
            else:
                flag-=1
            if flag<0:
                return False
        return True
    def get_uv(tmp):
        s_left = []
        s_right = []
        u = v = None
        idx = 0
        if tmp==None:
            return u, v
        while idx<len(tmp):
            if tmp[idx]=='(':
                s_left.append(0)
            else:
                s_right.append(0)
            if len(s_left) == len(s_right):
                break
            idx += 1
        u = tmp[0:idx+1]
        v = tmp[idx+1:] if idx+1<len(tmp) else None
        return u, v

    def chk_balance(tmp, rs):
        if tmp==None:
            return rs
        u, v = get_uv(tmp)
        if chk_right(u):
            if v==None:
                return rs
            rs += ''.join(u)
            rs = chk_balance(v, rs)
        else:
            add = ['(']
            u1, v1 = get_uv(v)
            add.append(u1)
            add.append(')')
            for x in u[1:-1]:
                if x=='(':
                    add.append(')')
                else:
                    add.append('(')
            if v!=None:
                if add!= None:
                    rs = chk_balance(v, rs + ''.join(add))
                else:
                    rs = chk_balance(v, rs)
        return rs

    return chk_balance(p, '')


print('rs: ', solution('()))((()'))
print('rs: ', solution(')('))
