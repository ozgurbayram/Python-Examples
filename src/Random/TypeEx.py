from typing import Type,TypeVar

class User: ...

class BasicUser(User): ...

class ProUser(BasicUser): ...

class TeamUser(ProUser): ...

U = TypeVar('U',bound=User)

def create_new_user(user_class= Type[U]) -> User:
    user = user_class()

    return user

ozgur = create_new_user(ProUser)
eren = create_new_user(BasicUser)
mehmet = create_new_user(TeamUser)

print(type(ozgur))
print(type(eren))
print(type(mehmet))
