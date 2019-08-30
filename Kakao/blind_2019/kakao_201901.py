def solution(record):
    answer = []
    uid_dics = {}
    orders = []
    for rec in record:
        splits = rec.split(" ")
        if len(splits)==3:
            order, uid, nickname = splits[0], splits[1], splits[2]
            uid_dics.update({uid:nickname})
        else:
            order, uid = splits[0], splits[1]
        if order != "Change":
            orders.append([order, uid])
    for order in orders:
        if order[0]=="Enter":
            answer.append("{}님이 들어왔습니다.".format(uid_dics[order[1]]))
        elif order[0]=="Leave":
            answer.append("{}님이 나갔습니다.".format(uid_dics[order[1]]))
    return answer

record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
rs = solution(record)
print(rs)
