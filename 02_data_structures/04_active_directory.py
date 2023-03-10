class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name


parent = Group("parent")
child = Group("child")
sub_child = Group("subchild")

sub_child_user = "sub_child_user"
sub_child.add_user(sub_child_user)

child.add_group(sub_child)
parent.add_group(child)

def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    if user in group.get_users():
        return True
    for sub_group in group.get_groups():
        if is_user_in_group(user, sub_group):
            return True
    return False



# Test case 1
user = "sub_child_user"
group = parent
result = is_user_in_group(user, group)
assert result == True, f"Expected True, but got {result}"

# Test case 2
user = "nonexistent_user"
group = parent
result = is_user_in_group(user, group)
assert result == False, f"Expected False, but got {result}"

# Test case 3
user = None
group = parent
result = is_user_in_group(user, group)
assert result == False, f"Expected False, but got {result}"

# Test case 4
user = ""
group = parent
result = is_user_in_group(user, group)
assert result == False, f"Expected False, but got {result}"
