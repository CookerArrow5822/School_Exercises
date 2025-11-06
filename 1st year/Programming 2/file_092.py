#!/usr/bin/env python3

class File(object):
    def __init__(self, name):
        self.name = name
        self.content = []
        self.permissions = {}

    def add_line(self, line):
        self.content.append(line)

    def add_permission(self, user, permission):
        if user not in self.permissions:
            self.permissions[user] = set()
        self.permissions[user].add(permission)

    def del_permission(self, user, permission):
        if user in self.permissions and permission in self.permissions[user]:
            self.permissions[user].remove(permission)
            if not self.permissions[user]:
                del self.permissions[user]

    def can_read(self, user):
        return 'r' in self.permissions.get(user, set())

    def can_write(self, user):
        return 'w' in self.permissions.get(user, set())

    def __str__(self):
        result = f'File: {self.name}'
        if self.content:
            result += '\n' + '\n'.join(self.content)
        if self.permissions:
            result += '\nPermissions:'
            for user in sorted(self.permissions.keys()):
                perms = ', '.join(sorted(self.permissions[user]))
                result += f'\n{user}: {perms}'
        return result
