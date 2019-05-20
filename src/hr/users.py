import pwd

def get_users():
    valid_users = []
    total_users = pwd.getpwall()
    for i in range(len(total_users) -1, -1, -1):
        if total_users[i].pw_uid < 1000:
            break
        else:
            valid_users.append({
                "name": total_users[i].pw_name,
                "id": total_users[i].pw_uid,
                "home": total_users[i].pw_dir,
                "shell": total_users[i].pw_shell
            })
    return valid_users
        